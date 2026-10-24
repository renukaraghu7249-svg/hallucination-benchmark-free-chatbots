# Verification Report

## Scope
This report documents how each answer from the three selected chatbots is checked. Complete this document after collecting responses.

## Verification procedure
1. Copy the answer verbatim and assign a unique Question ID.
2. Split compound answers into individual factual claims where necessary.
3. Open the primary source linked in `data/question_bank.csv`.
4. Confirm that the source directly supports or contradicts the claim.
5. Use a second authoritative source for disputed or high-impact claims.
6. Record the source URL, source date/version and date accessed.
7. Assign an error label and explain the evidence.

## Error taxonomy
| Label | Meaning | Example pattern |
|---|---|---|
| Correct | Checked claims are supported | Definition matches official documentation |
| Partially correct | Main idea is right but a material detail is wrong/missing | Correct protocol purpose, wrong port |
| Incorrect | A checkable claim is contradicted by evidence | Incorrect complexity or definition |
| Unsupported | No adequate evidence found | Confident claim with no verifiable support |
| Fabricated reference | Citation or identifier cannot be found | Nonexistent RFC or paper |
| Outdated | Conflicts with current version or guidance | Deprecated API presented as current |
| Unsafe | Could cause harm if followed | Destructive or insecure command recommended |

## Summary table
Fill after testing.

| Chatbot/model | Questions scored | Correct | Partial | Incorrect | Unsupported | Outdated | Unsafe |
|---|---:|---:|---:|---:|---:|---:|---:|
| Chatbot A | TODO | TODO | TODO | TODO | TODO | TODO | TODO |
| Chatbot B | TODO | TODO | TODO | TODO | TODO | TODO | TODO |
| Chatbot C | TODO | TODO | TODO | TODO | TODO | TODO | TODO |

## Evidence log
For every non-correct answer, add:
- Question ID and chatbot/model
- Exact claim that failed verification
- Source that contradicts or fails to support the claim
- Error category and severity
- Corrected answer
- Date verified

## Limitations
A small, fixed question bank cannot represent every CSE task. Scoring involves judgment, so borderline answers should be reviewed consistently. Free chatbot products can change between dates. Do not generalize beyond the recorded test conditions.
