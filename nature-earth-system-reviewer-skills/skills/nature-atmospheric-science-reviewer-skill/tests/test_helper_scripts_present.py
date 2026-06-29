from __future__ import annotations

import ast
from pathlib import Path


def test_common_helper_scripts_are_present_and_parseable() -> None:
    root = Path(__file__).resolve().parents[1]
    required = [
        'scripts/extract_text_with_anchors.py',
        'scripts/published_paper_query_builder.py',
        'scripts/reviewer_db.py',
        'scripts/sample_referee_style.py',
    ]
    for relative_path in required:
        path = root / relative_path
        assert path.is_file(), relative_path
        ast.parse(path.read_text(encoding='utf-8'))
