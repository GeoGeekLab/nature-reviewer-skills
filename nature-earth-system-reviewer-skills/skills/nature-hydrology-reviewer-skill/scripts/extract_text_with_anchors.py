#!/usr/bin/env python3
"""Extract readable manuscript text with stable review anchors.

Supported formats are plain text, Markdown, CSV, DOCX, and PDF when ``pypdf`` is
available. Generated anchors are review aids; they are not original line numbers
unless the source already contains line numbers.
"""

from __future__ import annotations

import argparse
import re
import zipfile
from collections.abc import Iterable
from pathlib import Path
from xml.etree import ElementTree as ET

WORD_NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def clean_text(value: str) -> str:
    """Normalize whitespace in extracted text."""
    return re.sub(r"\s+", " ", value or "").strip()


def extract_docx(path: Path) -> list[str]:
    """Extract paragraphs from a DOCX file without external dependencies."""
    paragraphs: list[str] = []
    with zipfile.ZipFile(path) as archive:
        names = [name for name in archive.namelist() if name.startswith("word/") and name.endswith(".xml")]
        preferred = ["word/document.xml"] + [
            name for name in names if name.startswith(("word/footnotes", "word/endnotes"))
        ]
        seen: set[str] = set()
        for name in preferred:
            if name not in names or name in seen:
                continue
            seen.add(name)
            root = ET.fromstring(archive.read(name))
            for paragraph in root.findall(".//w:p", WORD_NS):
                parts = [node.text for node in paragraph.findall(".//w:t", WORD_NS) if node.text]
                text = clean_text("".join(parts))
                if text:
                    paragraphs.append(text)
    return paragraphs


def extract_text(path: Path) -> list[str]:
    """Extract non-empty lines from a UTF-8-compatible text file."""
    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    return [cleaned for line in lines if (cleaned := clean_text(line))]


def extract_pdf(path: Path) -> list[str]:
    """Extract PDF text when pypdf is available."""
    try:
        from pypdf import PdfReader  # type: ignore[import-not-found]
    except ImportError:
        return [f"[PDF text extraction unavailable without pypdf: {path.name}]"]

    reader = PdfReader(str(path))
    output: list[str] = []
    for page_number, page in enumerate(reader.pages, start=1):
        page_text = page.extract_text() or ""
        for line in page_text.splitlines():
            text = clean_text(line)
            if text:
                output.append(f"[Page {page_number}] {text}")
    return output


def extract_any(path: Path) -> list[str]:
    """Extract readable text from a supported file."""
    suffix = path.suffix.lower()
    if suffix == ".docx":
        return extract_docx(path)
    if suffix in {".txt", ".md", ".markdown", ".csv"}:
        return extract_text(path)
    if suffix == ".pdf":
        return extract_pdf(path)
    return [f"[Unsupported file type for anchored extraction: {path.name}]"]


def write_anchored(source: Path, paragraphs: Iterable[str], output: Path, prefix: str) -> None:
    """Write extracted paragraphs with stable generated anchors."""
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as handle:
        handle.write(f"# Anchored extraction for {source.name}\n\n")
        handle.write(
            "These anchors are generated from extracted readable text for review-specific "
            "referencing. They are not original manuscript line numbers unless the source "
            "text already contained line numbers.\n\n"
        )
        for index, paragraph in enumerate(paragraphs, start=1):
            handle.write(f"[{prefix}{index:04d}] {paragraph}\n\n")


def safe_stem(path: Path) -> str:
    """Return a filesystem-safe output stem."""
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", path.stem)[:80] or "file"


def main() -> int:
    """Run the command-line interface."""
    parser = argparse.ArgumentParser(description="Extract anchored text for manuscript review.")
    parser.add_argument("inputs", nargs="+", help="Input manuscript or supplement files")
    parser.add_argument("--out-dir", default="review_inputs_extracted")
    parser.add_argument("--prefix", default="P")
    args = parser.parse_args()

    output_dir = Path(args.out_dir)
    outputs: list[Path] = []
    for file_index, item in enumerate(args.inputs, start=1):
        source = Path(item)
        paragraphs = extract_any(source)
        output = output_dir / f"{file_index:02d}_{safe_stem(source)}_anchored.md"
        write_anchored(source, paragraphs, output, f"{args.prefix}{file_index:02d}-")
        outputs.append(output)

    for output in outputs:
        print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
