---
name: api-functional-testing
description: Design API functional, negative, authorization and contract tests for verified endpoints. Use with OpenAPI specifications or provided API contracts.
---

# api-functional-testing

## Operating procedure
1. Derive endpoints, methods, required payload fields, status codes and auth rules from an authoritative API contract.
2. Generate happy path, invalid input, boundary, unauthorized, forbidden, idempotency and schema cases as applicable.
3. Never assume a 200 response implies success; assert key body properties and side effects.
4. Use synthetic data and test-only credentials; label destructive cases for approval.
5. Produce portable cases and an optional Playwright API test template only for confirmed endpoints.

## Output
Return a JSON-compatible record containing `status`, `items`, `evidence`, `assumptions`, and `blockers`. Use stable IDs, provenance, and actionable next steps. No fabricated execution results.
