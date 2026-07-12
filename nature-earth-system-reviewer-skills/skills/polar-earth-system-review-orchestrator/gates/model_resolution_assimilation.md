# Model Resolution Assimilation

Geometry, boundaries, data assimilation, ensembles, tuning, subgrid schemes and conditional projection language.

## Internal questions

- **Grid cannot represent key geometry:** Model resolution is too coarse for grounding zones, shelf channels, narrow straits, fjords, leads, steep terrain, or polygonal permafrost invoked in the explanation. Resolution: Demonstrate convergence or use parameterizations validated for the target scale; limit mechanistic claims when the feature is unresolved.
- **Boundary conditions encode the result:** Ocean, atmosphere, basal, geothermal, bed, or ecological boundary conditions are prescribed in a way that already imposes the claimed response. Resolution: Identify which conclusions follow from boundary choices, run alternative plausible conditions, and avoid causal language unsupported by sensitivity.
- **Assimilation product used as independent validation:** A reanalysis or assimilated product is used both to force or constrain the model and to validate its performance. Resolution: Use withheld observations or an independent product, disclose assimilation lineage, and separate fit to constraints from predictive skill.
- **Single model presented as structural certainty:** A result from one model, one configuration, or one parameterization is presented as a robust system response. Resolution: Use a multi-model or structural ensemble, perturb key process choices, and label model-contingent results.
- **Ensemble members are not independent:** Initial-condition members or models sharing code and parameterizations are treated as independent samples when estimating probability. Resolution: Describe ensemble dependence, estimate effective sample size, and avoid precise event probabilities unsupported by the ensemble design.
- **Tuning and evaluation periods overlap:** Parameters are selected using the same period, event, or site used to claim predictive accuracy or mechanism fidelity. Resolution: Separate calibration and evaluation by time and region, report pre-specified metrics, and test out-of-sample stability.
- **Subgrid scheme lacks scale-aware validation:** A subgrid process such as leads, melt ponds, snow redistribution, calving, drainage, or thermokarst is parameterized without validation across the operating range. Resolution: Validate the scheme against process observations, test extrapolation, and report when the result depends on the closure.
- **Scenario spread is mistaken for forecast uncertainty:** A selected scenario set or forcing range is presented as the full uncertainty distribution. Resolution: Decompose uncertainty sources and state whether results are conditional projections, scenarios, hindcasts, or forecasts.

Use only when relevant to a central claim. Do not expose this gate name or pattern IDs in the final referee report.
