from __future__ import annotations

from pathlib import Path

from scripts.validate_package import validate_package


def test_validate_package_root() -> None:
    validate_package(Path(__file__).resolve().parents[1])
