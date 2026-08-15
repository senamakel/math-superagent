#!/bin/bash
cd /workspace
timeout 120 python3 code/out/check_oeis_vs_f.py 2>&1 | tee code/out/check_oeis_vs_f.captured.txt
echo EXIT_CODE=$?
