# CRD-v1 data audit

This audit describes the released dataset structure. It is a deterministic construction audit, not a reviewer-performance result.

## Dataset balance

- Cases: **48**
- Matched pairs: **24**
- Positive cases: **24**
- Negative controls: **24**
- Review groups: **8**
- Cases per review group: **6** (3 positive + 3 controls)
- Distinct target issue IDs: **24**
- Methodological source keys referenced by cases: **22**

## Excerpt size

Tokenization here uses a simple lowercase alphanumeric/hyphen word tokenizer for descriptive auditing only.

- Minimum excerpt length: **65 words**
- Maximum excerpt length: **121 words**
- Mean excerpt length: **89.8 words**
- Median excerpt length: **89 words**

The excerpts are intentionally short diagnostic stimuli, not simulated full manuscripts.

## Pair matching

Positive and control cases share the same scientific setting and target claim family, but controls are not restricted to a single-token or single-sentence edit. Depending on the challenge, the counterfactual repair may require:

- adding an independent validation design;
- adding discriminating controls;
- changing the uncertainty/replication structure;
- replacing an unmatched benchmark with a matched benchmark; or
- narrowing the conclusion so it no longer exceeds the evidence.

As a coarse descriptive check, set-based word-token Jaccard similarity across the 24 pairs ranges from **0.314 to 0.773**, with mean **0.446**. This statistic is not a benchmark endpoint and should not be interpreted as semantic equivalence.

Because repairs sometimes require substantive method text, CRD-v1 should be described as a **matched scientific counterfactual benchmark**, not a minimal-edit benchmark.

## Balance is not representativeness

Equal domain counts are deliberate experimental blocking. They prevent high-volume domains from dominating pooled metrics, but they do not estimate the natural frequency of review failures in the scientific literature.

Likewise, the 24 challenge types were selected to exercise evidence risks represented by the reviewer skills. This supports controlled diagnostic testing but creates construction bias. Open-world performance requires an independently designed held-out set.

## Scientific plausibility

Numerical values and experimental settings were chosen to be plausible rather than copied from published manuscripts. They are synthetic and should not be interpreted as empirical measurements or literature-derived effect sizes.

Each case contains source keys that document the methodological principle motivating the target defect. Source material supports the **evaluation principle**; it is not presented as provenance for the synthetic numerical values.
