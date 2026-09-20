from __future__ import annotations

import argparse
import hashlib
import json
import random
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "benchmarks/pilot_v1/config.json"
CASES_PATH = ROOT / "benchmarks/controlled_v1/cases.jsonl"
GENERIC_PROMPT_PATH = ROOT / "benchmarks/controlled_v1/prompts/generic_review.md"
SKILL_PROMPT_PATH = ROOT / "benchmarks/controlled_v1/prompts/skill_assisted_review.md"

SKILL_PATHS = {
    "remote-sensing": (
        "nature-earth-system-reviewer-skills/skills/nature-remote-sensing-reviewer-skill"
    ),
    "chemistry": "nature-chemistry-reviewer-skill",
    "engineering": "nature-engineering-reviewer-skill",
}


def _read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"Expected JSON object in {path}")
    return value


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            value = json.loads(line)
            if not isinstance(value, dict):
                raise ValueError(f"Expected JSON object at {path}:{number}")
            records.append(value)
    return records


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _safe_order(
    records: list[dict[str, Any]],
    *,
    seed: int,
) -> list[dict[str, Any]]:
    rng = random.Random(seed)  # noqa: S311  # nosec B311
    for _attempt in range(10_000):
        candidate = list(records)
        rng.shuffle(candidate)  # noqa: S311  # nosec B311
        if all(
            str(candidate[index]["pair_id"]) != str(candidate[index - 1]["pair_id"])
            for index in range(1, len(candidate))
        ):
            return candidate
    raise RuntimeError("Could not construct a non-adjacent pair ordering")


def prepare(model_id: str, output: Path) -> dict[str, Any]:
    if not model_id.strip():
        raise ValueError("--model-id must be a non-empty exact model/version identifier")

    config = _read_json(CONFIG_PATH)
    domains = {str(value) for value in config["domains"]}
    source_cases = _read_jsonl(CASES_PATH)
    selected = [case for case in source_cases if str(case.get("domain")) in domains]

    expected_cases = int(config["expected_cases"])
    expected_pairs = int(config["expected_pairs"])
    runs_per_case = int(config["runs_per_case"])
    seed = int(config["randomization_seed"])

    if len(selected) != expected_cases:
        raise ValueError(f"Expected {expected_cases} selected cases, found {len(selected)}")
    pair_ids = {str(case["pair_id"]) for case in selected}
    if len(pair_ids) != expected_pairs:
        raise ValueError(f"Expected {expected_pairs} selected pairs, found {len(pair_ids)}")

    by_domain: dict[str, int] = {}
    for case in selected:
        domain = str(case["domain"])
        by_domain[domain] = by_domain.get(domain, 0) + 1
        if domain not in SKILL_PATHS:
            raise ValueError(f"No skill path configured for domain {domain}")

    output.mkdir(parents=True, exist_ok=True)
    packet_dir = output / "execution_packets"
    packet_dir.mkdir(parents=True, exist_ok=True)

    generic_prompt = GENERIC_PROMPT_PATH.read_text(encoding="utf-8").strip()
    skill_prompt = SKILL_PROMPT_PATH.read_text(encoding="utf-8").strip()

    mapping: list[dict[str, Any]] = []
    blind_counter = 0

    conditions = [str(value) for value in config["conditions"]]
    for condition_index, condition in enumerate(conditions):
        if condition not in {"generic", "skill-assisted"}:
            raise ValueError(f"Unsupported condition: {condition}")
        for run_index in range(1, runs_per_case + 1):
            order_seed = seed + condition_index * 100_000 + run_index
            ordered = _safe_order(selected, seed=order_seed)
            packet_path = packet_dir / f"{condition}_run_{run_index:02d}.jsonl"

            packet_records: list[dict[str, Any]] = []
            for position, case in enumerate(ordered, 1):
                blind_counter += 1
                blind_id = f"B{blind_counter:06d}"
                domain = str(case["domain"])
                packet: dict[str, Any] = {
                    "blind_id": blind_id,
                    "prompt": generic_prompt if condition == "generic" else skill_prompt,
                    "manuscript_text": str(case["manuscript_text"]),
                }
                if condition == "skill-assisted":
                    packet["skill_path"] = SKILL_PATHS[domain]
                packet_records.append(packet)

                mapping.append(
                    {
                        "blind_id": blind_id,
                        "condition": condition,
                        "run_index": run_index,
                        "position": position,
                        "case_id": str(case["case_id"]),
                        "pair_id": str(case["pair_id"]),
                        "case_type": str(case["case_type"]),
                        "domain": domain,
                        "challenge": str(case["challenge"]),
                        "target_issue_id": str(case["target_issue_id"]),
                    }
                )

            packet_path.write_text(
                "".join(json.dumps(record, ensure_ascii=False) + "\n" for record in packet_records),
                encoding="utf-8",
            )

    mapping_path = output / "private_mapping.json"
    mapping_path.write_text(json.dumps(mapping, indent=2) + "\n", encoding="utf-8")

    manifest = {
        "pilot_id": str(config["pilot_id"]),
        "model_id": model_id,
        "source_suite": str(config["source_suite"]),
        "domains": sorted(domains),
        "case_count": len(selected),
        "pair_count": len(pair_ids),
        "runs_per_case": runs_per_case,
        "condition_count": len(conditions),
        "expected_raw_outputs": len(mapping),
        "randomization_seed": seed,
        "config_sha256": _sha256(CONFIG_PATH),
        "cases_sha256": _sha256(CASES_PATH),
        "generic_prompt_sha256": _sha256(GENERIC_PROMPT_PATH),
        "skill_prompt_sha256": _sha256(SKILL_PROMPT_PATH),
        "by_domain": dict(sorted(by_domain.items())),
        "inference_policy": config["inference_policy"],
        "private_mapping": "DO NOT PROVIDE TO TESTED MODEL OR INITIAL ANNOTATORS",
    }
    (output / "run_manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n",
        encoding="utf-8",
    )
    return manifest


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-id", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(prepare(args.model_id, args.output), indent=2))
