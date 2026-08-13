#!/usr/bin/env bash
cd /workspace
echo "== RUNNER1 (C1 all-cells + intruder, C2 identity) =="
timeout 540 python3 code/out/runner1.py 2>&1 | tee code/out/runner1.captured.txt; echo "EXIT=$?"
echo "== RUNNER2 (C1 universality random + C3 restricted) =="
timeout 540 python3 code/out/runner2.py 2>&1 | tee code/out/runner2.captured.txt; echo "EXIT=$?"
echo "== RUNNER3 (C1 all-cells standalone) =="
timeout 540 python3 code/out/runner3.py 2>&1 | tee code/out/runner3.captured.txt; echo "EXIT=$?"
