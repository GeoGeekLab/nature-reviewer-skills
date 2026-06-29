# Statistical inference and uncertainty gate

## Purpose
Use this gate when a manuscript makes claims related to statistical inference and uncertainty.

## Trigger signals

- `statistical`
- `significance`
- `p-value`
- `confidence`
- `credible`
- `effect size`
- `regression`
- `correlation`
- `variance`
- `random effect`
- `mixed model`
- `sample size`
- `bootstrap`
- `multiple testing`

## Reviewer concern patterns distilled from corpus

- **CECO-P0081** (abstracted_reviewer_concern): Statistical inference should match the sampling design, including spatial/temporal autocorrelation, hierarchical structure, multiple testing, and effect-size interpretation.
- **CECO-P0082** (abstracted_reviewer_concern): Uncertainty intervals should propagate measurement, model, and sampling uncertainty rather than only reporting fitted-model error.
- **CECO-P0083** (abstracted_reviewer_concern): Claims of difference, threshold, or nonlinear response need robustness to model specification and data leverage points.
- **CECO-P0084** (issue_cluster): For Statistical inference and uncertainty gate, reviewers repeatedly flag statistical/inference when the manuscript's evidence chain does not make this point explicit enough for a broad high-impact-journal audience.
- **CECO-P0085** (issue_cluster): For Statistical inference and uncertainty gate, reviewers repeatedly flag uncertainty when the manuscript's evidence chain does not make this point explicit enough for a broad high-impact-journal audience.
- **CECO-P0086** (issue_cluster): For Statistical inference and uncertainty gate, reviewers repeatedly flag sampling/representativeness when the manuscript's evidence chain does not make this point explicit enough for a broad high-impact-journal audience.
- **CECO-P0087** (issue_cluster): For Statistical inference and uncertainty gate, reviewers repeatedly flag novelty/significance when the manuscript's evidence chain does not make this point explicit enough for a broad high-impact-journal audience.
- **CECO-P0088** (issue_cluster): For Statistical inference and uncertainty gate, reviewers repeatedly flag figure/table clarity when the manuscript's evidence chain does not make this point explicit enough for a broad high-impact-journal audience.

## Evidence expected before accepting the claim

- model-design alignment
- autocorrelation handling
- effect sizes
- multiple testing
- robust alternatives

## Typical claim-language risk

- confusing statistical significance with ecological importance

## Corpus support summary

- Distilled unit count: 96
- Source article count: 30
- Frequent issue labels: statistical/inference (27), uncertainty (22), sampling/representativeness (21), novelty/significance (9), figure/table clarity (6), data/code reproducibility (5), causal overclaim (3), definition/scope (2)

## Output expectation

When this gate is triggered, write reviewer comments that are claim-specific, evidence-chain aware, and calibrated to the manuscript's actual scope. Prefer explicit tests or revisions over generic requests.

## Additional stress tests

- Check effective sample size under spatial and temporal autocorrelation.
- Check whether reported intervals propagate measurement, sampling, model and scenario uncertainty.
- Check sensitivity to model specification, leverage points, variable collinearity, threshold placement, window length and multiple comparisons.
