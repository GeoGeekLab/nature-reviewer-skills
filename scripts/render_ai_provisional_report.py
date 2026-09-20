from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


PRIMARY = [
    "essential_issue_recall",
    "target_specificity",
    "essential_balanced_accuracy",
    "paired_pass_rate",
]
SECONDARY = ["micro_precision", "micro_recall", "micro_f1"]


def _json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"Expected object in {path}")
    return value


def _fmt(value: Any) -> str:
    if isinstance(value, float):
        return f"{value:.4f}"
    return str(value)


def render(
    *,
    agreement_path: Path,
    consensus_path: Path,
    a_path: Path,
    b_path: Path,
    intersection_path: Path,
    union_path: Path,
    output_path: Path,
) -> dict[str, Any]:
    agreement = _json(agreement_path)
    consensus = _json(consensus_path)
    analyses = {
        "Annotator A — Llama 3.2 3B": _json(a_path),
        "Annotator B — Gemma 2 2B": _json(b_path),
        "Intersection consensus (primary provisional)": _json(intersection_path),
        "Union sensitivity bound": _json(union_path),
    }

    lines = [
        "# CRD-v1 three-domain pilot — AI double-blind provisional analysis",
        "",
        "> Status: automated provisional annotation. This is **not** independent human validation,",
        "> expert annotation, or evidence of expert equivalence.",
        "",
        "## Annotation design",
        "",
        "- Two condition-blinded AI annotators from different model families.",
        "- Annotators saw only annotation ID, domain, manuscript excerpt, review output, and the domain codebook.",
        "- They did not see generic/skill condition, case type, pair ID, target issue, gold, oracle, or private mapping.",
        "- Primary provisional consensus is the intersection of independently coded issue IDs.",
        "- Union is reported only as a sensitivity bound.",
        "",
        "## Agreement before unblinded scoring",
        "",
        f"- Target-issue observed agreement: {_fmt(agreement['overall']['observed_agreement'])}",
        f"- Target-issue Cohen's kappa: {_fmt(agreement['overall']['cohen_kappa'])}",
        f"- Annotation packets with any codebook-label disagreement: "
        f"{consensus['annotations_with_any_label_disagreement']} / {consensus['annotation_count']}",
        f"- Total codebook-label disagreements: {consensus['label_disagreement_count']}",
        "",
        "## Primary endpoints",
        "",
        "| Coding view | Endpoint | Generic | Skill-assisted | Δ skill − generic | 95% pair-bootstrap CI for Δ |",
        "|---|---|---:|---:|---:|---:|",
    ]
    for name, analysis in analyses.items():
        for endpoint in PRIMARY:
            generic = analysis["observed"]["generic"][endpoint]
            skill = analysis["observed"]["skill-assisted"][endpoint]
            delta = analysis["delta_skill_minus_generic"][endpoint]
            ci = analysis["bootstrap_95ci"]["delta_skill_minus_generic"][endpoint]
            lines.append(
                f"| {name} | {endpoint} | {_fmt(generic)} | {_fmt(skill)} | "
                f"{_fmt(delta)} | [{_fmt(ci[0])}, {_fmt(ci[1])}] |"
            )

    lines.extend(
        [
            "",
            "## Secondary endpoints",
            "",
            "| Coding view | Endpoint | Generic | Skill-assisted | Δ skill − generic | 95% pair-bootstrap CI for Δ |",
            "|---|---|---:|---:|---:|---:|",
        ]
    )
    for name, analysis in analyses.items():
        for endpoint in SECONDARY:
            generic = analysis["observed"]["generic"][endpoint]
            skill = analysis["observed"]["skill-assisted"][endpoint]
            delta = analysis["delta_skill_minus_generic"][endpoint]
            ci = analysis["bootstrap_95ci"]["delta_skill_minus_generic"][endpoint]
            lines.append(
                f"| {name} | {endpoint} | {_fmt(generic)} | {_fmt(skill)} | "
                f"{_fmt(delta)} | [{_fmt(ci[0])}, {_fmt(ci[1])}] |"
            )

    lines.extend(
        [
            "",
            "## Interpretation boundary",
            "",
            "These numbers describe a public synthetic controlled diagnostic subset under one fixed Qwen2.5-3B",
            "review-generation configuration and automated AI coding. The benchmark taxonomy overlaps the",
            "reviewer-skill taxonomy by design. Results must not be described as independent expert validation,",
            "real-manuscript performance, editorial-decision accuracy, or expert-level reviewing.",
            "",
            "The intersection consensus is intentionally conservative. Differences between the individual",
            "annotators, intersection, and union should be treated as annotation uncertainty rather than hidden.",
            "",
        ]
    )
    output_path.write_text("\n".join(lines), encoding="utf-8")

    summary = {
        "status": "automated provisional annotation",
        "agreement": agreement,
        "consensus": consensus,
        "analyses": analyses,
    }
    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--agreement", type=Path, required=True)
    parser.add_argument("--consensus", type=Path, required=True)
    parser.add_argument("--annotator-a-analysis", type=Path, required=True)
    parser.add_argument("--annotator-b-analysis", type=Path, required=True)
    parser.add_argument("--intersection-analysis", type=Path, required=True)
    parser.add_argument("--union-analysis", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--summary-json", type=Path, required=True)
    args = parser.parse_args()

    result = render(
        agreement_path=args.agreement,
        consensus_path=args.consensus,
        a_path=args.annotator_a_analysis,
        b_path=args.annotator_b_analysis,
        intersection_path=args.intersection_analysis,
        union_path=args.union_analysis,
        output_path=args.output,
    )
    args.summary_json.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "report": str(args.output)}, indent=2))
