# Climate trend and attribution gate

## Purpose
Use this gate when a manuscript makes claims related to climate trend and attribution.

## Trigger signals

- `trend`
- `attribution`
- `drivers`
- `climate change`
- `warming`
- `temperature`
- `precipitation`
- `extreme`
- `drought`
- `time series`
- `baseline`
- `counterfactual`
- `causal`
- `correlation`
- `teleconnection`
- `scenario`

## Reviewer concern patterns distilled from corpus

- **CECO-P0025** (abstracted_reviewer_concern): Trend or climate-impact claims require temporal consistency, explicit baselines, and tests that separate climate drivers from geography, land use, sampling design, and observation-system change.
- **CECO-P0026** (abstracted_reviewer_concern): Attribution language should be calibrated to the evidence: observational associations, model experiments, and counterfactual analyses support different strengths of claim.
- **CECO-P0027** (abstracted_reviewer_concern): Climate velocity, warming, drought, wildfire, or extreme-event conclusions need sensitivity to baseline period, scenario choice, spatial aggregation, and uncertainty propagation.
- **CECO-P0028** (issue_cluster): For Climate trend and attribution gate, reviewers repeatedly flag climate/trend/attribution when the manuscript's evidence chain does not make this point explicit enough for a broad high-impact-journal audience.
- **CECO-P0029** (issue_cluster): For Climate trend and attribution gate, reviewers repeatedly flag causal overclaim when the manuscript's evidence chain does not make this point explicit enough for a broad high-impact-journal audience.
- **CECO-P0030** (issue_cluster): For Climate trend and attribution gate, reviewers repeatedly flag sampling/representativeness when the manuscript's evidence chain does not make this point explicit enough for a broad high-impact-journal audience.
- **CECO-P0031** (issue_cluster): For Climate trend and attribution gate, reviewers repeatedly flag figure/table clarity when the manuscript's evidence chain does not make this point explicit enough for a broad high-impact-journal audience.
- **CECO-P0032** (issue_cluster): For Climate trend and attribution gate, reviewers repeatedly flag uncertainty when the manuscript's evidence chain does not make this point explicit enough for a broad high-impact-journal audience.

## Evidence expected before accepting the claim

- baseline definition
- temporal consistency
- driver separation
- sensitivity to aggregation
- uncertainty propagation
- conservative attribution wording

## Typical claim-language risk

- overstating climate causality from observational trends or short baselines

## Corpus support summary

- Distilled unit count: 593
- Source article count: 53
- Frequent issue labels: climate/trend/attribution (182), causal overclaim (102), sampling/representativeness (90), figure/table clarity (63), uncertainty (51), novelty/significance (43), assumption/parameterization (27), definition/scope (12)

## Output expectation

When this gate is triggered, write reviewer comments that are claim-specific, evidence-chain aware, and calibrated to the manuscript's actual scope. Prefer explicit tests or revisions over generic requests.

## Additional stress tests

- For resilience-loss, tipping-point or critical-transition claims, check sensitivity to proxy choice, sensor changes, detrending, window length, autocorrelation assumptions, spatial dependence, drought/flood history and alternative indicators.
- For climate-impact attribution, distinguish climate association, model attribution, causal attribution and mechanism evidence.
- For trend claims, require robustness to starting year, endpoint, seasonality, product version, autocorrelation and multiple testing.
