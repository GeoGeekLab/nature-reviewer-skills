# CRD-v1 annotation protocol

The scorer consumes coded issue IDs, but tested systems must not see those IDs during inference.

Annotators receive one excerpt, one raw review output, and the public codebook. They should be blinded to case_type and should not see the matched counterpart during initial coding.

Split the review into distinct concerns. For each concern record issue_id, severity, manuscript anchor, and reviewer/concern identifier.

A concern matches only when it identifies the **specific evidence failure**. A generic request for more experiments, more detail, more discussion, or more citations is not sufficient.

For scientific reporting:

1. use at least two domain-competent annotators;
2. code independently;
3. calculate agreement before adjudication;
4. adjudicate with a documented rule;
5. retain pre-adjudication and adjudicated files.

Cohen's kappa is appropriate for two annotators on binary issue presence; Krippendorff's alpha is appropriate for multiple annotators or missing ratings. Ordered severity can use weighted agreement.

Developer-authored gold is suitable for controlled diagnostics and software regression, not independent expert gold.
