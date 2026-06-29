from __future__ import annotations

from pathlib import Path


def test_required_repository_files_exist() -> None:
    root = Path(__file__).resolve().parents[1]
    required = [
        'README.md',
        'SKILL.md',
        'MANIFEST.json',
        'pyproject.toml',
        'scripts/validate_package.py',
        'scripts/render_review_docx.py',
        'scripts/extract_text_with_anchors.py',
        'scripts/published_paper_query_builder.py',
        'scripts/reviewer_db.py',
        'scripts/sample_referee_style.py',
    ]
    missing = [path for path in required if not (root / path).exists()]
    assert missing == []
