# Changelog

## 2.2.0 - Controlled evaluation and adoption release

### Added

- Public CRD-v1 controlled diagnostic benchmark with 48 synthetic excerpts in 24 matched counterfactual pairs across seven domain reviewers plus the polar orchestrator.
- Gold-free benchmark execution packets, target-specific specificity scoring, paired-pass metrics, and pair-cluster bootstrap confidence intervals.
- Frozen generic and skill-assisted review prompts plus validation and comparison tooling for reproducible controlled experiments.
- Three independent 60-second synthetic examples covering remote-sensing harmonization, chemistry quantification integrity, and engineering autonomy boundaries.
- Preregistered three-domain blinded pilot harness covering remote sensing, chemistry, and engineering with 18 cases, 9 matched pairs, and 3 repeated runs per condition.

### Changed

- Refocused the project README around claim/evidence stress testing, practical adoption, transparent limitations, and direct domain entry points.
- Standardized active package, runtime, skill, and README version metadata at 2.2.0.
- Standardized active skill license declarations to MIT to match repository and manifest licensing.

### Evaluation boundary

- CRD-v1 is a public, synthetic, skill-aligned controlled diagnostic benchmark.
- Included oracle predictions are scorer/harness self-tests, not model-performance results.
- This release does not claim independent expert validation, expert equivalence, editorial-decision accuracy, or prospective real-manuscript performance.
- Automated provisional annotation experiments are not part of the v2.2.0 release claims.

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
