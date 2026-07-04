#!/usr/bin/env bash

set -euo pipefail

API_PORT="${API_PORT:-8010}"
REPORT_NAME="${1:-zap-api-report.html}"

TARGET_URL="http://host.docker.internal:${API_PORT}/openapi.json"

docker run --rm -t \
  -v "$(pwd):/zap/wrk:rw" \
  zaproxy/zap-stable zap-api-scan.py \
  -t "$TARGET_URL" \
  -f openapi \
  -r "$REPORT_NAME"
