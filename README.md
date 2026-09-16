# DevOps SonarQube Integration

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ThanushaBai_devops-sonarqube-integration&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=ThanushaBai_devops-sonarqube-integration)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=ThanushaBai_devops-sonarqube-integration&metric=coverage)](https://sonarcloud.io/summary/new_code?id=ThanushaBai_devops-sonarqube-integration)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=ThanushaBai_devops-sonarqube-integration&metric=bugs)](https://sonarcloud.io/summary/new_code?id=ThanushaBai_devops-sonarqube-integration)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=ThanushaBai_devops-sonarqube-integration&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=ThanushaBai_devops-sonarqube-integration)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=ThanushaBai_devops-sonarqube-integration&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=ThanushaBai_devops-sonarqube-integration)

A DevOps project demonstrating **SonarQube Cloud** static code analysis integrated with **GitHub Actions CI/CD**. Every push to `main` automatically triggers a code-quality scan, with results published to the SonarQube Cloud dashboard.

---

## Overview

This repository showcases a complete CI-based code-quality pipeline:

- **SonarQube Cloud** analyzes the codebase for bugs, vulnerabilities, code smells, and security hotspots.
- **GitHub Actions** runs the SonarQube scanner on every push and pull request.
- **Quality Gate** results are reported back to the repository and displayed as a status check.
- **Unit tests** with `pytest` provide coverage data (87.5% achieved).

---

## Architecture

```
┌─────────────┐   push    ┌──────────────────┐   scan    ┌─────────────────┐
│  Developer  │──────────▶│  GitHub Actions  │──────────▶│ SonarQube Cloud │
│             │   code    │  (ubuntu-latest) │  results  │   (dashboard)   │
└─────────────┘           └──────────────────┘           └─────────────────┘
                                   │
                                   │ reads
                                   ▼
                     ┌──────────────────────────────┐
                     │  sonar-project.properties    │
                     │  .github/workflows/build.yml │
                     │  SONAR_TOKEN (GitHub Secret) │
                     └──────────────────────────────┘
```

---

## Project Structure

```
devops-sonarqube-integration/
├── .github/
│   └── workflows/
│       └── build.yml              # GitHub Actions workflow (CI pipeline)
├── tests/
│   └── test_app.py                # Unit tests for app.py
├── app.py                         # Sample Python source code
├── conftest.py                    # Pytest configuration (path setup)
├── requirements.txt               # Pinned test dependencies
├── sonar-project.properties       # SonarQube project configuration
└── README.md                      # This file
```

---

## Configuration

### SonarQube Cloud Project

| Setting | Value |
|---|---|
| Project Key | `ThanushaBai_devops-sonarqube-integration` |
| Organization | `thanushabai` |
| Analysis Mode | CI-based (Automatic Analysis disabled) |
| Quality Gate | Sonar way |

### sonar-project.properties

```properties
sonar.projectKey=ThanushaBai_devops-sonarqube-integration
sonar.organization=thanushabai

sonar.projectName=devops-sonarqube-integration
sonar.projectVersion=1.0

# Target Python version for accurate analysis
sonar.python.version=3.12

# Path to coverage report produced by pytest-cov
sonar.python.coverage.reportPaths=coverage.xml
```

### requirements.txt

```
pytest==8.3.4
pytest-cov==6.0.0
```

### GitHub Actions Workflow (.github/workflows/build.yml)

```yaml
name: Build

on:
  push:
    branches:
      - main
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  sonarqube:
    name: SonarQube
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683  # v4.2.2
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@0b93645e9fea7318ecaed2b359559ac225c90a2b  # v5.3.2
        with:
          python-version: '3.12'

      - name: Install test dependencies
        run: |
          python -m pip install --upgrade pip
          pip install --only-binary :all: -r requirements.txt

      - name: Run tests with coverage
        run: |
          pytest --cov=. --cov-report=xml

      - name: SonarQube Scan
        uses: SonarSource/sonarqube-scan-action@fd88b7d7ccbaefd23d8f36f73b59db7a3d246602  # v6.0.0
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
```

**Note:** GitHub Actions are pinned to full commit SHAs to satisfy SonarQube's supply-chain security rule.

### GitHub Secret

| Secret Name | Purpose |
|---|---|
| `SONAR_TOKEN` | Authentication token generated in SonarQube Cloud, used by GitHub Actions to publish analysis results |

---

## How It Works

1. Developer pushes code to `main` (or opens a Pull Request).
2. GitHub Actions triggers the workflow defined in `.github/workflows/build.yml`.
3. The workflow checks out the repository (`fetch-depth: 0` for full history).
4. Python 3.12 is set up and test dependencies are installed from `requirements.txt`.
5. `pytest` runs the unit tests and generates `coverage.xml`.
6. The SonarQube Scan action reads `sonar-project.properties`, authenticates with `SONAR_TOKEN`, and uploads analysis results.
7. The Quality Gate is evaluated and reported on the dashboard.

---

## Verification

The CI pipeline runs successfully on every push — verified by:

- ✅ Green GitHub Actions run (Build workflow)
- ✅ Log output: `ANALYSIS SUCCESSFUL`
- ✅ SonarQube Cloud dashboard showing **Quality Gate: Passed**
  - Coverage: **87.5%** (required ≥ 80%)
  - New Issues: 0
  - Duplications: 0.0%
  - Security Hotspots: 0

**Dashboard:** https://sonarcloud.io/project/overview?id=ThanushaBai_devops-sonarqube-integration

**Note on accepted issues:** Three informational pip-install hardening rules were reviewed and marked as accepted risk. Dependencies are pinned in `requirements.txt`, but pip's transitive dependency resolution cannot be hash-locked in a lightweight CI setup without additional tooling.

---

## Tech Stack

| Tool | Purpose |
|---|---|
| SonarQube Cloud | Static code analysis / quality gate |
| GitHub Actions | CI/CD automation |
| Python 3.12 | Sample source code language |
| pytest / pytest-cov | Unit testing & coverage reporting |
| YAML | Workflow & configuration |
| Git | Version control |

---

## Key Concepts Covered

- **Static Code Analysis** — scanning source code without executing it
- **Quality Gate** — a pass/fail rule set applied to every analysis
- **CI-based Analysis** — running SonarQube via a CI pipeline (vs. Automatic Analysis)
- **Secrets Management** — storing sensitive tokens in GitHub Secrets
- **Pipeline as Code** — defining CI workflows in version-controlled YAML
- **Supply-chain Security** — pinning GitHub Actions to full commit SHAs
- **Test Coverage** — measuring how much of the code is exercised by tests

---

## Reproducing This Setup

1. Create a public GitHub repository with sample Python code.
2. Sign up at [SonarQube Cloud](https://sonarcloud.io/) and import the repository.
3. Choose **GitHub Actions** as the analysis method.
4. Generate a SonarQube token and add it to GitHub as the `SONAR_TOKEN` secret.
5. Add `sonar-project.properties` to the repo root with your project key and organization.
6. Add unit tests under `tests/` and pin test dependencies in `requirements.txt`.
7. Add `.github/workflows/build.yml` to enable the CI pipeline.
8. **Disable Automatic Analysis** in SonarQube → Administration → Analysis Method.
9. Push to `main` and watch the scan run.

---

## References

- [SonarQube Cloud Documentation](https://docs.sonarsource.com/sonarcloud/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [SonarSource GitHub Action](https://github.com/SonarSource/sonarqube-scan-action)

---

## Author

**Thanusha Bai**
GitHub: [@ThanushaBai](https://github.com/ThanushaBai)
```
