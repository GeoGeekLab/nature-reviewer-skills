# Polar Earth-System Review Orchestrator - Product Report

## Product definition

This release adds one upper-layer Polar Earth-System Review Orchestrator while preserving the repository taxonomy of seven foundational domain reviewer skills. The orchestrator routes a polar manuscript to the relevant existing skills, applies polar-specific evidence gates, assigns distinct reviewer responsibilities, and synthesizes a deduplicated review.

## Repository placement

The product is installed at `nature-earth-system-reviewer-skills/skills/polar-earth-system-review-orchestrator/`. It is colocated with the Earth-system skills for discoverability, while `package_type: orchestrator` keeps the taxonomy at seven foundational domain skills plus one upper-layer polar orchestrator.

## Source collection

- 34 downloaded and hash-verified public peer-review PDFs
- 24 Nature Portfolio peer-review files
  - 15 Nature Communications
  - 7 Communications Earth & Environment
  - 1 Nature
  - 1 Nature Climate Change
- 10 open referee comments from The Cryosphere Discussions
- 8 official standards, product guides, research-priority or treaty sources
- 850 peer-review pages inspected
- 47,518,365 downloaded peer-review bytes hashed

The source PDFs were held in a temporary analysis cache only. They are not included in the deliverable. The repository distributes source metadata, public URLs, SHA-256 hashes, page counts, aggregate corpus statistics and non-verbatim abstractions.

## Distilled product

- 104 polar reviewer patterns
- 13 claim-dependent evidence gates
- 7 subsystem routes to existing domain skills
- 3 default reviewers plus 1 conditionally triggered responsibility/governance reviewer
- 12 synthetic benchmark fixtures, including 4 negative controls
- deterministic routing, retrieval, package validation and corpus-integrity tests

## Scientific coverage

The patterns cover regional and seasonal scope, logistics-driven sampling, cryosphere variable identity, polar satellite products, conservation budgets, model resolution and assimilation, attribution and nonstationarity, statistical validation, glacier and ice-sheet dynamics, sea-ice-ocean-atmosphere coupling, permafrost/ecology/biogeochemistry, paleoclimate chronology and research responsibility.

## Distillation controls

- All patterns are written as transferable claim-risk-revision abstractions.
- No anonymous reviewer wording is intentionally retained.
- A 10-word exact-overlap audit against the extracted peer-review text found zero matches in pattern concerns and revision directions.
- Pattern IDs are unique and pairwise concern similarity remained below the duplication threshold.
- Every pattern source identifier resolves to the provenance index.
- Raw PDF distribution is prohibited by package validation.

## Evaluation boundary

The corpus and synthetic fixtures do not demonstrate expert-equivalent peer review. Scientific validation still requires independent polar experts, blinded manuscripts, negative controls, inter-annotator agreement, routing evaluation and prospective studies.
