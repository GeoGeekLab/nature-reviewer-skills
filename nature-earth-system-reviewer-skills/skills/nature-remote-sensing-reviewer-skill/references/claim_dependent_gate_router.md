# Claim-Dependent Gate Router

This file controls gate selection and gate weight. The reviewer must begin from the manuscript's own content. Do not import concerns merely because they are important in remote-sensing literature. Apply a gate only when a claim, method, dataset, figure, table, or conclusion in the manuscript makes that gate relevant.

## Step 1: Identify Claim Types

Classify the manuscript's central and secondary claims into one or more of the following:

- product or retrieval claim;
- validation or benchmark claim;
- spatial mapping or spatial generalization claim;
- trend, seasonal-change, breakpoint, acceleration, stability, or time-series claim;
- causal, mechanism, attribution, policy, or intervention claim;
- rare-event or extreme-event detection claim;
- novelty or prior-work-positioning claim;
- reproducibility, product-release, or operational-use claim;
- interpretation or management-relevance claim.

The classification must be based only on the manuscript and any verified retrieved sources allowed by the user.

## Step 2: Assign Gate Activation Levels

Use four levels:

- **Level 0 — not triggered.** The manuscript does not make a claim that depends on this gate. Do not mention it.
- **Level 1 — peripheral.** The gate is relevant only to a small detail. Use at most a minor comment or a cautiously worded limitation.
- **Level 2 — substantive.** The gate is important to a result, method, or figure. Use it as a substantive concern if evidence is weak.
- **Level 3 — central.** The gate is central to the journal-level claim or main conclusion. A weakness can become a major concern.

## Step 3: Conditional Gate Map

Apply gates as follows:

- **Trend and Time-Series Evidence Gate:** activate for claims of increase, decline, recovery, degradation, stability, acceleration, slowdown, breakpoint, seasonal change, temporal anomaly, climate signal, policy period, or temporal attribution.
- **Sampling, Validation, and Inference Integrity Gate:** activate for any reliance on reference observations, field data, station data, labels, benchmark products, in situ match-ups, geospatial machine learning, spatial mapping, rare-event analysis, causal attribution, or management conclusion.
- **Published-Paper Comparison Gate:** activate for novelty, priority, Nature-level positioning, similar product/method claims, or when retrieval is explicitly allowed. Use only verified sources.
- **Micro-Consistency Gate:** activate for all manuscript reviews, but keep it at minor-comment level unless a consistency issue affects the main claim.
- **Claim Calibration Gate:** activate whenever language such as demonstrates, proves, driven by, mechanism, direct evidence, first, unprecedented, robust, global, policy-driven, or dominant driver appears.

## Step 4: Avoid Overweighting

Do not apply every methodological concern as if it were equally important. A gate becomes a major concern only when the manuscript's central contribution depends on it. For example:

- a static classification paper should not be dominated by trend-detection requirements;
- a local descriptive case study should not be rejected for lacking global transferability unless it claims global relevance;
- a paper without causal language should not be forced into a causal-inference framework;
- a paper without extreme-event claims should not be critiqued using rare-event requirements;
- a manuscript that does not permit external retrieval should not be penalized for absence of unverified external comparisons, although its own references can still be assessed.

## Step 5: Translate Gates Into Natural Referee Prose

Do not name gates in the author-facing report. Convert gate findings into referee language, for example:

- "My foremost concern is that the evidence supporting the temporal claim is weaker than the manuscript implies."
- "I am not convinced that the reported validation demonstrates generalization beyond the sampled locations."
- "The reference observations should be treated as measurements with their own scale and uncertainty rather than as ground truth."
- "The manuscript should clarify whether the event definition was specified before examining the anomaly."
