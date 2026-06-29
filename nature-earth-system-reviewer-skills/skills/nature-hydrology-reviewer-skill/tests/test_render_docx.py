from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_render_review_docx(tmp_path: Path) -> None:
    out = tmp_path / 'example.docx'
    subprocess.run(
        [
            sys.executable,
            str(ROOT / 'scripts/render_review_docx.py'),
            str(ROOT / 'examples/example_review_report.md'),
            str(out),
        ],
        check=True,
    )
    assert out.exists()
    assert out.stat().st_size > 1000
