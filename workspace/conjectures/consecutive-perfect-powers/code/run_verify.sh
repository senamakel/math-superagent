#!/usr/bin/env bash
cd /workspace
timeout 540 python3 code/out/verify_claims.py 2>&1 | tee code/out/verify_claims.captured.txt
echo EXIT_CODE=$?
