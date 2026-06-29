# Validation Results

Run before release:

```bash
python scripts/validate_package.py .
python -m compileall -q scripts
python -m pytest -q
```
