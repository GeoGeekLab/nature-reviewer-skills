# AI weather and climate model fidelity gate

Use when claims depend on neural weather forecasts, climate emulators, downscaling systems, or ML-based atmospheric diagnostics.

Claim type → evidence risk → reviewer concern → revision direction

- Forecast skill claim → benchmark leakage or unfair baseline → improvement may not be operationally meaningful → enforce temporally separated tests and fair baselines.
- Long-rollout climate claim → spectral drift or unstable conservation → physically relevant behaviour is not shown → evaluate rollouts, extremes, spectra, budgets, and vertical coupling.
- OOD generalization claim → test period resembles training distribution → robustness is unproven → test rare regimes, extremes, shifts, and reanalysis dependence.
