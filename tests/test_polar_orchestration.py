from pathlib import Path

from nature_reviewer_core.orchestration import load_router, route_text

ROOT = Path(__file__).resolve().parents[1]
ROUTER = load_router(
    ROOT
    / "nature-earth-system-reviewer-skills/skills/polar-earth-system-review-orchestrator/router.json"
)


def test_multi_domain_routing() -> None:
    result = route_text(
        "Antarctic ice-shelf basal melt from radar observations and an ocean model",
        ROUTER,
    )
    assert "ice_sheet_glacier" in result["routes"]
    assert "polar_instrumentation" in result["routes"]
    assert "nature-hydrology-reviewer-skill" in result["skills"]
    assert "mass_energy_water_budget" in result["gates"]


def test_no_unfounded_domain_guess() -> None:
    result = route_text("A general manuscript with no polar subsystem description", ROUTER)
    assert result["routes"] == []
    assert result["skills"] == []
    assert "regional_scope_seasonality" in result["gates"]


def test_conditional_responsibility_review() -> None:
    result = route_text("Arctic community and Indigenous knowledge co-production", ROUTER)
    assert result["responsibility_review"] is True
