"""Tests for package validation."""

from __future__ import annotations

from pathlib import Path

from scripts.validate_package import validate_package


def test_validate_current_package_passes() -> None:
    """The repository root should pass all package validation checks."""
    root = Path(__file__).resolve().parents[1]

    results = validate_package(root)

    assert all(result.is_valid for result in results)
