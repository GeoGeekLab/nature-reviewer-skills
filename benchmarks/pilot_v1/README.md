# CRD-v1 three-domain blinded pilot

This directory turns the CRD-v1 comparison protocol into an executable pilot for:

- remote sensing;
- chemistry; and
- engineering.

The pilot contains 18 cases / 9 matched pairs and specifies three independent runs per case in each of two conditions.

## Why this pilot exists

CRD-v1 already defines the benchmark. This pilot tests whether the **experimental workflow itself** is workable before expanding to all 48 cases.

The two arms are:

- frozen generic scientific review;
- the same base model plus the corresponding domain reviewer skill.

## Important contamination boundary

Do not use the current development conversation or any model instance that has already inspected CRD-v1 gold metadata to generate benchmark outputs.

A valid pilot run must use a fresh model execution context that has not been shown case types, target issues, gold concerns, oracle predictions, or paired counterparts.

## Prepare blinded execution packets

~~~bash
python scripts/prepare_blinded_pilot.py \
  --model-id "<exact-model-version>" \
  --output pilot_runs/crd-v1-three-domain
~~~

Then validate that the generated packets contain no gold metadata:

~~~bash
python scripts/validate_pilot_packets.py pilot_runs/crd-v1-three-domain
~~~

The generated directory is gitignored by default.

## Generated structure

~~~text
pilot_runs/crd-v1-three-domain/
  run_manifest.json
  execution_packets/
    generic_run_01.jsonl
    generic_run_02.jsonl
    generic_run_03.jsonl
    skill-assisted_run_01.jsonl
    skill-assisted_run_02.jsonl
    skill-assisted_run_03.jsonl
  private_mapping.json
~~~

`private_mapping.json` must not be supplied to the tested model or initial annotators.

## What each execution packet contains

A packet record contains only:

- opaque `blind_id`;
- frozen prompt text;
- manuscript excerpt;
- skill path for the skill-assisted arm.

It deliberately omits CRD-v1 case IDs and gold metadata.

## Raw output

For each packet, save the model response unchanged as JSONL:

~~~json
{"blind_id":"B000001","review_text":"..."}
~~~

Do not add issue IDs during inference.

## Annotation

After all outputs are frozen, create condition-blinded annotation packets:

~~~bash
python scripts/build_pilot_annotation_packets.py \
  --pilot-dir pilot_runs/crd-v1-three-domain \
  --raw-outputs pilot_runs/crd-v1-three-domain/raw_outputs.jsonl
~~~

Initial annotators receive the generated `annotation_packets.jsonl`, not `private_mapping.json`.

Follow [PREREGISTRATION.md](PREREGISTRATION.md) and the main [CRD-v1 annotation protocol](../controlled_v1/ANNOTATION_PROTOCOL.md).

## Analysis

Analysis must use adjudicated annotations and pair-clustered uncertainty. The analysis script is intentionally separate from inference so gold metadata cannot leak into model generation.

See [RESULTS_TEMPLATE.md](RESULTS_TEMPLATE.md) for the required public reporting format.

## Current status

This directory provides the **pre-registered harness only**. No model-performance number should be added until a fresh, uncontaminated model run and blinded annotation have been completed.
