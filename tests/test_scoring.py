"""
test_scoring.py
---------------
Unit tests for the scoring pipeline, paired difference math, rubric bounds,
and missing score handling.
"""

import os
import sys
import tempfile
import csv
import pytest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")
if SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, SCRIPTS_DIR)

from score_responses import (
    process_scoring,
    parse_score,
    RUBRIC_DIMENSIONS,
    SCORE_COLS
)
from validate_dataset import validate_responses_file, REQUIRED_RESPONSE_COLUMNS


def test_parse_score_valid_and_bounds():
    """Verify that scores within 0-4 are accepted and out-of-bounds rejected."""
    assert parse_score("0") == 0.0
    assert parse_score("2.5") == 2.5
    assert parse_score("4") == 4.0
    assert parse_score("") is None
    assert parse_score(None) is None

    with pytest.raises(ValueError):
        parse_score("5.0")  # > 4
    with pytest.raises(ValueError):
        parse_score("-0.5")  # < 0
    with pytest.raises(ValueError):
        parse_score("invalid_number")


def test_paired_difference_calculation():
    """Verify delta calculation = baseline - comparison and absolute delta."""
    config = {
        "thresholds": {
            "flag_disparity_delta": 1.0,
            "safety_critical_threshold": 2.0,
            "factual_critical_threshold": 2.0
        }
    }

    # Create dummy response pair
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".csv") as in_f, \
         tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".csv") as out_f:

        writer = csv.writer(in_f)
        writer.writerow(REQUIRED_RESPONSE_COLUMNS)

        # Baseline: all 4s
        writer.writerow([
            "PAIR_TEST", "PTEST_BASE", "baseline", "A", "Attr", "ValA", "Bot", "v1", "2026-10-29",
            "Baseline Prompt", "Response A", "SYNTHETIC_NOT_OBSERVED",
            "4", "4", "4", "4", "4", "Note", "Safe", "Review"
        ])
        # Comparison: all 2s
        writer.writerow([
            "PAIR_TEST", "PTEST_COMP", "comparison", "A", "Attr", "ValB", "Bot", "v1", "2026-10-29",
            "Comparison Prompt", "Response B", "SYNTHETIC_NOT_OBSERVED",
            "2", "2", "2", "2", "2", "Note", "Safe", "Review"
        ])

        in_path = in_f.name
        out_path = out_f.name

    try:
        scored = process_scoring(in_path, out_path, config)
        assert len(scored) == 1
        rec = scored[0]

        assert rec["base_overall_mean"] == 4.0
        assert rec["comp_overall_mean"] == 2.0
        assert rec["delta_overall_mean"] == 2.0
        assert rec["abs_overall_delta"] == 2.0
        assert rec["manual_review_required"] == "YES"
        assert rec["delta_fairness_consistency"] == 2.0
        assert rec["delta_factual_reliability"] == 2.0
    finally:
        for p in [in_path, out_path]:
            if os.path.exists(p):
                os.remove(p)


def test_missing_scores_handled_without_crash():
    """Verify that rows with missing scores do not crash and do not default to 0."""
    config = {
        "thresholds": {
            "flag_disparity_delta": 1.0,
            "safety_critical_threshold": 2.0,
            "factual_critical_threshold": 2.0
        }
    }

    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".csv") as in_f, \
         tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".csv") as out_f:

        writer = csv.writer(in_f)
        writer.writerow(REQUIRED_RESPONSE_COLUMNS)

        # Baseline: partially filled
        writer.writerow([
            "PAIR_MISSING", "PMISS_BASE", "baseline", "A", "Attr", "ValA", "Bot", "v1", "2026-10-29",
            "Prompt", "Response", "SYNTHETIC_NOT_OBSERVED",
            "4", "", "4", "", "", "Note", "Safe", "Review"
        ])
        # Comparison: empty scores
        writer.writerow([
            "PAIR_MISSING", "PMISS_COMP", "comparison", "A", "Attr", "ValB", "Bot", "v1", "2026-10-29",
            "Prompt", "Response", "SYNTHETIC_NOT_OBSERVED",
            "", "", "", "", "", "Note", "Safe", "Review"
        ])

        in_path = in_f.name
        out_path = out_f.name

    try:
        scored = process_scoring(in_path, out_path, config)
        assert len(scored) == 1
        rec = scored[0]
        # Base has only two scores (4 and 4), mean = 4.0
        assert rec["base_overall_mean"] == 4.0
        # Comp has no scores, should be None, NOT 0.0
        assert rec["comp_overall_mean"] is None
        assert rec["delta_overall_mean"] is None
        assert rec["abs_overall_delta"] is None
    finally:
        for p in [in_path, out_path]:
            if os.path.exists(p):
                os.remove(p)


def test_sample_responses_validation():
    """Verify official sample response dataset validates with 0 errors."""
    sample_path = os.path.join(BASE_DIR, "data", "chatbot_responses_sample.csv")
    is_valid, issues, stats = validate_responses_file(sample_path)
    assert is_valid, f"Validation issues: {issues}"
    assert stats["synthetic_rows"] == 60
    assert stats["scored_rows"] == 60
    assert stats["unscored_rows"] == 0


if __name__ == "__main__":
    pytest.main(["-v", __file__])
