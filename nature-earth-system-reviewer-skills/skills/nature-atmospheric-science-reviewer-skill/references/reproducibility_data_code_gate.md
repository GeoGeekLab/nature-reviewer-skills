# Reproducibility, data, code, and workflow provenance gate

Use when the result requires specialized data processing, model configuration, trained weights, benchmark code, intermediate products, or quality-control filters.

Claim type → evidence risk → reviewer concern → revision direction

- Data product claim → versions and preprocessing not archived → result cannot be audited → provide data versions, filters, and intermediate products.
- Model or AI claim → configuration, seeds, weights, or code unavailable → reproduction is limited → archive executable workflow and environment details.
- Figure-level result → source data not mapped to code → audit trail is incomplete → provide scripts and source data for main figures.
