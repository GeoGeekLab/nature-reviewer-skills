from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path


def search(patterns_csv: Path, query: str) -> list[dict[str, str]]:
    terms = [term.lower() for term in query.split() if term]
    with patterns_csv.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if not terms:
        return rows
    results = []
    for row in rows:
        haystack = " ".join(row.values()).lower()
        if all(term in haystack for term in terms):
            results.append(row)
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Search abstract reviewer patterns.")
    parser.add_argument("query", nargs="*", help="Search terms")
    parser.add_argument("--patterns", type=Path, default=Path("reviewer_db/patterns.csv"))
    args = parser.parse_args()
    rows = search(args.patterns, " ".join(args.query))
    for row in rows:
        print(f"{row['pattern_id']}\t{row['gate']}\t{row['pattern_name']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
