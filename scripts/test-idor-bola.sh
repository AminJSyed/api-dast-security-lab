#!/usr/bin/env bash

set -euo pipefail

BASE_URL="${BASE_URL:-http://localhost:8010}"

echo "Test 1: No token should return 401"
curl -i "$BASE_URL/booking/1001"

echo
echo "Test 2: Amin can access booking 1001"
curl -i "$BASE_URL/booking/1001" \
  -H "Authorization: Bearer token-amin"

echo
echo "Test 3: Amin cannot access booking 1002"
curl -i "$BASE_URL/booking/1002" \
  -H "Authorization: Bearer token-amin"

echo
echo "Test 4: Test user can access booking 1002"
curl -i "$BASE_URL/booking/1002" \
  -H "Authorization: Bearer token-test"
