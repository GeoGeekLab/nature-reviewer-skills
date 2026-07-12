from __future__ import annotations

import argparse
import json
from pathlib import Path

import _bootstrap  # noqa: F401

from nature_reviewer_core.evaluation import aggregate, load_case, load_predictions, score_case

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("cases", type=Path)
    parser.add_argument("predictions", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    predictions = load_predictions(args.predictions)
    scores = []
    for path in sorted(args.cases.glob("*.json")):
        case = load_case(path)
        scores.append(score_case(case, predictions.get(case.case_id, [])))
    report = {"cases": scores, "aggregate": aggregate(scores)}
    rendered = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
