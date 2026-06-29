# Validation results

Validation date: 2026-06-25

Local environment notes:

- `ruff` and `bandit` were not installed in the execution environment.
- Both tools are included in `requirements-dev.txt` and in GitHub Actions CI.

## Local checks run

```text
python scripts/validate_package.py .
Result: PASS

python -m compileall -q scripts
Result: PASS

python -m pytest -q
Result: PASS, 9 tests passed

python scripts/render_review_docx.py examples/example_review_report.md /tmp/example_review_report.docx
Result: PASS, DOCX smoke-test file created
```

## CI-covered checks

The GitHub Actions workflow `.github/workflows/ci.yml` runs:

```text
python scripts/validate_package.py .
python -m compileall -q scripts
python -m pytest -q
python -m ruff check .
python -m ruff format --check .
python -m bandit -q -r scripts
python scripts/render_review_docx.py examples/example_review_report.md /tmp/example_review_report.docx
```


Validation coverage:

- Pattern database count: 158
- `patterns.csv` and `patterns.jsonl` are synchronized.
- Example review contains 3 independent referees, major comments, specific comments and figure/table/method-level anchors.
- No raw peer-review PDF or raw reviewer text is included in the repository.
