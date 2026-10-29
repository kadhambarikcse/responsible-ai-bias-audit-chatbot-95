# Verification and Pipeline Execution Report

**Project Title:** CAPSTONE 16 — Responsible AI and Bias Audit of a Chatbot  
**Execution Timestamp:** 2026-10-29 22:35 UTC+05:30  
**Environment:** Windows 10/11 Architecture (x86_64)  
**Python Runtime:** CPython 3.11.15 via Dedicated Virtual Environment (`.venv`)  

---

## 1. Execution Environment Details

| Component | Verified Specification |
| :--- | :--- |
| **Operating System** | Windows (PowerShell Shell Environment) |
| **Python Version** | Python 3.11.15 (64-bit) |
| **Virtual Environment Location** | `g:\nofakezone\audit-ai\auditai\audit-ai\.venv` |
| **Key Installed Packages** | `pandas==3.1.0`, `matplotlib==3.11.2`, `openpyxl==3.1.5`, `python-pptx==1.0.2`, `numpy==2.4.6` |
| **Matplotlib Config Dir** | `$env:MPLCONFIGDIR = "responsible-ai-bias-audit\outputs\charts"` |

---

## 2. Commands Actually Executed

The following shell commands were executed and verified during the development and testing cycle:

```powershell
# 1. Dataset Generation and Internal Consistency Check
& ".venv\Scripts\python.exe" responsible-ai-bias-audit\scripts\generate_test_dataset.py
# Return code: 0 | Output: 60 prompts generated across 30 pairs; all category checks passed.

# 2. Dataset Schema and Bounds Validation
& ".venv\Scripts\python.exe" responsible-ai-bias-audit\scripts\validate_dataset.py
# Return code: 0 | Output: test_prompts.csv (PASS), template.csv (PASS), sample.csv (PASS).

# 3. Illustrative Sample Response Generation
& ".venv\Scripts\python.exe" responsible-ai-bias-audit\scripts\generate_sample_responses.py
# Return code: 0 | Output: 60 sample synthetic response records created.

# 4. Response Scoring and Difference Calculation
& ".venv\Scripts\python.exe" responsible-ai-bias-audit\scripts\score_responses.py
# Return code: 0 | Output: scored_results.csv and scored_results.xlsx successfully exported.

# 5. Bias and Group Disparity Statistical Analysis
& ".venv\Scripts\python.exe" responsible-ai-bias-audit\scripts\analyze_bias.py
# Return code: 0 | Output: group_summary.csv and bias_audit_summary.json generated.

# 6. High-Resolution Chart Generation
$env:MPLCONFIGDIR = "G:\nofakezone\audit-ai\auditai\audit-ai\responsible-ai-bias-audit\outputs\charts"
& ".venv\Scripts\python.exe" responsible-ai-bias-audit\scripts\generate_charts.py
# Return code: 0 | Output: 5 charts (300 DPI PNGs) saved in outputs/charts/.

# 7. Six-Slide Academic Presentation Generation
& ".venv\Scripts\python.exe" responsible-ai-bias-audit\scripts\create_presentation.py
# Return code: 0 | Output: responsible_ai_bias_audit.pptx generated (exactly 6 slides).

# 8. Automated Unit Test Execution
& ".venv\Scripts\python.exe" responsible-ai-bias-audit\scripts\run_tests.py
# Return code: 0 | Output: 9/9 unit tests PASSED (100% success rate).
```

---

## 3. Dataset Validation Results

The dataset validation suite executed by `scripts/validate_dataset.py` returned:
- **`data/test_prompts.csv`:**
  - Total prompt rows: 60 (Expected: 60) — **PASS**
  - Unique prompt pairs: 30 (Expected: 30) — **PASS**
  - Category distribution: Exactly 5 pairs per category (A to F) — **PASS**
  - Duplicate IDs: 0 — **PASS**
  - Missing text fields: 0 — **PASS**
- **`data/chatbot_responses_sample.csv`:**
  - Total records: 60 — **PASS**
  - Source type audit: 60 records labeled `SYNTHETIC_NOT_OBSERVED` — **PASS**
  - Rubric score range audit: 100% of scores within $[0.0, 4.0]$ — **PASS**
  - Fully scored records: 60 / 60 — **PASS**

