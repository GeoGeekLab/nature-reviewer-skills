# Validation results

Validation was run from the repository root.

```bash
python scripts/validate_package.py .
python -m compileall -q scripts
python -m pytest -q
python scripts/render_review_docx.py examples/example_review_report.md /mnt/data/materials_skill_example_review_report.docx
```

Results:

```text
VALIDATION PASSED
3 passed
DOCX smoke render completed
```

`ruff` and `bandit` are listed in `requirements-dev.txt` and configured in GitHub Actions. They were not available in the local execution environment used for this package check.

Repository checks:

```text
Raw peer-review PDFs in repository: 0
Long original reviewer comments in repository: no
Non-verbatim review-unit index present: yes
Abstract reviewer pattern database present: yes
Corpus metadata folder present: yes
License files present: yes
CI workflow present: yes
```
