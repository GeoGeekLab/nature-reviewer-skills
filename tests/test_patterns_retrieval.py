from pathlib import Path

from nature_reviewer_core.discovery import discover_review_package_roots
from nature_reviewer_core.patterns import load_patterns
from nature_reviewer_core.retrieval import search_patterns, tokenize

ROOT = Path(__file__).resolve().parents[1]


def test_unicode_tokenization() -> None:
    assert "cross-validation" in tokenize("Cross-validation and uncertainty")


def test_all_source_schemas_normalize() -> None:
    for skill in discover_review_package_roots(ROOT):
        patterns = load_patterns(skill)
        assert patterns
        assert all(
            item.pattern_id and item.concern and item.revision_direction for item in patterns
        )


def test_query_expansion_finds_mechanism_pattern() -> None:
    chemistry = ROOT / "nature-chemistry-reviewer-skill"
    results = search_patterns(load_patterns(chemistry), "causal mechanism alternatives", limit=5)
    assert results
    assert any("mechan" in item.pattern.searchable_text().casefold() for item in results)


def test_diversification_avoids_identical_ids() -> None:
    chemistry = ROOT / "nature-chemistry-reviewer-skill"
    results = search_patterns(load_patterns(chemistry), "evidence validation uncertainty", limit=10)
    assert len({item.pattern.pattern_id for item in results}) == len(results)
