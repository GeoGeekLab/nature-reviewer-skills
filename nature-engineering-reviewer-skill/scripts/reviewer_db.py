#!/usr/bin/env python3
"""Search local abstracted reviewer-memory records.

The script searches JSONL and CSV files under ``reviewer_db`` without requiring
raw peer-review PDFs. It is intentionally schema-tolerant because the reviewer
skills use domain-specific pattern fields.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections.abc import Iterator, Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any

SEARCH_EXTENSIONS = {".jsonl", ".csv"}
TEXT_WEIGHTS = {
    "pattern_name": 5,
    "name": 5,
    "gate": 4,
    "claim_type": 4,
    "evidence_risk": 4,
    "reviewer_concern": 4,
    "revision_direction": 4,
    "trigger": 3,
    "requested_action": 3,
    "requested_actions": 3,
    "why_it_matters": 3,
    "safe_phrase": 2,
    "style": 2,
    "description": 2,
    "text": 1,
}


@dataclass(frozen=True, slots=True)
class SearchRecord:
    """One searchable reviewer-memory record."""

    source_file: str
    line_number: int
    payload: Mapping[str, Any]


def tokenize(text: str) -> list[str]:
    """Return normalized query terms."""
    return re.findall(r"[a-z0-9_+.-]+", text.lower())


def flatten(value: object) -> str:
    """Flatten nested JSON-like values into searchable text."""
    if isinstance(value, Mapping):
        return " ".join(flatten(item) for item in value.values())
    if isinstance(value, list | tuple | set):
        return " ".join(flatten(item) for item in value)
    return str(value)


def iter_jsonl_records(path: Path, root: Path) -> Iterator[SearchRecord]:
    """Yield records from a JSONL file."""
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            stripped = line.strip()
            if not stripped:
                continue
            payload = json.loads(stripped)
            if isinstance(payload, Mapping):
                yield SearchRecord(str(path.relative_to(root)), line_number, payload)


def iter_csv_records(path: Path, root: Path) -> Iterator[SearchRecord]:
    """Yield records from a CSV file."""
    with path.open("r", encoding="utf-8", newline="") as handle:
        for line_number, row in enumerate(csv.DictReader(handle), start=2):
            yield SearchRecord(str(path.relative_to(root)), line_number, row)


def iter_records(db: Path) -> Iterator[SearchRecord]:
    """Yield searchable records from supported reviewer_db files."""
    root = db.parent
    for path in sorted(db.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in SEARCH_EXTENSIONS:
            continue
        if path.suffix.lower() == ".jsonl":
            yield from iter_jsonl_records(path, root)
        elif path.suffix.lower() == ".csv":
            yield from iter_csv_records(path, root)


def score_payload(payload: Mapping[str, Any], query_terms: list[str]) -> int:
    """Score one record against query terms."""
    score = 0
    for key, value in payload.items():
        text = flatten(value).lower()
        if not text:
            continue
        weight = TEXT_WEIGHTS.get(str(key), 1)
        for term in query_terms:
            if term in text:
                score += weight * (1 + text.count(term) // 3)
    return score


def label(payload: Mapping[str, Any]) -> str:
    """Return a compact human-readable record label."""
    for key in ("pattern_id", "pattern_name", "gate", "name", "unit_id"):
        value = payload.get(key)
        if value:
            return str(value)
    return "record"


def snippet(payload: Mapping[str, Any]) -> str:
    """Return a short non-authoritative preview of the record."""
    for key in ("reviewer_concern", "revision_direction", "evidence_risk", "trigger", "description", "text"):
        value = payload.get(key)
        if value:
            text = re.sub(r"\s+", " ", flatten(value)).strip()
            return text[:240] + ("..." if len(text) > 240 else "")
    text = re.sub(r"\s+", " ", flatten(payload)).strip()
    return text[:240] + ("..." if len(text) > 240 else "")


def search(db: Path, query: str, limit: int) -> int:
    """Search reviewer-memory records and print ranked hits."""
    if not db.exists():
        print(f"Reviewer DB not found: {db}")
        return 1
    query_terms = tokenize(query)
    if not query_terms:
        print("No query terms supplied.")
        return 0

    results: list[tuple[int, SearchRecord]] = []
    for record in iter_records(db):
        score = score_payload(record.payload, query_terms)
        if score > 0:
            results.append((score, record))
    results.sort(key=lambda item: (-item[0], item[1].source_file, item[1].line_number))

    if not results:
        print("No results found.")
        return 0
    for rank, (score, record) in enumerate(results[:limit], start=1):
        print(f"{rank}. [{record.source_file}:{record.line_number}] {label(record.payload)} (score={score})")
        print(f"   {snippet(record.payload)}")
    return 0


def main() -> int:
    """Run the command-line interface."""
    parser = argparse.ArgumentParser(description="Search local reviewer behavior memory.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    search_parser = subparsers.add_parser("search", help="Search reviewer memory.")
    search_parser.add_argument("query")
    search_parser.add_argument("--db", default="reviewer_db")
    search_parser.add_argument("--limit", type=int, default=8)
    args = parser.parse_args()

    if args.command == "search":
        return search(Path(args.db), args.query, args.limit)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
