# Claim-dependent gate router

## Purpose

Route manuscript claims to only the reviewer gates that are scientifically relevant. This prevents checklist-style reviews and prevents any familiar dispute, method concern, or subfield preference from dominating a manuscript whose claims do not depend on that issue.

## Routing levels

| Level | Meaning | Review use |
|---|---|---|
| 0 | Not relevant | Do not mention. |
| 1 | Peripheral | Mention only as a local comment. |
| 2 | Important | Use as a substantive concern. |
| 3 | Central | May become a major or decision-level concern. |

## Routing workflow

1. List the manuscript's strongest claims.
2. Identify each claim's evidence layer: direct measurement, proxy, model, classification, experiment, synthesis, observational product, or expert interpretation.
3. Assign gates only to claims whose evidence layer triggers that gate.
4. Weight the gate by how much the contribution depends on it.
5. Use `decision_threshold_gate` for the central claims.
6. Use `detail_audit_gate` for the definitions, units, baselines, thresholds, figures and reproducibility details that condition the central claims.
7. Collapse overlapping concerns into a few high-value major comments.

## Common routing patterns

- A trend, extreme or tipping-point manuscript should normally trigger climate trend/attribution, observational-product uncertainty, statistical inference, claim calibration, decision threshold, and detail audit.
- A biodiversity field study should normally trigger sampling representativeness, biodiversity/ecosystem-function, statistical inference, mechanism, decision threshold, and detail audit.
- A carbon or nitrogen-cycle paper should normally trigger model assumptions, biogeochemistry, uncertainty, reproducibility, published-paper comparison, and detail audit.
- A conservation or restoration paper should normally trigger land-use/conservation, sampling, biodiversity/ecosystem-function, policy/management, published-paper comparison, decision threshold, and detail audit.

## Overweighting guard

Do not elevate a concern because it is familiar. Elevate it only if the manuscript's claim relies on the same vulnerable evidence layer.
