# Raw pilot outputs

Raw outputs are intentionally not committed by default.

For every execution packet, preserve the model response unchanged:

~~~json
{"blind_id":"B000001","review_text":"full model response"}
~~~

Rules:

- exactly one record per blind ID;
- no manual editing of review text;
- no issue IDs added during inference;
- no case metadata added to this file;
- technical retries documented separately;
- freeze raw outputs before annotation.

The generated `pilot_runs/` workspace is gitignored to reduce accidental benchmark leakage or selective publication of intermediate runs.
