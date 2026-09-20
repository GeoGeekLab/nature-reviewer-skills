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


def test_negative_control_does_not_depress_positive_macro_metrics() -> None:
    from nature_reviewer_core.models import BenchmarkCase

    positive = BenchmarkCase(
        case_id="p",
        domain="demo",
        manuscript_text="positive",
        gold_concerns=(Concern("issue", "major", "target", anchors=("paragraph:1",)),),
        case_type="positive",
        pair_id="pair",
    )
    control = BenchmarkCase(
        case_id="c",
        domain="demo",
        manuscript_text="control",
        gold_concerns=(),
        case_type="negative_control",
        pair_id="pair",
    )
    positive_score = score_case(
        positive,
        [Concern("issue", "major", "target", anchors=("paragraph:1",))],
    )
    control_score = score_case(control, [])
    result = aggregate([positive_score, control_score])

    assert result["macro"]["f1"] == 1.0
    assert result["controls"]["specificity"] == 1.0
    assert result["essential_balanced_accuracy"] == 1.0
    assert result["paired_pass_rate"] == 1.0


def test_negative_control_false_positive_is_counted() -> None:
    from nature_reviewer_core.models import BenchmarkCase

    control = BenchmarkCase(
        case_id="c",
        domain="demo",
        manuscript_text="control",
        gold_concerns=(),
        case_type="negative_control",
        pair_id="pair",
    )
    score = score_case(control, [Concern("invented", "major", "unsupported concern")])

    assert score["negative_control_pass"] is False
    assert score["false_positive"] == 1
    assert score["precision"] is None


def test_control_specificity_is_target_specific_when_challenge_is_known() -> None:
    from nature_reviewer_core.models import BenchmarkCase

    control = BenchmarkCase(
        case_id="control-target",
        domain="demo",
        manuscript_text="A matched control excerpt with the target defect repaired.",
        gold_concerns=(),
        case_type="negative_control",
        pair_id="pair-target",
        challenge="target-issue",
        target_issue_id="target-issue",
    )
    unrelated = Concern("other-issue", "moderate", "A different coded concern")
    score = score_case(control, [unrelated])

    assert score["negative_control_pass"] is True
    assert score["false_positive"] == 1


def test_control_specificity_fails_when_target_issue_reappears() -> None:
    from nature_reviewer_core.models import BenchmarkCase

    control = BenchmarkCase(
        case_id="control-target",
        domain="demo",
        manuscript_text="A matched control excerpt with the target defect repaired.",
        gold_concerns=(),
        case_type="negative_control",
        pair_id="pair-target",
        challenge="target-issue",
        target_issue_id="target-issue",
    )
    target = Concern("target-issue", "major", "The repaired target is incorrectly flagged")
    score = score_case(control, [target])

    assert score["negative_control_pass"] is False
