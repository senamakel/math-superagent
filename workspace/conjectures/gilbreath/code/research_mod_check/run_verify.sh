#!/bin/sh
# Run the mod-6 claim verification with a hard timeout; capture output.
cd "$(dirname "$0")"
timeout 300 python3 verify_mod6_claims.py 2>&1 | tee mod6_verify.captured.txt
echo "EXIT_CODE=$?"