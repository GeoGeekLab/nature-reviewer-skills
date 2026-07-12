# Sampling Representativeness

Station, ship, campaign, access, habitat, archive, missingness and independent-validation biases.

## Internal questions

- **Logistics-driven sampling bias:** Sampling is concentrated near stations, ship tracks, air routes, roads, accessible glaciers, or safe summer conditions but treated as population-representative. Resolution: Map the sampling frame, quantify coverage by environmental stratum, use weighting or hierarchical inference, and narrow claims where coverage is absent.
- **Summer observations infer winter process:** Warm-season measurements are used to infer winter fluxes, stratification, snow processes, ecology, or atmosphere-surface exchange. Resolution: Add winter evidence, use a validated seasonal model with uncertainty, or limit the conclusion to the observed season.
- **Sparse sites support trend estimate:** A trend is estimated from a small or changing station network without accounting for spatial covariance, site turnover, and unequal record length. Resolution: Report site histories, use methods robust to unbalanced panels and spatial dependence, and test leave-site-out stability.
- **Cruise track treated as synoptic map:** Shipboard observations collected over days or weeks are interpreted as a simultaneous spatial field. Resolution: Model or remove temporal drift, use repeat sections or autonomous observations, and report the synoptic limitation.
- **Validation sites overlap development sites:** The same stations, cores, scenes, transects, or reanalysis-constrained products contribute to algorithm tuning and reported validation. Resolution: Create a genuinely independent holdout by site, period, sensor, or region and disclose all data dependencies.
- **Biological samples ignore habitat structure:** Ecological samples are pooled across ice edge, open water, under-ice, benthic, stream, or terrestrial habitats without a design that represents their area and season. Resolution: Use stratified sampling or multilevel models, report habitat-specific effects, and weight only with defensible habitat prevalence.
- **Core or archive is spatially overinterpreted:** One sediment core, lake, or ice core is used to infer regional climate without demonstrating source area and replication. Resolution: Constrain the source footprint, compare independent nearby archives, and state the spatial scale actually supported.
- **Missingness assumed random:** Cloud, darkness, instrument failure, unsafe conditions, melt contamination, or inaccessible terrain creates missing data that are treated as random. Resolution: Characterize missingness by state and season, use sensitivity bounds or explicit observation models, and avoid unconditional interpolation.

Use only when relevant to a central claim. Do not expose this gate name or pattern IDs in the final referee report.
