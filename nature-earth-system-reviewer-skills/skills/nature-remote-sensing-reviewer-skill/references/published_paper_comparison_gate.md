# Published-Paper Comparison Gate

Use this gate when the review can benefit from comparison with already published work that is highly aligned with the submitted manuscript. This gate is evidence-sensitive: use only papers that are actually retrieved from an allowed source, provided by the user, or present in the manuscript reference list. Do not invent papers, titles, authors, years, DOIs, journals, products, algorithms, datasets, or findings.

## Activation

Run this gate when any of the following conditions applies:

- the user asks for a Nature / Nature Communications-level review and web or literature retrieval is available;
- the manuscript makes strong claims of novelty, first demonstration, unprecedented coverage, direct evidence, policy relevance, mechanism, or generality;
- the manuscript proposes a new satellite product, retrieval framework, long-term reconstruction, attribution analysis, or management interpretation;
- the manuscript topic is likely to overlap with published remote-sensing, Earth-observation, water-quality, land-cover, cryosphere, hydrology, atmosphere, or geospatial machine-learning studies.

If the user forbids web search, if retrieval is unavailable, or if no verified source can be accessed, state in the internal audit that external published-paper comparison was not performed. In the author-facing report, discuss prior work generically unless the manuscript itself provides verifiable references.

## Search strategy

Build search queries from the manuscript title, abstract, keywords, target variable, sensor/product, study region, method, validation data, and central claim. Prefer precise combinations over broad generic queries.

Recommended query families:

1. Topic + target variable + remote-sensing method.
2. Study region + target variable + satellite/product.
3. Sensor/product + retrieval target + validation.
4. Main claim + environmental process + remote sensing.
5. Method family + target variable + region or ecosystem type.

For example, a water-quality manuscript might produce queries such as:

```text
Pearl River Estuary total nitrogen total phosphorus MODIS remote sensing
estuarine nutrient retrieval satellite in situ validation uncertainty
water quality nutrient trend MODIS estuary machine learning validation
```

## Source requirements

Use only verified published or accepted scholarly sources. Prefer journal articles, peer-reviewed conference papers when relevant, official publisher pages, DOI records, Crossref/Semantic Scholar/OpenAlex records, PubMed/Google Scholar records when available, or publisher-hosted pages. Preprints may be used only as context and must be labelled as preprints.

A paper is usable for comparison only if at least these metadata are verified:

- title;
- year;
- venue or source;
- DOI or stable URL when available;
- why it is similar to the manuscript.

## Similarity standard

Do not compare the manuscript with generic background papers unless no closer paper exists and the limitation is stated. Prioritize highly aligned papers sharing several of these dimensions:

- same or closely related target variable;
- same sensor, product, or data type;
- same ecosystem or geographic setting;
- similar retrieval or machine-learning strategy;
- similar validation design;
- similar trend, attribution, management, or causal claim;
- similar journal-level contribution claim.

## Comparison dimensions

For each high-similarity paper, compare:

- research question and novelty;
- data sources and sensors;
- retrieval/modeling design;
- validation independence and temporal coverage;
- uncertainty propagation;
- trend or attribution design;
- reproducibility and data/code availability;
- claim strength and calibration;
- whether the submitted manuscript clearly advances beyond that paper.

## How to write the comparison

In the author-facing referee report, use the comparison sparingly and naturally. Do not turn the report into a literature review. Acceptable formulations include:

```text
The manuscript should clarify how its product and validation design advance beyond closely related published remote-sensing water-quality reconstructions.

Compared with published estuarine water-quality retrieval studies, the present manuscript makes stronger trend and attribution claims but does not yet provide the corresponding temporal validation and uncertainty propagation.

I am not convinced that the claimed novelty is established unless the authors explicitly distinguish their contribution from already published satellite-based nutrient or water-quality products in comparable estuarine settings.
```

When naming specific papers, cite only verified metadata. If the retrieval evidence is weak or only metadata are available, frame the concern as a request for the authors to position the manuscript more carefully rather than as a definitive priority claim.

## Internal audit

Record the retrieval status separately in the internal audit:

- whether external retrieval was allowed;
- search queries used;
- sources checked;
- verified high-similarity papers found;
- papers excluded and why;
- comparison limitations;
- whether any author-facing claims depend on external comparison.


## Decision relevance

Highly related published papers should affect the review only when they bear directly on novelty, method choice, validation design, uncertainty treatment, trend interpretation, or attribution claims. Do not cite loosely related papers just to lengthen the report. If a close published analogue already resolves the same question with stronger evidence, state clearly that the manuscript must explain its incremental or conceptual advance.
