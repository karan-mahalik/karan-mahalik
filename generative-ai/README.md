# Generative AI project lab — planning collection

> **Status: PLANNED / NOT IMPLEMENTED.** These are candidate project briefs, not a list of existing deployed GitHub projects. Karan's public repositories currently document analytics and software-development projects; no verifiable completed LLM-based project was identified during this profile update.

## Why this collection exists

Karan's established work covers Power BI, SQL, Excel, Python, application UIs and REST APIs. This lab defines potential future projects in which those skills can be applied to generative AI. It does **not** represent work performed at GenerativeAiTechshila; the internship certificate specifically describes general software and UI development.

## Candidate projects (all planned)

| Proposed project | Goal | First demonstrable milestone | Evaluation |
| --- | --- | --- | --- |
| **Analytics Document Q&A (RAG)** | Ask questions about public, non-sensitive project documentation with citations | Ingest a small sample of public READMEs and return cited answers | Groundedness, citation correctness, refusal on unknowns |
| **Read-only Text-to-SQL Assistant** | Translate constrained natural-language reporting questions into safe SQL | Generate queries against a synthetic test schema; execute only read-only statements in a sandbox | Query accuracy, invalid-query handling, SQL injection and data-leak safeguards |
| **Data Quality Copilot** | Suggest transparent validation rules for tabular datasets | Produce human-reviewed pandas/SQL checks for a synthetic dataset | Rule precision, false positives, reproducibility |
| **Portfolio Q&A Assistant** | Answer questions about Karan's verified public project work | Compile a source-grounded FAQ before integrating any LLM | Hallucination rate, link correctness, accurate qualification |

## Standards before marking a project "completed"

1. Add the actual source repository and license (where appropriate).
2. Commit a minimal reproducible demo with sample/synthetic data; avoid proprietary data.
3. Add test cases, evaluation evidence and a working local setup.
4. Document model/provider versions, costs if applicable, privacy and API-key handling.
5. Provide screenshots or demos of the **actual** implementation, never invented analytics screenshots.
6. Update this index and the GitHub profile with the verified project link and accurate status.

## Status log

- **2026-10-30:** Planning directory created; no GenAI source repository or demo linked yet.

For a repeatable project specification, use [PROJECT_TEMPLATE.md](PROJECT_TEMPLATE.md).

[Back to Karan's GitHub profile](../README.md)
