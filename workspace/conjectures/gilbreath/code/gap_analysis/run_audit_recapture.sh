#!/bin/bash
# Re-capture reduction_audit.py output to a NEW file (not clobbering the
# stale .captured.txt that holds the defective verdict line).
cd /workspace && timeout 540 python3 code/gap_analysis/reduction_audit.py 2>&1 | tee code/out/reduction_audit.captured2.txt; echo EXIT_CODE=$?
