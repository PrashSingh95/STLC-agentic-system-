---
name: test-planning
description: Create risk-based and traceable plans for backend API and frontend testing. Use after requirements and repository analysis.
---

# test-planning

## Operating procedure
1. Map each requirement and critical user journey to unique test IDs.
2. Categorize tests by `api`, `backend`, `frontend`, `integration`, and later optional domains.
3. Record priority, severity-of-failure, preconditions, setup, expected assertion and evidence source.
4. Separate confirmed requirements from assumptions; never invent business rules.
5. Obtain plan approval before write-capable or destructive execution.

## Output
Return a JSON-compatible record containing `status`, `items`, `evidence`, `assumptions`, and `blockers`. Use stable IDs, provenance, and actionable next steps. No fabricated execution results.
