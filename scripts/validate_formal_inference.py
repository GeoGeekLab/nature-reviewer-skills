from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
LOCK_PATH = ROOT / "benchmarks/pilot_v1/FORMAL_INFERENCE_LOCK_QWEN25_3B.json"


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
                raise ValueError(f"Expected JSON object at {path}:{number}")
            rows.append(value)
    return rows


def validate(pilot_dir: Path) -> dict[str, Any]:
    lock = _json(LOCK_PATH)
    raw = _jsonl(pilot_dir / "raw_outputs.jsonl")
    metadata = _jsonl(pilot_dir / "inference_metadata.jsonl")
    private_mapping = _json(pilot_dir / "private_mapping.json")
    if not isinstance(private_mapping, list):
        raise ValueError("private_mapping.json must be a list")

    expected = int(lock["execution"]["expected_raw_outputs"])
    if len(raw) != expected or len(metadata) != expected:
        raise ValueError(
            f"Expected {expected} raw/metadata rows; found raw={len(raw)}, metadata={len(metadata)}"
        )

    raw_ids = [str(row.get("blind_id", "")) for row in raw]
    meta_ids = [str(row.get("blind_id", "")) for row in metadata]
    mapping_ids = [str(row.get("blind_id", "")) for row in private_mapping]
    if len(set(raw_ids)) != expected:
        raise ValueError("Raw outputs do not have exactly one unique blind_id each")
    if set(raw_ids) != set(meta_ids) or set(raw_ids) != set(mapping_ids):
        raise ValueError("Raw outputs, metadata, and private mapping cover different blind IDs")

    for row in raw:
        if set(row) != {"blind_id", "review_text"}:
            raise ValueError("Raw outputs must contain only blind_id and review_text")
        if not str(row["review_text"]).strip():
            raise ValueError(f"{row['blind_id']}: empty review_text")

    counts = Counter((str(row["condition"]), int(row["run_index"])) for row in metadata)
    expected_counts = {
        (condition, run_index): 18
        for condition in ("generic", "skill-assisted")
        for run_index in (1, 2, 3)
    }
    if counts != expected_counts:
        raise ValueError(f"Unexpected condition/run counts: {dict(counts)}")

    seeds = lock["generation"]["run_seeds"]
    for row in metadata:
        expected_seed = int(seeds[str(row["run_index"])])
        if int(row["seed"]) != expected_seed:
            raise ValueError(f"{row['blind_id']}: seed mismatch")
        if row["condition"] == "generic" and row["skill_context_sha256"] is not None:
            raise ValueError(f"{row['blind_id']}: generic arm has skill context")
        if row["condition"] == "skill-assisted" and not row["skill_context_sha256"]:
            raise ValueError(f"{row['blind_id']}: skill arm lacks skill context hash")

    summary = _json(pilot_dir / "formal_inference_summary.json")
    if not isinstance(summary, dict):
        raise ValueError("formal_inference_summary.json must be an object")
    raw_sha = hashlib.sha256((pilot_dir / "raw_outputs.jsonl").read_bytes()).hexdigest()
    meta_sha = hashlib.sha256((pilot_dir / "inference_metadata.jsonl").read_bytes()).hexdigest()
    if summary.get("raw_outputs_sha256") != raw_sha:
        raise ValueError("Raw-output checksum mismatch")
    if summary.get("inference_metadata_sha256") != meta_sha:
        raise ValueError("Inference-metadata checksum mismatch")

    return {
        "status": "pass",
        "raw_output_count": len(raw),
        "generic_outputs": sum(1 for row in metadata if row["condition"] == "generic"),
        "skill_assisted_outputs": sum(
            1 for row in metadata if row["condition"] == "skill-assisted"
        ),
        "runs_per_condition": {
            f"{condition}-run-{run_index}": counts[(condition, run_index)]
            for condition in ("generic", "skill-assisted")
            for run_index in (1, 2, 3)
        },
        "raw_outputs_sha256": raw_sha,
        "inference_metadata_sha256": meta_sha,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("pilot_dir", type=Path)
    args = parser.parse_args()
    print(json.dumps(validate(args.pilot_dir), indent=2))
