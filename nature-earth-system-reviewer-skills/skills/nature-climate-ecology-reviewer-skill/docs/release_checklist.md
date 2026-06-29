# Release Checklist

Before publishing a release:

- Confirm `SKILL.md`, `README.md`, `MANIFEST.json` and `summary.json` use the same version.
- Run `python scripts/validate_package.py .`.
- Run `python -m compileall -q scripts`.
- Run `python -m pytest -q`.
- Run `python -m ruff check .` and `python -m ruff format --check .`.
- Confirm no raw reviewer text or peer-review PDFs are included.
- Confirm generated review outputs are not committed unless intended as examples.
