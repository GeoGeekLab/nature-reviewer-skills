# Nature Earth-System Reviewer Skills

This directory contains the four foundational Earth-system reviewer skills and one cross-disciplinary polar review orchestrator. All packages are independently validatable and use the shared runtime from the monorepo root.

## Foundational domain skills

- `nature-atmospheric-science-reviewer-skill/`
- `nature-climate-ecology-reviewer-skill/`
- `nature-hydrology-reviewer-skill/`
- `nature-remote-sensing-reviewer-skill/`

## Cross-disciplinary orchestrator

- `polar-earth-system-review-orchestrator/`

The polar package is stored alongside the Earth-system skills for discoverability, but its `MANIFEST.json` declares `package_type: orchestrator`. It therefore remains an upper-layer routing and synthesis component rather than an eighth foundational domain skill.

Run installation, synchronization, validation, and tests from the monorepo root.
