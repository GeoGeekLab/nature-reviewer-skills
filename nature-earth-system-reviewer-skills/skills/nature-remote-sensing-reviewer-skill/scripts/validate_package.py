#!/usr/bin/env python3
import argparse
import csv
import json
import re
import sys
from pathlib import Path

FORBIDDEN_NAMES = [".bak", ".tmp", ".patch", ".diff", "old", "backup", "archive", "migration", "copy"]
REQUIRED_FILES = [
    "SKILL.md", "README.md", "MANIFEST.json", "provenance.md", "THIRD_PARTY_NOTICES.md",
    "reviewer_db/manifest.json", "reviewer_db/documents.jsonl", "reviewer_db/review_units.jsonl",
    "reviewer_db/issue_patterns.jsonl", "reviewer_db/contribution_patterns.jsonl", "reviewer_db/style_moves.jsonl",
    "reviewer_db/style_motifs.jsonl", "reviewer_db/trend_issue_patterns.jsonl", "reviewer_db/inference_integrity_patterns.jsonl",
    "reviewer_db/referee_voice_profiles.jsonl", "reviewer_db/method_reference_patterns.jsonl", "reviewer_db/anchor_comment_patterns.jsonl",
    "references/claim_dependent_gate_router.md", "references/trend_time_series_evidence_gate.md",
    "references/sampling_validation_inference_integrity_gate.md", "references/nature_referee_format_gate.md",
    "references/nature_referee_style_gate.md", "references/uploaded_file_autorun_gate.md", "references/micro_consistency_gate.md",
    "references/published_paper_comparison_gate.md", "references/referee_voice_diversity_gate.md",
    "references/editorial_assessment_gate.md", "references/method_reference_suggestion_gate.md",
    "references/external_literature_search_gate.md", "references/output_delivery_gate.md",
    "references/review_depth_and_completeness_gate.md", "references/line_anchor_specificity_gate.md",
    "templates/nature_peer_review_file_template.md", "templates/internal_review_audit_template.md",
    "templates/published_paper_comparison_template.md", "templates/review_output_delivery_template.md",
    "scripts/reviewer_db.py", "scripts/sample_referee_style.py", "scripts/published_paper_query_builder.py",
    "scripts/render_review_docx.py", "scripts/extract_text_with_anchors.py", "scripts/validate_package.py"
]
EXAMPLE_DIRS = [
    "examples/abstract_only_review", "examples/full_text_no_line_numbers", "examples/figure_only_review",
    "examples/ml_remote_sensing_review", "examples/long_term_trend_review", "examples/product_validation_review",
    "examples/minimal_uploaded_file_review"
]
SKILL_TERMS = [
    "Uploaded-File Autorun", "Claim-Dependent Gate Routing", "Trend and Time-Series Evidence Gate",
    "Sampling, Validation, and Inference Integrity Gate", "Published-Paper", "Editorial Assessment Gate",
    "Referee Voice Diversity", "Method-Reference", "Output Delivery", "Review Depth and Completeness Gate", "Markdown", ".docx",
    "Reviewer Behavior Memory", "external retrieval is allowed", "Line/Page/Paragraph Anchor Specificity Gate", "locatable comments"
]

def parse_json(p):
    with p.open("r", encoding="utf-8") as f:
        return json.load(f)

