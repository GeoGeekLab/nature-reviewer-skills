# Uncertainty Statistics Validation

Dependence, propagation, sensitivity, multiplicity, rare events, leakage, baselines and external validity.

## Internal questions

- **Serial and spatial dependence ignored:** Significance tests treat polar time series, pixels, stations, or model cells as independent. Resolution: Use dependence-aware uncertainty, report effective sample size, and test robustness across correlation models.
- **Uncertainty is not propagated to headline result:** Input, calibration, retrieval, age-model, density, forcing, or parameter uncertainties are listed but not propagated to the final trend, budget, or projection. Resolution: Propagate all material uncertainty sources, including covariance, and report their contribution to the final interval.
- **Sensitivity tests do not span plausible choices:** Robustness is claimed from a narrow set of thresholds, windows, products, priors, or model parameters selected near the preferred analysis. Resolution: Predefine a plausible sensitivity space, include alternative products and methods, and show which conclusions survive.
- **Multiple comparisons are unaccounted:** Large spatial, temporal, taxonomic, or parameter searches report selected significant patterns without multiplicity or selection correction. Resolution: Control the false-discovery process or use hierarchical models, report the search space, and validate selected patterns independently.
- **Rare-event probability is overprecise:** The date or probability of an ice-free day, tipping event, extreme melt, or circulation threshold is estimated from too few effective samples. Resolution: Report interval and threshold sensitivity, effective sample size, and conditional probability wording rather than a precise deterministic date.
- **Cross-validation leaks space or time:** Random splits place neighboring pixels, repeated sites, adjacent years, or derived samples in both train and test sets. Resolution: Use blocked spatial and temporal validation, hold out entire sites or regions, and report out-of-domain performance.
- **Baseline comparison is weak or mismatched:** A new method or model is compared with an outdated, differently forced, differently resolved, or insufficiently tuned baseline. Resolution: Use strong matched baselines, harmonize inputs and evaluation domains, and report uncertainty in performance differences.
- **Confidence language exceeds validation domain:** The manuscript claims robustness, ubiquity, prediction, or early warning despite narrow data, one event, or an in-sample fit. Resolution: Separate in-domain precision from transfer uncertainty and align language with the actual validation design.

Use only when relevant to a central claim. Do not expose this gate name or pattern IDs in the final referee report.
