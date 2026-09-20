from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "benchmarks/pilot_v1/config.json"
CASES_PATH = ROOT / "benchmarks/controlled_v1/cases.jsonl"
GENERIC_PROMPT_PATH = ROOT / "benchmarks/controlled_v1/prompts/generic_review.md"
SKILL_PROMPT_PATH = ROOT / "benchmarks/controlled_v1/prompts/skill_assisted_review.md"

FORBIDDEN_PACKET_KEYS = {
    "case_id",
    "pair_id",
    "case_type",
    "challenge",
    "target_issue_id",
    "source_keys",
    "gold_concerns",
    "oracle_predictions",
}


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


def validate(pilot_dir: Path) -> dict[str, Any]:
    config = _json(CONFIG_PATH)
    cases = _jsonl(CASES_PATH)
    case_by_id = {str(case["case_id"]): case for case in cases}

    manifest = _json(pilot_dir / "run_manifest.json")
    mapping = _json(pilot_dir / "private_mapping.json")
    if not isinstance(manifest, dict) or not isinstance(mapping, list):
        raise ValueError("Invalid pilot manifest or private mapping")

    expected_cases = int(config["expected_cases"])
    runs_per_case = int(config["runs_per_case"])
    conditions = [str(value) for value in config["conditions"]]
    expected_outputs = expected_cases * runs_per_case * len(conditions)

    if len(mapping) != expected_outputs:
        raise ValueError(f"Expected {expected_outputs} mappings, found {len(mapping)}")

    blind_ids = [str(row["blind_id"]) for row in mapping]
    if len(blind_ids) != len(set(blind_ids)):
        raise ValueError("Duplicate blind IDs in private mapping")

    mapping_by_packet: dict[tuple[str, int], list[dict[str, Any]]] = defaultdict(list)
    for row in mapping:
        mapping_by_packet[(str(row["condition"]), int(row["run_index"]))].append(row)

    generic_prompt = GENERIC_PROMPT_PATH.read_text(encoding="utf-8").strip()
    skill_prompt = SKILL_PROMPT_PATH.read_text(encoding="utf-8").strip()
    packet_total = 0

    for condition in conditions:
        for run_index in range(1, runs_per_case + 1):
            key = (condition, run_index)
            mapped = sorted(mapping_by_packet[key], key=lambda row: int(row["position"]))
            if len(mapped) != expected_cases:
                raise ValueError(f"{condition} run {run_index}: wrong mapping count")

            case_ids = [str(row["case_id"]) for row in mapped]
            if len(case_ids) != len(set(case_ids)):
                raise ValueError(f"{condition} run {run_index}: duplicate case")

            pair_ids = [str(row["pair_id"]) for row in mapped]
            if any(pair_ids[index] == pair_ids[index - 1] for index in range(1, len(pair_ids))):
                raise ValueError(f"{condition} run {run_index}: adjacent pair counterparts")

            packet_path = (
                pilot_dir / "execution_packets" / f"{condition}_run_{run_index:02d}.jsonl"
            )
            packets = _jsonl(packet_path)
            if len(packets) != expected_cases:
                raise ValueError(f"{packet_path}: wrong packet count")

            for packet, row in zip(packets, mapped, strict=True):
                packet_total += 1
                forbidden = FORBIDDEN_PACKET_KEYS & set(packet)
                if forbidden:
                    raise ValueError(f"{packet_path}: leaked forbidden keys {sorted(forbidden)}")
                if str(packet.get("blind_id")) != str(row["blind_id"]):
                    raise ValueError(f"{packet_path}: blind ID mismatch")

                source_case = case_by_id[str(row["case_id"])]
                if str(packet.get("manuscript_text")) != str(source_case["manuscript_text"]):
                    raise ValueError(f"{packet_path}: manuscript text mismatch")

                expected_prompt = generic_prompt if condition == "generic" else skill_prompt
                if str(packet.get("prompt")) != expected_prompt:
                    raise ValueError(f"{packet_path}: frozen prompt mismatch")

                if condition == "generic" and "skill_path" in packet:
                    raise ValueError(f"{packet_path}: generic packet contains skill_path")
                if condition == "skill-assisted" and not str(packet.get("skill_path", "")):
                    raise ValueError(f"{packet_path}: skill-assisted packet lacks skill_path")

    if packet_total != expected_outputs:
        raise ValueError("Packet total does not match expected output count")

    return {
        "pilot_id": manifest["pilot_id"],
        "model_id": manifest["model_id"],
        "packet_count": packet_total,
        "mapping_count": len(mapping),
        "conditions": len(conditions),
        "runs_per_case": runs_per_case,
        "gold_metadata_in_execution_packets": False,
        "adjacent_pair_counterparts": False,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("pilot_dir", type=Path)
    args = parser.parse_args()
    print(json.dumps(validate(args.pilot_dir), indent=2))
