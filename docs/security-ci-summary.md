# CI/CD Security Pipeline

## Objective

This scenario demonstrates a basic CI/CD security pipeline using
GitHub Actions.

The goal is to run security checks automatically when code is pushed
or a pull request is opened.

## Pipeline Stages

The pipeline includes:

1. Python syntax check
2. Bandit Python security scan
3. pip-audit dependency vulnerability scan
4. Semgrep SAST scan
5. Docker image build
6. Trivy container image scan
7. Manual authenticated OWASP ZAP DAST scan

## Python Security Checks

The Python job validates the application code and runs security tools.

Tools:

- compileall
- Bandit
- pip-audit
- Semgrep

## Container Security Checks

The container job builds the Docker image and scans it using Trivy.

Trivy checks the container image for known vulnerabilities in the
operating system packages and application dependencies.

## Authenticated DAST

The authenticated DAST job starts the API and runs OWASP ZAP against
the OpenAPI schema.

This job runs only when manually triggered with workflow_dispatch.

Reason:

Active DAST scans should be controlled and should normally run against
staging or approved test environments.

## Blocking vs Reporting

In this lab, the Trivy scan is configured as report-only using:

exit-code: 0

This keeps the pipeline stable while still showing findings.

In production, high and critical findings may be configured to fail
the pipeline based on risk, exploitability, and environment.

## Production Considerations

For production CI/CD security:

- Pin GitHub Actions to trusted versions or commit SHAs
- Use least-privilege workflow permissions
- Store secrets in GitHub Actions secrets
- Avoid scanning production with active DAST
- Upload reports as artifacts
- Define severity-based gates
- Review false positives
- Track remediation through tickets or backlog items

## Key Learning

A CI/CD security pipeline helps detect security issues early.

It should combine SAST, dependency scanning, container scanning,
secrets scanning, and controlled DAST.
