from __future__ import annotations

import json
import random
from collections import defaultdict
from pathlib import Path
from typing import Any

from .models import BenchmarkCase, Concern
from .panel import concern_overlap
from .patterns import normalize_severity

_POSITIVE_METRICS = (
    "precision",
    "recall",
    "f1",
    "essential_issue_recall",
    "severity_agreement",
    "anchor_coverage",
    "panel_duplicate_rate",
)


def _concern_from_dict(value: dict[str, Any]) -> Concern:
    return Concern(
        issue_id=str(value["issue_id"]),
        severity=normalize_severity(value.get("severity", "unknown")),
        text=str(value.get("text", "")),
        anchors=tuple(str(anchor) for anchor in value.get("anchors", [])),
        reviewer_id=str(value.get("reviewer_id", "")),
    )


def _case_from_dict(value: dict[str, Any], source: str = "<memory>") -> BenchmarkCase:
    case_type = str(value.get("case_type", "positive"))
    if case_type not in {"positive", "negative_control"}:
        raise ValueError(f"Unsupported benchmark case_type in {source}: {case_type}")
    return BenchmarkCase(
        case_id=str(value["case_id"]),
        domain=str(value["domain"]),
        manuscript_text=str(value.get("manuscript_text", "")),
        gold_concerns=tuple(_concern_from_dict(item) for item in value.get("gold_concerns", [])),
        case_type=case_type,  # type: ignore[arg-type]
        pair_id=str(value.get("pair_id", "")),
        challenge=str(value.get("challenge", "")),
        suite=str(value.get("suite", "")),
    )


def load_case(path: Path) -> BenchmarkCase:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"Expected one benchmark object in {path}")
    return _case_from_dict(value, str(path))


def load_cases(path: Path) -> list[BenchmarkCase]:
    if path.is_dir():
        return [load_case(case_path) for case_path in sorted(path.glob("*.json"))]

    if path.suffix == ".jsonl":
        cases: list[BenchmarkCase] = []
        with path.open("r", encoding="utf-8") as handle:
            for number, line in enumerate(handle, 1):
                if not line.strip():
                    continue
                value = json.loads(line)
                if not isinstance(value, dict):
                    raise ValueError(f"Expected object at {path}:{number}")
                cases.append(_case_from_dict(value, f"{path}:{number}"))
        return cases

    if path.suffix == ".json":
        value = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(value, list):
            return [_case_from_dict(item, str(path)) for item in value]
        if isinstance(value, dict):
            return [_case_from_dict(value, str(path))]

    raise ValueError(f"Unsupported benchmark case source: {path}")


def load_predictions(path: Path) -> dict[str, list[Concern]]:
    predictions: dict[str, list[Concern]] = {}
    with path.open("r", encoding="utf-8") as handle:
        for number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            value = json.loads(line)
            case_id = str(value["case_id"])
            concerns = [_concern_from_dict(item) for item in value.get("concerns", [])]
            if case_id in predictions:
                raise ValueError(f"Duplicate prediction for {case_id} at line {number}")
            predictions[case_id] = concerns
    return predictions


def _positive_metrics(
    case: BenchmarkCase,
    predicted_by_id: dict[str, Concern],
    gold_by_id: dict[str, Concern],
) -> dict[str, float]:
    gold_ids = set(gold_by_id)
    predicted_ids = set(predicted_by_id)
    matched = gold_ids & predicted_ids
    true_positive = len(matched)
    false_positive = len(predicted_ids - gold_ids)
    false_negative = len(gold_ids - predicted_ids)
    precision = true_positive / max(true_positive + false_positive, 1)
    recall = true_positive / max(true_positive + false_negative, 1)
    f1 = 2 * precision * recall / max(precision + recall, 1e-12)

    severity_matches = 0
    anchor_hits = 0
    for issue_id in matched:
        gold = gold_by_id[issue_id]
        candidate = predicted_by_id[issue_id]
        severity_matches += int(gold.severity == candidate.severity)
        anchor_hits += int(bool(set(gold.anchors) & set(candidate.anchors)))

    essential_gold = {
        item.issue_id for item in case.gold_concerns if item.severity in {"critical", "major"}
    }
    essential_recall = len(essential_gold & predicted_ids) / max(len(essential_gold), 1)
    overlap = concern_overlap(list(predicted_by_id.values()))
    return {
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1": round(f1, 4),
        "essential_issue_recall": round(essential_recall, 4),
        "severity_agreement": round(severity_matches / max(len(matched), 1), 4),
        "anchor_coverage": round(anchor_hits / max(len(matched), 1), 4),
        "panel_duplicate_rate": float(overlap["duplicate_rate"]),
    }


