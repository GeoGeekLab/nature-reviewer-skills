# Novelty, scope and Nature-level significance gate

## Purpose
Use this gate when a manuscript makes claims related to novelty, scope and nature-level significance.

## Trigger signals

- `novel`
- `incremental`
- `significant`
- `importance`
- `advance`
- `general`
- `scope`
- `nature`
- `impact`
- `broad`
- `interesting`
- `timely`
- `substantial`
- `new`

## Reviewer concern patterns distilled from corpus

- **CECO-P0065** (abstracted_reviewer_concern): A Nature-level manuscript must state the conceptual advance beyond known patterns, not only provide a larger dataset or familiar result.
- **CECO-P0066** (abstracted_reviewer_concern): The title, abstract, and discussion should avoid over-generalizing beyond the system, time period, taxa, or model domain actually studied.
- **CECO-P0067** (abstracted_reviewer_concern): The manuscript should explain why the result changes understanding rather than merely confirming expectations.
- **CECO-P0068** (issue_cluster): For Novelty, scope and Nature-level significance gate, reviewers repeatedly flag novelty/significance when the manuscript's evidence chain does not make this point explicit enough for a broad high-impact-journal audience.
- **CECO-P0069** (issue_cluster): For Novelty, scope and Nature-level significance gate, reviewers repeatedly flag novelty/scope when the manuscript's evidence chain does not make this point explicit enough for a broad high-impact-journal audience.
- **CECO-P0070** (issue_cluster): For Novelty, scope and Nature-level significance gate, reviewers repeatedly flag uncertainty when the manuscript's evidence chain does not make this point explicit enough for a broad high-impact-journal audience.
- **CECO-P0071** (issue_cluster): For Novelty, scope and Nature-level significance gate, reviewers repeatedly flag definition/scope when the manuscript's evidence chain does not make this point explicit enough for a broad high-impact-journal audience.
- **CECO-P0072** (issue_cluster): For Novelty, scope and Nature-level significance gate, reviewers repeatedly flag sampling/representativeness when the manuscript's evidence chain does not make this point explicit enough for a broad high-impact-journal audience.

## Evidence expected before accepting the claim

- explicit conceptual advance
- comparison with prior work
- scope-limited claims
- broad-interest framing

## Typical claim-language risk

- overselling incremental or context-specific findings as general advances

## Corpus support summary

- Distilled unit count: 377
- Source article count: 53
- Frequent issue labels: novelty/significance (134), novelty/scope (106), uncertainty (32), definition/scope (26), sampling/representativeness (22), figure/table clarity (21), causal overclaim (12), assumption/parameterization (10)

## Output expectation

When this gate is triggered, write reviewer comments that are claim-specific, evidence-chain aware, and calibrated to the manuscript's actual scope. Prefer explicit tests or revisions over generic requests.

## Additional stress tests

- Compare the manuscript against the closest papers by claim and evidence layer, not only by topic keyword.
- Distinguish novelty of dataset, novelty of method, novelty of inference and novelty of conceptual framing.
- A large scale or topical relevance does not by itself establish Nature-level contribution without a clear advance and strong evidence.
