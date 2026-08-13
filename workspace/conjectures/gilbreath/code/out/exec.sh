#!/usr/bin/env bash
cd /workspace
echo "== FINAL_RUN =="
timeout 540 python3 code/out/final_run.py 2>&1 | tee code/out/final_run.captured.txt; echo "EXIT=$?"
echo "== FINAL_RUN2 =="
timeout 540 python3 code/out/final_run2.py 2>&1 | tee code/out/final_run2.captured.txt; echo "EXIT=$?"
