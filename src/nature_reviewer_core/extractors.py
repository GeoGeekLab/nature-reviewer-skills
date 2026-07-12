from __future__ import annotations

import csv
import io
import json
import re
import zipfile
from pathlib import Path

from defusedxml.ElementTree import fromstring  # type: ignore[import-untyped]

from .security import (
    DEFAULT_LIMITS,
    IngestionLimits,
    UnsafeInputError,
    bounded_text,
    inspect_zip,
    safe_input_path,
)

ANCHOR_RE = re.compile(r"\s+")


def _records_from_text(text: str, source: str) -> list[dict[str, str | int]]:
    records: list[dict[str, str | int]] = []
    for number, raw_line in enumerate(text.splitlines(), 1):
        line = ANCHOR_RE.sub(" ", raw_line).strip()
        if line:
            records.append({"source": source, "anchor": f"line:{number}", "text": line})
    return records


def _extract_docx(path: Path, limits: IngestionLimits) -> list[dict[str, str | int]]:
    inspect_zip(path, limits)
    with zipfile.ZipFile(path) as archive:
        try:
            xml = archive.read("word/document.xml")
        except KeyError as exc:
            raise UnsafeInputError("DOCX has no word/document.xml") from exc
    root = fromstring(xml)
    namespace = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    records: list[dict[str, str | int]] = []
    characters = 0
    for index, paragraph in enumerate(root.findall(".//w:p", namespace), 1):
        text = "".join(node.text or "" for node in paragraph.findall(".//w:t", namespace)).strip()
        if text:
            characters += len(text)
            if characters > limits.max_extracted_characters:
                raise UnsafeInputError("Extracted DOCX text exceeds limit")
            records.append({"source": path.name, "anchor": f"paragraph:{index}", "text": text})
    return records


def _extract_pdf(path: Path, limits: IngestionLimits) -> list[dict[str, str | int]]:
    try:
        from pypdf import PdfReader
    except ImportError as exc:
        raise RuntimeError(
            "PDF support requires `pip install nature-reviewer-core[documents]`"
        ) from exc
    reader = PdfReader(str(path), strict=True)
    if reader.is_encrypted:
        raise UnsafeInputError("Encrypted PDF inputs are not accepted")
    if len(reader.pages) > limits.max_pdf_pages:
        raise UnsafeInputError(f"PDF exceeds {limits.max_pdf_pages} pages")
    records: list[dict[str, str | int]] = []
    characters = 0
    for page_number, page in enumerate(reader.pages, 1):
        text = page.extract_text() or ""
        characters += len(text)
        if characters > limits.max_extracted_characters:
            raise UnsafeInputError("Extracted PDF text exceeds limit")
        for paragraph_number, paragraph in enumerate(text.split("\n\n"), 1):
            cleaned = ANCHOR_RE.sub(" ", paragraph).strip()
            if cleaned:
                records.append(
                    {
                        "source": path.name,
                        "anchor": f"page:{page_number}:block:{paragraph_number}",
                        "text": cleaned,
                    }
                )
    return records


def extract_records(
    path: Path, limits: IngestionLimits = DEFAULT_LIMITS
) -> list[dict[str, str | int]]:
    safe = safe_input_path(path, limits)
    suffix = safe.suffix.casefold()
    if suffix in {".txt", ".md"}:
        text = bounded_text(safe.read_text(encoding="utf-8", errors="strict"), limits)
        return _records_from_text(text, safe.name)
    if suffix == ".csv":
        text = bounded_text(safe.read_text(encoding="utf-8-sig", errors="strict"), limits)
        records: list[dict[str, str | int]] = []
        for row_number, row in enumerate(csv.reader(io.StringIO(text)), 1):
            records.append(
                {"source": safe.name, "anchor": f"row:{row_number}", "text": " | ".join(row)}
            )
        return records
    if suffix in {".json", ".jsonl"}:
        text = bounded_text(safe.read_text(encoding="utf-8", errors="strict"), limits)
        if suffix == ".json":
            json.loads(text)
        else:
            for number, line in enumerate(text.splitlines(), 1):
                if line.strip():
                    try:
                        json.loads(line)
                    except json.JSONDecodeError as exc:
                        raise ValueError(f"Invalid JSONL line {number}") from exc
        return _records_from_text(text, safe.name)
    if suffix == ".docx":
        return _extract_docx(safe, limits)
    if suffix == ".pdf":
        return _extract_pdf(safe, limits)
    raise AssertionError("safe_input_path should reject unsupported suffixes")
