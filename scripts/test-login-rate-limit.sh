#!/usr/bin/env bash

set -euo pipefail

BASE_URL="${BASE_URL:-http://localhost:8010}"

echo "Restarting API to reset in-memory counters"
docker compose restart api >/dev/null

sleep 2

echo "Testing login rate limit"
echo

for i in 1 2 3 4; do
  echo "Failed login attempt $i"

  curl -s -o /dev/null -w "%{http_code}\n" \
    -X POST "$BASE_URL/login" \
    -H "Content-Type: application/json" \
    -d '{"username":"amin","password":"wrong"}'
done

echo
echo "Expected result:"
echo "Attempt 1: 401"
echo "Attempt 2: 401"
echo "Attempt 3: 401"
echo "Attempt 4: 429"
