from __future__ import annotations

import json
from pathlib import Path

from scripts.validate_package import validate

ROOT = Path(__file__).resolve().parents[1]


def test_required_files_present() -> None:
    assert validate(ROOT) == []


def test_manifest_release_boundary() -> None:
    data = json.loads((ROOT / 'MANIFEST.json').read_text(encoding='utf-8'))
    assert data['distillation']['raw_reviewer_text_in_release'] is False
    assert data['distillation']['raw_pdfs_in_release'] is False


def test_patterns_nonverbatim() -> None:
    text = (ROOT / 'reviewer_db/patterns.csv').read_text(encoding='utf-8')
    assert 'not_stored' in text
    assert 'verbatim_reviewer_text' in text


def test_review_template_has_referee_sections() -> None:
    text = (ROOT / 'templates/review_report_template.md').read_text(encoding='utf-8')
    assert 'Major comments:' in text
    assert 'Specific comments:' in text
    assert 'Overall judgment:' in text
