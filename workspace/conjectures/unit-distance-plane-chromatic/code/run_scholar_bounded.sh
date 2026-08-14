#!/usr/bin/env bash
# Bound every compute run. Scholar checks are tiny (exact integer graphs).
cd /workspace && timeout 120 python3 code/run_scholar_checks.py 2>&1 | tee /tmp/scholar_run.txt; echo "EXIT_CODE=$?"