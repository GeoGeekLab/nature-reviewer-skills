from pathlib import Path

from nature_reviewer_core.discovery import discover_skill_roots
from nature_reviewer_core.validation import validate_repository

ROOT = Path(__file__).resolve().parents[1]


def test_discovers_exactly_seven_skills() -> None:
    skills = discover_skill_roots(ROOT)
    assert len(skills) == 7
    assert len({skill.name for skill in skills}) == 7


def test_repository_validates() -> None:
    reports = validate_repository(ROOT)
    assert all(report.ok for report in reports), [
        (report.root, report.errors) for report in reports
    ]
    assert sum(report.pattern_count for report in reports) >= 540
