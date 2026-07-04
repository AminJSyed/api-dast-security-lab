# IDOR / BOLA Scenario

## Objective

This scenario demonstrates broken object-level authorization,
commonly known as IDOR or BOLA.

The goal is to show how an API can expose another user's object
when it checks only whether the object exists, but does not verify
whether the requester is allowed to access it.

## Insecure Behavior

Initially, the booking endpoint allowed access to any booking ID
without authentication or ownership validation.

Example:

GET /booking/1001

GET /booking/1002

Both requests returned booking data.

## Risk

An attacker could modify the object ID in the request and access
another user's booking data.

This is a common API security issue because APIs often expose object
identifiers such as booking IDs, order IDs, user IDs, or payment IDs.

## Remediation

The booking endpoint was updated to require an Authorization header.

The API now performs these checks:

1. Validate that an Authorization header is present
2. Validate that the token is valid
3. Identify the current user from the token
4. Load the requested booking
5. Check whether the booking owner matches the current user
6. Return 403 Forbidden if the user does not own the booking

## Validation

No token:

GET /booking/1001

Result:

401 Unauthorized

Valid owner token:

GET /booking/1001
Authorization: Bearer token-amin

Result:

200 OK

Wrong user token:

GET /booking/1002
Authorization: Bearer token-amin

Result:

403 Forbidden

Correct user token:

GET /booking/1002
Authorization: Bearer token-test

Result:

200 OK

## Key Learning

Authorization must be enforced on the server side.

Hiding object IDs is not a real fix. The API must verify that the
authenticated user is allowed to access the requested object.
