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

from nature_reviewer_core.extractors import extract_records  # noqa: E402
from nature_reviewer_core.security import IngestionLimits, atomic_write_text  # noqa: E402

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--max-file-mib", type=int, default=25)
    parser.add_argument("--max-pages", type=int, default=500)
    args = parser.parse_args()
    limits = IngestionLimits(
        max_file_bytes=args.max_file_mib * 1024 * 1024, max_pdf_pages=args.max_pages
    )
    records = extract_records(args.input, limits)
    atomic_write_text(
        args.output, "".join(json.dumps(record, ensure_ascii=False) + "\n" for record in records)
    )
    print(f"wrote {len(records)} anchored records to {args.output}")
