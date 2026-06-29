from __future__ import annotations

import argparse
import sys
from pathlib import Path

from docx import Document


def add_markdown_line(document: Document, line: str) -> None:
    stripped = line.strip()
    if not stripped:
        document.add_paragraph("")
        return
    if stripped.startswith("# "):
        document.add_heading(stripped[2:], level=1)
    elif stripped.startswith("## "):
        document.add_heading(stripped[3:], level=2)
    elif stripped.startswith("### "):
        document.add_heading(stripped[4:], level=3)
    elif stripped.startswith("- "):
        document.add_paragraph(stripped[2:], style="List Bullet")
    elif stripped[:3].replace(".", "").isdigit() and ". " in stripped[:5]:
        document.add_paragraph(stripped, style="List Number")
    else:
        document.add_paragraph(stripped)


def render_docx(input_md: Path, output_docx: Path) -> None:
    if not input_md.exists():
        raise FileNotFoundError(f"Input Markdown not found: {input_md}")
    document = Document()
    for line in input_md.read_text(encoding="utf-8").splitlines():
        add_markdown_line(document, line)
    output_docx.parent.mkdir(parents=True, exist_ok=True)
    document.save(output_docx)


def main() -> int:
    parser = argparse.ArgumentParser(description="Render a Markdown review report to DOCX.")
    parser.add_argument("input_md", type=Path)
    parser.add_argument("output_docx", type=Path)
    args = parser.parse_args()
    render_docx(args.input_md, args.output_docx)
    print(f"Wrote {args.output_docx}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
