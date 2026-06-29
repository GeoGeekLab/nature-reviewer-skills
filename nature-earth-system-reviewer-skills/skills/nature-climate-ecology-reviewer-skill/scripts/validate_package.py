"""Validate the Nature Climate Ecology Reviewer Skill v1.0 package."""

from __future__ import annotations

import argparse
import json
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path

REQUIRED_FILES: tuple[str, ...] = (
    "SKILL.md",
    "MANIFEST.json",
    "README.md",
    "reviewer_db/patterns.jsonl",
    "reviewer_db/patterns.csv",
    "reviewer_db/controversy_patterns.jsonl",
    "reviewer_db/controversy_patterns.csv",
    "templates/review_report_template.md",
    "references/claim_dependent_gate_router.md",
    "references/nature_review_format_gate.md",
    "references/referee_voice_style_gate.md",
    "references/published_paper_comparison_gate.md",
    "references/controversy_derived_stress_tests.md",
    "references/review_checkpoints_matrix.md",
    "references/decision_threshold_gate.md",
    "references/detail_audit_gate.md",
    "scripts/render_review_docx.py",
    "scripts/extract_text_with_anchors.py",
    "scripts/published_paper_query_builder.py",
    "scripts/reviewer_db.py",
    "scripts/sample_referee_style.py",
)

REQUIRED_SKILL_PHRASES: tuple[str, ...] = (
    "2-4 independent referees",
    "Do not organize the final report by internal gates",
    "Markdown `.md` file and a Word `.docx` file",
    "## Referee voice standard",
)

REQUIRED_TEMPLATE_PHRASES: tuple[str, ...] = (
    "Reviewer Reports on the Initial Version:",
    "Referees' comments:",
    "Referee #1 (Remarks to the Author):",
    "Referee #2 (Remarks to the Author):",
)


@dataclass(frozen=True, slots=True)
class ValidationResult:
    """Validation outcome for one package check."""

    is_valid: bool
    message: str


