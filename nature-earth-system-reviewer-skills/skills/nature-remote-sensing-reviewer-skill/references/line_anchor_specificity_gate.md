# Line, Page, and Paragraph Anchor Specificity Gate

Use this gate for every full-manuscript review. A review is not sufficiently detailed if it only gives broad thematic concerns and no locatable comments.

## Purpose

The report should help authors find the exact sentence, paragraph, figure, table, equation, data statement, or supplement item that triggered each detailed concern. The reviewer must not invent line or page numbers. Instead, use the strongest locatable anchor supported by the submitted material.

## Anchor hierarchy

Use anchors in this order:

1. Exact manuscript line ranges, when real line numbers are present in the submitted text or PDF.
2. Exact page and line ranges, when PDF extraction or the manuscript visibly provides them.
3. Figure, table, equation, box, extended-data, or supplementary-text labels.
4. Section plus paragraph number assigned during extraction, for example `Methods, paragraph 12` or `Main text ¶043`.
5. Section plus a short quoted sentence opening, for example `Methods, paragraph beginning "We acquired 10,355..."`.
6. If only figures or captions are available, use `Figure 2 caption`, `Fig. S4`, or the visible panel label.

Do not write `Line 65-68` unless those line numbers are present in the input or generated in a documented extracted-text file. If line numbers are not present in the manuscript, create an extracted text file with paragraph or line anchors and cite those anchors consistently.

## Extraction-anchor workflow

When reviewing `.docx`, `.pdf`, `.md`, `.txt`, or extracted text files in a file-capable environment:

1. Create `review_inputs_extracted/`.
2. Extract manuscript and supplement text into anchored files such as:
   - `review_inputs_extracted/main_manuscript_anchored.md`
   - `review_inputs_extracted/supplement_anchored.md`
3. Preserve headings, captions, table labels, figure labels, data/code availability sections, and references when possible.
4. Assign stable anchors to paragraphs and extracted lines.
5. Use those anchors in detailed comments when original line numbers are unavailable.

The extraction anchors are review aids; they are not a claim that the original Word document has line numbers.

## Required detailed comments for full reviews

For a readable full manuscript, include a locatable detailed-comment layer unless the user explicitly asks for a high-level assessment only.

A normal full review should include, across the referee report:

- at least several page/line/paragraph/figure/table-specific comments;
- wording and consistency comments tied to exact anchors;
- at least one method or equation accessibility comment when equations/tables are central and extraction shows an issue;
- data/code availability and reproducibility comments tied to the relevant statement;
- supplement-specific comments when supplement material is readable.

The detailed comments may appear as `Specific comments`, `Line-specific comments`, `A few smaller points`, or be integrated into each referee section. Do not force every referee to use the same heading.

## Style rules

Line-specific comments can be concise and conversational, as in real referee reports:

- `Lines 65-68: I am not sure this causal wording follows from the analysis presented here.`
- `Page 13: I would prefer to see these trait results in the main body of the paper.`
- `Data availability: why is access dependent on a single corresponding author? This seems at odds with the open-science framing.`
- `Table S2: the significance notation appears inconsistent.`
- `Methods ¶027: the 3 x 3 pixel match-up rule needs sensitivity testing in this estuarine setting.`

Use this style to increase specificity, not to make the review casual or adversarial.

## Guardrails

- Do not fabricate line/page numbers.
- Do not quote long passages.
- Do not overfocus on copyediting when central evidence problems remain.
- Do not let line comments replace substantive reasoning; they are an additional layer.
- If no stable anchors can be extracted, state that line-specific commenting was limited and use section/figure/table references.
