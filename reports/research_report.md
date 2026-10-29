# Research Report: Structured Black-Box Counterfactual Auditing of Conversational Agents for Bias, Safety, and Factual Reliability

**Project Title:** CAPSTONE 16 — Responsible AI and Bias Audit of a Chatbot  
**Target Audience:** Computer Science and Engineering (CSE) Students, Faculty Mentors, and Student AI Ethics Groups  
**Author:** AI Ethics and Responsible AI Audit Research Team  
**Date:** October 2026  

---

## 1. Abstract
Free conversational artificial intelligence agents have achieved ubiquity across higher education and technical workplaces, serving as daily assistants for writing, career planning, and problem-solving. However, these systems operate as opaque black boxes whose training data and alignment techniques encode historical inequalities, subtle demographic stereotypes, and factual hallucinations. This capstone project introduces a structured, accessible, and ethical audit methodology answering the central research question: *“How can we test free chatbots for bias and unfair outputs in a structured, ethical way?”* By designing a benchmark of 30 counterfactual prompt pairs (60 total prompts) spanning six evaluation categories, establishing a 5-dimensional scoring rubric (0–4 scale), and building an automated, open-source Python processing pipeline, this project demonstrates how undergraduate researchers can conduct reproducible AI audits without expensive APIs or access to proprietary weights. We emphasize scientific integrity by clearly demarcating synthetic demonstration data from genuine real-world observations and distinguishing statistical score disparities from proven legal discrimination.

---

## 2. Introduction
The transition of large language models (LLMs) from academic research to consumer-facing free chatbots—such as OpenAI ChatGPT, Google Gemini, Microsoft Copilot, and Anthropic Claude—has democratized access to natural language interfaces. Millions of undergraduate students, job seekers, and developers interact with these platforms daily. Yet commercial deployments present a fundamental accountability dilemma: users interact with black-box systems whose model architectures, system prompts, moderation filters, and training corpora are proprietary and subject to continuous, unannounced server-side modifications.

When conversational agents exhibit disparate behavior across demographic groups, linguistic dialects, or socioeconomic contexts, the harms are rarely overt slurs. Instead, they manifest as allocative and representational micro-disparities: recommending less aggressive compensation strategies to female engineers, framing Global South startups as humanitarian charities rather than commercial ventures, or subjecting working-class postal codes to financial redlining. Developing structured, low-cost auditing protocols for engineering students is therefore a critical pedagogical and societal imperative.

---

## 3. Problem Statement
Current methods for evaluating fairness in generative models largely rely on access to internal model weights, log-probabilities, or massive programmatic API scraping budgets that exceed the resources of undergraduate computer science students and independent researchers. Conversely, informal testing by casual users is typically ad-hoc, uncontrolled, and prone to confirmation bias, often relying on deliberately inflammatory prompts that fail to reflect authentic user scenarios. There is a lack of structured, reproducible, and ethically sound testing frameworks that allow students to evaluate free chatbots using transparent scientific controls, standardized scoring rubrics, and automated statistical analysis.

---

## 4. Research Objectives
This project pursues five core objectives:
1. Formulate a controlled counterfactual paired-prompt audit framework that isolates demographic, geographic, and socioeconomic attributes.
2. Develop a benchmark of 30 balanced prompt pairs (60 prompts) across six key categories with zero shock-value or offensive prompts.
3. Establish a transparent, 5-dimensional evaluation rubric measuring Fairness, Factual Reliability, Safety, Respect, and Transparency on an anchored 0–4 scale.
4. Build a lightweight, cross-platform Python pipeline automating data validation, score computation, paired difference calculation, statistical aggregation, and chart generation.
5. Provide comprehensive ethical guidelines that prevent premature discrimination claims by systematically examining plausible non-discriminatory alternative explanations.

---

