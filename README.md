# Agentic STLC - runnable local pilot v0.2

This is the next iteration of the v0.1 agent/skill registry, configured for **GitHub local checkouts**, **mixed FE/BE**, **local execution**, and **sample requirements**.

## Quick start
Requires Python 3.10+, Node.js 18+, for the included HTTP tests; Chromium browser execution is not yet enabled.

```bash
python3 scripts/validate_registry.py
python3 scripts/stlc.py inspect --config examples/demo.project.json
python3 scripts/stlc.py plan --config examples/demo.project.json
python3 scripts/stlc.py run-demo --config examples/demo.project.json --approve --output artifacts/demo-run.json
```

Inspect/plan are read-only. `run-demo` starts a localhost Node.js server and tests real HTTP endpoints and delivered frontend HTML. An explicit `--approve` gate is mandatory. No external repo is executed.

## Structure
- `agents/`: 7 agent specifications from v0.1
- `skills/`: 7 reusable skill definitions from v0.1
- `adapters/repositories/github_local.py`: GitHub/local checkout read-only framework and test discovery
- `scripts/stlc.py`: inspect/plan/approved demo workflow
- `tests/run_demo.py`: runnable HTTP backend and Chromium frontend smoke tests
- `examples/demo-repo/`: minimal example FE + BE app
- `examples/sample-requirements.md`: traceable requirement inputs
- `docs/local-execution.md`: instructions and execution boundaries

## Scope limitations
This is a **deterministic prototype**, not an LLM agent runtime. Agent definitions specify intended behavior; no AI inference is performed. Planning uses simple project signals and parsed requirement IDs, not generative test design. Frontend smoke checks HTTP HTML, not browser rendering; interactive E2E, real GitHub API, GitHub Actions, sandboxed external-repo execution, flaky-test triage, and release approval remain future work.

## GitHub repository onboarding
Prepared for [PrashSingh95/STLC-agentic-system-](https://github.com/PrashSingh95/STLC-agentic-system-).
The public repository was empty when inspected; this ZIP contains the files to commit. See [docs/github-setup.md](docs/github-setup.md) for exact `git` commands.

The GitHub Actions workflow `.github/workflows/validate.yml` runs validation, read-only inspection, preliminary planning, and the approved bundled FE/BE demo. No external repository is executed.

Inspect the platform itself with:

```sh
python3 scripts/stlc.py inspect --config examples/platform.project.json
python3 scripts/stlc.py plan --config examples/platform.project.json
```
