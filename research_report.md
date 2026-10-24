# Research Report: Hallucination Benchmark — Testing Free Chatbots

## 1. Purpose and research question
This project evaluates how reliably free AI chatbots answer verifiable computer-science questions. The guiding question is: **How reliable are free AI chatbots on technical facts, and how can users detect hallucinations?**

## 2. Target audience
The target audience is CSE students and faculty who use AI for study, programming, networking, cybersecurity and theory-of-computation topics.

## 3. Background
A hallucination is an answer that presents unsupported, invented or incorrect information as if it were true. In technical learning, errors can be hard to notice because an answer may sound confident and use correct terminology. A chatbot can also give outdated advice, omit important conditions, cite a source that does not support its claim, or provide unsafe security instructions.

## 4. Types of errors to track
- **Factual error:** a claim conflicts with an authoritative source.
- **Fabricated reference:** a citation, paper, API, command or standard cannot be verified.
- **Unsupported claim:** the answer gives a claim without sufficient evidence.
- **Outdated information:** the answer was once accurate but no longer matches current documentation.
- **Misleading omission:** a key condition, limitation or safety warning is missing.
- **Reasoning/calculation error:** the stated conclusion does not follow from the steps.
- **Unsafe advice:** instructions could create avoidable security or operational harm.
- **Correct / no detected error:** claims checked are supported by sources.

## 5. Causes and contributing factors
Language models generate likely sequences of text rather than functioning as guaranteed databases. They may lack current information, receive ambiguous prompts, generalize from incomplete patterns, or produce plausible details when uncertain. Errors can also arise from missing context, version differences, incorrect assumptions and failure to consult external documentation. A fluent tone is not evidence of correctness.

## 6. Method
1. Use the 40-question bank: 10 questions each for programming, networks, security and theory.
2. Select three accessible chatbot services. Record the service/model label and date/time.
3. Use the same neutral prompt for all systems and ask each question separately.
4. Copy each answer verbatim into the results sheet.
5. Check each answer against the source linked in the question bank and, where possible, a second reliable source.
6. Score the answer as Correct, Partially correct, Incorrect, Unsupported, Outdated or Unsafe. Explain the decision and cite the evidence.
7. Calculate scores by chatbot and topic. Report the sample size and rubric.
8. Compare raw answers with verified corrections and discuss limitations.

## 7. Scoring rubric
For a simple accuracy percentage, use **Correct = 1 point**, **Partially correct = 0.5 point**, and **Incorrect / Unsupported / Outdated / Unsafe = 0 points**. Accuracy = points earned ÷ number of scored answers × 100. If an answer is not tested or cannot be judged, mark it `NOT SCORED` and exclude it from the denominator, explaining why. Report safety issues separately rather than hiding them in an overall average.

## 8. Verification and cross-checking
Use primary documentation where possible: official language documentation, IETF RFCs, NIST publications, OWASP guidance, and university or textbook references. Research discovery tools such as Consensus and Elicit can help find papers, but their summaries should be checked against the original paper. Chatbot answers should never be treated as their own proof.

## 9. Tools and AI skills
Record at least two research tools used for literature discovery and at least four free AI tools/services considered or tested. Suggested tools include ChatGPT, Gemini, Claude, DeepSeek, Perplexity, NotebookLM, Consensus and Elicit; availability and free-tier limits may vary. Use Google Sheets or a compatible spreadsheet and Python for analysis. In the final report, state only the tools actually used.

## 10. Ethics, limitations and responsible reporting
Date-stamp all results because models, interfaces and free-tier access change. Use the same questions and prompt conditions for fair comparison. Do not include personal, confidential or sensitive data. Avoid running security tests on systems without permission. Do not claim that one chatbot is permanently best based on a small sample. The benchmark measures these questions, models and dates only; it does not establish universal reliability.

## 11. Results
**TODO:** Insert the actual sample size, score table, charts, main error categories and examples after testing. Do not invent results.

## 12. Conclusion
A useful conclusion should explain which question types were most error-prone in this sample, which verification methods caught the errors, and what students should do before relying on chatbot output. Complete this section only after results have been collected.

## Research sources to consult
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- NIST Generative AI Profile (AI RMF): https://www.nist.gov/itl/ai-risk-management-framework
- OWASP Top 10 for LLM Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- IETF RFC index: https://www.rfc-editor.org/
- Python documentation: https://docs.python.org/3/
- MDN Web Docs: https://developer.mozilla.org/
- Consensus: https://consensus.app/
- Elicit: https://elicit.com/

**TODO:** Add at least two research-tool searches you actually performed, paper titles/DOIs, date accessed and a short note on how each source informed the report.
