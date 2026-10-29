---
name: defect-analysis
description: Analyze real test failures and generate reproducible bug reports while distinguishing application defects, flaky tests and infrastructure failures.
---

# defect-analysis

## Operating procedure
1. Consume actual failure traces, response data and logs with secret redaction.
2. Group failures by signature and classify as `product_defect`, `test_defect`, `environment`, or `unknown` with confidence.
3. Include expected/actual behavior, steps, environment, assertion and source artifact IDs.
4. Do not assert root cause without code/log evidence; report hypotheses separately.
5. Avoid automatic ticket creation without user approval.

## Output
Return a JSON-compatible record containing `status`, `items`, `evidence`, `assumptions`, and `blockers`. Use stable IDs, provenance, and actionable next steps. No fabricated execution results.
