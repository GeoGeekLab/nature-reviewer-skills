# Trend and Time-Series Evidence Gate

Use this gate only when the manuscript makes a temporal claim: trend, decline, increase, acceleration, slowdown, surge, stability, recovery, degradation, seasonal change, breakpoint, changepoint, before/after comparison, climate signal, policy-period effect, or temporal attribution. Do not apply this gate mechanically to manuscripts without temporal claims.

## Gate Activation

- **Level 0:** no temporal claim. Do not mention this gate.
- **Level 1:** time is contextual, not central. Mention only obvious limitations such as short record length or seasonal coverage.
- **Level 2:** temporal change is a substantive result. Check autocorrelation, uncertainty, seasonality, and sampling consistency.
- **Level 3:** temporal change is the central journal-level contribution or is used for attribution, mechanism, policy, or management conclusions. Require a full temporal evidence chain.

## Core Checks

### 1. Trend, Seasonality, Disturbance, and Noise

Ask whether the manuscript separates long-term trend from seasonality, episodic anomalies, abrupt disturbances, data gaps, residual noise, and observation bias. A single fitted line is rarely sufficient for seasonal or irregular remote-sensing series.

Review language:

> I am not convinced that the reported temporal change has been separated from seasonal variability, episodic anomalies, and product-level noise.

### 2. Autocorrelation and Effective Sample Size

Ask whether serial dependence is modelled or diagnosed. Monthly, seasonal, and annual remote-sensing products are rarely independent. Naive regression p-values or uncorrected trend tests can overstate significance.

Review language:

> The trend test appears to treat temporally adjacent observations as independent; the authors should account for serial autocorrelation and the resulting reduction in effective sample size.

### 3. Trend Uncertainty Propagation

Ask whether retrieval uncertainty, compositing uncertainty, valid-observation uncertainty, sampling uncertainty, spatial dependence, and reference-data uncertainty propagate into slopes, ratios, regional means, breakpoints, and maps.

Review language:

> The uncertainty analysis appears to stop at the product-error level, whereas the main conclusion depends on the trend and breakpoint estimates.

### 4. Detection Power and Minimum Detectable Effect

If the manuscript claims no trend, stability, no acceleration, no breakpoint, or unchanged ratios, ask whether the record has enough power to detect a change of meaningful size. Absence of significance is not evidence of stability unless detectability is quantified.

Review language:

> The absence of a significant trend should not be interpreted as stability unless the authors report the detectable effect size for the available record length and uncertainty.

### 5. Changepoint Discipline

If the manuscript uses pre/post periods or identifies a breakpoint, ask whether the breakpoint was specified independently or selected after inspecting the time series. Check uncertainty in breakpoint timing and sensitivity to alternative break years.

Review language:

> The manuscript should clarify whether the breakpoint was specified a priori or chosen after inspecting the time series; otherwise the stated significance may be overstated.

### 6. Product Temporal Consistency

Ask whether the time series is homogeneous across the full period: sensor changes, orbital drift, product-version changes, atmospheric correction changes, cloud/aerosol screening, valid-observation fraction, cross-sensor harmonization, and processing updates.

Review language:

> A long-term trend claim requires evidence that the satellite product is temporally homogeneous over the full analysis period.

### 7. Proxy Stability

If the target variable is inferred indirectly, ask whether the proxy-target relationship is stable over time. This is especially important for variables not directly observed by the sensor, but the principle applies to any derived proxy.

Review language:

> The manuscript needs to show that the relationship between the satellite proxy and the target variable remained stable over the period over which trends are inferred.

### 8. Multivariate Trend Covariance

If multiple bands, indices, products, regions, taxa, or variables are used as evidence, ask whether covariance and effective dimensionality are handled. Correlated variables do not provide independent confirmations.

Review language:

> The multivariate trend evidence should account for covariance among the variables rather than treating them as independent evidence.

### 9. Multiple Testing and Spatial Dependence

For pixel-wise, grid-cell, station-wise, wavelength-wise, or region-wise trend tests, ask how multiple testing and spatial dependence are handled. Local p-values alone are insufficient for interpreting a field of significant pixels.

Review language:

> The pixel-wise significance map is difficult to interpret without field-significance or false-discovery-rate control that accounts for spatial dependence.

### 10. Detection Before Attribution

If the manuscript attributes a temporal change to climate, policy, management, disturbance, or drivers, first ask whether the temporal change itself is statistically detected. Then ask whether attribution is supported by an identification strategy rather than temporal coincidence.

Review language:

> The manuscript should distinguish detection of a temporal change from attribution of that change to a driver.

## Weight Control

Do not raise these checks as major concerns unless the manuscript's central contribution depends on the trend, breakpoint, acceleration, stability, seasonal-change, or temporal attribution claim. When time series are secondary, use this gate only to calibrate language or identify a limited analysis gap.
