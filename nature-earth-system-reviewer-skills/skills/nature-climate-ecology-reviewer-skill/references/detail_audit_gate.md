# Detail audit gate

## Purpose

Check the technical details that determine whether central results are interpretable and reproducible.

## Required audit targets

- Definitions: ecosystem class, treatment, baseline, control, exposure, threshold, response variable.
- Units: area, mass, flux, concentration, rate, time step, currency, carbon or nitrogen form.
- Denominators: per area, per biomass, per capita, per species, per grid cell, per year.
- Baselines: historical period, reference ecosystem, counterfactual, scenario, pre/post window.
- Spatial handling: masks, projections, buffers, grid resolution, aggregation, edge treatment.
- Temporal handling: seasonal window, lag, smoothing, breakpoint, autocorrelation, missing years.
- Sampling: sample size, exclusion rules, replication, independence, detection, imbalance.
- Model details: parameters, priors, tuning, convergence, boundary conditions, forcing, initialization.
- Figures: color scale, uncertainty display, sample size, statistical meaning, caption consistency.
- Tables: units, rounding, missing values, category definitions, reproducibility links.
- Supplement: whether key validation or sensitivity is present but underused in the main claim.
- Data/code: availability, version, script-to-figure traceability, non-public restrictions.

## Review standard

Use details to test the claim, not to produce an exhaustive checklist. Elevate a detail only when it changes the interpretation, uncertainty, reproducibility or scope of the main conclusion.
