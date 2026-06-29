# Observational product and measurement uncertainty gate

## Purpose
Use this gate when a manuscript makes claims related to observational product and measurement uncertainty.

## Trigger signals

- `satellite`
- `remote sensing`
- `observation`
- `measurement`
- `dataset`
- `database`
- `product`
- `inventory`
- `sensor`
- `map`
- `classification`
- `detection`
- `uncertainty`
- `error`
- `accuracy`
- `ground truth`

## Reviewer concern patterns distilled from corpus

- **CECO-P0073** (abstracted_reviewer_concern): Observation-product claims require evidence that the measured or remotely sensed variable validly represents the ecological or climate quantity being inferred.
- **CECO-P0074** (abstracted_reviewer_concern): Maps, inventories, classifications, and satellite products should report accuracy, bias, false positives/negatives, and spatially explicit uncertainty.
- **CECO-P0075** (abstracted_reviewer_concern): Product intercomparison or historical reconstruction should address sensor/product changes and out-of-domain regions.
- **CECO-P0076** (issue_cluster): For Observational product and measurement uncertainty gate, reviewers repeatedly flag uncertainty when the manuscript's evidence chain does not make this point explicit enough for a broad high-impact-journal audience.
- **CECO-P0077** (issue_cluster): For Observational product and measurement uncertainty gate, reviewers repeatedly flag observational/product/uncertainty when the manuscript's evidence chain does not make this point explicit enough for a broad high-impact-journal audience.
- **CECO-P0078** (issue_cluster): For Observational product and measurement uncertainty gate, reviewers repeatedly flag figure/table clarity when the manuscript's evidence chain does not make this point explicit enough for a broad high-impact-journal audience.
- **CECO-P0079** (issue_cluster): For Observational product and measurement uncertainty gate, reviewers repeatedly flag sampling/representativeness when the manuscript's evidence chain does not make this point explicit enough for a broad high-impact-journal audience.
- **CECO-P0080** (issue_cluster): For Observational product and measurement uncertainty gate, reviewers repeatedly flag novelty/significance when the manuscript's evidence chain does not make this point explicit enough for a broad high-impact-journal audience.

## Evidence expected before accepting the claim

- product validation
- measurement bias
- classification accuracy
- spatially explicit uncertainty
- sensor/dataset-change checks

## Typical claim-language risk

- treating observation products as ground truth without validation

## Corpus support summary

- Distilled unit count: 217
- Source article count: 37
- Frequent issue labels: uncertainty (83), observational/product/uncertainty (70), figure/table clarity (16), sampling/representativeness (11), novelty/significance (11), validation (9), causal overclaim (8), definition/scope (7)

## Output expectation

When this gate is triggered, write reviewer comments that are claim-specific, evidence-chain aware, and calibrated to the manuscript's actual scope. Prefer explicit tests or revisions over generic requests.

## Additional stress tests

- Treat satellite products, inventories, biodiversity databases, reanalysis fields, climate model outputs and expert-derived maps as evidence layers with known uncertainties, not as ground truth.
- Check sensor discontinuities, product-version changes, spatial grain, temporal compositing, detectability, sampling bias, gap filling and cross-product disagreement.
- If the manuscript infers ecological process from a proxy, require a validation or sensitivity analysis showing that plausible artifacts cannot explain the central pattern.
