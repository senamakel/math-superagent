#!/usr/bin/env bash
cd /workspace
timeout 540 python3 code/out/reproduce_A080839.py 2>&1 | tee code/out/reproduce_A080839.captured.txt; echo EXIT_CODE=$?
