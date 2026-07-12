from __future__ import annotations

import os
import zipfile
from dataclasses import dataclass
from pathlib import Path, PurePosixPath


class UnsafeInputError(ValueError):
    """Raised when an untrusted input violates defensive limits."""


@dataclass(frozen=True, slots=True)
class IngestionLimits:
    max_file_bytes: int = 25 * 1024 * 1024
    max_archive_uncompressed_bytes: int = 100 * 1024 * 1024
    max_archive_ratio: float = 100.0
    max_pdf_pages: int = 500
    max_extracted_characters: int = 5_000_000


SUPPORTED_SUFFIXES = {".txt", ".md", ".csv", ".json", ".jsonl", ".docx", ".pdf"}
DEFAULT_LIMITS = IngestionLimits()


def safe_input_path(path: Path, limits: IngestionLimits = DEFAULT_LIMITS) -> Path:
    expanded = path.expanduser()
    if expanded.is_symlink():
        raise UnsafeInputError("Symlink inputs are not accepted")
    resolved = expanded.resolve(strict=True)
    if not resolved.is_file():
        raise UnsafeInputError(f"Not a regular file: {path}")
    if resolved.suffix.casefold() not in SUPPORTED_SUFFIXES:
        raise UnsafeInputError(f"Unsupported input type: {resolved.suffix}")
    size = resolved.stat().st_size
    if size > limits.max_file_bytes:
        raise UnsafeInputError(f"Input exceeds {limits.max_file_bytes} bytes")
    return resolved


def inspect_zip(path: Path, limits: IngestionLimits = DEFAULT_LIMITS) -> None:
    with zipfile.ZipFile(path) as archive:
        total_uncompressed = 0
        total_compressed = 0
        for member in archive.infolist():
            member_path = PurePosixPath(member.filename)
            if member_path.is_absolute() or ".." in member_path.parts:
                raise UnsafeInputError(f"Archive path traversal: {member.filename}")
            unix_mode = member.external_attr >> 16
            if unix_mode and (unix_mode & 0o170000) == 0o120000:
                raise UnsafeInputError(f"Archive contains symlink: {member.filename}")
            total_uncompressed += member.file_size
            total_compressed += member.compress_size
            if total_uncompressed > limits.max_archive_uncompressed_bytes:
                raise UnsafeInputError("Archive uncompressed size limit exceeded")
        ratio = total_uncompressed / max(total_compressed, 1)
        if ratio > limits.max_archive_ratio:
            raise UnsafeInputError(f"Archive expansion ratio {ratio:.1f}:1 exceeds limit")


def bounded_text(text: str, limits: IngestionLimits = DEFAULT_LIMITS) -> str:
    if len(text) > limits.max_extracted_characters:
        raise UnsafeInputError("Extracted text exceeds configured character limit")
    return text


def atomic_write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    temporary.write_text(content, encoding="utf-8")
    temporary.replace(path)
