from __future__ import annotations

from pathlib import Path


def test_earth_system_skills_remain_independent() -> None:
    root = Path(__file__).resolve().parents[1]
    expected = [
        'nature-remote-sensing-reviewer-skill',
        'nature-atmospheric-science-reviewer-skill',
        'nature-hydrology-reviewer-skill',
        'nature-climate-ecology-reviewer-skill',
    ]
    for name in expected:
        skill_root = root / 'skills' / name
        assert (skill_root / 'SKILL.md').is_file()
        assert (skill_root / 'MANIFEST.json').is_file()
        assert (skill_root / 'reviewer_db').is_dir()
        assert (skill_root / 'references').is_dir()
