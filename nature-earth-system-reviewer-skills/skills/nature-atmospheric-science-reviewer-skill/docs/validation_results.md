# Validation results

Validation environment: local package smoke test.

```bash
python scripts/validate_package.py .
python -m compileall -q scripts
python -m pytest -q
python scripts/render_review_docx.py examples/example_review_report.md /tmp/example_review_report.docx
```

Results:

```text
PASS: package validation complete
compileall: PASS
pytest: 4 passed
DOCX smoke test: PASS
raw PDFs in release: 0
```

`ruff` and `bandit` are declared in `requirements-dev.txt`, configured in `pyproject.toml`, and included in CI. They were not available in the local runtime used for this smoke test.
