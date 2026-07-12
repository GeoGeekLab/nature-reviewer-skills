# Polar Earth-System Review Reorganization Report

## Final placement

The Polar Earth-System Review product is installed at:

```text
nature-earth-system-reviewer-skills/skills/polar-earth-system-review-orchestrator/
```

It is colocated with the four foundational Earth-system reviewer skills for discoverability and repository consistency.

## Taxonomy preservation

The product remains an upper-layer orchestrator rather than an eighth foundational domain skill. Classification now uses `MANIFEST.json`:

```json
{
  "package_type": "orchestrator"
}
```

Repository discovery, synchronization, validation, tests, and CI read this manifest field instead of inferring package type solely from the directory name.

## Files and references updated

- moved the complete polar package under `nature-earth-system-reviewer-skills/skills/`;
- renamed the directory to `polar-earth-system-review-orchestrator`;
- updated root README and the Earth-system umbrella README;
- updated CI package-matrix paths;
- updated routing and discovery tests;
- updated package commands and documentation paths;
- updated the root manifest product identifier;
- updated the router and reviewer-pattern domain identifier;
- preserved all 104 polar reviewer patterns, 13 gates, 42 provenance sources, benchmark fixtures, scripts, and tests;
- removed the obsolete top-level `orchestrators/` directory.

## Validation results

- repository taxonomy: 7 domain skills + 1 orchestrator;
- repository packages validated: 8/8;
- total patterns: 644;
- polar patterns: 104;
- root test suite: 18/18;
- independent package tests: 21/21;
- Ruff lint: passed;
- Ruff format: 66 files passed;
- MyPy strict: 13 source modules passed;
- Bandit: no reported findings;
- benchmark pipeline: passed;
- no raw peer-review PDFs distributed.
