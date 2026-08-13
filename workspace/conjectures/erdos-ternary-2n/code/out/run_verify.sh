#!/bin/bash
cd /workspace
timeout 300 python3 code/out/check_binomial_approach.py 2>&1 | tee code/out/check_binomial_approach.captured.txt
echo "EXIT_CODE=$?"
