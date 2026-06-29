from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

REQUIRED_PATHS = [
    'README.md', 'SKILL.md', 'MANIFEST.json', 'LICENSE', 'LICENSE-MIT', 'LICENSE-APACHE',
    'CHANGELOG.md', 'CONTRIBUTING.md', 'CODE_OF_CONDUCT.md', 'SECURITY.md',
    'pyproject.toml', 'requirements-dev.txt', '.gitignore', '.editorconfig',
    '.github/workflows/ci.yml',
    '.github/PULL_REQUEST_TEMPLATE.md',
    '.github/ISSUE_TEMPLATE/bug_report.md',
    'references/referee_voice_style_gate.md',
    'reviewer_db/patterns.csv',
    'reviewer_db/patterns.jsonl',
    'reviewer_db/gate_router.yaml', 'templates/nature_style_review.md',
    'scripts/render_review_docx.py',
    'scripts/extract_text_with_anchors.py',
    'scripts/published_paper_query_builder.py',
    'scripts/reviewer_db.py',
    'scripts/sample_referee_style.py', 'tests/test_manifest.py', 'docs/distillation_report.md',
    'docs/distillation_qc.csv', '_internal/review_unit_index.csv', 'summary.json'
]

FORBIDDEN_SUFFIXES = {'.pdf'}


def fail(message: str) -> None:
    raise SystemExit(f'VALIDATION FAILED: {message}')


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open('r', encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


def validate(root: Path) -> None:
    if not root.exists():
        fail(f'root does not exist: {root}')
    for rel in REQUIRED_PATHS:
        if not (root / rel).exists():
            fail(f'missing required path: {rel}')
    manifest = json.loads((root / 'MANIFEST.json').read_text(encoding='utf-8'))
    if manifest.get('name') != 'nature-materials-science-reviewer-skill':
        fail('MANIFEST.json has unexpected name')
    skill = (root / 'SKILL.md').read_text(encoding='utf-8')
    skill_name = 'name: nature-materials-science-reviewer'
    if not skill.startswith('---') or skill_name not in skill:
        fail('SKILL.md front matter is missing or invalid')
    patterns = read_csv_rows(root / 'reviewer_db/patterns.csv')
    if len(patterns) < 20:
        fail('patterns.csv has too few abstract reviewer patterns')
    units = read_csv_rows(root / '_internal/review_unit_index.csv')
    if len(units) < 100:
        fail('review_unit_index.csv has too few non-verbatim units')
    if any(row.get('non_verbatim') != 'true' for row in units[:100]):
        fail('review_unit_index.csv must mark units as non_verbatim=true')
    for p in root.rglob('*'):
        if p.is_file() and p.suffix.lower() in FORBIDDEN_SUFFIXES:
            fail(f'raw PDF found in repository: {p.relative_to(root)}')
    print('VALIDATION PASSED')


def main() -> int:
    parser = argparse.ArgumentParser(
        description='Validate the materials science reviewer skill package.'
    )
    parser.add_argument('root', type=Path)
    args = parser.parse_args()
    validate(args.root.resolve())
    return 0

if __name__ == '__main__':
    sys.exit(main())
