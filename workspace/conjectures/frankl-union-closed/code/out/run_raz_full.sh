#!/bin/sh
cd /workspace && PYTHONPATH=/workspace/code python3 code/out/verify/run_raz_full.py > code/out/verify/run_raz_full.captured.txt 2>&1
echo "exit=$?"
cat code/out/verify/run_raz_full.captured.txt