## 5. Background on AI Bias and Algorithmic Fairness
In statistical learning theory, bias represents systematic error that skews outputs away from true parameters. In conversational language models, algorithmic bias arises from multiple interconnected stages of the machine learning lifecycle:
- **Historical Bias:** Embedded cultural inequities preserved in historical text corpora.
- **Sampling & Representation Bias:** Web-scale scrapes that disproportionately amplify high-resource languages and dominant socio-cultural demographics.
- **Measurement Bias:** Employing flawed proxies (such as postal codes for financial solvency).
- **Alignment Bias:** Subjective values introduced during Reinforcement Learning from Human Feedback (RLHF).

Fairness definitions in machine learning frequently conflict. While *Demographic Parity* demands equal positive outcomes across groups ($P(\hat{Y}=1|A=a) = P(\hat{Y}=1|A=b)$), it can overlook legitimate context-specific distinctions. In contrast, *Counterfactual Fairness* (Kusner et al., 2017) provides an ideal diagnostic foundation for conversational auditing: an agent's response to an individual is counterfactually fair if it remains identical in a counterfactual world where only a protected characteristic was modified while all qualifications and context were held constant.

---

## 6. Literature and Regulatory Framework Review
Our audit methodology is grounded in three regulatory and scientific pillars:
1. **NIST AI Risk Management Framework (AI RMF 1.0, NIST SP 1270):** Specifically operationalizes the *Govern 1.2*, *Map 1.5*, and *Measure 2.5* functions, establishing structured workflows to identify, measure, and manage socio-technical harms.
2. **European Union Artificial Intelligence Act (Regulation (EU) 2024/1689):** Serves as an international statutory benchmark, particularly Article 10 (data governance and bias mitigation) and Articles 50/52 (mandatory AI transparency and disclosure).
3. **Government of India MeitY Advisories (March 2024):** Highlights digital intermediary due diligence under IT Rule 3(1)(b), emphasizing the prevention of bias, mandatory watermarking of synthetic media, and labeling untested or fallible AI systems.
4. **Foundational Academic Research:** Integrates empirical insights from Buolamwini & Gebru (*Gender Shades*, 2018) regarding intersectional error disparities, and Bender et al. (*Stochastic Parrots*, 2021) regarding ungrounded mimicry and pretraining bias risks.

---

## 7. Research Methodology: Counterfactual Paired Testing Design
The benchmark comprises **30 unique pairs (60 individual prompts)** divided into six balanced categories:
- **Category A (Names & Perceived Gender):** Executive biographies, salary negotiation tactics, parental leave re-entry, graduate recommendation letters, and assertive leadership coaching.
- **Category B (Regional & Cultural Variation):** B2B tech pitches across Global North and South, university climate grants, religious holiday policies, foreign resume degrees, and traditional dietary appraisals.
- **Category C (Educational & Career Opportunities):** PhD applications (state university vs. Ivy League), self-taught vs. CS degree holders, communication styles, first-generation internship navigation, and career pivots at age 24 vs. 52.
- **Category D (Language, Communication & Accessibility):** Business email rewrites (AAVE vs. Standard English), neuro-inclusive algorithm explanations, World English idioms, physical vs. mental health accommodations, and WCAG 2.1 AA developer checklists.
- **Category E (Recommendations & Service Quality):** Wealth building across ZIP codes at identical income ($50k), healthcare navigation for insured vs. uninsured individuals, public housing vs. luxury tenant rights, and enterprise vs. free service complaint letters.
- **Category F (Factual Reliability, Safety & Outdated Information):** Legislative status of the EU AI Act, pediatric paracetamol dosing safety refusals vs. adult OTC advice, academic citation verification, dual-use cybersecurity vulnerability reporting, and Indian MeitY regulatory updates.

Each pair modifies exactly one isolated attribute, holding technical credentials, background facts, and prompt complexity strictly constant.

---

## 8. Five-Dimensional Scoring Rubric
Responses are reviewed on an anchored 0–4 scale:
1. **Fairness and Consistency (0–4):** Measures parity of tone, effort, quality, and recommendations between counterpart prompts.
2. **Factual Reliability (0–4):** Evaluates truthfulness, absence of hallucinations, and verified accuracy against primary legal and academic sources.
3. **Safety (0–4):** Evaluates enforcement of safety boundaries against physical, medical, or cybersecurity hazards.
4. **Respect and Inclusiveness (0–4):** Assesses dignity, absence of cultural stereotypes, and inclusive phrasing.
5. **Transparency and Uncertainty (0–4):** Evaluates whether the chatbot appropriately qualifies assumptions, admits knowledge boundaries, and notes date limitations.

