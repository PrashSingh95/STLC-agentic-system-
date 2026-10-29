---
name: frontend-e2e-testing
description: Design browser E2E user-journey tests for web applications using Playwright. Use after routes and expected UI behavior are confirmed.
---

# frontend-e2e-testing

## Operating procedure
1. Convert verified user journeys into independent test cases with preconditions and observable assertions.
2. Prefer accessible role/label/test ID locators and stable waiting; prohibit hard-coded sleeps.
3. Verify both UI outcome and relevant backend state when the contract supports it.
4. Capture traces/screenshots on failure; redact personal content.
5. Do not auto-approve snapshot changes or weaken checks to make tests pass.

## Output
Return a JSON-compatible record containing `status`, `items`, `evidence`, `assumptions`, and `blockers`. Use stable IDs, provenance, and actionable next steps. No fabricated execution results.
