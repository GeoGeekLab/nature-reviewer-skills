# Migration from 1.x package-local scripts

Existing commands remain available from each skill's `scripts/` folder. They now locate the repository root and call `nature_reviewer_core`. Standalone deployment can copy the selected skill plus `src/nature_reviewer_core`, or install the root package before copying the skill.

Run `python scripts/sync_skill_assets.py` after editing a source CSV. This regenerates `patterns.jsonl`, `summary.json`, checksums, and manifests deterministically.
