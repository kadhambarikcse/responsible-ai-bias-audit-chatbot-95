"""
validate_dataset.py
-------------------
Validates integrity of prompt benchmarks and response datasets for
CAPSTONE 16 — Responsible AI and Bias Audit of a Chatbot.

Checks:
  1. File existence and CSV formatting
  2. Required column schemas
  3. Unique pair and prompt IDs
  4. Prompt pair symmetry (exactly 2 prompts per pair: 1 baseline, 1 comparison)
  5. Score bounds (0 <= score <= 4)
  6. Source type labeling (GENUINE_OBSERVED vs SYNTHETIC_NOT_OBSERVED)
  7. Missing fields or malformed records
"""

import os
import sys
import csv
import json
from typing import Dict, List, Tuple


REQUIRED_PROMPT_COLUMNS = [
    "prompt_id", "pair_id", "prompt_type", "category", "category_name",
    "test_objective", "prompt_text", "controlled_attribute",
    "attribute_value", "counterpart_attribute_value",
    "expected_fairness_behavior", "evaluation_criteria",
    "risk_level", "status", "notes"
]

REQUIRED_RESPONSE_COLUMNS = [
    "pair_id", "prompt_id", "prompt_type", "category",
    "controlled_attribute", "attribute_value", "chatbot_name",
    "model_version", "run_date", "exact_prompt", "raw_response",
    "source_type", "score_fairness_consistency",
    "score_factual_reliability", "score_safety",
    "score_respect_inclusiveness", "score_transparency_uncertainty",
    "factual_verification_notes", "safety_concerns", "reviewer_notes"
]

SCORE_FIELDS = [
    "score_fairness_consistency",
    "score_factual_reliability",
    "score_safety",
    "score_respect_inclusiveness",
    "score_transparency_uncertainty"
]


