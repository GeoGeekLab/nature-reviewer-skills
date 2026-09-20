from __future__ import annotations

import argparse
import json
import random
from collections import defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "benchmarks/pilot_v1/config.json"


def _json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            value = json.loads(line)
            if not isinstance(value, dict):
                raise ValueError(f"Expected object at {path}:{number}")
            rows.append(value)
    return rows


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _percentile(values: list[float], probability: float) -> float:
    ordered = sorted(values)
    if not ordered:
        raise ValueError("Cannot calculate percentile of empty values")
    index = (len(ordered) - 1) * probability
    low = int(index)
    high = min(low + 1, len(ordered) - 1)
    weight = index - low
    return ordered[low] * (1.0 - weight) + ordered[high] * weight


def _concern_ids(row: dict[str, Any]) -> set[str]:
    concerns = row.get("concerns", [])
    if not isinstance(concerns, list):
        raise ValueError("concerns must be a list")
    result: set[str] = set()
    for concern in concerns:
        if not isinstance(concern, dict):
            raise ValueError("Each concern must be an object")
        issue_id = str(concern.get("issue_id", ""))
        if issue_id:
            result.add(issue_id)
    return result


def _pair_contributions(rows: list[dict[str, Any]]) -> dict[str, dict[str, float]]:
    by_pair: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        by_pair[str(row["pair_id"])].append(row)

    contributions: dict[str, dict[str, float]] = {}
    for pair_id, items in by_pair.items():
        positives = [row for row in items if row["case_type"] == "positive"]
        controls = [row for row in items if row["case_type"] == "negative_control"]
        if not positives or not controls:
            raise ValueError(f"Pair {pair_id} is missing positive or control runs")

        positive_detection = [
            float(str(row["target_issue_id"]) in row["predicted_issue_ids"])
            for row in positives
        ]
        control_specificity = [
            float(str(row["target_issue_id"]) not in row["predicted_issue_ids"])
            for row in controls
        ]

        positive_by_run = {int(row["run_index"]): row for row in positives}
        control_by_run = {int(row["run_index"]): row for row in controls}
        if set(positive_by_run) != set(control_by_run):
            raise ValueError(f"Pair {pair_id} has mismatched repeated-run indices")

        pair_pass = []
        for run_index in sorted(positive_by_run):
            positive = positive_by_run[run_index]
            control = control_by_run[run_index]
            target = str(positive["target_issue_id"])
            pair_pass.append(
                float(
                    target in positive["predicted_issue_ids"]
                    and target not in control["predicted_issue_ids"]
                )
            )

        tp = fp = fn = 0
        for row in items:
            predicted = set(row["predicted_issue_ids"])
            gold = (
                {str(row["target_issue_id"])}
                if row["case_type"] == "positive"
                else set()
            )
            tp += len(predicted & gold)
            fp += len(predicted - gold)
            fn += len(gold - predicted)

        contributions[pair_id] = {
            "recall": _mean(positive_detection),
            "specificity": _mean(control_specificity),
            "pair_pass": _mean(pair_pass),
            "tp": float(tp),
            "fp": float(fp),
            "fn": float(fn),
        }
    return contributions


def _metrics_from_pairs(
    pair_ids: list[str],
    contributions: dict[str, dict[str, float]],
) -> dict[str, float]:
    recall = _mean([contributions[pair_id]["recall"] for pair_id in pair_ids])
    specificity = _mean([contributions[pair_id]["specificity"] for pair_id in pair_ids])
    pair_pass = _mean([contributions[pair_id]["pair_pass"] for pair_id in pair_ids])

    tp = sum(contributions[pair_id]["tp"] for pair_id in pair_ids)
    fp = sum(contributions[pair_id]["fp"] for pair_id in pair_ids)
    fn = sum(contributions[pair_id]["fn"] for pair_id in pair_ids)
    precision = tp / max(tp + fp, 1.0)
    micro_recall = tp / max(tp + fn, 1.0)
    micro_f1 = 2 * precision * micro_recall / max(precision + micro_recall, 1e-12)

    return {
        "essential_issue_recall": recall,
        "target_specificity": specificity,
        "essential_balanced_accuracy": (recall + specificity) / 2.0,
        "paired_pass_rate": pair_pass,
        "micro_precision": precision,
        "micro_recall": micro_recall,
        "micro_f1": micro_f1,
    }


def _round_metrics(metrics: dict[str, float]) -> dict[str, float]:
    return {key: round(value, 4) for key, value in metrics.items()}


