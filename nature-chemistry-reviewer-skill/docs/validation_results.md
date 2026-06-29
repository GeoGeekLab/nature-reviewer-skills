# Validation results

Package: nature-chemistry-reviewer-skill-v1.0

Validated commands:

```bash
python scripts/validate_package.py .
python -m compileall -q scripts
python -m pytest -q
python scripts/render_review_docx.py examples/example_review_report.md /tmp/example_review_report.docx
```

Results:

```text
validation passed
compileall passed
2 passed
DOCX smoke test passed
```

Additional CI checks configured but not available in this local runtime:

```bash
python -m ruff check .
python -m ruff format --check .
python -m bandit -q -r scripts
```

Ruff and Bandit are included in `requirements-dev.txt`, `pyproject.toml`, and the GitHub Actions workflow.
