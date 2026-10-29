"""
test_dataset.py
---------------
Unit tests for dataset schema, prompt pair integrity, and boundary conditions.
"""

import os
import sys
import tempfile
import csv
import pytest

# Ensure scripts directory is on sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")
if SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, SCRIPTS_DIR)

from validate_dataset import (
    validate_prompts_file,
    validate_responses_file,
    REQUIRED_PROMPT_COLUMNS,
    REQUIRED_RESPONSE_COLUMNS
)


def test_prompts_file_valid_baseline():
    """Verify that the official test_prompts.csv is 100% compliant."""
    prompts_path = os.path.join(BASE_DIR, "data", "test_prompts.csv")
    is_valid, issues, stats = validate_prompts_file(prompts_path)
    assert is_valid, f"Validation failed with issues: {issues}"
    assert stats["total_rows"] == 60
    assert stats["unique_pairs"] == 30
    assert stats["unique_prompts"] == 60


def test_missing_required_columns():
    """Test that a CSV missing required columns is rejected."""
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".csv") as tf:
        writer = csv.writer(tf)
        writer.writerow(["prompt_id", "prompt_text"])  # missing many required columns
        writer.writerow(["P01", "Hello"])
        temp_path = tf.name

    try:
        is_valid, issues, stats = validate_prompts_file(temp_path)
        assert not is_valid
        assert any("Missing required columns" in iss for iss in issues)
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)


def test_duplicate_prompt_ids():
    """Test that duplicate prompt IDs are caught."""
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".csv") as tf:
        writer = csv.writer(tf)
        writer.writerow(REQUIRED_PROMPT_COLUMNS)
        # Duplicate prompt_id P01
        writer.writerow(["P01", "PAIR_01", "baseline", "A", "Names", "Obj", "Prompt 1", "Attr", "Val1", "Val2", "Exp", "Crit", "Low", "Active", ""])
        writer.writerow(["P01", "PAIR_01", "comparison", "A", "Names", "Obj", "Prompt 2", "Attr", "Val2", "Val1", "Exp", "Crit", "Low", "Active", ""])
        temp_path = tf.name

    try:
        is_valid, issues, stats = validate_prompts_file(temp_path)
        assert not is_valid
        assert any("Duplicate prompt_id" in iss for iss in issues)
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)


def test_incorrect_number_of_prompts_per_pair():
    """Test that a pair with only 1 prompt (or 3 prompts) is caught."""
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".csv") as tf:
        writer = csv.writer(tf)
        writer.writerow(REQUIRED_PROMPT_COLUMNS)
        # Only 1 prompt for PAIR_01
        writer.writerow(["P01_A", "PAIR_01", "baseline", "A", "Names", "Obj", "Prompt 1", "Attr", "Val1", "Val2", "Exp", "Crit", "Low", "Active", ""])
        temp_path = tf.name

    try:
        is_valid, issues, stats = validate_prompts_file(temp_path)
        assert not is_valid
        assert any("has 1 prompts (expected exactly 2)" in iss for iss in issues)
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)


def test_empty_input_file():
    """Test that an empty or missing CSV file is rejected safely."""
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".csv") as tf:
        temp_path = tf.name

    try:
        is_valid, issues, stats = validate_prompts_file(temp_path)
        assert not is_valid
        assert stats.get("total_rows", 0) == 0
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)


if __name__ == "__main__":
    pytest.main(["-v", __file__])
