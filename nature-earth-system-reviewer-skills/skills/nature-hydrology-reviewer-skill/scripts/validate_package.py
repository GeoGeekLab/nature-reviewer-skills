from __future__ import annotations

import argparse
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

from nature_reviewer_core.validation import validate_skill  # noqa: E402

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=HERE.parents[1])
    args = parser.parse_args()
    report = validate_skill(args.root)
    print(f"[{'PASS' if report.ok else 'FAIL'}] patterns={report.pattern_count}")
    for warning in report.warnings:
        print(f"warning: {warning}")
    for error in report.errors:
        print(f"error: {error}")
    raise SystemExit(int(not report.ok))
