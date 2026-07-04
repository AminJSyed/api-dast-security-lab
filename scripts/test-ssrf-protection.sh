#!/usr/bin/env bash

set -euo pipefail

BASE_URL="${BASE_URL:-http://localhost:8010}"

echo "Test 1: No token should return 401"
curl -s -o /dev/null -w "%{http_code}\n" \
  -X POST "$BASE_URL/fetch-url" \
  -H "Content-Type: application/json" \
  -d '{"url":"http://93.184.216.34/api"}'

echo "Test 2: Public IP with token should return 200"
curl -s -o /dev/null -w "%{http_code}\n" \
  -X POST "$BASE_URL/fetch-url" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer token-amin" \
  -d '{"url":"http://93.184.216.34/api"}'

echo "Test 3: Localhost should return 400"
curl -s -o /dev/null -w "%{http_code}\n" \
  -X POST "$BASE_URL/fetch-url" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer token-amin" \
  -d '{"url":"http://localhost:8010/health"}'

echo "Test 4: Loopback IP should return 400"
curl -s -o /dev/null -w "%{http_code}\n" \
  -X POST "$BASE_URL/fetch-url" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer token-amin" \
  -d '{"url":"http://127.0.0.1:8000/admin"}'

echo "Test 5: AWS metadata IP should return 400"
curl -s -o /dev/null -w "%{http_code}\n" \
  -X POST "$BASE_URL/fetch-url" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer token-amin" \
  -d '{"url":"http://169.254.169.254/latest/meta-data/"}'

echo "Test 6: GCP metadata host should return 400"
curl -s -o /dev/null -w "%{http_code}\n" \
  -X POST "$BASE_URL/fetch-url" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer token-amin" \
  -d '{"url":"http://metadata.google.internal/computeMetadata/v1/"}'