For each pair, the pipeline computes dimension deltas ($\Delta = \text{Score}_{\text{base}} - \text{Score}_{\text{comp}}$), overall mean scores, and absolute disparity ($|\Delta_{\text{overall}}|$). A pair is automatically flagged for human review if $|\Delta_{\text{overall}}| \ge 1.0$, if any dimension delta $\ge 1.0$, or if safety/factual scores fall $\le 2.0$.

---

## 9. Ethical Safeguards and Auditor Integrity
Auditors must adhere to strict ethical constraints:
- **Zero Shock-Value Prompts:** Prompts avoid hate speech, slurs, or deliberate toxicity; subtle real-world scenarios reveal authentic model tendencies.
- **Provenance Transparency:** Synthetic demonstration data is strictly marked `source_type = SYNTHETIC_NOT_OBSERVED` to avoid presenting simulated examples as real-world findings.
- **Scientific Humility:** Score differences indicate candidates for qualitative review, not definitive legal proof of discrimination. Legitimate contextual differentiation (e.g., safety refusals or contractual service tiers) must be distinguished from unfair bias.

---

## 10. Expected Usefulness and Limitations
This framework provides an immediate, open-source educational laboratory for university AI clubs, capstone projects, and ethics courses. However, several methodological limitations persist:
- **Black-Box Stochasticity:** Temperature-based decoding introduces run-to-run variance; findings represent a point-in-time assessment.
- **Sample Size:** While qualitatively rich, 30 pairs cannot encompass all global subcultures or intersectional edge cases.
- **Opaque Server Drift:** Commercial providers continuously patch models, complicating longitudinal comparisons.

---

## 11. Conclusion
Capstone 16 establishes that rigorous responsible AI auditing does not require massive compute infrastructure or proprietary access. By combining counterfactual paired prompts, multi-dimensional anchored rubrics, and automated Python validation, undergraduate students and researchers can systematically evaluate conversational agents for fairness, factual integrity, and safety. This structured methodology bridges the gap between abstract ethical principles and hands-on software engineering, cultivating the next generation of responsible AI practitioners.

---

## 12. References
1. Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the Dangers of Stochastic Parrots: Can Language Models Be Too Big? 🦜 *Proceedings of the 2021 ACM FAccT Conference*, 610–623.
2. Bommasani, R., et al. (2021). On the Opportunities and Risks of Foundation Models. *arXiv preprint arXiv:2108.07258*.
3. Buolamwini, J., & Gebru, T. (2018). Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification. *Proceedings of Machine Learning Research (PMLR)*, 81, 77–91.
4. European Union. (2024). Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act). *Official Journal of the European Union*, L 2024/1689.
5. Hardt, M., Price, E., & Srebro, N. (2016). Equality of Opportunity in Supervised Learning. *Advances in Neural Information Processing Systems (NeurIPS 2016)*, 29, 3315–3323.
6. Kusner, M. J., Loftus, J. R., Russell, C., & Silva, R. (2017). Counterfactual Fairness. *Advances in Neural Information Processing Systems (NeurIPS 2017)*, 30, 4066–4076.
7. Ministry of Electronics and Information Technology (MeitY), Government of India. (2024). Advisory on Due Diligence by Intermediaries regarding Artificial Intelligence Models (Revised March 15, 2024).
8. National Institute of Standards and Technology (NIST). (2023). *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*. NIST Special Publication 1270.
9. Schwartz, R., et al. (2022). *Towards a Standard for Identifying and Managing Bias in Artificial Intelligence*. NIST Special Publication 1270.
10. World Wide Web Consortium (W3C). (2018). *Web Content Accessibility Guidelines (WCAG) 2.1*. W3C Recommendation.
