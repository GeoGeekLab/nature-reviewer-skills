# Biodiversity and ecosystem-function gate

## Purpose
Use this gate when a manuscript makes claims related to biodiversity and ecosystem-function.

## Trigger signals

- `biodiversity`
- `species`
- `richness`
- `diversity`
- `community`
- `food web`
- `trophic`
- `predator`
- `ecosystem function`
- `stability`
- `resilience`
- `network`
- `trait`
- `functional diversity`
- `habitat`

## Reviewer concern patterns distilled from corpus

- **CECO-P0001** (abstracted_reviewer_concern): Biodiversity and ecosystem-function claims need direct metrics rather than assuming richness, composition, resilience, or trophic structure from proxy variables alone.
- **CECO-P0002** (abstracted_reviewer_concern): Food-web, community, or ecosystem-stability conclusions should make the unit of analysis and ecological mechanism explicit.
- **CECO-P0003** (abstracted_reviewer_concern): Species distribution or community-response claims need attention to detectability, taxonomic resolution, temporal mismatch, and spatial representativeness.
- **CECO-P0004** (issue_cluster): For Biodiversity and ecosystem-function gate, reviewers repeatedly flag biodiversity/ecosystem/function when the manuscript's evidence chain does not make this point explicit enough for a broad high-impact-journal audience.
- **CECO-P0005** (issue_cluster): For Biodiversity and ecosystem-function gate, reviewers repeatedly flag sampling/representativeness when the manuscript's evidence chain does not make this point explicit enough for a broad high-impact-journal audience.
- **CECO-P0006** (issue_cluster): For Biodiversity and ecosystem-function gate, reviewers repeatedly flag causal overclaim when the manuscript's evidence chain does not make this point explicit enough for a broad high-impact-journal audience.
- **CECO-P0007** (issue_cluster): For Biodiversity and ecosystem-function gate, reviewers repeatedly flag uncertainty when the manuscript's evidence chain does not make this point explicit enough for a broad high-impact-journal audience.
- **CECO-P0008** (issue_cluster): For Biodiversity and ecosystem-function gate, reviewers repeatedly flag figure/table clarity when the manuscript's evidence chain does not make this point explicit enough for a broad high-impact-journal audience.

## Evidence expected before accepting the claim

- direct biodiversity or ecosystem-function metrics
- detectability/taxonomic resolution
- mechanism evidence
- ecological unit clarity

## Typical claim-language risk

- assuming biodiversity, stability, or function without direct measurement

## Corpus support summary

- Distilled unit count: 918
- Source article count: 47
- Frequent issue labels: biodiversity/ecosystem/function (367), sampling/representativeness (142), causal overclaim (77), uncertainty (73), figure/table clarity (70), novelty/significance (64), assumption/parameterization (49), definition/scope (44)

## Output expectation

When this gate is triggered, write reviewer comments that are claim-specific, evidence-chain aware, and calibrated to the manuscript's actual scope. Prefer explicit tests or revisions over generic requests.

## Additional stress tests

- Distinguish richness, abundance, composition, turnover, beta diversity, functional diversity, phylogenetic diversity, ecosystem function, resilience and stability.
- For biodiversity time-series claims, check whether local assemblage change is being conflated with global extinction risk or whether turnover is being presented as loss.
- Check detectability, taxonomic resolution, sampling effort, rare-species treatment, invasive/common species effects and temporal baseline choice.
