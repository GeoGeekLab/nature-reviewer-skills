# Reproducibility, data and code availability gate

## Purpose
Use this gate when a manuscript makes claims related to reproducibility, data and code availability.

## Trigger signals

- `data availability`
- `code`
- `reproduc`
- `repository`
- `method details`
- `supplementary`
- `source data`
- `protocol`
- `equation`
- `parameter`
- `workflow`

## Reviewer concern patterns distilled from corpus

- **CECO-P0096** (abstracted_reviewer_concern): Critical datasets, code, equations, parameters, and preprocessing decisions should be available or sufficiently described for independent reproduction.
- **CECO-P0097** (abstracted_reviewer_concern): Complex workflows need an auditable path from raw observations/products to the final claim.
- **CECO-P0098** (abstracted_reviewer_concern): Supplementary methods should include enough detail to reproduce classifications, model runs, and sensitivity analyses.
- **CECO-P0099** (issue_cluster): For Reproducibility, data and code availability gate, reviewers repeatedly flag data/code reproducibility when the manuscript's evidence chain does not make this point explicit enough for a broad high-impact-journal audience.
- **CECO-P0100** (issue_cluster): For Reproducibility, data and code availability gate, reviewers repeatedly flag assumption/parameterization when the manuscript's evidence chain does not make this point explicit enough for a broad high-impact-journal audience.

## Evidence expected before accepting the claim

- data/code links
- equations and parameters
- preprocessing workflow
- versioned products
- reproducible supplement

## Typical claim-language risk

- making non-auditable claims from complex workflows

## Corpus support summary

- Distilled unit count: 48
- Source article count: 27
- Frequent issue labels: data/code reproducibility (29), assumption/parameterization (11), sampling/representativeness (4), uncertainty (2), causal overclaim (2)

## Output expectation

When this gate is triggered, write reviewer comments that are claim-specific, evidence-chain aware, and calibrated to the manuscript's actual scope. Prefer explicit tests or revisions over generic requests.
