from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve()
for candidate in HERE.parents:
    source = candidate / "src"
    if (source / "nature_reviewer_core").is_dir():
        sys.path.insert(0, str(source))
        break
else:
    raise SystemExit("Install nature-reviewer-core or run this script inside the monorepo")

from nature_reviewer_core.patterns import load_patterns  # noqa: E402
from nature_reviewer_core.retrieval import search_patterns  # noqa: E402

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=HERE.parents[1])
    parser.add_argument("--query", required=True)
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--no-diversify", action="store_true")
    args = parser.parse_args()
    for result in search_patterns(
        load_patterns(args.root), args.query, limit=args.limit, diversify=not args.no_diversify
    ):
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
