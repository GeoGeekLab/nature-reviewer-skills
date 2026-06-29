from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def test_validate_package_runs() -> None:
    root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [sys.executable, 'scripts/validate_package.py', str(root)],
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr + result.stdout
