# CRD-v1 run protocol

## Pre-register

Record the exact model/version, access date, review condition, inference settings, tool policy, number of runs, and endpoints before generating outputs.

The recommended experiment compares the same base model under:

1. the frozen generic-review prompt; and
2. the frozen skill-assisted prompt plus the corresponding domain skill.

## Blind the tested system

Provide only manuscript_text and the frozen condition prompt. The skill-assisted arm also receives the designated skill package.

Do not expose case_id, pair_id, case_type, challenge, source_keys, codebook, gold_concerns, oracle predictions, or the paired counterpart. Randomize order independently for each run.

## Hold conditions fixed

Use the same base model, excerpt, output instructions, and tool policy in both arms. Do not revise prompts after inspecting benchmark outputs. If the system is stochastic, use at least three independent runs per case.

## Preserve raw output

Save raw model output before annotation with system identifier, condition, run ID, timestamp, and inference settings. Do not ask the tested model to emit benchmark issue IDs.

## Annotation

Follow ANNOTATION_PROTOCOL.md. Scientific claims should use at least two independent domain-competent annotators before adjudication.

## Report

Report essential-issue recall, negative-control specificity, essential balanced accuracy, matched-pair pass rate, micro precision/F1, per-domain metrics, and pair-level bootstrap intervals.

CRD-v1 evaluates controlled issue detection. It does not establish editorial decision accuracy, literature completeness, novelty assessment, expert equivalence, or full-manuscript multimodal performance.
