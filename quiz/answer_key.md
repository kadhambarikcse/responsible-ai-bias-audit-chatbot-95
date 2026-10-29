# Responsible AI and Bias Audit Quiz — Answer Key & Explanations

This answer key provides official solutions, scoring guidance, and pedagogical rationales for **CAPSTONE 16 — Responsible AI and Bias Audit of a Chatbot**.

---

### Question 1: Counterfactual Fairness
- **Correct Answer:** **[B] To isolate causality and determine whether the modified attribute alone triggers systematic differences in tone, recommendations, or effort.**
- **Explanation:** In experimental design, keeping all semantic context, metrics, and qualifications strictly invariant ensures that any observed differential behavior is attributable to the single manipulated attribute (e.g., gender, geographic region, dialect). This prevents confounding factors from distorting the evaluation.

---

### Question 2: Disparity vs. Discrimination
- **Correct Answer:** **False**
- **Explanation:** A numerical score difference (disparity) flags a candidate case for human contextual review, but does not inherently prove unlawful discrimination. Legitimate contextual differences—such as strict pediatric safety refusals or differing statutory legal hearing rights—require differential responses to be legally and medically responsible.

---

### Question 3: EU AI Act Prohibited Practices
- **Correct Answer:** **[C] Deploying AI systems that evaluate or classify natural persons based on social behavior or personality traits resulting in social scoring.**
- **Explanation:** Under Article 5(1)(c) of Regulation (EU) 2024/1689, AI systems that evaluate or classify individuals based on social behavior over time or known personality characteristics leading to detrimental or disproportionate treatment (social scoring) are classified as Unacceptable Risk and strictly prohibited.

---

### Question 4: NIST AI RMF Core Functions
- **Correct Answer:** **[D] GOVERN**
- **Explanation:** The **GOVERN** function in the NIST AI Risk Management Framework (SP 1270) cultivates an organizational culture of risk management, defining policies, transparent accountability roles, and risk tolerances for bias, fairness, and safety across the AI lifecycle.

---

### Question 5: Lexical Asymmetry (Agentic vs. Communal Descriptors)
- **Model Answer:**
  - **Agentic Descriptors:** Words emphasizing competence, technical mastery, strategic authority, and analytical rigor (e.g., *"visionary"*, *"decisive"*, *"intellectually rigorous"*, *"leader"*).
  - **Communal Descriptors:** Words emphasizing interpersonal warmth, supportiveness, agreeableness, and helpfulness (e.g., *"warm"*, *"pleasant"*, *"delightful"*, *"supportive"*).
  - **Harmful Impact:** When language models disproportionately ascribe agentic traits to male profiles and communal traits to female profiles with identical technical achievements, they reinforce the stereotype that women are supportive caretakers rather than executive technical leaders, impairing hiring and promotion evaluations.

---

### Question 6: Medical Safety Guardrails
- **Correct Answer:** **False**
- **Explanation:** Under no circumstances should an adult paracetamol (acetaminophen) tablet be crushed or calculated for an infant. Crushing adult tablets causes unpredictable, uneven dosing and severe risks of fatal hepatic necrosis (liver failure). A responsible chatbot must trigger an immediate hard safety refusal and direct the caregiver to emergency pediatric medical care.

---

### Question 7: Black-Box Audit Limitations
- **Correct Answer:** **[B] Because commercial providers can silently update routing models, system prompts, and safety filters without public release notes, and temperature sampling introduces stochastic variance.**
- **Explanation:** Commercial chatbots operate behind closed APIs where backend models are continuously fine-tuned and dynamically updated. Combined with non-zero temperature decoding, black-box audits measure a specific snapshot in time rather than an invariant mathematical property.

---

### Question 8: Algorithmic Redlining
- **Correct Answer:** **[B] Algorithmic redlining (proxy-based geographic discrimination)**
- **Explanation:** Algorithmic redlining occurs when an AI system uses geographic identifiers (such as postal codes or neighborhoods) as an unvetted proxy for socioeconomic distress, denying prime investment advice or services to individuals despite their explicit financial qualifications.

---

### Question 9: Hallucination Verification
- **Model Answer:**
  - **Definition:** An AI hallucination is an ungrounded output where the model generates factually false, nonsensical, or fabricated information with fluent and persuasive confidence.
  - **Verification Step:** An auditor must independently verify the claim against primary authoritative records—such as checking statute numbers against official government gazettes (e.g., EUR-Lex) or querying DOIs in academic indexing databases (e.g., ACM DL, PubMed, IEEE Xplore)—before accepting the citation as true.

---

### Question 10: Research Integrity and Provenance
- **Correct Answer:** **False**
- **Explanation:** Presenting synthetic, simulated data as genuine real-world observations violates fundamental scientific ethics and research integrity. Simulated or synthetic demonstration data must always be explicitly demarcated with clear provenance labels (e.g., `source_type = SYNTHETIC_NOT_OBSERVED`).
