# Pilot annotations

Initial annotation must be blinded to model condition and case type.

Use the packet builder after all raw outputs are frozen. It generates:

- `annotation_packets.jsonl` — safe for initial annotators;
- `annotation_mapping.json` — private mapping back to execution blind IDs.

Each annotation record should eventually contain:

~~~json
{
  "annotation_id": "A000001",
  "annotator_id": "annotator-1",
  "concerns": [
    {
      "issue_id": "example-codebook-id",
      "severity": "major",
      "anchors": ["paragraph:2"]
    }
  ]
}
~~~

Annotators may record zero concerns.

Do not show initial annotators:

- generic vs skill-assisted condition;
- case_type;
- target_issue_id;
- paired counterpart;
- oracle predictions.

For public scientific interpretation, use at least two independent domain-competent annotators and retain pre-adjudication labels before adjudication.
