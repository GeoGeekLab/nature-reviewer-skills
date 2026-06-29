from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

REQUIRED_ROOT = [
    'README.md', 'SKILL.md', 'MANIFEST.json', 'LICENSE', 'LICENSE-MIT', 'LICENSE-APACHE',
    'CHANGELOG.md', 'CONTRIBUTING.md', 'CODE_OF_CONDUCT.md', 'SECURITY.md',
    'pyproject.toml', 'requirements-dev.txt', '.gitignore', '.editorconfig',
]
REQUIRED_DIRS = [
    '.github/workflows', '.github/ISSUE_TEMPLATE', 'references', 'reviewer_db', 'templates',
    'scripts', 'tests', 'docs', 'examples', '_internal', 'corpus'
]
REQUIRED_FILES = [
    '.github/workflows/ci.yml', '.github/PULL_REQUEST_TEMPLATE.md',
    '.github/ISSUE_TEMPLATE/bug_report.md', '.github/ISSUE_TEMPLATE/feature_request.md',
    'references/referee_voice_style_gate.md', 'references/classic_hydrology_stress_test_gate.md', 'reviewer_db/patterns.csv',
    'reviewer_db/patterns.jsonl', '_internal/review_unit_index.csv',
    'docs/distillation_report.md', 'docs/distillation_qc.csv', 'summary.json',
]


def fail(msg: str) -> None:
    raise SystemExit(f'VALIDATION FAILED: {msg}')


def validate(root: Path) -> None:
    for rel in REQUIRED_ROOT + REQUIRED_FILES:
        if not (root / rel).is_file():
            fail(f'missing file: {rel}')
    for rel in REQUIRED_DIRS:
        if not (root / rel).is_dir():
            fail(f'missing directory: {rel}')

    skill = (root / 'SKILL.md').read_text(encoding='utf-8')
    if not skill.startswith('---'):
        fail('SKILL.md missing YAML front matter')
    if 'Reviewer Reports on the Initial Version' not in skill:
        fail('SKILL.md missing Nature-style output format')
    if 'gate routing' not in skill.lower():
        fail('SKILL.md should instruct not to expose gate routing')
    if 'short exact manuscript phrase' not in skill:
        fail('SKILL.md missing close-reading quotation guidance')

    manifest = json.loads((root / 'MANIFEST.json').read_text(encoding='utf-8'))
    if manifest.get('skill_name') != 'nature-hydrology-reviewer':
        fail('MANIFEST.json skill_name mismatch')
    if manifest.get('license') != 'MIT OR Apache-2.0':
        fail('MANIFEST.json license mismatch')
    if manifest.get('classic_stress_tests_weighted') is not False:
        fail('classic stress tests must be non-weighted')


    example = (root / 'examples/example_review_report.md').read_text(encoding='utf-8')
    referee_count = example.count('Referee #')
    if not 2 <= referee_count <= 4:
        fail(f'example_review_report.md should contain 2-4 referees, found {referee_count}')
    if 'Overall judgment:' not in example:
        fail('example_review_report.md missing Overall judgment section')

    with (root / 'reviewer_db/patterns.csv').open(newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    jsonl_rows = [json.loads(line) for line in (root / 'reviewer_db/patterns.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
    if len(rows) != len(jsonl_rows):
        fail('patterns.csv and patterns.jsonl are not synchronized')
    if len(rows) < 100:
        fail('patterns.csv should contain at least 100 abstracted patterns')
    required_cols = {'pattern_id','gate','claim_type','evidence_risk','reviewer_concern','revision_direction'}
    if not required_cols.issubset(rows[0].keys()):
        fail('patterns.csv missing required columns')
    if any('Reviewer #' in (r.get('reviewer_concern','') + r.get('revision_direction','')) for r in rows):
        fail('patterns.csv appears to contain raw reviewer markers')

    with (root / '_internal/review_unit_index.csv').open(newline='', encoding='utf-8') as f:
        unit_rows = list(csv.DictReader(f))
    if not unit_rows:
        fail('review_unit_index.csv is empty')
    if 'raw_text_stored' not in unit_rows[0]:
        fail('review_unit_index.csv missing raw_text_stored column')
    if any(str(r.get('raw_text_stored')).lower() == 'true' for r in unit_rows):
        fail('raw text is marked as stored in review unit index')

    print('Package validation passed')


def main() -> None:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')
    validate(root.resolve())


if __name__ == '__main__':
    main()
