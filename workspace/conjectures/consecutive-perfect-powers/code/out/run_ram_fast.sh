#!/usr/bin/env bash
cd /workspace && timeout 540 python3 code/out/verify_ram_fast.py 2>&1 | tee code/out/verify_ram_fast.captured.txt; echo EXIT_CODE=$?