---

## 4. Automated Unit Test Results

The automated test suite in `scripts/run_tests.py` (covering `tests/test_dataset.py` and `tests/test_scoring.py`) executed 9 comprehensive unit tests:

| Test Case Name | Objective Tested | Execution Result |
| :--- | :--- | :---: |
| `test_prompts_file_valid_baseline` | Validates official `test_prompts.csv` schema and 30-pair structure | **PASS** |
| `test_missing_required_columns_rejected` | Verifies rejection when mandatory schema columns are omitted | **PASS** |
| `test_duplicate_prompt_ids_rejected` | Checks that duplicate prompt identifiers trigger validation errors | **PASS** |
| `test_incorrect_prompt_count_per_pair` | Verifies rejection of asymmetrical pairs (1 or >2 prompts) | **PASS** |
| `test_empty_input_file_handled` | Confirms empty or missing CSV files are handled gracefully | **PASS** |
| `test_rubric_bounds_and_parsing` | Validates score bounds $[0, 4]$ and non-numeric error handling | **PASS** |
| `test_paired_difference_calculation` | Validates baseline minus comparison deltas and review flags | **PASS** |
| `test_missing_scores_handled_safely` | Proves missing scores do not crash or silently default to zero | **PASS** |
| `test_sample_responses_dataset_valid` | Validates schema and labeling of sample demonstration responses | **PASS** |

**Summary: 9 passed, 0 failed, 0 warnings.**

---

## 5. Artifact and Output Files Generated

| Output Path | File Type | Description & Verification |
| :--- | :--- | :--- |
| `data/test_prompts.csv` | CSV | 60 prompts across 30 pairs with full controlled attribute metadata. |
| `data/chatbot_responses_template.csv` | CSV | Blank data collection template for student field testing. |
| `data/chatbot_responses_sample.csv` | CSV | 60 synthetic demonstration responses with full rubric scoring. |
| `data/scored_results.csv` | CSV | Pair-level difference matrix with deltas and review flags. |
| `data/scored_results.xlsx` | Excel (XLSX) | Excel-compatible workbook formatted with openpyxl. |
| `data/group_summary.csv` | CSV | Category-level statistical summary table. |
| `outputs/summary/bias_audit_summary.json` | JSON | Machine-readable audit summary for programmatic ingestion. |
| `outputs/charts/01_score_by_dimension.png` | PNG (300 DPI) | Dimension scores: Baseline vs Comparison. |
| `outputs/charts/02_score_by_category.png` | PNG (300 DPI) | Performance parity across Categories A to F. |
| `outputs/charts/03_baseline_vs_comparison_differences.png` | PNG (300 DPI) | Absolute delta distribution per pair with 1.0 threshold. |
| `outputs/charts/04_flagged_cases_by_category.png` | PNG (300 DPI) | Number and percentage of flagged pairs per category. |
| `outputs/charts/05_audit_data_completion.png` | PNG (300 DPI) | Test completion and data source composition report. |
| `presentation/responsible_ai_bias_audit.pptx` | PPTX | Exactly 6 slides with embedded charts and speaker notes. |

---

## 6. Known Bugs and Unresolved Issues
- **None detected.** All scripts execute deterministically with exit code 0.
- Missing score handling was defensively implemented so that empty cells remain `None` rather than coercing to `0.0`.

---

## 7. Manual Checks Still Required Prior to Capstone Submission
1. **Live Chatbot Response Collection (Optional Field Testing):**
   - If students choose to audit a live commercial chatbot (e.g. ChatGPT, Gemini, Copilot), they must manually copy prompts from `data/test_prompts.csv`, paste them into fresh incognito sessions, record the raw text into `data/chatbot_responses_template.csv`, mark `source_type = GENUINE_OBSERVED`, and re-run `python scripts/score_responses.py`.
2. **Qualitative Peer Review Meeting:**
   - Review the 7 flagged pairs with faculty mentors using `reports/bias_testing_checklist.md` to confirm consensus scoring.
