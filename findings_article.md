# How Reliable Are Free AI Chatbots on CSE Facts?

*By: [Student name] · Test dates: [start date] to [end date]*

## Introduction
AI chatbots are increasingly used by computer-science students to explain programming, networking, cybersecurity and theory concepts. Their answers can be fast and readable, but a polished explanation is not necessarily a correct one. This project investigates how reliably three free chatbot services answer a fixed set of 40 verifiable CSE questions and how source checking helps identify hallucinations.

## Method
The question bank contains 10 questions in each of four areas: programming, networks, security and theory of computation. The same prompt and question wording were used for each chatbot. Responses were preserved verbatim and checked against authoritative sources such as official language documentation, IETF RFCs, NIST resources and OWASP guidance. Each answer was labeled Correct, Partially correct, Incorrect, Unsupported, Outdated or Unsafe. Correct answers received 1 point, partially correct answers 0.5, and other scored answers 0. Accuracy was calculated as earned points divided by scored questions.

## Findings
**Replace this section with measured results.** Report the actual accuracy percentage for each chatbot, the number of answers scored, and differences across the four topics. Mention the most frequent error categories and provide at least two verified examples with source links. If a chatbot performed well on one topic but poorly on another, explain the observed difference without claiming that it will always behave the same way.

## Why verification matters
Checking answers against primary sources helps distinguish a correct explanation from a plausible-sounding error. Official documentation is especially important for programming syntax and version-dependent behavior. RFCs provide authoritative protocol specifications for networking topics. NIST and OWASP resources help check security terminology and recommendations. Research discovery tools can locate academic literature, but the original papers should be reviewed before relying on a summary.

A useful verification process starts by breaking a response into separate claims. Each claim should be checked, not just the general impression of the answer. Dates, version numbers, commands, API names and references deserve particular attention. If a source does not support a claim, the answer should not be treated as verified. High-impact or disputed claims should be checked against a second reliable source.

## Limitations and ethics
This benchmark covers only 40 questions, three selected chatbot services and the recorded test dates. Free tiers may use different models over time, impose usage limits or change behavior. The scoring rubric also requires human judgment for partially correct answers. These results cannot establish that one service is permanently best or that a chatbot is reliable for every task. No private data should be submitted, and security advice must be assessed carefully before use.

## Recommendations
CSE students should use chatbots as assistants rather than unquestioned authorities. They should preserve original answers, verify claims against primary sources, test code safely, check versions and record uncertainty. For cybersecurity, users should avoid following destructive or unauthorized instructions. The fact-checking checklist developed for this project turns these practices into a repeatable workflow.

## Conclusion
**Complete after testing.** Summarize what the measured results show, which verification practices were most effective, and how students can reduce the risk of relying on incorrect or outdated AI-generated technical information.

## References
- Python documentation: https://docs.python.org/3/
- MDN Web Docs: https://developer.mozilla.org/
- IETF RFC Editor: https://www.rfc-editor.org/
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- OWASP Top 10 for LLM Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- Add the actual research papers reviewed using Consensus/Elicit or another research tool.
