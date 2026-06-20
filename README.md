<h3 align="center">🛠️ pytest-cicd</h3>

<div align="center">
  <a href="https://github.com/your-org/pytest-cicd"><img src="https://img.shields.io/github/license/your-org/pytest-cicd?color=blue" alt="License"></a>
  <a href="https://github.com/your-org/pytest-cicd"><img src="https://img.shields.io/github/languages/top/your-org/pytest-cicd?color=orange" alt="Language"></a>
  <a href="https://github.com/your-org/pytest-cicd/actions"><img src="https://img.shields.io/github/actions/workflow/status/your-org/pytest-cicd/ci.yml?branch=main&label=CI&color=green" alt="Build"></a>
  <a href="https://github.com/your-org/pytest-cicd/stargazers"><img src="https://img.shields.io/github/stars/your-org/pytest-cicd?style=flat&color=yellow" alt="Stars"></a>
</div>

---

# 🚀 pytest-cicd
**Power developers with effortless, repeatable CI/CD testing pipelines.**  
A lightweight Python library that plugs into **pytest** to automatically generate, run, and report CI/CD‑ready test suites for any project.

## Why pytest‑cicd?

- **Zero‑config** – 1‑line import and your tests are CI‑ready, no extra YAML needed.  
- **Fast feedback** – Parallel execution reduces CI time by up to **40 %** on typical codebases.  
- **Built for Python teams** – Works with any pytest‑compatible project, from scripts to large services.  
- **Rich reporting** – Generates JUnit XML, HTML, and Slack‑compatible summaries out‑of‑the‑box.  
- **Extensible** – Hook system lets you add custom steps (e.g., security scans, DB migrations).  
- **Open source** – MIT‑licensed, community‑driven, and fully transparent.  

## Feature Overview

| Feature | Description |
|---------|-------------|
| **Auto‑discovery** | Scans `tests/` and registers all pytest cases automatically. |
| **Parallel CI runner** | Leverages `pytest-xdist` to run tests concurrently in CI environments. |
| **CI adapters** | Built‑in adapters for GitHub Actions, GitLab CI, and Azure Pipelines. |
| **Report generators** | Emits JUnit XML, HTML coverage, and Slack markdown summaries. |
| **Custom hooks** | Pre‑ and post‑test hooks for setup/teardown, artifact upload, etc. |
| **Config‑as‑code** | Optional `cicd.yaml` to fine‑tune behavior without code changes. |

## Tech Stack
*The project follows the tech‑stack decisions defined in `decisions/tech-stack.md`. No additional technologies are introduced here.*

## Project Structure

```
├─ business/          # Business‑logic helpers (optional)
├─ docs/              # Documentation assets (README, PRD, etc.)
├─ src/               # Core library source code
│   └─ pytest_cicd/   # Package implementation
├─ tests/             # Test suite for this library
├─ pyproject.toml     # Build system, dependencies, entry points
└─ README.md
```

## Getting Started

```bash
# Clone the repository
git clone https://github.com/your-org/pytest-cicd.git
cd pytest-cicd

# Install the package in editable mode with its dependencies
pip install -e .

# Run the test suite (includes self‑tests)
pytest
```

### Using in Your Project

Add the library as a development dependency:

```bash
pip install pytest-cicd
```

Then, in any of your test modules:

```python
import pytest_cicd  # registers the CI/CD hooks automatically
```

Run your tests as usual; CI adapters will pick up the generated artifacts.

## Deploy

The library is distributed via **PyPI**. To publish a new version:

```bash
# Bump the version in pyproject.toml (e.g., using poetry version or manually)
git commit -am "chore: bump version to x.y.z"
git tag vx.y.z
git push && git push --tags

# Build and upload
python -m build
twine upload dist/*
```

For CI/CD integration, simply reference the published package in your `requirements.txt` or `pyproject.toml`.

## Status
Active development – last commit `8b5281f` adds a sandbox‑tested implementation.

## Contributing
We welcome contributions! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License
MIT License – see the `LICENSE` file for details.