from __future__ import annotations

import argparse
import json
import random
from collections import defaultdict
from pathlib import Path
from typing import Any

import _bootstrap  # noqa: F401

from nature_reviewer_core.evaluation import load_cases, load_predictions, score_case


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _metrics(scores: list[dict[str, Any]]) -> dict[str, float]:
    positive = [item for item in scores if item["case_type"] == "positive"]
    controls = [item for item in scores if item["case_type"] == "negative_control"]

    essential_recall = _mean(
        [float(item["essential_issue_recall"]) for item in positive]
    )
    specificity = _mean(
        [float(bool(item["negative_control_pass"])) for item in controls]
    )

    tp = sum(int(item["true_positive"]) for item in scores)
    fp = sum(int(item["false_positive"]) for item in scores)
    fn = sum(int(item["false_negative"]) for item in scores)
    precision = tp / max(tp + fp, 1)
    recall = tp / max(tp + fn, 1)
    micro_f1 = 2 * precision * recall / max(precision + recall, 1e-12)

    by_pair: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in scores:
        if item["pair_id"]:
            by_pair[str(item["pair_id"])].append(item)
    pair_outcomes = []
    for items in by_pair.values():
        pos = next(item for item in items if item["case_type"] == "positive")
        ctl = next(item for item in items if item["case_type"] == "negative_control")
        pair_outcomes.append(
            float(
                float(pos["essential_issue_recall"]) == 1.0
                and bool(ctl["negative_control_pass"])
            )
        )

    return {
        "essential_issue_recall": round(essential_recall, 4),
        "specificity": round(specificity, 4),
        "essential_balanced_accuracy": round(
            (essential_recall + specificity) / 2.0, 4
        ),
        "paired_pass_rate": round(_mean(pair_outcomes), 4),
        "micro_f1": round(micro_f1, 4),
    }


def _units(scores: list[dict[str, Any]]) -> list[list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in scores:
        pair_id = str(item["pair_id"])
        if not pair_id:
            raise ValueError("Paired comparison requires pair_id on every case")
        grouped[pair_id].append(item)
    return list(grouped.values())


def _percentile(values: list[float], probability: float) -> float:
    ordered = sorted(values)
    index = (len(ordered) - 1) * probability
    lo = int(index)
    hi = min(lo + 1, len(ordered) - 1)
    weight = index - lo
    return ordered[lo] * (1.0 - weight) + ordered[hi] * weight


def paired_bootstrap_delta(
    scores_a: list[dict[str, Any]],
    scores_b: list[dict[str, Any]],
    iterations: int = 5000,
    seed: int = 20260920,
) -> dict[str, list[float]]:
    units_a = {str(unit[0]["pair_id"]): unit for unit in _units(scores_a)}
    units_b = {str(unit[0]["pair_id"]): unit for unit in _units(scores_b)}
    if set(units_a) != set(units_b):
        raise ValueError("Prediction files do not cover identical pair IDs")

    pair_ids = sorted(units_a)
    rng = random.Random(seed)  # noqa: S311  # nosec B311
    metrics = (
        "essential_issue_recall",
        "specificity",
        "essential_balanced_accuracy",
        "paired_pass_rate",
        "micro_f1",
    )
    deltas: dict[str, list[float]] = {metric: [] for metric in metrics}

    for _ in range(iterations):
        sampled_ids = [
            rng.choice(pair_ids)  # noqa: S311  # nosec B311
            for _index in range(len(pair_ids))
        ]
        sampled_a = [item for pair_id in sampled_ids for item in units_a[pair_id]]
        sampled_b = [item for pair_id in sampled_ids for item in units_b[pair_id]]
        metrics_a = _metrics(sampled_a)
        metrics_b = _metrics(sampled_b)
        for metric in metrics:
            deltas[metric].append(metrics_b[metric] - metrics_a[metric])

    return {
        metric: [
            round(_percentile(values, 0.025), 4),
            round(_percentile(values, 0.975), 4),
        ]
        for metric, values in deltas.items()
    }


def score_predictions(cases_path: Path, predictions_path: Path) -> list[dict[str, Any]]:
    predictions = load_predictions(predictions_path)
    return [
        score_case(case, predictions.get(case.case_id, []))
        for case in load_cases(cases_path)
    ]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("cases", type=Path)
    parser.add_argument("predictions_a", type=Path)
    parser.add_argument("predictions_b", type=Path)
    parser.add_argument("--label-a", default="generic")
    parser.add_argument("--label-b", default="skill-assisted")
    parser.add_argument("--iterations", type=int, default=5000)
    parser.add_argument("--seed", type=int, default=20260920)
    args = parser.parse_args()

    scores_a = score_predictions(args.cases, args.predictions_a)
    scores_b = score_predictions(args.cases, args.predictions_b)
    metrics_a = _metrics(scores_a)
    metrics_b = _metrics(scores_b)
    deltas = {
        metric: round(metrics_b[metric] - metrics_a[metric], 4)
        for metric in metrics_a
    }

    report = {
        "system_a": {"label": args.label_a, "metrics": metrics_a},
        "system_b": {"label": args.label_b, "metrics": metrics_b},
        "delta_b_minus_a": deltas,
        "paired_bootstrap_95ci_delta": paired_bootstrap_delta(
            scores_a,
            scores_b,
            iterations=args.iterations,
            seed=args.seed,
        ),
        "bootstrap_unit": "matched pair_id",
    }
    print(json.dumps(report, indent=2))
