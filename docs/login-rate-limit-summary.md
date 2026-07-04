# Login Rate Limiting Scenario

## Objective

This scenario demonstrates a basic login rate-limiting control.

The goal is to reduce brute-force login attempts by temporarily
blocking clients after repeated failed authentication attempts.

## Insecure Behavior

Without rate limiting, an attacker can repeatedly call the login
endpoint and try many password combinations.

Example:

POST /login

The API would continue responding with 401 Unauthorized without
slowing down or blocking repeated failures.

## Remediation

The login endpoint now tracks failed login attempts per client IP.

After three failed login attempts, the API temporarily blocks further
login attempts from the same IP address.

The API returns:

429 Too Many Requests

## Validation

Test sequence:

1. Failed login attempt returns 401
2. Failed login attempt returns 401
3. Failed login attempt returns 401
4. Failed login attempt returns 429

## Implementation Notes

This lab uses an in-memory dictionary to track failed login attempts.

This keeps the implementation simple for learning purposes.

## Production Considerations

In-memory rate limiting is not suitable for distributed production
systems because each application instance has its own memory.

For production, use a centralized or edge-level control such as:

- Redis-backed rate limiting
- API Gateway throttling
- Cloud Armor
- WAF rules
- Identity provider lockout policies
- Centralized authentication service controls

## Key Learning

Rate limiting helps reduce brute-force and credential stuffing risk.

It should be combined with strong authentication, monitoring,
alerting, lockout policies, MFA, and detection of suspicious login
patterns.
