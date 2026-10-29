---
name: test-reporting
description: Summarize authentic STLC execution evidence as coverage, pass/fail, blockers and release quality risks. Use at test closure.
---

# test-reporting

## Operating procedure
1. Aggregate executed cases and never count unexecuted or skipped cases as passed.
2. Compute test totals, status mix, requirement coverage, affected components and known limitations.
3. Include links or paths to evidence, environment and build/commit identity.
4. Separate release recommendation from release authorization; never assert 100% quality or full coverage.
5. Emit both a human-readable summary and machine-readable JSON.

## Output
Return a JSON-compatible record containing `status`, `items`, `evidence`, `assumptions`, and `blockers`. Use stable IDs, provenance, and actionable next steps. No fabricated execution results.
