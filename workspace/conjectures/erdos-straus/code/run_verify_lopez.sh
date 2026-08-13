#!/usr/bin/env bash
cd /workspace && timeout 300 python3 code/verify_lopez_2521.py 2>&1 | tee code/out/verify_lopez_2521.captured.txt; echo EXIT_CODE=$?
