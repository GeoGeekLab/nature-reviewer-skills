# Claim-dependent gate router

Use gates only when the manuscript's own claims require them.

## Routing levels

- 0: not relevant.
- 1: peripheral issue.
- 2: important but not central.
- 3: central to the headline claim.

A concern becomes major only when a level-3 or strong level-2 gate exposes a weakness that changes the confidence, interpretation, or generality of a central claim.

## Claim routing map

| Claim type | Primary gates |
|---|---|
| Satellite/reanalysis atmospheric product claim | observational product validity; scale consistency; validation; uncertainty |
| Model-based atmospheric mechanism claim | model physics; sensitivity; scale consistency; mechanism causality |
| AI weather/climate claim | AI fidelity; benchmark fairness; physical consistency; OOD stability; reproducibility |
| Aerosol-cloud-radiation claim | microphysics; observational validity; model sensitivity; radiative uncertainty |
| Atmospheric chemistry/emissions claim | chemistry budget; emissions inventory; transport/deposition closure; uncertainty |
| Extreme-event attribution claim | event definition; counterfactual design; internal variability; tail uncertainty |
| Trend/signal-detection claim | time-series robustness; baseline sensitivity; product/ensemble agreement |
| Circulation/feedback claim | mechanism closure; confounder control; scale consistency |
| Policy or operational claim | claim calibration; validation; uncertainty; applicability boundary |

Never review by checklist saturation. Review by claim dependence.
