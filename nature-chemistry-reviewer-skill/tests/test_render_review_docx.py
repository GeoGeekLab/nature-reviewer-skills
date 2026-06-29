from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def test_render_review_docx(tmp_path: Path) -> None:
    root = Path(__file__).resolve().parents[1]
    output = tmp_path / 'example_review_report.docx'
    result = subprocess.run(
        [sys.executable, 'scripts/render_review_docx.py', 'examples/example_review_report.md', str(output)],
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr + result.stdout
    assert output.is_file()
    assert output.stat().st_size > 0
