from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Any


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


def _issues(row: dict[str, Any]) -> set[str]:
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


def _binary_metrics(pairs: list[tuple[int, int]]) -> dict[str, float | int]:
    if not pairs:
        raise ValueError("No paired annotations available")

    n00 = sum(1 for left, right in pairs if left == 0 and right == 0)
    n01 = sum(1 for left, right in pairs if left == 0 and right == 1)
    n10 = sum(1 for left, right in pairs if left == 1 and right == 0)
    n11 = sum(1 for left, right in pairs if left == 1 and right == 1)
    total = len(pairs)

    observed = (n00 + n11) / total
    p_left = (n10 + n11) / total
    p_right = (n01 + n11) / total
    expected = p_left * p_right + (1.0 - p_left) * (1.0 - p_right)
    if expected == 1.0:
        kappa = 1.0 if observed == 1.0 else 0.0
    else:
        kappa = (observed - expected) / (1.0 - expected)

    return {
        "n": total,
        "n00": n00,
        "n01": n01,
        "n10": n10,
        "n11": n11,
        "observed_agreement": round(observed, 4),
        "cohen_kappa": round(kappa, 4),
    }


def measure(
    pilot_dir: Path,
    annotator_a_path: Path,
    annotator_b_path: Path,
) -> dict[str, Any]:
    private_mapping = _json(pilot_dir / "private_mapping.json")
    annotation_mapping = _json(pilot_dir / "annotation_mapping.json")
    if not isinstance(private_mapping, list) or not isinstance(annotation_mapping, list):
        raise ValueError("Pilot mapping files must be lists")

    private_by_blind = {str(row["blind_id"]): row for row in private_mapping}
    blind_by_annotation = {
        str(row["annotation_id"]): str(row["blind_id"]) for row in annotation_mapping
    }

    def load_annotation_map(path: Path) -> dict[str, set[str]]:
        result: dict[str, set[str]] = {}
        for row in _jsonl(path):
            annotation_id = str(row.get("annotation_id", ""))
            if not annotation_id:
                raise ValueError(f"{path}: missing annotation_id")
            if annotation_id in result:
                raise ValueError(f"{path}: duplicate annotation_id {annotation_id}")
            result[annotation_id] = _issues(row)
        return result

    left = load_annotation_map(annotator_a_path)
    right = load_annotation_map(annotator_b_path)
    expected = set(blind_by_annotation)
    if set(left) != expected or set(right) != expected:
        raise ValueError("Both annotator files must cover every annotation packet exactly once")

    overall: list[tuple[int, int]] = []
    by_domain: dict[str, list[tuple[int, int]]] = defaultdict(list)

    for annotation_id in sorted(expected):
        blind_id = blind_by_annotation[annotation_id]
        private = private_by_blind[blind_id]
        target_issue = str(private["target_issue_id"])
        pair = (
            int(target_issue in left[annotation_id]),
            int(target_issue in right[annotation_id]),
        )
        overall.append(pair)
        by_domain[str(private["domain"])].append(pair)

    return {
        "agreement_target": "presence/absence of the paired target issue",
        "overall": _binary_metrics(overall),
        "by_domain": {
            domain: _binary_metrics(pairs)
            for domain, pairs in sorted(by_domain.items())
        },
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--pilot-dir", type=Path, required=True)
    parser.add_argument("--annotator-a", type=Path, required=True)
    parser.add_argument("--annotator-b", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    report = measure(args.pilot_dir, args.annotator_a, args.annotator_b)
    rendered = json.dumps(report, indent=2)
    if args.output is not None:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
