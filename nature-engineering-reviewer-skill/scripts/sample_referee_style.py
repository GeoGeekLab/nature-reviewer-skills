#!/usr/bin/env python3
"""Inspect short referee-style motifs in local abstracted reviewer memory.

This helper is for package maintenance. It avoids long reproduced passages and
works with schema differences across the reviewer skills.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections.abc import Iterator, Mapping
from pathlib import Path
from typing import Any

MOTIFS = (
    r"\bmajor concern\b",
    r"\bnot convinced\b",
    r"\bshould clarify\b",
    r"\bshould provide\b",
    r"\bI suggest\b",
    r"\buncertainty\b",
    r"\bvalidation\b",
    r"\bbenchmark\b",
    r"\bcontrol\b",
    r"\bmechanism\b",
)

TEXT_KEYS = (
    "safe_phrase",
    "reviewer_concern",
    "revision_direction",
    "evidence_risk",
    "review_language",
    "language_patterns",
    "text",
)


def flatten(value: object) -> str:
    """Flatten nested JSON-like values."""
    if isinstance(value, Mapping):
        return " ".join(flatten(item) for item in value.values())
    if isinstance(value, list | tuple | set):
        return " ".join(flatten(item) for item in value)
    return str(value)


def iter_jsonl(path: Path) -> Iterator[Mapping[str, Any]]:
    """Yield JSON objects from a JSONL file."""
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            stripped = line.strip()
            if not stripped:
                continue
            row = json.loads(stripped)
            if isinstance(row, Mapping):
                yield row


def iter_csv(path: Path) -> Iterator[Mapping[str, Any]]:
    """Yield rows from a CSV file."""
    with path.open("r", encoding="utf-8", newline="") as handle:
        yield from csv.DictReader(handle)


def iter_records(db: Path) -> Iterator[tuple[str, Mapping[str, Any]]]:
    """Yield records from local reviewer-memory files."""
    for path in sorted(db.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix.lower() == ".jsonl":
            for row in iter_jsonl(path):
                yield str(path.relative_to(db)), row
        elif path.suffix.lower() == ".csv":
            for row in iter_csv(path):
                yield str(path.relative_to(db)), row


def preview(row: Mapping[str, Any]) -> str:
    """Return a short style preview from safe fields."""
    for key in TEXT_KEYS:
        if row.get(key):
            text = re.sub(r"\s+", " ", flatten(row[key])).strip()
            return text[:180] + ("..." if len(text) > 180 else "")
    text = re.sub(r"\s+", " ", flatten(row)).strip()
    return text[:180] + ("..." if len(text) > 180 else "")


def record_id(row: Mapping[str, Any]) -> str:
    """Return a compact record identifier."""
    for key in ("pattern_id", "unit_id", "profile_id", "gate", "pattern_name"):
        if row.get(key):
            return str(row[key])
    return "record"


def main() -> int:
    """Run the command-line interface."""
    parser = argparse.ArgumentParser(description="Sample short referee-style motifs.")
    parser.add_argument("--db", default="reviewer_db")
    parser.add_argument("--limit", type=int, default=20)
    args = parser.parse_args()
    db = Path(args.db)
    if not db.exists():
        print(f"Reviewer DB not found: {db}")
        return 1

    hits: list[dict[str, str]] = []
    for source, row in iter_records(db):
        text = preview(row)
        for motif in MOTIFS:
            if re.search(motif, text, flags=re.IGNORECASE):
                hits.append({"source": source, "id": record_id(row), "motif": motif, "preview": text})
                break
        if len(hits) >= args.limit:
            break

    if not hits:
        print("No motif hits found.")
        return 0
    for hit in hits:
        print(json.dumps(hit, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
