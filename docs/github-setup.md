# GitHub setup: PrashSingh95/STLC-agentic-system-

GitHub repository: https://github.com/PrashSingh95/STLC-agentic-system-

As inspected on 2026-10-29, GitHub's public web page displayed **This repository is empty**. This bundle is prepared locally and has **not** been pushed to GitHub.

## Upload the project (Mac terminal)
1. Extract the ZIP archive into an empty directory. The top-level folder is `STLC-agentic-system-`.
2. Run the following commands inside it. GitHub authentication may be requested by Git when pushing.

```sh
cd STLC-agentic-system-
git init
git branch -M main
git remote add origin https://github.com/PrashSingh95/STLC-agentic-system-.git
git add .
git commit -m "Initialize Agentic STLC registry and local FE/BE pilot"
git push -u origin main
```

If the GitHub repository already has content by then, **do not force push**. Clone it and merge changes after reviewing conflicts.

## After upload
The workflow `.github/workflows/validate.yml` checks the registry, inspects the repository, makes a preliminary plan, and executes the **bundled demo only** in GitHub Actions. It doesn't execute third-party project scripts or issue write permissions.

## Configure a separate real FE/BE project
Copy `examples/github-local.project.example.json` to a local configuration file, set `repo_path` to an approved local checkout and set `requirements_path` to a requirements Markdown file. Leave `execution_enabled` false. `inspect` and `plan` are read-only. `run-demo` refuses to run any repo except the bundled demo. Interactive browser testing is not implemented in this version.
