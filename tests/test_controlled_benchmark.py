from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path

from nature_reviewer_core.evaluation import aggregate, load_cases, load_predictions, score_case

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "benchmarks/controlled_v1/cases.jsonl"
ORACLE = ROOT / "benchmarks/controlled_v1/oracle_predictions.jsonl"


def test_controlled_suite_is_balanced_and_paired() -> None:
    cases = load_cases(CASES)
    assert len(cases) == 48

    types = Counter(case.case_type for case in cases)
    assert types == {"positive": 24, "negative_control": 24}

    domains = Counter(case.domain for case in cases)
    assert len(domains) == 8
    assert set(domains.values()) == {6}

    pairs: dict[str, list[str]] = defaultdict(list)
    for case in cases:
        pairs[case.pair_id].append(case.case_type)
    assert len(pairs) == 24
    assert all(sorted(types) == ["negative_control", "positive"] for types in pairs.values())


def test_controlled_suite_oracle_is_only_a_scorer_self_test() -> None:
    cases = load_cases(CASES)
    predictions = load_predictions(ORACLE)
    scores = [score_case(case, predictions.get(case.case_id, [])) for case in cases]
    report = aggregate(scores)

    assert report["macro"]["essential_issue_recall"] == 1.0
    assert report["controls"]["specificity"] == 1.0
    assert report["essential_balanced_accuracy"] == 1.0
    assert report["paired_pass_rate"] == 1.0
    assert report["micro"]["f1"] == 1.0
    assert report["bootstrap_95ci"]["essential_balanced_accuracy"] == [1.0, 1.0]
