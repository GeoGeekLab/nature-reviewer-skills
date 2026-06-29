# Contributing

Contributions should preserve the skill's central contract: claim-dependent climate and ecology review with independent Nature-style referee output.

## Review expectations

Before submitting changes, run:

```bash
python scripts/validate_package.py .
python -m compileall -q scripts
python -m pytest -q
python -m ruff check .
python -m ruff format --check .
```

## Content standards

- Keep expressions concise, high-level and transferable.
- Do not add raw peer-review text or peer-review PDFs.
- Do not identify or infer anonymous reviewers.
- Do not expose internal gate routing in default review reports.
- Preserve 2-4 independent-referee output as the default report format.

## Code standards

- Keep scripts small and readable.
- Use `pathlib.Path` and explicit UTF-8 text IO.
- Add or update tests for behavior that should remain stable.
- Avoid unnecessary dependencies.
