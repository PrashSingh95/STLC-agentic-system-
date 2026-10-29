---
name: test-execution
description: Execute pre-approved backend/API/frontend test plans using allowlisted tools in an isolated environment, then collect verifiable results.
---

# test-execution

## Operating procedure
1. Require an explicit environment profile, non-production target and approved command registry.
2. Run only tool commands from a vetted allowlist; never execute raw LLM-generated shell strings.
3. Use separate temporary workspaces, timeouts, resource caps, no privileged containers and secret injection outside prompts.
4. Collect exit code, test count, cases, JUnit output and artifact paths.
5. If no runner is configured, output `blocked` and missing integrations; never synthesize passing test results.

## Output
Return a JSON-compatible record containing `status`, `items`, `evidence`, `assumptions`, and `blockers`. Use stable IDs, provenance, and actionable next steps. No fabricated execution results.
