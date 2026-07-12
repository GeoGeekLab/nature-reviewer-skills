# Changelog

## 2.1.0 - Polar Earth-System Review Orchestrator

### Added

- One upper-layer Polar Earth-System Review Orchestrator without changing the seven-skill domain taxonomy.
- 104 non-verbatim polar reviewer patterns distilled from 34 public peer-review files and eight official sources.
- Claim routing, distinct reviewer roles, polar evidence gates, source provenance, negative-control benchmarks and package tests.
- Shared deterministic routing utilities and explicit discovery of orchestrators.

### Changed

- Repository validation now requires seven domain skills plus one orchestrator.
- Asset synchronization and pattern tests cover all review packages.

## 2.0.0 — Reliability and evaluation refactor

### Added
- Root-level matrix CI and repository-wide discovery.
- Shared typed runtime for loading, normalizing, searching, validating, extracting, and evaluating.
- BM25-style retrieval with field weights, phrase boosts, synonym expansion, confidence labels, and MMR diversification.
- Defensive document ingestion limits and ZIP/DOCX expansion checks.
- Gold-case and prediction schemas with quantitative benchmark metrics.
- Reviewer-panel perspective contracts and duplicate-concern detection.
- Uniform manifests, generated JSONL databases, summaries, tests, templates, and security documentation for all seven skills.

### Changed
- Standardized package licensing to MIT at the refactor layer.
- Replaced duplicated package scripts with thin wrappers around one shared implementation.
- Added explicit scientific-evidence boundaries to every skill.

### Known limitations
- Synthetic benchmark fixtures validate infrastructure, not expert-level reviewing quality.
- Semantic retrieval is deterministic and dependency-free; it is not an embedding model.
- Figures, spectra, equations, and chemical structures still require a multimodal reviewer runtime.
