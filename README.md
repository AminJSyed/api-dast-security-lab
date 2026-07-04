# API DAST Security Lab

A hands-on API security lab for practicing Dynamic Application
Security Testing with OWASP ZAP.

The lab uses a small FastAPI application and demonstrates how to
run an OpenAPI-based DAST scan, review findings, apply remediation,
and validate the result with a second scan.

## Purpose

This project demonstrates a practical API security testing workflow:

1. Build and run a containerized API
2. Scan the running API with OWASP ZAP
3. Use the OpenAPI schema for API discovery
4. Review DAST findings
5. Apply security fixes
6. Re-run the scan to validate remediation

## Tools Used

- FastAPI
- Docker
- Docker Compose
- OWASP ZAP
- OpenAPI
- Bash

## Security Focus

The lab focuses on API DAST testing and validation.

Covered areas:

- OpenAPI-based endpoint discovery
- Security header validation
- DAST report generation
- Remediation verification
- Repeatable scan execution

## Scan Results

Initial scan:

FAIL-NEW: 0
WARN-NEW: 2
PASS: 116

After remediation:

FAIL-NEW: 0
WARN-NEW: 0
PASS: 118

The remediation added the following headers:

X-Content-Type-Options: nosniff

Cross-Origin-Resource-Policy: same-origin

## Run Locally

Copy the example environment file:

cp .env.example .env

Start the API:

docker compose up -d --build

Test the API:

curl http://localhost:8010/health

Open API documentation:

http://localhost:8010/docs

## Run OWASP ZAP API Scan

Run the reusable scan script:

./scripts/run-zap-api-scan.sh zap-api-report.html

The report will be created in the project folder.

## Project Structure

app/

FastAPI application source code.

docs/

DAST summary and remediation notes.

reports/

OWASP ZAP scan reports.

scripts/

Reusable scan scripts.

Dockerfile

Container image definition.

docker-compose.yml

Local container runtime configuration.

## Notes

This project is intended for security learning, interview
preparation, and portfolio demonstration.

The current code represents the remediated state after the DAST
findings were fixed.

## Scenario: Object-Level Authorization

This lab includes an IDOR / BOLA scenario for API authorization
testing.

The booking endpoint requires a bearer token and enforces ownership
before returning booking data.

Validation cases:

- No token returns 401 Unauthorized
- Valid owner token returns 200 OK
- Valid token for another user returns 403 Forbidden

Run the scenario test:

./scripts/test-idor-bola.sh

See detailed notes:

docs/idor-bola-summary.md

## Scenario: Python Log Analysis

This lab includes a Python-based brute-force detection exercise.

The script reads sample login logs, counts failed login attempts per
IP address, and reports IPs that exceed the configured threshold.

Run the exercise:

python3 python-practice/bruteforce_detector.py

See detailed notes:

docs/python-log-analysis-summary.md

## Scenario: Login Rate Limiting

This lab includes a login rate-limiting scenario to demonstrate
basic brute-force protection.

The login endpoint tracks failed login attempts per client IP.
After three failed attempts, further login attempts are temporarily
blocked with:

429 Too Many Requests

Run the scenario test:

./scripts/test-login-rate-limit.sh

See detailed notes:

docs/login-rate-limit-summary.md
