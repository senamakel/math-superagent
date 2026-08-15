#!/bin/bash
cd /workspace && timeout 300 python3 code/refute/break_old_universe.py 2>&1 | tee code/out/break_old_universe.captured.txt; echo EXIT_CODE=$?
