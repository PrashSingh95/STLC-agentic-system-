# Conventions

- Stable IDs: `REQ-001`, `TC-API-001`, `TC-FE-001`, `RUN-<id>`.
- Every test must specify `requirement_ids`, preconditions, actions, assertions, severity and evidence source.
- Agent manifests use `agent.yml`; workflow definition uses `workflow.yml`; reusable instructions use `SKILL.md`.
- All cross-agent outputs are JSON-compatible and carry `status`, `evidence`, `assumptions`, `blockers`.
- Unavailable data must be identified as unknown. Never convert a generated test into an executed test.
