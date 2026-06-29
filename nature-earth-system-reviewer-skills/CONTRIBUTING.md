# Contributing

Contributions should be small, reviewable, and consistent with the existing skill structure. Do not add raw peer-review PDFs, long verbatim reviewer reports, or non-public reviewer material.

Before opening a pull request, run:

```bash
python scripts/validate_package.py .
python -m compileall -q scripts
python -m pytest -q
```
