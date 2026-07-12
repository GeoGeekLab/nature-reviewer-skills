from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from .models import BenchmarkCase, Concern
from .panel import concern_overlap
from .patterns import normalize_severity


def _concern_from_dict(value: dict[str, Any]) -> Concern:
    return Concern(
        issue_id=str(value["issue_id"]),
        severity=normalize_severity(value.get("severity", "unknown")),
        text=str(value.get("text", "")),
        anchors=tuple(str(anchor) for anchor in value.get("anchors", [])),
        reviewer_id=str(value.get("reviewer_id", "")),
    )


def load_case(path: Path) -> BenchmarkCase:
    value = json.loads(path.read_text(encoding="utf-8"))
    return BenchmarkCase(
        case_id=str(value["case_id"]),
        domain=str(value["domain"]),
        manuscript_text=str(value.get("manuscript_text", "")),
        gold_concerns=tuple(_concern_from_dict(item) for item in value.get("gold_concerns", [])),
    )


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


def score_case(case: BenchmarkCase, predicted: list[Concern]) -> dict[str, Any]:
    gold_by_id = {concern.issue_id: concern for concern in case.gold_concerns}
    predicted_by_id = {concern.issue_id: concern for concern in predicted}
    gold_ids = set(gold_by_id)
    predicted_ids = set(predicted_by_id)
    true_positive = len(gold_ids & predicted_ids)
    false_positive = len(predicted_ids - gold_ids)
    false_negative = len(gold_ids - predicted_ids)
    precision = true_positive / max(true_positive + false_positive, 1)
    recall = true_positive / max(true_positive + false_negative, 1)
    f1 = 2 * precision * recall / max(precision + recall, 1e-12)
    severity_matches = 0
    anchor_hits = 0
    matched = gold_ids & predicted_ids
    for issue_id in matched:
        gold = gold_by_id[issue_id]
        candidate = predicted_by_id[issue_id]
        severity_matches += int(gold.severity == candidate.severity)
        if gold.anchors:
            anchor_hits += int(bool(set(gold.anchors) & set(candidate.anchors)))
        else:
            anchor_hits += int(bool(candidate.anchors))
    essential_gold = {
        item.issue_id for item in case.gold_concerns if item.severity in {"critical", "major"}
    }
    essential_recall = len(essential_gold & predicted_ids) / max(len(essential_gold), 1)
    overlap = concern_overlap(predicted)
    return {
        "case_id": case.case_id,
        "domain": case.domain,
        "gold_count": len(gold_ids),
        "predicted_count": len(predicted_ids),
        "true_positive": true_positive,
        "false_positive": false_positive,
        "false_negative": false_negative,
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1": round(f1, 4),
        "essential_issue_recall": round(essential_recall, 4),
        "severity_agreement": round(severity_matches / max(len(matched), 1), 4),
        "anchor_coverage": round(anchor_hits / max(len(matched), 1), 4),
        "panel_duplicate_rate": overlap["duplicate_rate"],
    }


def aggregate(scores: list[dict[str, Any]]) -> dict[str, Any]:
    if not scores:
        return {"case_count": 0}
    metric_names = (
        "precision",
        "recall",
        "f1",
        "essential_issue_recall",
        "severity_agreement",
        "anchor_coverage",
        "panel_duplicate_rate",
    )
    by_domain: dict[str, dict[str, float]] = {}
    domain_counts: Counter[str] = Counter()
    for score in scores:
        domain = str(score["domain"])
        domain_counts[domain] += 1
        bucket = by_domain.setdefault(domain, defaultdict(float))
        for metric in metric_names:
            bucket[metric] += float(score[metric])
    return {
        "case_count": len(scores),
        "macro": {
            metric: round(sum(float(item[metric]) for item in scores) / len(scores), 4)
            for metric in metric_names
        },
        "by_domain": {
            domain: {
                metric: round(values[metric] / domain_counts[domain], 4) for metric in metric_names
            }
            for domain, values in sorted(by_domain.items())
        },
    }
