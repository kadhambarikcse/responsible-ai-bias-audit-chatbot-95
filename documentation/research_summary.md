# Research Summary: Responsible AI, Fairness Metrics, and Black-Box Auditing

This research summary synthesizes the theoretical, empirical, and regulatory foundations of **CAPSTONE 16 — Responsible AI and Bias Audit of a Chatbot**.

---

## 1. What is AI Bias and Algorithmic Fairness?

### 1.1 Definition of AI Bias
In artificial intelligence and statistical learning, **bias** refers to systematic, repeatable errors in model predictions, recommendations, or generations that lead to unfair advantages or disadvantages for specific demographic groups, geographic regions, or individuals. 

Unlike random stochastic variance (statistical noise), bias operates systematically. It is rooted in:
1. **Historical Bias:** Pre-existing cultural inequalities, wage disparities, and prejudices recorded in pretraining datasets.
2. **Representation & Sampling Bias:** Systematic under-representation of non-Western languages, low-income communities, and minority identities in web crawls.
3. **Measurement & Labeling Bias:** Using proxy indicators that fail to capture true attributes (e.g., using ZIP codes to proxy creditworthiness, leading to algorithmic redlining).
4. **Aggregation Bias:** Applying a one-size-fits-all model across diverse sub-populations with distinct distributions.
5. **Alignment / RLHF Bias:** Reinforcement Learning from Human Feedback (RLHF) reflecting the subjective cultural norms and political assumptions of annotator pools.

### 1.2 Defining Algorithmic Fairness
Fairness in AI is not a singular mathematical formula, but a multidimensional ethical and mathematical construct. Key formal definitions include:
- **Demographic Parity (Statistical Parity):** Requires that the likelihood of receiving a positive recommendation or high score is identical across protected demographic groups ($P(\hat{Y}=1 | A=a) = P(\hat{Y}=1 | A=b)$). While intuitive, demographic parity is not always applicable when underlying distributions or legitimate contexts differ.
- **Equal Opportunity:** Requires that individuals who are equally qualified have an equal probability of receiving a positive prediction ($P(\hat{Y}=1 | A=a, Y=1) = P(\hat{Y}=1 | A=b, Y=1)$).
- **Counterfactual Fairness:** Asserts that an algorithm’s decision is fair towards an individual if the decision would have been identical had the individual belonged to another demographic group in a hypothetical counterfactual world where all non-demographic qualifications remained constant. This provides the primary foundation for our paired-prompt testing.

---

## 2. Core Responsible AI Principles

Responsible AI rests upon seven interlocking pillars:
1. **Fairness & Equity:** Ensuring parity of quality, effort, and tone regardless of identity attributes.
2. **Factual Reliability & Truthfulness:** Eliminating hallucinations, fabricated citations, and confident falsehoods.
3. **Safety & Non-Harm:** Enforcing strict boundaries against dangerous medical dosing, malware creation, and illegal activities.
4. **Respect & Inclusiveness:** Upholding user dignity, avoiding cultural stereotypes, and recognizing global dialects.
5. **Transparency & Explainability:** Acknowledging operational boundaries, training date cutoffs, and knowledge uncertainty.
6. **Privacy & Data Protection:** Never extracting, leaking, or storing personally identifiable information (PII).
7. **Accountability & Human Governance:** Maintaining human oversight, review checklists, and audit trails.

---

## 3. Black-Box Auditing: Challenges and Strengths

When auditing free commercial conversational agents (e.g., free tiers of ChatGPT, Gemini, Copilot, Claude), researchers face a **black-box environment**:
- Model weights, internal activation vectors, and attention heads are inaccessible.
- Underlying system prompts and safety moderation filters change dynamically without version notes.
- Generative decoding uses non-zero temperatures, causing stochastic response variation across identical prompts.

### Methodological Solution: Controlled Paired Benchmarks
Despite these challenges, black-box auditing via **counterfactual paired prompts** offers remarkable diagnostic power:
- By querying the model with two prompts that differ in exactly one controlled attribute (e.g., swapping a male name for a female name, or a London university for an Argentine university) while keeping all credentials identical, any observed difference in recommendations or tone isolates the model's sensitivity to that attribute.
- Multiple evaluations across balanced categories (A to F) establish empirical evidence of systemic disparities without violating terms of service or reverse-engineering proprietary weights.

---

## 4. Translating Research into Practice

This Capstone operationalizes these insights into an actionable three-stage pipeline:
1. **Design & Validation:** Creating 30 unique, balanced prompt pairs across 6 categories with zero offensive prompts.
2. **Standardized Rubric Scoring:** Measuring responses on a 0–4 scale across 5 dimensions (Fairness, Facts, Safety, Respect, Transparency).
3. **Automated Flagging & Qualitative Review:** Using Python to automatically flag pairs exhibiting score differences $\ge 1.0$ or safety/fact scores $\le 2.0$ for detailed contextual review, while strictly avoiding premature claims of "proven discrimination" from single-run score deltas.
