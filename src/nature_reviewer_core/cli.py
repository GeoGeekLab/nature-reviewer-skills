from __future__ import annotations

import argparse
import json
from pathlib import Path

from .evaluation import aggregate, load_case, load_predictions, score_case
from .patterns import load_patterns
from .retrieval import search_patterns
from .validation import validate_repository, validate_skill


def validate_main() -> int:
    parser = argparse.ArgumentParser(description="Validate Nature Reviewer skill packages")
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--repository", action="store_true")
    args = parser.parse_args()
    reports = validate_repository(args.root) if args.repository else [validate_skill(args.root)]
    failed = False
    for report in reports:
        print(f"[{'PASS' if report.ok else 'FAIL'}] {report.root} patterns={report.pattern_count}")
        for warning in report.warnings:
            print(f"  warning: {warning}")
        for error in report.errors:
            print(f"  error: {error}")
        failed |= not report.ok
    return int(failed)


def search_main() -> int:
    parser = argparse.ArgumentParser(description="Search a normalized reviewer-pattern database")
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--query", required=True)
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--no-diversify", action="store_true")
    args = parser.parse_args()
    results = search_patterns(
        load_patterns(args.root), args.query, limit=args.limit, diversify=not args.no_diversify
    )
    for result in results:
        print(
            json.dumps(
                {
                    "pattern_id": result.pattern.pattern_id,
                    "gate": result.pattern.gate,
                    "title": result.pattern.title,
                    "concern": result.pattern.concern,
                    "revision_direction": result.pattern.revision_direction,
                    "severity": result.pattern.severity,
                    "score": result.score,
                    "confidence": result.confidence,
                    "matched_terms": result.matched_terms,
                },
                ensure_ascii=False,
            )
        )
    return 0


def evaluate_main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate predictions against benchmark cases")
    parser.add_argument("cases", type=Path)
    parser.add_argument("predictions", type=Path)
    args = parser.parse_args()
    predictions = load_predictions(args.predictions)
    scores = [
        score_case(load_case(path), predictions.get(path.stem, []))
        for path in sorted(args.cases.glob("*.json"))
    ]
    print(
        json.dumps({"cases": scores, "aggregate": aggregate(scores)}, ensure_ascii=False, indent=2)
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(validate_main())
