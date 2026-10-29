# Final Demonstration and Deployment Guide

A beginner-friendly, step-by-step walkthrough for running, verifying, demonstrating, and extending **CAPSTONE 16 — Responsible AI and Bias Audit of a Chatbot** on Windows.

---

## 1. Prerequisites
- **Operating System:** Windows 10 or Windows 11.
- **Python:** Python 3.10, 3.11, or 3.12 (CPython x86_64).
- **PowerShell:** Standard Windows PowerShell (default in Windows).
- **Microsoft Excel / LibreOffice / Google Sheets:** For inspecting exported `.xlsx` and `.csv` files.
- **PowerPoint / Google Slides:** For viewing the 6-slide presentation (`.pptx`).

---

## 2. Step-by-Step Execution Walkthrough (Windows PowerShell)

Open PowerShell and navigate to the project directory:

### Step 1: Open the Project Folder
```powershell
cd G:\nofakezone\audit-ai\auditai\audit-ai\responsible-ai-bias-audit
```

### Step 2: Create a Virtual Environment
```powershell
python -m venv .venv
```
*(If `python` is not recognized, use `py -3.11 -m venv .venv` or reference your installed Python path).*

### Step 3: Activate the Virtual Environment in PowerShell
```powershell
.\.venv\Scripts\Activate.ps1
```
*(If PowerShell displays an execution policy error, run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process` once).*

### Step 4: Install Dependencies
```powershell
pip install -r requirements.txt
```
*(Packages installed: `pandas`, `matplotlib`, `openpyxl`, `python-pptx`, `pytest`).*

### Step 5: Generate the 30-Pair Benchmark Dataset
```powershell
python scripts\generate_test_dataset.py
```
*Creates `data/test_prompts.csv` (60 prompts) and `data/chatbot_responses_template.csv`.*

### Step 6: Validate Dataset Schemas & Bounds
```powershell
python scripts\validate_dataset.py
```
*Audits column schemas, checks that prompt counts equal exactly 2 per pair, and verifies score bounds.*

### Step 7: Score Responses & Calculate Differences
```powershell
python scripts\score_responses.py
```
*Calculates baseline/comparison means, computes dimension deltas, evaluates review flags, and exports `data/scored_results.csv` and `data/scored_results.xlsx`.*

### Step 8: Run Bias & Group Disparity Analysis
```powershell
python scripts\analyze_bias.py
```
*Aggregates descriptive statistics by category, outputs `data/group_summary.csv` and `outputs/summary/bias_audit_summary.json`.*

### Step 9: Generate High-Resolution Visual Charts
```powershell
$env:MPLCONFIGDIR = "$pwd\outputs\charts"
python scripts\generate_charts.py
```
*Builds 5 publication-quality PNG charts at 300 DPI in `outputs/charts/`:*
1. `01_score_by_dimension.png`
2. `02_score_by_category.png`
3. `03_baseline_vs_comparison_differences.png`
4. `04_flagged_cases_by_category.png`
5. `05_audit_data_completion.png`

### Step 10: Run Automated Unit Test Suite
```powershell
python scripts\run_tests.py
```
*Executes all 9 unit tests verifying schema validation, bound checks, difference calculations, and missing data safety.*

### Step 11: Inspect CSV and Excel Outputs
```powershell
# Open the Excel workbook directly in Microsoft Excel
Start-Process data\scored_results.xlsx

# Or view summary in PowerShell
Get-Content data\group_summary.csv | Select-Object -First 10
```

### Step 12: Preparing for a Live Chatbot Test (Field Testing)
To audit a real external chatbot (e.g. ChatGPT, Claude, Gemini, Copilot):
1. Open `data/chatbot_responses_template.csv` in Excel or Google Sheets.
2. Open a fresh private/incognito window for the target chatbot.
3. For each prompt in `data/test_prompts.csv`, paste the exact prompt text.
4. Copy the raw text response into the `raw_response` column of the template.
5. Set `source_type` to `GENUINE_OBSERVED`, record the chatbot name and date.
6. Score each response (0.0 to 4.0) across the 5 dimensions.
7. Save as `data/my_live_responses.csv`.
8. Run the scoring engine on your real data:
   ```powershell
   python scripts\score_responses.py --input data\my_live_responses.csv --output data\my_scored_results.csv
   ```

### Step 13: Updating the Final Audit Report
1. Open `reports/audit_report.md`.
2. Replace the synthetic demonstration findings in Section 5 with your genuine observed metrics.
3. Review flagged cases with your faculty mentor using `reports/bias_testing_checklist.md`.

### Step 14: Present the Six-Slide Presentation
```powershell
Start-Process presentation\responsible_ai_bias_audit.pptx
```
*Presents the clean, academic 6-slide deck with original embedded charts and detailed speaker notes.*

---

## 3. Troubleshooting Guide for Common Errors

| Issue / Error Message | Likely Root Cause | Solution |
| :--- | :--- | :--- |
| **`python : The term 'python' is not recognized`** | Python not added to system Windows `PATH`. | Re-run Python installer, check "Add Python to PATH", or invoke via full path (e.g., `& "$env:LOCALAPPDATA\Programs\Python\Python311\python.exe"`). |
| **`Execution of scripts is disabled on this system`** | PowerShell script restriction policy. | Run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process` in your PowerShell window. |
| **`No module named 'matplotlib'` or `'openpyxl'`** | Dependencies not installed in active virtual environment. | Verify activation prompt says `(.venv)`, then run `pip install -r requirements.txt`. |
| **`FileNotFoundError: [Errno 2] No such file`** | Executing script from wrong working directory. | Verify current directory using `pwd`. Ensure you are inside `responsible-ai-bias-audit`. |
| **`Score out of range [0, 4]`** | A rubric score was entered as $<0$ or $>4$ (e.g., entered 5 or 10). | Correct the score in your CSV to a float between 0.0 and 4.0. |
| **`Pair has 1 prompts (expected exactly 2)`** | An auditor accidentally deleted the baseline or comparison row. | Each pair must contain exactly one `baseline` and one `comparison` row. |
| **`Permission denied: scored_results.xlsx`** | The Excel file is open in Microsoft Excel while the script is running. | Close Excel and re-run `python scripts\score_responses.py`. |

---

## 4. Scientific Honesty & Provenance Notice
- The bundled sample data in `data/chatbot_responses_sample.csv` is explicitly marked `source_type = SYNTHETIC_NOT_OBSERVED`.
- Actual real-world response collection requires manual human submission and independent review to satisfy academic research ethics.
