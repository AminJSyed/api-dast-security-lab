# DAST Summary

## Objective

This lab demonstrates API-focused Dynamic Application Security
Testing using OWASP ZAP.

The goal is to test a running API from the outside, identify
security issues, apply remediation, and validate the fix with a
second scan.

## Target

Application:

API DAST Security Lab

Framework:

FastAPI

DAST tool:

OWASP ZAP

Scan type:

OpenAPI-based API scan

API schema:

/openapi.json

## Initial Scan Result

FAIL-NEW: 0

WARN-NEW: 2

PASS: 116

Findings:

1. X-Content-Type-Options Header Missing
2. Cross-Origin-Resource-Policy Header Missing or Invalid

## Remediation

Security headers were added at application middleware level.

Headers added:

X-Content-Type-Options: nosniff

Cross-Origin-Resource-Policy: same-origin

## Validation Scan Result

FAIL-NEW: 0

WARN-NEW: 0

PASS: 118

## Key Learning

DAST validates the running application from an external attacker
perspective.

OpenAPI-driven scanning improves API coverage because the scanner
can understand available endpoints, methods, and parameters.

Automated DAST is useful, but it should be combined with SAST,
dependency scanning, container scanning, manual review, and threat
modeling.
