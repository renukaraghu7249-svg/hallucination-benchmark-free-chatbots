# CAPSTONE 17 — Hallucination Benchmark: Testing Free Chatbots

## Project question
How reliable are free AI chatbots on technical facts, and how can users detect hallucinations?

## Audience
CSE students and faculty who use AI tools for learning and technical work.

## Status
Research and testing project template. Complete the dated chatbot tests and replace all TODO markers before final submission. Scores are intentionally not fabricated.

## Repository structure
- `research/research_report.md` — background, methods and research summary
- `reports/fact_checking_checklist.md` — practical verification checklist
- `data/question_bank.csv` — 40 verifiable CSE questions, 10 per topic
- `data/chatbot_results_template.csv` — record actual answers and verification
- `reports/verification_report.md` — error categories and source-checking method
- `reports/before_after_analysis.md` — compare initial answers with verified corrections
- `articles/findings_article.md` — findings article draft with results placeholders
- `presentation/slides.md` — six-slide presentation outline
- `scripts/calculate_accuracy.py` — computes accuracy from completed results CSV
- `prompts/prompt_library.md` — prompts used for consistent testing
- `charts/README.md` — instructions for creating charts from real scores
- `demo/final_demo_plan.md` — final demo walkthrough

## Suggested workflow
1. Review the question bank and confirm every answer against its linked primary/authoritative source.
2. Choose three free chatbot services and record their exact names/model labels and date tested.
3. Ask each chatbot the same 40 questions with the same prompt instructions.
4. Save responses verbatim; do not edit answers before scoring.
5. Verify each response against sources and score it using the rubric.
6. Run the script to calculate accuracy by chatbot and topic.
7. Replace placeholders in the article, report and slides with measured results.
8. Commit the files to GitHub.

## Important research integrity note
This package includes question-bank reference answers and templates, not fabricated chatbot results. Do not claim that testing occurred until it has. Free-tier access, models and answers can change; date-stamp all observations.