def load_json(path: Path) -> dict[str, object]:
    """Load a JSON object from a UTF-8 file."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON file: {path}: {exc}") from exc

    if not isinstance(data, dict):
        raise ValueError(f"Expected a JSON object in {path}")
    return data


def count_jsonl_rows(path: Path) -> int:
    """Return the number of non-empty JSONL rows and validate JSON syntax."""
    row_count = 0
    with path.open("r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            stripped = line.strip()
            if not stripped:
                continue
            try:
                json.loads(stripped)
            except json.JSONDecodeError as exc:
                message = f"Invalid JSONL at {path}:{line_number}: {exc}"
                raise ValueError(message) from exc
            row_count += 1
    return row_count


def find_missing_files(root: Path, required_files: Iterable[str]) -> list[str]:
    """Return required package files that do not exist under root."""
    return [
        relative_path
        for relative_path in required_files
        if not (root / relative_path).exists()
    ]


def find_missing_phrases(text: str, required_phrases: Iterable[str]) -> list[str]:
    """Return required phrases that are absent from text."""
    return [phrase for phrase in required_phrases if phrase not in text]


def validate_required_files(root: Path) -> ValidationResult:
    """Validate that all required package files are present."""
    missing_files = find_missing_files(root, REQUIRED_FILES)
    if missing_files:
        return ValidationResult(
            False,
            _format_list("Missing required files", missing_files),
        )
    return ValidationResult(True, "Required files found.")


def validate_pattern_counts(
    root: Path,
    manifest: dict[str, object],
) -> ValidationResult:
    """Validate reviewer pattern counts against MANIFEST metadata."""
    pattern_count = count_jsonl_rows(root / "reviewer_db/patterns.jsonl")
    controversy_count = count_jsonl_rows(
        root / "reviewer_db/controversy_patterns.jsonl"
    )

    corpus = manifest.get("corpus", {})
    if not isinstance(corpus, dict):
        return ValidationResult(False, "MANIFEST field `corpus` must be an object.")

    expected_pattern_count = corpus.get("abstracted_pattern_count")
    if (
        expected_pattern_count is not None
        and int(expected_pattern_count) != pattern_count
    ):
        message = (
            "Pattern count mismatch: "
            f"manifest={expected_pattern_count}, reviewer_db={pattern_count}"
        )
        return ValidationResult(False, message)

    expected_controversy_count = corpus.get("controversy_derived_pattern_count")
    if (
        expected_controversy_count is not None
        and int(expected_controversy_count) != controversy_count
    ):
        message = (
            "Controversy pattern count mismatch: "
            f"manifest={expected_controversy_count}, "
            f"reviewer_db={controversy_count}"
        )
        return ValidationResult(False, message)

    if pattern_count == 0:
        return ValidationResult(False, "No reviewer patterns found.")
    if controversy_count == 0:
        return ValidationResult(
            False,
            "No controversy-derived stress-test patterns found.",
        )

    return ValidationResult(
        True,
        (
            f"Pattern counts valid: {pattern_count} total, "
            f"{controversy_count} stress tests."
        ),
    )


def validate_output_constraints(root: Path) -> ValidationResult:
    """Validate the independent-referee output constraints in SKILL and template."""
    skill_text = (root / "SKILL.md").read_text(encoding="utf-8")
    missing_skill_phrases = find_missing_phrases(skill_text, REQUIRED_SKILL_PHRASES)
    if missing_skill_phrases:
        return ValidationResult(
            False,
            _format_list(
                "Missing required output-format constraints",
                missing_skill_phrases,
            ),
        )

    template_text = (root / "templates/review_report_template.md").read_text(
        encoding="utf-8"
    )
    missing_template_phrases = find_missing_phrases(
        template_text,
        REQUIRED_TEMPLATE_PHRASES,
    )
    if missing_template_phrases:
        return ValidationResult(
            False,
            _format_list("Missing required template markers", missing_template_phrases),
        )

    return ValidationResult(True, "Output constraints valid.")


def validate_manifest_file_list(
    root: Path,
    manifest: dict[str, object],
) -> ValidationResult:
    """Validate MANIFEST file listings when present."""
    listed_files = manifest.get("files")
    if listed_files is None:
        return ValidationResult(
            True,
            "MANIFEST has no file list; skipped file-list check.",
        )
    if not isinstance(listed_files, list) or not all(
        isinstance(item, str) for item in listed_files
    ):
        return ValidationResult(
            False,
            "MANIFEST field `files` must be a list of strings.",
        )

    missing_listed_files = find_missing_files(root, listed_files)
    if missing_listed_files:
        return ValidationResult(
            False,
            _format_list("MANIFEST lists files that are missing", missing_listed_files),
        )
    return ValidationResult(True, "MANIFEST file list valid.")


def validate_package(root: Path) -> list[ValidationResult]:
    """Run all package validation checks."""
    manifest_path = root / "MANIFEST.json"
    manifest = load_json(manifest_path) if manifest_path.exists() else {}

    return [
        validate_required_files(root),
        validate_manifest_file_list(root, manifest),
        validate_pattern_counts(root, manifest),
        validate_output_constraints(root),
    ]


def _format_list(title: str, values: Iterable[str]) -> str:
    """Format a human-readable validation failure list."""
    formatted_values = "\n".join(f"- {value}" for value in values)
    return f"{title}:\n{formatted_values}"


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Validate the reviewer skill package.")
    parser.add_argument(
        "root",
        nargs="?",
        default=".",
        help="Skill package root directory. Defaults to the current directory.",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Only print failures and final status.",
    )
    return parser.parse_args()


def main() -> int:
    """Validate a skill package and return a shell status code."""
    args = parse_args()
    root = Path(args.root).resolve()

    results = validate_package(root)
    failures = [result for result in results if not result.is_valid]

    if failures:
        for failure in failures:
            print(failure.message)
        return 1

    if not args.quiet:
        for result in results:
            print(result.message)

    manifest = load_json(root / "MANIFEST.json")
    print(
        "Package OK: "
        f"{manifest.get('name')} v{manifest.get('version')} "
        f"with {count_jsonl_rows(root / 'reviewer_db/patterns.jsonl')} patterns "
        f"({count_jsonl_rows(root / 'reviewer_db/controversy_patterns.jsonl')} "
        "controversy-derived stress tests)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
