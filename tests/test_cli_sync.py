import json
from pathlib import Path

from nature_reviewer_core.discovery import discover_review_package_roots
from nature_reviewer_core.sync import sync_repository

ROOT = Path(__file__).resolve().parents[1]


def test_sync_is_deterministic() -> None:
    first = sync_repository(ROOT)
    hashes_one = {
        skill.name: json.loads((skill / "reviewer_db/summary.json").read_text(encoding="utf-8"))[
            "normalized_sha256"
        ]
        for skill in discover_review_package_roots(ROOT)
    }
    second = sync_repository(ROOT)
    hashes_two = {
        skill.name: json.loads((skill / "reviewer_db/summary.json").read_text(encoding="utf-8"))[
            "normalized_sha256"
        ]
        for skill in discover_review_package_roots(ROOT)
    }
    assert first == second
    assert hashes_one == hashes_two
