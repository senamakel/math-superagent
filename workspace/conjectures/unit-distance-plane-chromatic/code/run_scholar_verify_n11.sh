#!/bin/bash
# NOT EXECUTED by the scholar (no program-execution tool in this role).
# Would run the C_11 re-derivation. See scholar_verify_n11.py header.
cd /workspace
timeout 540 python3 code/run_scholar_verify_n11.py 2>&1 | tee code/out/scholar_verify_n11.captured.txt
echo EXIT_CODE=$?
