#!/usr/bin/env bash
cd /workspace
timeout 540 python3 code/out/verify_ramification.py 3 5 7 11 13 17 19 23 2>&1 | tee code/out/verify_ramification.captured.txt; echo EXIT_CODE=$?
