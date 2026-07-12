from pathlib import Path

from nature_reviewer_core.discovery import discover_orchestrator_roots, discover_skill_roots
from nature_reviewer_core.validation import validate_repository

ROOT = Path(__file__).resolve().parents[1]


def test_discovers_seven_skills_and_one_orchestrator() -> None:
    skills = discover_skill_roots(ROOT)
    orchestrators = discover_orchestrator_roots(ROOT)
    assert len(skills) == 7
    assert len({skill.name for skill in skills}) == 7
    assert [item.name for item in orchestrators] == ["polar-earth-system-review-orchestrator"]
    assert orchestrators[0].relative_to(ROOT).as_posix() == (
        "nature-earth-system-reviewer-skills/skills/polar-earth-system-review-orchestrator"
    )


def test_repository_validates() -> None:
    reports = validate_repository(ROOT)
    assert all(report.ok for report in reports), [
        (report.root, report.errors) for report in reports
    ]
    assert sum(report.pattern_count for report in reports) >= 644
