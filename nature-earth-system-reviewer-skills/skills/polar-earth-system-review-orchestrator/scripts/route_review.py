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

from nature_reviewer_core.orchestration import load_router, route_text  # noqa: E402

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", required=True)
    parser.add_argument("--root", type=Path, default=HERE.parents[1])
    args = parser.parse_args()
    result = route_text(args.text, load_router(args.root / "router.json"))
    print(json.dumps(result, ensure_ascii=False, indent=2))
