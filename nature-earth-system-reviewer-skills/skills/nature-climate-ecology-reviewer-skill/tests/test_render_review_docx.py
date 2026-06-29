"""Tests for Markdown-to-DOCX rendering."""

from __future__ import annotations

from pathlib import Path

from scripts.render_review_docx import render_markdown_to_docx


def test_render_markdown_to_docx_creates_nonempty_file(tmp_path: Path) -> None:
    """The renderer should create a non-empty DOCX from a referee report."""
    source_path = tmp_path / "review.md"
    output_path = tmp_path / "review.docx"
    source_path.write_text(
        "Reviewer Reports on the Initial Version:\n\n"
        "Referees' comments:\n\n"
        "Referee #1 (Remarks to the Author):\n\n"
        "The central claim is not fully established.\n",
        encoding="utf-8",
    )

    render_markdown_to_docx(source_path, output_path)

    assert output_path.exists()
    assert output_path.stat().st_size > 0
