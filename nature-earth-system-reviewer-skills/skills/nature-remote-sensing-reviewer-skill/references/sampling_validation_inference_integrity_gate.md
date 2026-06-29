# Sampling, Validation, and Inference Integrity Gate

Use this gate when a manuscript relies on field observations, reference data, station data, expert labels, benchmark products, satellite-product validation, geospatial machine learning, spatial mapping, ecological or environmental inference, rare-event detection, causal attribution, management conclusions, or operational product claims.

This gate is general. It must be applied to the manuscript under review, not to the research objects of any source paper used to develop the gate. The reviewer should ask what the manuscript claims, what evidence it provides, and what inferential structure connects the two.

## Gate Activation

- **Level 0:** the manuscript has no validation, sampling, inference, or product claim that depends on this gate. Do not mention it.
- **Level 1:** the gate affects a minor detail. Use as a minor comment or scope limitation.
- **Level 2:** the gate affects a substantive result, model, or map. Use as a substantive concern.
- **Level 3:** the gate affects the central journal-level contribution, spatial generalization, temporal conclusion, causal attribution, or management claim. A weakness can be a major concern.

## A. Reference Data and Sampling Design

Do not treat reference observations as unquestioned truth. Ask what was measured, at what scale, with what protocol, and with what uncertainty.

Check:

- the measurand of the reference observation;
- spatial, temporal, vertical, taxonomic, or thematic support;
- match-up rules and mismatch error;
- sampling depth, laboratory method, detection limits, QA/QC, or label protocol when relevant;
- whether the sample covers the prediction domain rather than only convenient cases;
- whether difficult regimes are under-sampled;
- whether observation availability is seasonally or environmentally biased.

Review language:

> The field observations should be treated as reference measurements with their own scale, protocol and uncertainty, not as ground truth.

## B. Non-Independence, Effective Sample Size, and Pseudoreplication

Ask what the true independent sampling unit is. Nominal sample count can be much larger than independent information.

Potential non-independence includes:

- neighboring pixels;
- repeated observations at the same station, site, image, field campaign, or event;
- multiple plots within one landscape unit;
- multiple dates from the same event;
- training and validation samples from spatially autocorrelated regions;
- time series with repeated seasonal structure.

Review language:

> The effective sample size appears smaller than the nominal number of observations. Nearby pixels, repeated station measurements, or repeated observations from the same campaign should not be treated as independent unless the dependence structure is modelled.

## C. Spatial Validation and Generalization

Random cross-validation can overstate performance when samples are spatially autocorrelated or when a model memorizes spatial structure. Ask whether validation is independent in the dimension needed for the claim.

Check:

- spatially blocked validation;
- leave-region-out or leave-site-out validation;
- station/campaign/year blocking;
- validation outside the calibration geography;
- comparison of random and blocked validation;
- stratified error by environment, class, region, or domain;
- whether spatial coordinates or stable auxiliary variables allow spatial memorization.

Review language:

> I am not convinced that the reported validation demonstrates spatial generalization; a blocked or leave-region-out validation is needed if the manuscript claims prediction beyond sampled locations.

## D. Uncertainty Cascade

Uncertainty is not only model error. It can arise from the sensor, preprocessing, reference data, matching, sampling, interpolation, model structure, extrapolation, aggregation, and downstream inference.

Check whether uncertainty is propagated into:

- maps;
- regional means;
- ratios;
- trends;
- breakpoints;
- hotspots;
- source or driver attribution;
- management or policy conclusions.

Review language:

> The uncertainty analysis appears to stop at the prediction-error level, whereas the conclusions depend on downstream quantities that should inherit uncertainty from the full processing chain.

## E. Ill-Posed Inversion, Proxy Stability, and Equifinality

Many remote-sensing retrievals are non-unique: different environmental states can produce similar observations. This applies to physical inversion, empirical models, and machine-learning proxies.

Check:

- whether the target variable is directly observable or inferred through a proxy;
- whether several states can produce similar satellite signatures;
- what priors, constraints, auxiliary data, or regularization make the problem identifiable;
- whether spatial or seasonal priors dominate the prediction;
- whether uncertainty increases in ambiguous feature space;
- whether proxy-target relationships are stable across time and domain.

Review language:

> The retrieval problem is potentially non-unique. The manuscript should explain what prior information or constraints make the inverse problem identifiable, and how this affects uncertainty.

## F. Multiplicity and Field Significance

Spatial, temporal, spectral, station-wise, class-wise, or driver-wise analyses can involve many tests. Local significance thresholds can overstate evidence.

Check:

- number of tests;
- false-discovery-rate or family-wise adjustment;
- field significance;
- spatial dependence in significance assessment;
- cluster-level inference;
- whether significant area exceeds chance expectation;
- whether many correlated variables are counted as independent confirmation.

Review language:

> The significance map is difficult to interpret without field-significance or false-discovery-rate assessment, particularly because the tests are spatially or temporally dependent.

## G. Rare Events and Post-Hoc Event Definitions

Extreme events and rare classes are difficult because independent events are few, class imbalance is severe, and definitions may be chosen after seeing the anomaly.

Check:

- number of independent events rather than pixels or time steps;
- event-threshold definition;
- study region and time-window selection;
- class imbalance;
- false alarms and missed detections;
- event-level validation;
- stationarity assumptions;
- whether an event-specific storyline is confused with class-level probabilistic attribution.

Review language:

> The event definition appears partly conditioned on the observed anomaly, which makes the rarity and attribution claims difficult to interpret.

## H. Causal, Intervention, and Management Inference

Feature importance, SHAP values, correlations, before/after contrasts, or mapped coincidences are not causal identification strategies by themselves.

Check:

- causal estimand;
- assumed causal graph or identification logic;
- confounding control;
- nonrandom treatment or intervention placement;
- counterfactual, control group, interrupted time-series, difference-in-differences, or sensitivity analysis;
- lag structure and interference;
- whether model explanation is being interpreted as source contribution or causal effect.

Review language:

> The analysis identifies variables associated with the fitted product, but it does not by itself establish causal drivers of the environmental change.

## I. FAIR Reproducibility and Product Auditability

For product-driven manuscripts, reproducibility is part of the evidence. Reviewers need enough material during review to evaluate the central claims.

Check:

- data and product versions;
- code and environment;
- trained model details;
- random seeds;
- masks and QA rules;
- match-up construction;
- projection, resampling, and aggregation rules;
- figure/table generation logic;
- access restrictions and repository metadata.

Review language:

> For a product-driven manuscript, reproducibility cannot be deferred entirely until after acceptance; reviewers need enough information to audit the processing workflow and central claims.

## Weight Control

Do not apply every section mechanically. Use only the sections triggered by the manuscript's content. Elevate a concern only when the manuscript's central claim depends on the relevant sampling, validation, inference, or reproducibility layer.
