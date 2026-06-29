# Review Depth and Completeness Gate

Use this gate for every full-manuscript review. Voice diversity must not reduce evidentiary depth. A conversational referee style may change sentence rhythm, comment ordering, or paragraph shape, but it must not turn a full Nature-style review into a short summary.

## Depth routing

First determine material scope.

- Abstract-only, title-only, figure-only, or heavily unreadable submissions: concise review is allowed, but state the limitation.
- Main manuscript readable, supplement absent or partial: full review is required, with missing supplementary evidence clearly identified.
- Main manuscript and supplementary material readable: full-depth review is required.

## Full-depth minimum

For a readable full manuscript, the author-facing report should normally include:

1. A submitted-material completeness statement before the referee report.
2. Three referee sections unless the user requests another format.
3. At least two substantive evidence paragraphs per referee, and usually three or more when the manuscript makes product, validation, trend, attribution, novelty, or policy claims.
4. Specific comments tied to exact lines, pages, paragraphs, sections, figures, tables, equations, data/code availability, wording, or supplementary material when supported by the input.
5. Enough detail for the author to understand what analysis, validation, rewording, or evidence is needed.

Do not use a fixed word count as a visible rule, but internally avoid underdeveloped full reviews. A full review that only gives one or two broad concerns per referee is usually incomplete unless the submitted material is very short.

## Preserve older high-depth strengths

The report should retain the strengths of a rigorous technical review:

- trace claims to the data, validation, uncertainty, and interpretation layers;
- explain why a limitation matters for the central claim;
- name the specific missing analysis or sensitivity test;
- include micro-consistency and wording issues when present;
- distinguish major evidence failures from minor presentation issues.

## Avoid compression caused by style diversity

Do not let these style instructions shorten the review:

- varying reviewer voice;
- avoiding repetitive phrases such as "my foremost concern";
- reducing use of "Minor comments";
- making the report more conversational.

These should improve naturalness, not reduce technical coverage.

## File-output completeness

A review is not complete in a file-capable environment until both files exist:

- `review_outputs/nature_review_report.md`
- `review_outputs/nature_review_report.docx`

If the environment allows writing files and the files are not created, the task is incomplete.

## Locatable detailed-comment floor

For a readable full manuscript, the review should normally contain a line/page/paragraph-specific layer in addition to broad concerns. This layer should include multiple comments that an author can find directly in the manuscript or in an anchored extraction file.

Acceptable anchors include real line ranges, page ranges, figure/table/equation labels, supplementary labels, generated paragraph anchors, or section plus sentence-opening anchors. If the input does not contain real line numbers, use generated anchors rather than inventing manuscript line numbers.

A full review that contains only broad paragraphs and three short minor comments is underdeveloped when the source manuscript is complete and readable.
