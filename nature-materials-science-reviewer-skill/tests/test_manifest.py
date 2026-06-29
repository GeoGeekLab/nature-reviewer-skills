from __future__ import annotations

import json
from pathlib import Path


def test_manifest_name() -> None:
    root = Path(__file__).resolve().parents[1]
    manifest = json.loads((root / 'MANIFEST.json').read_text(encoding='utf-8'))
    assert manifest['name'] == 'nature-materials-science-reviewer-skill'
    assert manifest['license'] == 'MIT OR Apache-2.0'


def test_patterns_exist() -> None:
    root = Path(__file__).resolve().parents[1]
    rows = (root / 'reviewer_db' / 'patterns.csv').read_text(encoding='utf-8').splitlines()
    assert len(rows) > 20
