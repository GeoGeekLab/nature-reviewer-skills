from pathlib import Path

from nature_reviewer_core.orchestration import load_router, route_text
from nature_reviewer_core.patterns import load_patterns
from nature_reviewer_core.retrieval import search_patterns
from nature_reviewer_core.validation import validate_skill

ROOT = Path(__file__).resolve().parents[1]


def test_package_validates() -> None:
    report = validate_skill(ROOT)
    assert report.ok, report.errors
    assert report.pattern_count == 104


def test_route_sea_ice_remote_sensing() -> None:
    result = route_text(
        "Arctic sea ice concentration from passive microwave sensors",
        load_router(ROOT / "router.json"),
    )
    assert "sea_ice" in result["routes"]
    assert "nature-remote-sensing-reviewer-skill" in result["skills"]


def test_ethics_trigger() -> None:
    result = route_text(
        "Indigenous knowledge and community observations in Arctic research",
        load_router(ROOT / "router.json"),
    )
    assert result["responsibility_review"] is True


def test_search_returns_polar_pattern() -> None:
    results = search_patterns(load_patterns(ROOT), "sea ice sensor transition uncertainty", limit=5)
    assert results
    assert any("sensor" in r.pattern.searchable_text().casefold() for r in results)


def test_corpus_counts_and_no_raw_pdfs() -> None:
    import csv

    rows = list(csv.DictReader((ROOT / "corpus/index.csv").open(encoding="utf-8")))
    assert len(rows) == 42
    assert sum(row["source_id"].startswith("NP-") for row in rows) == 24
    assert sum(row["source_id"].startswith("TC-") for row in rows) == 10
    assert sum(row["source_id"].startswith("STD-") for row in rows) == 8
    assert not list(ROOT.rglob("*.pdf"))


def test_pattern_source_ids_resolve() -> None:
    import csv
    import json

    source_ids = {
        row["source_id"]
        for row in csv.DictReader((ROOT / "corpus/index.csv").open(encoding="utf-8"))
    }
    for pattern in load_patterns(ROOT):
        nested = pattern.raw.get("source_fields", "")
        if nested:
            metadata = json.loads(str(nested))
            assert set(metadata.get("source_ids", [])) <= source_ids


def test_all_router_gates_have_patterns() -> None:
    router = load_router(ROOT / "router.json")
    pattern_gates = {pattern.gate for pattern in load_patterns(ROOT)}
    configured = set(router.get("always_apply", []))
    configured.update(gate for route in router["routes"] for gate in route.get("gates", []))
    assert configured <= pattern_gates
