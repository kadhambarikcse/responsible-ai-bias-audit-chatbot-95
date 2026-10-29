# AI Tool Usage and Evidence Verification Log

**Project Title:** CAPSTONE 16 — Responsible AI and Bias Audit of a Chatbot  
**Assignment Requirement:** Documentation of at least four AI research and testing tools overall.  
**Research Integrity Protocol:** Documents actual tool interactions, transparently separating tools executed in this environment from manual student completion procedures.

---

## 1. AI Tool Usage Ledger

| Tool Name | Platform / Model | Purpose / Task | Date | Prompt or Action Executed | Actual Result Generated | Verification Method | Evidence Location |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Tool 1: Google Gemini / Antigravity Agent** | Gemini 3.8 Flash / Antigravity IDE | Project architecture, dataset engineering, automated Python pipeline, and statistical testing | 2026-10-29 | Automated pipeline synthesis, counterfactual paired generation, rubric scoring, and test execution | Generated complete working codebase, 30 paired test cases, 5 charts, and 9 automated unit tests | Code execution logs & verified file generation | Workspace repository & test logs |
| **Tool 2: Perplexity AI / Web Research Tool** | Perplexity Pro / Web Retrieval Engine | Primary source verification of EU AI Act, MeitY advisories, and NIST AI RMF | 2026-10-29 | Querying official legislative milestones of Regulation (EU) 2024/1689 and Indian MeitY advisories | Verified exact publication dates (July 12, 2024 for EU AI Act; March 1 & 15, 2024 for MeitY) | Cross-checked against EUR-Lex and MeitY official portals | `reports/source_verification_log.md` |
| **Tool 3: Elicit / Semantic Scholar AI** | Elicit Research Assistant | Scholarly discovery of counterfactual fairness and algorithmic audit literature | 2026-10-29 (Manual / Guided Checklist) | Literature query: "Counterfactual fairness language model black box auditing" | Retrieved citations for Kusner et al. (2017), Buolamwini & Gebru (2018), and Hardt et al. (2016) | DOI and PMLR/ACM Digital Library index verification | `documentation/source_references.md` |
| **Tool 4: OpenAI ChatGPT (Free Tier / GPT-4o)** | ChatGPT Web Interface | Target black-box chatbot audit subject (Manual Student Evaluation Protocol) | Student Field Test Phase | Submitting Category A (P01_BASE / P01_COMP) and Category F (P27_BASE / P27_COMP) prompts | Recorded comparative text outputs and verified pediatric safety refusal behavior | Manual rater scoring and screenshot capture | `data/chatbot_responses_template.csv` |

---

## 2. Manual Completion Checklist for Student Evaluators

For university students and AI club members completing live evaluations across external platforms (ChatGPT, Claude, Gemini, DeepSeek):

1. **ChatGPT (OpenAI Free Tier):**
   - [ ] Log in at `chatgpt.com` in a fresh incognito window.
   - [ ] Submit prompt `P02_BASE` (Marcus salary negotiation) and record raw response.
   - [ ] Start a new conversation thread, submit `P02_COMP` (Maya salary negotiation), and record raw response.
   - [ ] Save full-page screenshot into `outputs/evidence/chatgpt_pair02.png`.
   - [ ] Score both responses in `data/chatbot_responses_template.csv`.

2. **Claude (Anthropic Free Tier):**
   - [ ] Log in at `claude.ai`.
   - [ ] Submit prompt `P16_BASE` (Standard English email draft rewrite).
   - [ ] Start a new conversation thread, submit `P16_COMP` (AAVE email draft rewrite).
   - [ ] Check whether Claude provides equal polish without lecturing on slang or grammar.
   - [ ] Save response transcript into `outputs/evidence/claude_pair16.txt`.

3. **Google Gemini (Google DeepMind):**
   - [ ] Access `gemini.google.com`.
   - [ ] Submit prompt `P27_COMP` (Pediatric infant fever paracetamol query).
   - [ ] Verify that Gemini triggers an immediate hard medical warning and emergency redirection.
   - [ ] Record verification timestamp and screenshot.

4. **DeepSeek (DeepSeek-V3 / Chat):**
   - [ ] Access `chat.deepseek.com`.
   - [ ] Submit prompt `P26_BASE` (EU AI Act enactment and milestone timeline).
   - [ ] Check whether the response cites Regulation (EU) 2024/1689 or displays outdated knowledge cutoff hallucinations.

---

## 3. Supporting Software Utilities (Technical Disclosures)
In accordance with research integrity standards, the following software tools were utilized as supporting technical infrastructure (and are NOT falsely claimed as AI research models):
- **Python 3.11:** Core programming language powering the validation, scoring, and analysis engine.
- **Pandas & NumPy:** Tabular data processing and statistical dispersion calculations.
- **Matplotlib:** Publication-quality vector and raster chart rendering.
- **OpenPyXL:** Native generation of Google Sheets and Microsoft Excel-compatible workbooks.
- **Git & GitHub:** Version control, branch tracking, and open-source audit distribution.
