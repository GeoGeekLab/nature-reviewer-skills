# Evidence Chain Gate

Trace the full path from the manuscript's main claim back to the evidence that supports it. The reviewer should identify where uncertainty, bias, missing validation, dependence, or over-interpretation enters the chain.

## Evidence Chain

Check:

1. main claim and claim type;
2. input data and data versions;
3. preprocessing, masking, compositing, and quality control;
4. retrieval, classification, modeling, or inversion method;
5. reference observations or benchmark data;
6. sampling design and representativeness;
7. match-up and scale compatibility;
8. validation design and independence;
9. uncertainty propagation;
10. statistical inference;
11. interpretation and generalization;
12. claim calibration.

Use `claim_dependent_gate_router.md` to decide which specialized gates to activate. Trend/time-series issues, sampling/inference integrity issues, and published-paper comparison should enter the review only when the manuscript's own claims require them.

A strong referee report should explain not only that a conclusion is weak, but which link in the evidence chain is weak and what additional analysis or claim calibration would address it.
