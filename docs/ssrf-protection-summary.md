# SSRF Protection Scenario

## Objective

This scenario demonstrates basic Server-Side Request Forgery
protection for an API endpoint that accepts a user-provided URL.

The goal is to validate outbound URLs before the application makes
any server-side request.

## Risk

SSRF occurs when an attacker provides a URL and the server sends a
request to that destination.

This can allow attackers to reach internal services that are not
directly exposed to the internet.

Examples of risky targets:

- localhost
- 127.0.0.1
- private IP ranges
- link-local addresses
- cloud metadata services
- internal admin panels
- internal APIs

## Cloud Metadata Examples

AWS metadata endpoint:

169.254.169.254/latest/meta-data/

GCP metadata endpoint:

metadata.google.internal/computeMetadata/v1/

Azure metadata endpoint:

169.254.169.254/metadata/instance

## Remediation

The API validates the submitted URL before allowing it.

Validation checks:

1. Require authentication
2. Allow only http and https schemes
3. Require a hostname
4. Block known internal hostnames
5. Resolve hostname to IP addresses
6. Block non-public IP addresses
7. Disable the actual network fetch in this lab

## Validation Results

No token:

POST /fetch-url

Result:

401 Unauthorized

Public destination:

http://93.184.216.34/api

Result:

200 OK

Localhost:

http://localhost:8010/health

Result:

400 Bad Request

Loopback IP:

http://127.0.0.1:8000/admin

Result:

400 Bad Request

AWS metadata IP:

http://169.254.169.254/latest/meta-data/

Result:

400 Bad Request

GCP metadata host:

http://metadata.google.internal/computeMetadata/v1/

Result:

400 Bad Request

## Production Considerations

Application-level validation is useful, but it should not be the
only control.

Production systems should also use:

- Egress firewall rules
- Network policies
- Service mesh egress controls
- API gateway policies
- WAF rules
- Metadata service protections
- Least privilege IAM
- Monitoring and alerting for suspicious outbound traffic

## Key Learning

SSRF protection should use defense in depth.

Even if an application-level validation bypass occurs, network and
cloud-level controls should limit the blast radius.