def validate_prompts_file(filepath: str) -> Tuple[bool, List[str], Dict]:
    """Validates the test_prompts.csv file."""
    issues = []
    stats = {}

    if not os.path.exists(filepath):
        return False, [f"File not found: {filepath}"], stats

    with open(filepath, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames or []
        missing_cols = [c for c in REQUIRED_PROMPT_COLUMNS if c not in header]
        if missing_cols:
            issues.append(f"Missing required columns in prompts file: {missing_cols}")

        rows = list(reader)

    stats["total_rows"] = len(rows)
    if len(rows) != 60:
        issues.append(f"Expected exactly 60 prompt rows, found {len(rows)}")

    pair_counts = {}
    prompt_ids = set()

    for i, r in enumerate(rows, start=2):
        pid = r.get("prompt_id", "").strip()
        pair_id = r.get("pair_id", "").strip()
        ptype = r.get("prompt_type", "").strip()

        if not pid:
            issues.append(f"Row {i}: Missing prompt_id")
        elif pid in prompt_ids:
            issues.append(f"Row {i}: Duplicate prompt_id '{pid}'")
        prompt_ids.add(pid)

        if not pair_id:
            issues.append(f"Row {i}: Missing pair_id")
        else:
            pair_counts[pair_id] = pair_counts.get(pair_id, 0) + 1

        if ptype not in ["baseline", "comparison"]:
            issues.append(f"Row {i}: Invalid prompt_type '{ptype}'. Must be 'baseline' or 'comparison'")

        if not r.get("prompt_text", "").strip():
            issues.append(f"Row {i}: Empty prompt_text for prompt_id '{pid}'")

    # Verify each pair has exactly 2 prompts
    for pair_id, count in pair_counts.items():
        if count != 2:
            issues.append(f"Pair '{pair_id}' has {count} prompts (expected exactly 2)")

    stats["unique_pairs"] = len(pair_counts)
    stats["unique_prompts"] = len(prompt_ids)
    is_valid = len(issues) == 0
    return is_valid, issues, stats


def validate_responses_file(filepath: str) -> Tuple[bool, List[str], Dict]:
    """Validates response records and scoring entries."""
    issues = []
    stats = {
        "total_rows": 0,
        "scored_rows": 0,
        "unscored_rows": 0,
        "synthetic_rows": 0,
        "genuine_rows": 0,
        "unlabeled_source_rows": 0
    }

    if not os.path.exists(filepath):
        return False, [f"File not found: {filepath}"], stats

    with open(filepath, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames or []
        missing_cols = [c for c in REQUIRED_RESPONSE_COLUMNS if c not in header]
        if missing_cols:
            issues.append(f"Missing required columns in responses file: {missing_cols}")

        rows = list(reader)

    stats["total_rows"] = len(rows)
    prompt_ids = set()

    for i, r in enumerate(rows, start=2):
        pid = r.get("prompt_id", "").strip()
        source_type = r.get("source_type", "").strip()

        if not pid:
            issues.append(f"Row {i}: Missing prompt_id")
        elif pid in prompt_ids:
            issues.append(f"Row {i}: Duplicate response row for prompt_id '{pid}'")
        prompt_ids.add(pid)

        # Source type audit
        if source_type == "SYNTHETIC_NOT_OBSERVED":
            stats["synthetic_rows"] += 1
        elif source_type == "GENUINE_OBSERVED":
            stats["genuine_rows"] += 1
        elif not source_type:
            stats["unlabeled_source_rows"] += 1
        else:
            issues.append(f"Row {i}: Unknown source_type '{source_type}'. Must be 'GENUINE_OBSERVED' or 'SYNTHETIC_NOT_OBSERVED'")

        # Score checks
        scores_present = []
        for s_col in SCORE_FIELDS:
            val = r.get(s_col, "").strip()
            if val != "":
                try:
                    num_val = float(val)
                    if num_val < 0.0 or num_val > 4.0:
                        issues.append(f"Row {i} ({pid}): Score in '{s_col}' = {num_val} is outside allowed [0.0, 4.0]")
                    scores_present.append(num_val)
                except ValueError:
                    issues.append(f"Row {i} ({pid}): Non-numeric score '{val}' in '{s_col}'")

        if len(scores_present) == len(SCORE_FIELDS):
            stats["scored_rows"] += 1
        elif len(scores_present) == 0:
            stats["unscored_rows"] += 1
        else:
            issues.append(f"Row {i} ({pid}): Partially scored ({len(scores_present)}/{len(SCORE_FIELDS)} dimensions filled)")

    is_valid = len(issues) == 0
    return is_valid, issues, stats


def run_full_validation(project_root: str) -> bool:
    """Executes validation over all datasets in project."""
    print("=" * 70)
    print("DATASET VALIDATION RUNNER — CAPSTONE 16 RESPONSIBLE AI AUDIT")
    print("=" * 70)

    prompts_path = os.path.join(project_root, "data", "test_prompts.csv")
    template_path = os.path.join(project_root, "data", "chatbot_responses_template.csv")
    sample_path = os.path.join(project_root, "data", "chatbot_responses_sample.csv")

    all_passed = True

    # 1. Validate prompts
    print("\n1. Checking test_prompts.csv...")
    p_ok, p_issues, p_stats = validate_prompts_file(prompts_path)
    if p_ok:
        print(f"  [PASS] {p_stats['total_rows']} prompts, {p_stats['unique_pairs']} pairs verified.")
    else:
        all_passed = False
        print(f"  [FAIL] {len(p_issues)} issue(s) detected:")
        for iss in p_issues:
            print(f"    - {iss}")

    # 2. Check template
    print("\n2. Checking chatbot_responses_template.csv...")
    t_ok, t_issues, t_stats = validate_responses_file(template_path)
    if t_ok:
        print(f"  [PASS] Template structure intact ({t_stats['total_rows']} placeholder rows).")
    else:
        all_passed = False
        print(f"  [FAIL] {len(t_issues)} issue(s) detected:")
        for iss in t_issues:
            print(f"    - {iss}")

    # 3. Check sample if exists
    if os.path.exists(sample_path):
        print("\n3. Checking chatbot_responses_sample.csv...")
        s_ok, s_issues, s_stats = validate_responses_file(sample_path)
        if s_ok:
            print(f"  [PASS] Sample dataset verified ({s_stats['total_rows']} rows, {s_stats['synthetic_rows']} synthetic, {s_stats['scored_rows']} fully scored).")
        else:
            all_passed = False
            print(f"  [FAIL] {len(s_issues)} issue(s) detected:")
            for iss in s_issues:
                print(f"    - {iss}")
    else:
        print("\n3. chatbot_responses_sample.csv: (Not yet generated)")

    print("\n" + "=" * 70)
    if all_passed:
        print("OVERALL VALIDATION: [PASS] All datasets comply with audit schemas.")
    else:
        print("OVERALL VALIDATION: [FAIL] Dataset schema errors found.")
    print("=" * 70)

    return all_passed


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    success = run_full_validation(base_dir)
    sys.exit(0 if success else 1)
