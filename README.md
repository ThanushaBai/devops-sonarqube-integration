# DevOps SonarQube Integration

A DevOps project demonstrating **SonarQube Cloud** static code analysis integrated with **GitHub Actions CI/CD**. Every push to `main` automatically triggers a code-quality scan, with results published to the SonarQube Cloud dashboard.

---

## Overview

This repository showcases a complete CI-based code-quality pipeline:

- **SonarQube Cloud** analyzes the codebase for bugs, vulnerabilities, code smells, and security hotspots.
- **GitHub Actions** runs the SonarQube scanner on every push and pull request.
- **Quality Gate** results are reported back to the repository.

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
├── sonar-project.properties       # SonarQube project configuration
├── app.py                         # Sample Python source code
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
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: SonarQube Scan
        uses: SonarSource/sonarqube-scan-action@v5
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
```

### GitHub Secret

| Secret Name | Purpose |
|---|---|
| `SONAR_TOKEN` | Authentication token generated in SonarQube Cloud, used by GitHub Actions to publish analysis results |

---

## How It Works

1. Developer pushes code to `main` (or opens a Pull Request).
2. GitHub Actions triggers the workflow defined in `.github/workflows/build.yml`.
3. The workflow checks out the repository (`fetch-depth: 0` for full history).
4. The SonarQube Scan action runs on an Ubuntu runner.
5. The scanner reads `sonar-project.properties` and authenticates using `SONAR_TOKEN`.
6. Analysis results are uploaded to SonarQube Cloud.
7. The Quality Gate is evaluated and reported on the dashboard.

---

## Verification

The CI pipeline runs successfully — verified by:

- Green GitHub Actions run (Build workflow)
- Log output: `ANALYSIS SUCCESSFUL`
- SonarQube Cloud dashboard showing:
  - Quality Gate: Passed
  - 0 New Issues
  - 0 Security Hotspots

**Dashboard:** https://sonarcloud.io/project/overview?id=ThanushaBai_devops-sonarqube-integration

---

## Tech Stack

| Tool | Purpose |
|---|---|
| SonarQube Cloud | Static code analysis / quality gate |
| GitHub Actions | CI/CD automation |
| Python 3.12 | Sample source code language |
| YAML | Workflow & configuration |
| Git | Version control |

---

## Key Concepts Covered

- Static Code Analysis — scanning source code without executing it
- Quality Gate — a pass/fail rule set applied to every analysis
- CI-based Analysis — running SonarQube via a CI pipeline (vs. Automatic Analysis)
- Secrets Management — storing sensitive tokens in GitHub Secrets
- Pipeline as Code — defining CI workflows in version-controlled YAML

---

## Reproducing This Setup

1. Create a public GitHub repository with sample code.
2. Sign up at SonarQube Cloud and import the repository.
3. Choose GitHub Actions as the analysis method.
4. Generate a SonarQube token and add it to GitHub as the `SONAR_TOKEN` secret.
5. Add `sonar-project.properties` to the repo root.
6. Add `.github/workflows/build.yml` to enable the CI pipeline.
7. Disable Automatic Analysis in SonarQube → Administration → Analysis Method.
8. Push to `main` and watch the scan run.

---

## References

- SonarQube Cloud Documentation: https://docs.sonarsource.com/sonarcloud/
- GitHub Actions Documentation: https://docs.github.com/en/actions
- SonarSource GitHub Action: https://github.com/SonarSource/sonarqube-scan-action

---
