# Authenticated API DAST Scenario

## Objective

This scenario demonstrates authenticated API DAST scanning using
OWASP ZAP.

The goal is to scan protected API endpoints that require a bearer
token.

## Why Authentication Matters

Unauthenticated DAST scans can only test public endpoints.

Many real API endpoints require authentication, such as:

- User profile APIs
- Booking APIs
- Payment APIs
- Admin APIs
- Internal workflow APIs

If the scanner does not authenticate, it may receive only:

401 Unauthorized

This reduces scan coverage.

## Implementation

The lab uses a bearer token:

Authorization: Bearer token-amin

The ZAP scan script uses ZAP's replacer configuration to add the
Authorization header to API requests.

Script:

scripts/run-zap-auth-api-scan.sh

Report:

reports/zap-auth-api-report.html

## Validation

Protected endpoint without token:

GET /booking/1001

Result:

401 Unauthorized

Protected endpoint with token:

GET /booking/1001
Authorization: Bearer token-amin

Result:

200 OK

## Production Considerations

For production-like authenticated DAST:

- Use dedicated test users
- Use least-privilege test tokens
- Avoid real customer data
- Run active scans only in staging or approved environments
- Store tokens in CI/CD secrets
- Rotate test credentials regularly
- Avoid hardcoding production credentials
- Monitor scan activity

## Key Learning

Authenticated DAST improves API scan coverage by allowing the scanner
to access protected endpoints.

It must be done safely using controlled test accounts, limited
permissions, and non-production environments.
