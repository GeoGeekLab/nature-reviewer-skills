# Claim-dependent gate router

Use this router to choose only the gates that are necessary for the manuscript's central claims. Do not run every gate by default.

## Operating rule

1. Identify the strongest claim.
2. Identify the evidence chain required by that claim.
3. Select only gates that stress-test a real weak point in that chain.
4. Convert the activated gates into natural referee language.
5. Do not expose gate names, pattern IDs or routing decisions in the final report.

## Chemistry routing prompts

- If the claim depends on a new reaction, select novelty, reaction scope, controls, mechanism, analytical evidence and reproducibility gates.
- If the claim depends on catalysis or performance, select activity/selectivity normalization, product balance, stability, controls, mechanism, uncertainty and comparability gates.
- If the claim depends on chemical identity or structure, select synthesis, characterization, orthogonal validation, purity, speciation and data-availability gates.
- If the claim depends on chemical biology, select probe specificity, target engagement, off-target chemistry, biological readout separation, controls and uncertainty gates.
- If the claim depends on electrochemistry or photochemistry, select reference calibration, photon or electron balance, transport, inner-filter effects, durability, product quantification and matched controls gates.
- If the claim depends on computational chemistry or AI, select model assumptions, baselines, sensitivity, data leakage, out-of-domain validation, uncertainty and chemical interpretability gates.
- If the claim depends on materials or interface chemistry, select morphology/transport/interface separation, active-site assignment, stability, comparability and reproducibility gates.

A concern should become major only when it materially affects the claim's support, novelty, mechanism, generality, comparability or reproducibility.
