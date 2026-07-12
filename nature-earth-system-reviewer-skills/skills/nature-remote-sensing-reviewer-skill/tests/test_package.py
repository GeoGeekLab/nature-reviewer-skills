from pathlib import Path

from nature_reviewer_core.patterns import load_patterns
from nature_reviewer_core.retrieval import search_patterns
from nature_reviewer_core.validation import validate_skill

ROOT = Path(__file__).resolve().parents[1]


def test_package_validates() -> None:
    report = validate_skill(ROOT)
    assert report.ok, report.errors
    assert report.pattern_count >= 20


def test_database_search_returns_revision_direction() -> None:
    results = search_patterns(load_patterns(ROOT), "validation uncertainty mechanism", limit=3)
    assert results
    assert all(item.pattern.revision_direction for item in results)
