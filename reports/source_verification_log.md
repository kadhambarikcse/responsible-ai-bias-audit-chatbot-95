# Source Verification Log

This document records the verification methodology, provenance check, retrieval dates, and evidentiary audit status for every primary reference utilized in **CAPSTONE 16 — Responsible AI and Bias Audit of a Chatbot**.

---

## 1. Source Verification Ledger

| Reference ID | Source Title | Organization / Authors | Publication Date | Verification Method | URL / DOI Status | Audit Status | Key Verifiable Claim |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **REF-01** | *Artificial Intelligence Act (Regulation 2024/1689)* | European Parliament & Council of the EU | 2024-07-12 | Official Journal EUR-Lex Archive Check | Verified Active (`eur-lex.europa.eu`) | **VERIFIED** | Enacted July 2024; entered into force Aug 1, 2024; bans on prohibited AI take effect Feb 2, 2025. |
| **REF-02** | *Advisory on GenAI Intermediary Due Diligence* | MeitY, Government of India | 2024-03-15 (Rev) | MeitY Official Portal & Press Releases | Verified Active (`meity.gov.in`) | **VERIFIED** | Revised March 15 advisory mandates synthetic watermarking, unreliability disclaimers, and bias prevention. |
| **REF-03** | *AI Risk Management Framework (AI RMF 1.0)* | NIST, U.S. Dept of Commerce | 2023-01-26 | NIST ITL Publications Portal | Verified Active (`nist.gov/itl`) | **VERIFIED** | Defines four core functions: GOVERN, MAP, MEASURE, MANAGE; Measure 2.5 mandates bias audits. |
| **REF-04** | *Special Publication 1270: Identifying and Managing Bias in AI* | NIST (Schwartz et al.) | 2022-03-15 | NIST SP Repository (DOI: 10.6028/NIST.SP.1270) | Verified Active (`doi.org/10.6028/NIST.SP.1270`) | **VERIFIED** | Classifies bias into computational, systemic, and human evaluation categories. |
| **REF-05** | *Gender Shades: Intersectional Accuracy Disparities* | Joy Buolamwini & Timnit Gebru | 2018-02-23 | PMLR Vol 81 Archive | Verified Active (`proceedings.mlr.press`) | **VERIFIED** | Error rate on darker-skinned females was 34.7% vs <1% for lighter males. |
| **REF-06** | *On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?* | Emily Bender, Timnit Gebru, et al. | 2021-03-03 | ACM Digital Library (FAccT '21) | Verified Active (`doi.org/10.1145/3442188.3445922`) | **VERIFIED** | Foundational paper on statistical language mimicry without intent and pretraining bias risks. |
| **REF-07** | *Counterfactual Fairness* | Matt Kusner, Joshua Loftus, et al. | 2017-12-04 | NeurIPS 2017 Proceedings (arXiv:1703.06856) | Verified Active (`arxiv.org/abs/1703.06856`) | **VERIFIED** | Defines fairness as invariance under counterfactual interventions on protected attributes. |
| **REF-08** | *Equality of Opportunity in Supervised Learning* | Moritz Hardt, Eric Price, Nathan Srebro | 2016-10-07 | NeurIPS 2016 Proceedings (arXiv:1610.02413) | Verified Active (`arxiv.org/abs/1610.02413`) | **VERIFIED** | Formulates equalized odds and demonstrates mathematical tradeoffs with demographic parity. |
| **REF-09** | *Opportunities and Risks of Foundation Models* | Rishi Bommasani et al. (Stanford CRFM) | 2021-08-16 | arXiv Repository (arXiv:2108.07258) | Verified Active (`arxiv.org/abs/2108.07258`) | **VERIFIED** | Landmark survey identifying black-box homogenization risks in large foundation models. |
| **REF-10** | *WCAG 2.1 Web Content Accessibility Guidelines* | World Wide Web Consortium (W3C) | 2018-06-05 | W3C Recommendation Portal | Verified Active (`w3.org/TR/WCAG21`) | **VERIFIED** | Level AA success criteria (1.1.1, 1.3.1, 2.1.1, 2.4.7) for screen readers and keyboard navigation. |

---

## 2. Research Integrity Audit Protocol

To maintain complete scientific and academic honesty:
1. **Zero Citation Fabrication:** Every listed paper, regulation, and government advisory has been verified against recognized public indices (EUR-Lex, MeitY, NIST, PMLR, ACM DL, arXiv, W3C).
2. **Explicit Separation of Facts vs. Interpretations:**
   - *Verified Fact:* The EU AI Act was published in the Official Journal on July 12, 2024 as Regulation (EU) 2024/1689.
   - *Research Interpretation:* The Act's strict documentation mandates under Article 10 imply that student auditors can evaluate black-box commercial chatbots against emerging compliance baselines.
   - *Recommendation:* Academic institutions should establish structured counterfactual testing labs for AI club members.
3. **No Unobserved Data Confabulation:** All response data in `data/chatbot_responses_sample.csv` is explicitly labeled `source_type = SYNTHETIC_NOT_OBSERVED` to demonstrate pipeline functionality without falsely claiming real-world chatbot observations occurred during automatic script generation.
