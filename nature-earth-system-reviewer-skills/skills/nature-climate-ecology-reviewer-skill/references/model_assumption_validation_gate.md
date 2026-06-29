# Model assumptions and validation gate

## Purpose
Use this gate when a manuscript makes claims related to model assumptions and validation.

## Trigger signals

- `model`
- `assumption`
- `parameter`
- `validation`
- `calibration`
- `sensitivity`
- `uncertainty`
- `robust`
- `scenario`
- `simulation`
- `earth system model`
- `statistical model`
- `fit`
- `prediction`
- `cross-validation`

## Reviewer concern patterns distilled from corpus

- **CECO-P0041** (abstracted_reviewer_concern): Model-based claims need transparent assumptions, parameter sources, calibration/validation design, and sensitivity analyses for influential parameters.
- **CECO-P0042** (abstracted_reviewer_concern): Predictive or process models should be evaluated against independent observations appropriate to the scale of the claim.
- **CECO-P0043** (abstracted_reviewer_concern): Scenario or simulation conclusions should not be presented as empirical fact without uncertainty ranges and robustness checks.
- **CECO-P0044** (issue_cluster): For Model assumptions and validation gate, reviewers repeatedly flag uncertainty when the manuscript's evidence chain does not make this point explicit enough for a broad high-impact-journal audience.
- **CECO-P0045** (issue_cluster): For Model assumptions and validation gate, reviewers repeatedly flag model/assumption/validation when the manuscript's evidence chain does not make this point explicit enough for a broad high-impact-journal audience.
- **CECO-P0046** (issue_cluster): For Model assumptions and validation gate, reviewers repeatedly flag assumption/parameterization when the manuscript's evidence chain does not make this point explicit enough for a broad high-impact-journal audience.
- **CECO-P0047** (issue_cluster): For Model assumptions and validation gate, reviewers repeatedly flag validation when the manuscript's evidence chain does not make this point explicit enough for a broad high-impact-journal audience.
- **CECO-P0048** (issue_cluster): For Model assumptions and validation gate, reviewers repeatedly flag sampling/representativeness when the manuscript's evidence chain does not make this point explicit enough for a broad high-impact-journal audience.

## Evidence expected before accepting the claim

- assumption table
- calibration and validation split
- independent observations
- sensitivity analysis
- uncertainty ranges

## Typical claim-language risk

- presenting model output as empirical certainty

## Corpus support summary

- Distilled unit count: 479
- Source article count: 48
- Frequent issue labels: uncertainty (187), model/assumption/validation (86), assumption/parameterization (71), validation (31), sampling/representativeness (31), figure/table clarity (27), novelty/significance (16), causal overclaim (15)

## Output expectation

When this gate is triggered, write reviewer comments that are claim-specific, evidence-chain aware, and calibrated to the manuscript's actual scope. Prefer explicit tests or revisions over generic requests.

## Additional stress tests

- For process or Earth-system models, distinguish structural uncertainty, parameter uncertainty, scenario uncertainty and observational constraint uncertainty.
- For machine-learning or statistical models, check leakage, extrapolation outside training support, feature importance stability and independent validation.
- For scenario claims, separate what is projected under assumptions from what is empirically demonstrated.