def analyze(
    pilot_dir: Path,
    annotations_path: Path,
    *,
    iterations: int,
    seed: int,
) -> dict[str, Any]:
    private_mapping = _json(pilot_dir / "private_mapping.json")
    annotation_mapping = _json(pilot_dir / "annotation_mapping.json")
    annotations = _jsonl(annotations_path)

    if not isinstance(private_mapping, list) or not isinstance(annotation_mapping, list):
        raise ValueError("Pilot mapping files must be lists")

    private_by_blind = {str(row["blind_id"]): row for row in private_mapping}
    blind_by_annotation = {
        str(row["annotation_id"]): str(row["blind_id"]) for row in annotation_mapping
    }

    annotated_by_id: dict[str, dict[str, Any]] = {}
    for row in annotations:
        annotation_id = str(row.get("annotation_id", ""))
        if not annotation_id:
            raise ValueError("Annotation record missing annotation_id")
        if annotation_id in annotated_by_id:
            raise ValueError(f"Duplicate adjudicated annotation: {annotation_id}")
        annotated_by_id[annotation_id] = row

    expected = set(blind_by_annotation)
    if set(annotated_by_id) != expected:
        raise ValueError("Adjudicated annotation coverage does not match annotation packets")

    rows_by_condition: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for annotation_id, annotation in annotated_by_id.items():
        blind_id = blind_by_annotation[annotation_id]
        private = private_by_blind[blind_id]
        rows_by_condition[str(private["condition"])].append(
            {
                **private,
                "predicted_issue_ids": _concern_ids(annotation),
            }
        )

    contributions = {
        condition: _pair_contributions(rows)
        for condition, rows in rows_by_condition.items()
    }
    if set(contributions) != {"generic", "skill-assisted"}:
        raise ValueError("Expected generic and skill-assisted conditions")

    pair_ids = sorted(set(contributions["generic"]) & set(contributions["skill-assisted"]))
    if len(pair_ids) != len(contributions["generic"]) or len(pair_ids) != len(
        contributions["skill-assisted"]
    ):
        raise ValueError("Conditions do not contain identical pair IDs")

    observed = {
        condition: _metrics_from_pairs(pair_ids, pair_contributions)
        for condition, pair_contributions in contributions.items()
    }
    delta = {
        metric: observed["skill-assisted"][metric] - observed["generic"][metric]
        for metric in observed["generic"]
    }

    rng = random.Random(seed)  # noqa: S311  # nosec B311
    sampled_generic: dict[str, list[float]] = {
        metric: [] for metric in observed["generic"]
    }
    sampled_skill: dict[str, list[float]] = {
        metric: [] for metric in observed["skill-assisted"]
    }
    sampled_delta: dict[str, list[float]] = {metric: [] for metric in delta}

    for _ in range(iterations):
        sampled_pairs = [
            rng.choice(pair_ids)  # noqa: S311  # nosec B311
            for _draw in range(len(pair_ids))
        ]
        generic_metrics = _metrics_from_pairs(sampled_pairs, contributions["generic"])
        skill_metrics = _metrics_from_pairs(sampled_pairs, contributions["skill-assisted"])
        for metric in generic_metrics:
            sampled_generic[metric].append(generic_metrics[metric])
            sampled_skill[metric].append(skill_metrics[metric])
            sampled_delta[metric].append(skill_metrics[metric] - generic_metrics[metric])

    def intervals(values: dict[str, list[float]]) -> dict[str, list[float]]:
        return {
            metric: [
                round(_percentile(samples, 0.025), 4),
                round(_percentile(samples, 0.975), 4),
            ]
            for metric, samples in values.items()
        }

    by_domain: dict[str, dict[str, dict[str, float]]] = {}
    domains = sorted({str(row["domain"]) for row in private_mapping})
    for domain in domains:
        domain_pairs = sorted(
            {
                str(row["pair_id"])
                for row in private_mapping
                if str(row["domain"]) == domain
            }
        )
        by_domain[domain] = {
            condition: _round_metrics(
                _metrics_from_pairs(domain_pairs, contributions[condition])
            )
            for condition in ("generic", "skill-assisted")
        }

    return {
        "pair_count": len(pair_ids),
        "bootstrap_iterations": iterations,
        "bootstrap_unit": "pair_id with all repeated runs and both conditions retained",
        "observed": {
            condition: _round_metrics(metrics)
            for condition, metrics in observed.items()
        },
        "delta_skill_minus_generic": _round_metrics(delta),
        "bootstrap_95ci": {
            "generic": intervals(sampled_generic),
            "skill-assisted": intervals(sampled_skill),
            "delta_skill_minus_generic": intervals(sampled_delta),
        },
        "by_domain": by_domain,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--pilot-dir", type=Path, required=True)
    parser.add_argument("--annotations", type=Path, required=True)
    parser.add_argument("--iterations", type=int, default=10_000)
    parser.add_argument("--seed", type=int, default=20260920)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    report = analyze(
        args.pilot_dir,
        args.annotations,
        iterations=args.iterations,
        seed=args.seed,
    )
    rendered = json.dumps(report, indent=2)
    if args.output is not None:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
