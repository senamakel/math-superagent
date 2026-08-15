#!/bin/bash
cd /workspace
timeout 120 python3 code/lib/gilbreath.py 2>&1 | tee code/out/oracle_selfcheck_scholar.captured.txt
echo EXIT_CODE=$?
