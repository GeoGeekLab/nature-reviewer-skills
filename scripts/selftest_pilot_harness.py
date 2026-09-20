from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from analyze_pilot_annotations import analyze
from build_pilot_annotation_packets import build


def _json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def selftest(pilot_dir: Path) -> dict[str, Any]:
    mapping = _json(pilot_dir / "private_mapping.json")
    if not isinstance(mapping, list):
        raise ValueError("private_mapping.json must be a list")
    private_by_blind = {str(row["blind_id"]): row for row in mapping}

    raw_path = pilot_dir / "ci_raw_outputs.jsonl"
    raw_path.write_text(
        "".join(
            json.dumps(
                {
                    "blind_id": str(row["blind_id"]),
                    "review_text": f"CI harness placeholder for {row['blind_id']}",
                }
            )
            + "\n"
            for row in mapping
        ),
        encoding="utf-8",
    )

    build(pilot_dir, raw_path)
    annotation_mapping = _json(pilot_dir / "annotation_mapping.json")
    if not isinstance(annotation_mapping, list):
        raise ValueError("annotation_mapping.json must be a list")

    adjudicated_path = pilot_dir / "ci_adjudicated_annotations.jsonl"
    rows = []
    for item in annotation_mapping:
        annotation_id = str(item["annotation_id"])
        blind_id = str(item["blind_id"])
        private = private_by_blind[blind_id]
        concerns = []
        if str(private["case_type"]) == "positive":
            concerns = [
                {
                    "issue_id": str(private["target_issue_id"]),
                    "severity": "major",
                    "anchors": ["paragraph:2"],
                }
            ]
        rows.append({"annotation_id": annotation_id, "concerns": concerns})

    adjudicated_path.write_text(
        "".join(json.dumps(row) + "\n" for row in rows),
        encoding="utf-8",
    )

    report = analyze(
        pilot_dir,
        adjudicated_path,
        iterations=250,
        seed=20260920,
    )
    for condition in ("generic", "skill-assisted"):
        observed = report["observed"][condition]
        if observed["essential_issue_recall"] != 1.0:
            raise ValueError("Self-test recall must be 1.0")
        if observed["target_specificity"] != 1.0:
            raise ValueError("Self-test specificity must be 1.0")
        if observed["paired_pass_rate"] != 1.0:
            raise ValueError("Self-test paired pass rate must be 1.0")

    if any(value != 0.0 for value in report["delta_skill_minus_generic"].values()):
        raise ValueError("Identical self-test arms must have zero delta")

    return {
        "status": "pass",
        "note": "CI scorer/harness oracle only; not model performance.",
        "annotation_packets": len(annotation_mapping),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("pilot_dir", type=Path)
    args = parser.parse_args()
    print(json.dumps(selftest(args.pilot_dir), indent=2))
