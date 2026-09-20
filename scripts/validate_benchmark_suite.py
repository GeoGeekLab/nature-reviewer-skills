from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


def _load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _load_cases(source: Path) -> list[dict[str, Any]]:
    if source.is_dir():
        files = sorted(source.glob("*.json"))
        if not files:
            raise ValueError(f"No benchmark cases found in {source}")
        return [_load(path) for path in files]

    if source.suffix == ".jsonl":
        cases: list[dict[str, Any]] = []
        with source.open("r", encoding="utf-8") as handle:
            for number, line in enumerate(handle, 1):
                if not line.strip():
                    continue
                value = json.loads(line)
                if not isinstance(value, dict):
                    raise ValueError(f"Expected object at {source}:{number}")
                cases.append(value)
        if not cases:
            raise ValueError(f"No benchmark cases found in {source}")
        return cases

    raise ValueError(f"Unsupported benchmark case source: {source}")


def validate_suite(source: Path) -> dict[str, Any]:
    cases = _load_cases(source)
    case_ids = [str(case["case_id"]) for case in cases]
    if len(case_ids) != len(set(case_ids)):
        raise ValueError("Duplicate case_id values found")

    by_pair: dict[str, list[dict[str, Any]]] = defaultdict(list)
    domain_counts: Counter[str] = Counter()

    for case in cases:
        case_id = str(case["case_id"])
        case_type = str(case.get("case_type", ""))
        pair_id = str(case.get("pair_id", ""))
        domain = str(case.get("domain", ""))
        source_keys = case.get("source_keys", [])
        text = str(case.get("manuscript_text", ""))
        concerns = case.get("gold_concerns", [])

        if case_type not in {"positive", "negative_control"}:
            raise ValueError(f"{case_id}: unsupported case_type {case_type}")
        if not pair_id:
            raise ValueError(f"{case_id}: missing pair_id")
        if not domain:
            raise ValueError(f"{case_id}: missing domain")
        if not isinstance(source_keys, list) or not source_keys:
            raise ValueError(f"{case_id}: source_keys must be a non-empty list")
        if len(text) < 250:
            raise ValueError(f"{case_id}: manuscript_text is too short for a diagnostic case")
        if case_type == "positive" and len(concerns) != 1:
            raise ValueError(f"{case_id}: positive cases must contain exactly one gold concern")
        if case_type == "negative_control" and concerns:
            raise ValueError(f"{case_id}: negative controls must have no gold concerns")

        by_pair[pair_id].append(case)
        domain_counts[domain] += 1

    for pair_id, pair in by_pair.items():
        if len(pair) != 2:
            raise ValueError(f"{pair_id}: expected exactly two matched cases")
        types = {str(item["case_type"]) for item in pair}
        if types != {"positive", "negative_control"}:
            raise ValueError(f"{pair_id}: pair must contain one positive and one negative control")
        domains = {str(item["domain"]) for item in pair}
        challenges = {str(item.get("challenge", "")) for item in pair}
        if len(domains) != 1 or len(challenges) != 1:
            raise ValueError(f"{pair_id}: domain/challenge mismatch within pair")
        texts = {str(item["manuscript_text"]) for item in pair}
        if len(texts) != 2:
            raise ValueError(f"{pair_id}: positive and control text must differ")

    if len(set(domain_counts.values())) != 1:
        raise ValueError(f"Unbalanced domain case counts: {dict(domain_counts)}")

    return {
        "case_count": len(cases),
        "pair_count": len(by_pair),
        "domain_count": len(domain_counts),
        "cases_per_domain": dict(sorted(domain_counts.items())),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("cases", type=Path)
    args = parser.parse_args()
    print(json.dumps(validate_suite(args.cases), indent=2))