def score_case(case: BenchmarkCase, predicted: list[Concern]) -> dict[str, Any]:
    gold_by_id = {concern.issue_id: concern for concern in case.gold_concerns}
    predicted_by_id = {concern.issue_id: concern for concern in predicted}
    gold_ids = set(gold_by_id)
    predicted_ids = set(predicted_by_id)

    result: dict[str, Any] = {
        "case_id": case.case_id,
        "suite": case.suite,
        "domain": case.domain,
        "challenge": case.challenge,
        "pair_id": case.pair_id,
        "case_type": case.case_type,
        "gold_count": len(gold_ids),
        "predicted_count": len(predicted_ids),
        "true_positive": len(gold_ids & predicted_ids),
        "false_positive": len(predicted_ids - gold_ids),
        "false_negative": len(gold_ids - predicted_ids),
    }

    if case.case_type == "negative_control":
        overlap = concern_overlap(list(predicted_by_id.values()))
        result.update(
            {metric: None for metric in _POSITIVE_METRICS if metric != "panel_duplicate_rate"}
        )
        result["panel_duplicate_rate"] = float(overlap["duplicate_rate"])
        if case.challenge:
            result["negative_control_pass"] = case.challenge not in predicted_ids
        else:
            result["negative_control_pass"] = len(predicted_ids) == 0
        return result

    result.update(_positive_metrics(case, predicted_by_id, gold_by_id))
    result["negative_control_pass"] = None
    return result


def _mean(values: list[float]) -> float | None:
    if not values:
        return None
    return round(sum(values) / len(values), 4)


def _numeric_metric(scores: list[dict[str, Any]], metric: str) -> list[float]:
    values: list[float] = []
    for score in scores:
        value = score.get(metric)
        if isinstance(value, int | float):
            values.append(float(value))
    return values


def _pair_pass_rate(scores: list[dict[str, Any]]) -> float | None:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for score in scores:
        pair_id = str(score.get("pair_id", ""))
        if pair_id:
            grouped[pair_id].append(score)

    outcomes: list[float] = []
    for items in grouped.values():
        positive = next((item for item in items if item["case_type"] == "positive"), None)
        control = next((item for item in items if item["case_type"] == "negative_control"), None)
        if positive is None or control is None:
            continue
        positive_pass = float(positive.get("essential_issue_recall") or 0.0) == 1.0
        control_pass = bool(control.get("negative_control_pass"))
        outcomes.append(float(positive_pass and control_pass))
    return _mean(outcomes)


def _aggregate_core(scores: list[dict[str, Any]], include_domains: bool = True) -> dict[str, Any]:
    if not scores:
        return {"case_count": 0}

    positive = [item for item in scores if item.get("case_type") != "negative_control"]
    controls = [item for item in scores if item.get("case_type") == "negative_control"]

    macro = {metric: _mean(_numeric_metric(positive, metric)) for metric in _POSITIVE_METRICS}

    tp = sum(int(item["true_positive"]) for item in scores)
    fp = sum(int(item["false_positive"]) for item in scores)
    fn = sum(int(item["false_negative"]) for item in scores)
    micro_precision = tp / max(tp + fp, 1)
    micro_recall = tp / max(tp + fn, 1)
    micro_f1 = 2 * micro_precision * micro_recall / max(micro_precision + micro_recall, 1e-12)

    specificity = None
    false_positive_rate = None
    if controls:
        passed = sum(int(bool(item.get("negative_control_pass"))) for item in controls)
        specificity = round(passed / len(controls), 4)
        false_positive_rate = round(1.0 - specificity, 4)

    essential_recall = macro["essential_issue_recall"]
    balanced_accuracy = None
    if isinstance(essential_recall, float) and specificity is not None:
        balanced_accuracy = round((essential_recall + specificity) / 2.0, 4)

    result: dict[str, Any] = {
        "case_count": len(scores),
        "positive_case_count": len(positive),
        "negative_control_count": len(controls),
        "macro": macro,
        "micro": {
            "precision": round(micro_precision, 4),
            "recall": round(micro_recall, 4),
            "f1": round(micro_f1, 4),
        },
        "controls": {
            "specificity": specificity,
            "false_positive_rate": false_positive_rate,
        },
        "essential_balanced_accuracy": balanced_accuracy,
        "paired_pass_rate": _pair_pass_rate(scores),
    }

    if include_domains:
        by_domain: dict[str, dict[str, Any]] = {}
        domains = sorted({str(item["domain"]) for item in scores})
        for domain in domains:
            domain_scores = [item for item in scores if str(item["domain"]) == domain]
            by_domain[domain] = _aggregate_core(domain_scores, include_domains=False)
        result["by_domain"] = by_domain

    return result


