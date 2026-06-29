from __future__ import annotations

from pathlib import Path

from scripts.render_review_docx import render_docx


def test_render_review_docx(tmp_path: Path) -> None:
    root = Path(__file__).resolve().parents[1]
    output = tmp_path / "example.docx"
    render_docx(root / "examples" / "example_review_report.md", output)
    assert output.exists()
    assert output.stat().st_size > 0
