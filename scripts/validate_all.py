from __future__ import annotations

from pathlib import Path

import _bootstrap  # noqa: F401

from nature_reviewer_core.validation import validate_repository

ROOT = Path(__file__).resolve().parents[1]

if __name__ == "__main__":
    reports = validate_repository(ROOT)
    failed = False
    for report in reports:
        print(
            f"[{'PASS' if report.ok else 'FAIL'}] {report.root.relative_to(ROOT)} patterns={report.pattern_count}"
        )
        for warning in report.warnings:
            print(f"  warning: {warning}")
        for error in report.errors:
            print(f"  error: {error}")
        failed |= not report.ok
    raise SystemExit(int(failed))
