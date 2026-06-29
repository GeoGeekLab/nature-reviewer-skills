# Carbon and nitrogen biogeochemistry gate

## Purpose
Use this gate when a manuscript makes claims related to carbon and nitrogen biogeochemistry.

## Trigger signals

- `carbon`
- `co2`
- `methane`
- `ch4`
- `nitrogen`
- `n2o`
- `reactive nitrogen`
- `respiration`
- `sequestration`
- `sink`
- `flux`
- `emission`
- `soil organic`
- `biogeochemical`
- `mineralization`
- `decomposition`

## Reviewer concern patterns distilled from corpus

- **CECO-P0049** (abstracted_reviewer_concern): Carbon, nitrogen, respiration, sequestration, and emission claims need mass-balance logic, flux-vs-stock clarity, and explicit treatment of conversion factors and process assumptions.
- **CECO-P0050** (abstracted_reviewer_concern): Biogeochemical conclusions should distinguish measured fluxes from inferred fluxes and show whether alternative parameterizations change the main result.
- **CECO-P0051** (abstracted_reviewer_concern): Global carbon/nitrogen extrapolations need transparent scaling from site/product-level evidence to regional or global estimates.
- **CECO-P0052** (issue_cluster): For Carbon and nitrogen biogeochemistry gate, reviewers repeatedly flag carbon/nitrogen/cycle when the manuscript's evidence chain does not make this point explicit enough for a broad high-impact-journal audience.
- **CECO-P0053** (issue_cluster): For Carbon and nitrogen biogeochemistry gate, reviewers repeatedly flag novelty/significance when the manuscript's evidence chain does not make this point explicit enough for a broad high-impact-journal audience.
- **CECO-P0054** (issue_cluster): For Carbon and nitrogen biogeochemistry gate, reviewers repeatedly flag uncertainty when the manuscript's evidence chain does not make this point explicit enough for a broad high-impact-journal audience.
- **CECO-P0055** (issue_cluster): For Carbon and nitrogen biogeochemistry gate, reviewers repeatedly flag figure/table clarity when the manuscript's evidence chain does not make this point explicit enough for a broad high-impact-journal audience.
- **CECO-P0056** (issue_cluster): For Carbon and nitrogen biogeochemistry gate, reviewers repeatedly flag causal overclaim when the manuscript's evidence chain does not make this point explicit enough for a broad high-impact-journal audience.

## Evidence expected before accepting the claim

- measured vs inferred flux distinction
- mass-balance checks
- parameter provenance
- flux/stock units
- sensitivity to conversion factors

## Typical claim-language risk

- treating inferred stocks/fluxes as directly measured or policy-ready quantities

## Corpus support summary

- Distilled unit count: 446
- Source article count: 21
- Frequent issue labels: carbon/nitrogen/cycle (173), novelty/significance (57), uncertainty (53), figure/table clarity (42), causal overclaim (40), sampling/representativeness (35), assumption/parameterization (22), policy implication (12)

## Output expectation

When this gate is triggered, write reviewer comments that are claim-specific, evidence-chain aware, and calibrated to the manuscript's actual scope. Prefer explicit tests or revisions over generic requests.

## Additional stress tests

- For carbon-removal or sequestration claims, separate stock from flux, gross from net, potential from realized uptake, temporary storage from durable mitigation, and model-attributed effects from direct measurements.
- For soil carbon and microbial carbon-use-efficiency claims, test robustness to process-model structure, plant inputs, mineral stabilization, soil depth, land-use history, variable collinearity and parameter identifiability.
- For reactive nitrogen or greenhouse-gas forcing claims, require mass-balance consistency, sign convention clarity, uncertainty propagation and separation of CO2, CH4, N2O and aerosol effects.
