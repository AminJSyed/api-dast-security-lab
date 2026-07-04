# Python Log Analysis Scenario

## Objective

This scenario demonstrates basic Python-based security log analysis.

The goal is to detect possible brute-force login behavior by counting
failed login attempts per IP address.

## Input

The script reads a sample login log file containing:

- Timestamp
- IP address
- Username
- Login status

Example:

2026-07-04T10:00:05Z 192.168.1.11 admin FAILED

## Detection Logic

The script performs these steps:

1. Read the log file line by line
2. Split each line into fields
3. Extract IP address and login status
4. Count failed logins per IP address
5. Print IPs where failed attempts meet or exceed the threshold

## Threshold

Current threshold:

3 failed attempts

## Example Result

Suspicious IP: 192.168.1.11

Failed attempts: 3

## Security Relevance

This type of automation can help detect:

- Brute-force attacks
- Credential stuffing attempts
- Suspicious authentication behavior
- Repeated failed access attempts

## Key Learning

Python dictionaries are useful for counting security events such as
failed logins per IP, requests per user, or alerts per severity.
