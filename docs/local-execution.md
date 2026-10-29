# Local execution and adoption

The v0.2 fixture uses a Node.js localhost HTTP server and an HTTP markup smoke check; it has no npm install step.

```bash
python3 scripts/validate_registry.py
python3 scripts/stlc.py inspect --config examples/demo.project.json
python3 scripts/stlc.py plan --config examples/demo.project.json
python3 scripts/stlc.py run-demo --config examples/demo.project.json --approve --output artifacts/demo-run.json
```

The CLI only executes the **bundled demo repository**, and only with both `execution_enabled: true` and `--approve`.
No arbitrary package scripts or tests from a GitHub checkout are executed. A future external-repo runner must provide separate explicit permission, command allowlists, isolated workers, outbound network policy, timeouts and secrets injection.

For a private GitHub repo, clone outside this tool using your approved GitHub credentials, then set `repo_path` in a new JSON config to that checkout. Do not put tokens in config. `inspect` and `plan` can inspect it read-only. Remote clone is intentionally not implemented.

The frontend smoke check verifies HTTP-delivered login markup; Chromium browser execution is marked not_run in evidence. It does not click the form; API tests verify login behavior independently. Add Playwright for browser interaction and screenshots in the next phase.
