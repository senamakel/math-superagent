#!/bin/bash
cd /workspace && timeout 120 python3 code/refute/g_balance_check.py 2>&1 | tee code/out/g_balance_check.captured.txt; echo EXIT_CODE=$?
