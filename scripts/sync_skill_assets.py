from __future__ import annotations

import json
from pathlib import Path

import _bootstrap  # noqa: F401

from nature_reviewer_core.sync import sync_repository

ROOT = Path(__file__).resolve().parents[1]

if __name__ == "__main__":
    print(json.dumps(sync_repository(ROOT), ensure_ascii=False, indent=2))