def parse_jsonl(p):
    n = 0
    with p.open("r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            if line.strip():
                json.loads(line); n += 1
    return n

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root", nargs="?", default=".")
    ap.add_argument("--root", dest="root_option", default=None)
    args = ap.parse_args()
    root = Path(args.root_option or args.root).resolve()
    errors = []
    if not root.exists(): errors.append(f"root does not exist: {root}")

    for p in root.rglob("*"):
        name = p.name.lower()
        if p.is_file() and name.endswith(".pdf"):
            errors.append(f"raw PDF found: {p.relative_to(root)}")
        for bad in FORBIDDEN_NAMES:
            if bad in name: errors.append(f"forbidden trace name: {p.relative_to(root)}")

    for rel in REQUIRED_FILES:
        if not (root/rel).is_file(): errors.append(f"missing required file: {rel}")
    for rel in EXAMPLE_DIRS:
        if not (root/rel).is_dir(): errors.append(f"missing example dir: {rel}")

    for p in root.rglob("*.json"):
        try: parse_json(p)
        except Exception as e: errors.append(f"JSON parse failed {p.relative_to(root)}: {e}")
    for p in root.rglob("*.jsonl"):
        try: parse_jsonl(p)
        except Exception as e: errors.append(f"JSONL parse failed {p.relative_to(root)}: {e}")
    for p in root.rglob("*.csv"):
        try:
            with p.open("r", encoding="utf-8", newline="") as f: list(csv.reader(f))
        except Exception as e: errors.append(f"CSV parse failed {p.relative_to(root)}: {e}")

    try:
        m = parse_json(root/"reviewer_db/manifest.json")
        checks = {"source_pdf_count": 71, "raw_pdf_included": False, "document_count": 71, "cluster_count": 17, "embedding_runtime_required": False}
        for k, v in checks.items():
            if m.get(k) != v: errors.append(f"reviewer_db/manifest.json {k} expected {v!r}, got {m.get(k)!r}")
        if m.get("referee_voice_profile_count", 0) < 8: errors.append("referee_voice_profile_count too low")
        if m.get("method_reference_pattern_count", 0) < 6: errors.append("method_reference_pattern_count too low")
        if not m.get("referee_voice_diversity", {}).get("distinct_referee_styles"):
            errors.append("referee voice diversity not enabled")
        if not m.get("output_delivery", {}).get("docx_file"):
            errors.append("DOCX output delivery not enabled")
        if not m.get("output_delivery", {}).get("mandatory_in_file_capable_environment"):
            errors.append("mandatory file output not enabled")
        if not m.get("review_depth_and_completeness", {}).get("full_manuscript_depth_floor"):
            errors.append("full-manuscript depth floor not enabled")
        if not m.get("line_anchor_specificity", {}).get("enabled"):
            errors.append("line anchor specificity not enabled")
        if not m.get("line_anchor_specificity", {}).get("locatable_detailed_comments_required_for_full_reviews"):
            errors.append("locatable detailed comments not required")
        if m.get("anchor_comment_pattern_count", 0) < 6:
            errors.append("anchor_comment_pattern_count too low")
        if not m.get("editorial_assessment", {}).get("allowed_when_requested_or_warranted"):
            errors.append("editorial assessment gate not enabled")
    except Exception as e:
        errors.append(f"manifest check failed: {e}")

    try:
        docs = parse_jsonl(root/"reviewer_db/documents.jsonl")
        if docs != 71: errors.append(f"documents.jsonl expected 71 records, got {docs}")
    except Exception as e: errors.append(f"documents count check failed: {e}")

    skill = (root/"SKILL.md").read_text(encoding="utf-8") if (root/"SKILL.md").exists() else ""
    for term in SKILL_TERMS:
        if term not in skill: errors.append(f"SKILL.md missing term: {term}")
    if skill.count("my foremost concern") > 2:
        errors.append("SKILL.md overuses stock phrase 'my foremost concern'")

    author_template = (root/"templates/nature_peer_review_file_template.md").read_text(encoding="utf-8") if (root/"templates/nature_peer_review_file_template.md").exists() else ""
    for term in ["locatable", "generated paragraph anchors"]:
        if term not in author_template: errors.append(f"author-facing template missing anchor term: {term}")
    for term in ["Blind-test compliance check"]:
        if term in author_template: errors.append(f"author-facing template contains forbidden term: {term}")

    abs_pat = re.compile(r"[A-Za-z]:\\(?:[^\s<>:\"|?*]+\\)+")
    for p in root.rglob("*"):
        if p.is_file() and p.suffix.lower() in {".md", ".json", ".jsonl", ".py", ".txt"}:
            try: txt = p.read_text(encoding="utf-8", errors="ignore")
            except Exception: continue
            if abs_pat.search(txt): errors.append(f"local absolute Windows path found in {p.relative_to(root)}")

    if errors:
        for e in errors: print("FAIL:", e)
        return 1
    print("Validation passed")
    return 0
if __name__ == "__main__": sys.exit(main())
