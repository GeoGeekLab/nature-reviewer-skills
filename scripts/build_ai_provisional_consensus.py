from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


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


def _issues(row: dict[str, Any]) -> dict[str, dict[str, Any]]:
    concerns = row.get("concerns", [])
    if not isinstance(concerns, list):
        raise ValueError("concerns must be a list")
    result = {}
    for concern in concerns:
        if not isinstance(concern, dict):
            raise ValueError("concern must be an object")
        issue_id = str(concern.get("issue_id", ""))
        if issue_id:
            result[issue_id] = concern
    return result


def build(a_path: Path, b_path: Path, intersection_path: Path, union_path: Path) -> dict[str, Any]:
    a_rows = {str(row["annotation_id"]): row for row in _jsonl(a_path)}
    b_rows = {str(row["annotation_id"]): row for row in _jsonl(b_path)}
    if set(a_rows) != set(b_rows):
        raise ValueError("Annotators do not cover identical annotation IDs")

    intersection_lines = []
    union_lines = []
    disagreement_annotations = 0
    total_label_disagreements = 0

    for annotation_id in sorted(a_rows):
        a_issues = _issues(a_rows[annotation_id])
        b_issues = _issues(b_rows[annotation_id])
        shared = sorted(set(a_issues) & set(b_issues))
        combined = sorted(set(a_issues) | set(b_issues))
        symmetric = set(a_issues) ^ set(b_issues)
        if symmetric:
            disagreement_annotations += 1
            total_label_disagreements += len(symmetric)

        intersection_lines.append(
            json.dumps(
                {
                    "annotation_id": annotation_id,
                    "concerns": [
                        {
                            "issue_id": issue_id,
                            "severity": (
                                "major"
                                if "major"
                                in {
                                    str(a_issues[issue_id].get("severity", "minor")),
                                    str(b_issues[issue_id].get("severity", "minor")),
                                }
                                else "minor"
                            ),
                            "anchors": [],
                        }
                        for issue_id in shared
                    ],
                }
            )
            + "\n"
        )
        union_lines.append(
            json.dumps(
                {
                    "annotation_id": annotation_id,
                    "concerns": [
                        {
                            "issue_id": issue_id,
                            "severity": (
                                "major"
                                if any(
                                    str(source.get(issue_id, {}).get("severity", "minor"))
                                    == "major"
                                    for source in (a_issues, b_issues)
                                )
                                else "minor"
                            ),
                            "anchors": [],
                        }
                        for issue_id in combined
                    ],
                }
            )
            + "\n"
        )

    intersection_path.write_text("".join(intersection_lines), encoding="utf-8")
    union_path.write_text("".join(union_lines), encoding="utf-8")

    return {
        "annotation_count": len(a_rows),
        "annotations_with_any_label_disagreement": disagreement_annotations,
        "label_disagreement_count": total_label_disagreements,
        "primary_consensus": "intersection",
        "sensitivity_consensus": "union",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--annotator-a", type=Path, required=True)
    parser.add_argument("--annotator-b", type=Path, required=True)
    parser.add_argument("--intersection", type=Path, required=True)
    parser.add_argument("--union", type=Path, required=True)
    args = parser.parse_args()
    print(
        json.dumps(
            build(args.annotator_a, args.annotator_b, args.intersection, args.union),
            indent=2,
        )
    )