def _percentile(values: list[float], probability: float) -> float:
    ordered = sorted(values)
    if not ordered:
        raise ValueError("Cannot calculate a percentile from an empty sequence")
    index = (len(ordered) - 1) * probability
    lower = int(index)
    upper = min(lower + 1, len(ordered) - 1)
    weight = index - lower
    return ordered[lower] * (1.0 - weight) + ordered[upper] * weight


def _sampling_units(scores: list[dict[str, Any]]) -> list[list[dict[str, Any]]]:
    paired: dict[str, list[dict[str, Any]]] = defaultdict(list)
    unpaired: list[list[dict[str, Any]]] = []
    for score in scores:
        pair_id = str(score.get("pair_id", ""))
        if pair_id:
            paired[pair_id].append(score)
        else:
            unpaired.append([score])
    return list(paired.values()) + unpaired


def _extract_summary_metric(summary: dict[str, Any], metric: str) -> float | None:
    if metric == "essential_issue_recall":
        value = summary.get("macro", {}).get("essential_issue_recall")
    elif metric == "specificity":
        value = summary.get("controls", {}).get("specificity")
    elif metric == "essential_balanced_accuracy":
        value = summary.get("essential_balanced_accuracy")
    elif metric == "paired_pass_rate":
        value = summary.get("paired_pass_rate")
    elif metric == "micro_f1":
        value = summary.get("micro", {}).get("f1")
    else:
        raise ValueError(f"Unsupported bootstrap metric: {metric}")
    return float(value) if isinstance(value, int | float) else None


def _bootstrap_confidence_intervals(
    scores: list[dict[str, Any]],
    iterations: int = 2000,
    seed: int = 20260920,
) -> dict[str, list[float] | None]:
    units = _sampling_units(scores)
    metrics = (
        "essential_issue_recall",
        "specificity",
        "essential_balanced_accuracy",
        "paired_pass_rate",
        "micro_f1",
    )
    if len(units) < 2:
        return {metric: None for metric in metrics}

    rng = random.Random(seed)  # noqa: S311  # nosec B311
    sampled_metrics: dict[str, list[float]] = {metric: [] for metric in metrics}
    for _ in range(iterations):
        sampled_scores: list[dict[str, Any]] = []
        for draw_index in range(len(units)):
            unit = rng.choice(units)  # noqa: S311  # nosec B311
            for score in unit:
                sampled = dict(score)
                if sampled.get("pair_id"):
                    sampled["pair_id"] = f"bootstrap-{draw_index}"
                sampled_scores.append(sampled)
        summary = _aggregate_core(sampled_scores, include_domains=False)
        for metric in metrics:
            value = _extract_summary_metric(summary, metric)
            if value is not None:
                sampled_metrics[metric].append(value)

    intervals: dict[str, list[float] | None] = {}
    for metric, values in sampled_metrics.items():
        if not values:
            intervals[metric] = None
            continue
        intervals[metric] = [
            round(_percentile(values, 0.025), 4),
            round(_percentile(values, 0.975), 4),
        ]
    return intervals


def aggregate(scores: list[dict[str, Any]]) -> dict[str, Any]:
    result = _aggregate_core(scores)
    if scores:
        result["bootstrap_95ci"] = _bootstrap_confidence_intervals(scores)
    return result
