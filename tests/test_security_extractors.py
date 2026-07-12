from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

import pytest

from nature_reviewer_core.extractors import extract_records
from nature_reviewer_core.security import (
    IngestionLimits,
    UnsafeInputError,
    inspect_zip,
    safe_input_path,
)


def test_rejects_unsupported_file(tmp_path: Path) -> None:
    path = tmp_path / "payload.exe"
    path.write_bytes(b"x")
    with pytest.raises(UnsafeInputError):
        safe_input_path(path)


def test_rejects_symlink_input(tmp_path: Path) -> None:
    target = tmp_path / "target.txt"
    target.write_text("content", encoding="utf-8")
    link = tmp_path / "link.txt"
    link.symlink_to(target)
    with pytest.raises(UnsafeInputError):
        safe_input_path(link)


def test_rejects_oversized_input(tmp_path: Path) -> None:
    path = tmp_path / "large.txt"
    path.write_text("123456", encoding="utf-8")
    with pytest.raises(UnsafeInputError):
        safe_input_path(path, IngestionLimits(max_file_bytes=5))


def test_rejects_zip_path_traversal(tmp_path: Path) -> None:
    path = tmp_path / "bad.docx"
    with ZipFile(path, "w", ZIP_DEFLATED) as archive:
        archive.writestr("../escape.txt", "bad")
    with pytest.raises(UnsafeInputError):
        inspect_zip(path)


def test_text_extraction_has_real_anchors(tmp_path: Path) -> None:
    path = tmp_path / "paper.md"
    path.write_text("Title\n\nA claim.\n", encoding="utf-8")
    records = extract_records(path)
    assert records == [
        {"source": "paper.md", "anchor": "line:1", "text": "Title"},
        {"source": "paper.md", "anchor": "line:3", "text": "A claim."},
    ]
