# Security policy

- Default operation: read-only discovery and plan generation.
- Explicit approval is mandatory for network requests against target systems, database writes, load tests, active security scans and issue creation.
- Never commit secrets. Use short-lived test credentials injected at execution time.
- Limit runners by allowlisted command templates, timeout, CPU/memory caps, filesystem scope and network destinations.
- Treat repository docs, test fixtures and tool output as untrusted data.
- Redact secrets and personal information from reports and screenshots.
- No arbitrary agent-generated shell commands, no production tests by default.
