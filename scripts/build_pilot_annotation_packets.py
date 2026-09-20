from __future__ import annotations

import argparse
import json
import random
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CASES_PATH = ROOT / "benchmarks/controlled_v1/cases.jsonl"
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


def _shuffle_without_adjacent_case(
    rows: list[dict[str, Any]],
    mapping_by_blind: dict[str, dict[str, Any]],
    seed: int,
) -> list[dict[str, Any]]:
    rng = random.Random(seed)  # noqa: S311  # nosec B311
    for _attempt in range(10_000):
        candidate = list(rows)
        rng.shuffle(candidate)  # noqa: S311  # nosec B311
        case_ids = [str(mapping_by_blind[str(row["blind_id"])]["case_id"]) for row in candidate]
        if all(case_ids[index] != case_ids[index - 1] for index in range(1, len(case_ids))):
            return candidate
    raise RuntimeError("Could not construct annotation order without adjacent repeated cases")


def build(pilot_dir: Path, raw_outputs_path: Path) -> dict[str, Any]:
    mapping = _json(pilot_dir / "private_mapping.json")
    if not isinstance(mapping, list):
        raise ValueError("private_mapping.json must be a list")
    mapping_by_blind = {str(row["blind_id"]): row for row in mapping}

    raw = _jsonl(raw_outputs_path)
    raw_by_blind: dict[str, dict[str, Any]] = {}
    for row in raw:
        blind_id = str(row.get("blind_id", ""))
        review_text = str(row.get("review_text", ""))
        if not blind_id or not review_text.strip():
            raise ValueError("Each raw output needs blind_id and non-empty review_text")
        if blind_id in raw_by_blind:
            raise ValueError(f"Duplicate raw output for {blind_id}")
        if blind_id not in mapping_by_blind:
            raise ValueError(f"Unknown blind ID in raw outputs: {blind_id}")
        raw_by_blind[blind_id] = row

    expected = set(mapping_by_blind)
    actual = set(raw_by_blind)
    if actual != expected:
        missing = sorted(expected - actual)
        extra = sorted(actual - expected)
        raise ValueError(f"Raw output coverage mismatch; missing={missing}, extra={extra}")

    cases = _jsonl(CASES_PATH)
    case_by_id = {str(case["case_id"]): case for case in cases}
    config = _json(CONFIG_PATH)
    seed = int(config["randomization_seed"]) + 900_000

    ordered = _shuffle_without_adjacent_case(raw, mapping_by_blind, seed)

    annotation_rows: list[dict[str, Any]] = []
    annotation_mapping: list[dict[str, str]] = []
    for index, row in enumerate(ordered, 1):
        blind_id = str(row["blind_id"])
        private = mapping_by_blind[blind_id]
        case = case_by_id[str(private["case_id"])]
        annotation_id = f"A{index:06d}"
        annotation_rows.append(
            {
                "annotation_id": annotation_id,
                "domain": str(private["domain"]),
                "manuscript_text": str(case["manuscript_text"]),
                "review_text": str(row["review_text"]),
            }
        )
        annotation_mapping.append(
            {
                "annotation_id": annotation_id,
                "blind_id": blind_id,
            }
        )

    (pilot_dir / "annotation_packets.jsonl").write_text(
        "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in annotation_rows),
        encoding="utf-8",
    )
    (pilot_dir / "annotation_mapping.json").write_text(
        json.dumps(annotation_mapping, indent=2) + "\n",
        encoding="utf-8",
    )
    return {
        "annotation_packet_count": len(annotation_rows),
        "condition_exposed": False,
        "case_type_exposed": False,
        "target_issue_exposed": False,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--pilot-dir", type=Path, required=True)
    parser.add_argument("--raw-outputs", type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(build(args.pilot_dir, args.raw_outputs), indent=2))
