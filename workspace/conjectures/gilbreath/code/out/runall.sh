#!/usr/bin/env bash
cd /workspace
echo "== RUNNER1 =="
timeout 540 python3 code/out/runner1.py 2>&1 | tee code/out/runner1.captured.txt; echo "EXIT=$?"
echo "== RUNNER2 =="
timeout 540 python3 code/out/runner2.py 2>&1 | tee code/out/runner2.captured.txt; echo "EXIT=$?"
echo "== RUNNER3 =="
timeout 540 python3 code/out/runner3.py 2>&1 | tee code/out/runner3.captured.txt; echo "EXIT=$?"
