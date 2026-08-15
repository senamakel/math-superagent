#!/bin/bash
cd /workspace && timeout 540 python3 code/refute/dyadic_periodicity_test.py 2>&1 | tee code/out/dyadic_periodicity_test.captured.txt
echo EXIT_CODE=$?
