from pathlib import Path

from nature_reviewer_core.evaluation import aggregate, load_case, load_predictions, score_case
from nature_reviewer_core.models import Concern
from nature_reviewer_core.panel import assign_perspectives, concern_overlap

ROOT = Path(__file__).resolve().parents[1]


def test_default_panel_has_non_overlapping_primary_focus() -> None:
    panel = assign_perspectives(3)
    focus_sets = [set(item.primary_focus) for item in panel]
    assert not (focus_sets[0] & focus_sets[1] & focus_sets[2])


def test_duplicate_detection_across_reviewers() -> None:
    concerns = [
        Concern(
            "a",
            "major",
            "Spatial random validation leaks neighbouring pixel information",
            reviewer_id="referee-1",
        ),
        Concern(
            "b",
            "major",
            "Spatial random validation leaks neighbouring pixel information",
            reviewer_id="referee-2",
        ),
    ]
    report = concern_overlap(concerns)
    assert report["duplicate_rate"] > 0


def test_example_predictions_score_perfectly() -> None:
    predictions = load_predictions(ROOT / "benchmarks/predictions/example_predictions.jsonl")
    scores = []
    for path in sorted((ROOT / "benchmarks/cases").glob("*.json")):
        case = load_case(path)
        scores.append(score_case(case, predictions[case.case_id]))
    result = aggregate(scores)
    assert result["macro"]["f1"] == 1.0
    assert result["macro"]["severity_agreement"] == 1.0
    assert result["macro"]["anchor_coverage"] == 1.0
