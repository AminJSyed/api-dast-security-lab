#!/usr/bin/env bash

set -euo pipefail

API_PORT="${API_PORT:-8010}"
AUTH_TOKEN="${AUTH_TOKEN:-token-amin}"
REPORT_NAME="${1:-zap-auth-api-report.html}"

TARGET_URL="http://host.docker.internal:${API_PORT}/openapi.json"

DOCKER_ARGS=()

if [ "${CI:-}" = "true" ]; then
  DOCKER_ARGS+=(
    --add-host
    host.docker.internal:host-gateway
  )
fi

docker run --rm -t \
  "${DOCKER_ARGS[@]}" \
  -v "$(pwd):/zap/wrk:rw" \
  zaproxy/zap-stable zap-api-scan.py \
  -t "$TARGET_URL" \
  -f openapi \
  -r "$REPORT_NAME" \
  -z "-config replacer.full_list(0).description=auth-header \
      -config replacer.full_list(0).enabled=true \
      -config replacer.full_list(0).matchtype=REQ_HEADER \
      -config replacer.full_list(0).matchstr=Authorization \
      -config replacer.full_list(0).regex=false \
      -config replacer.full_list(0).replacement=Bearer\ ${AUTH_TOKEN}"
