#!/bin/bash
cd /workspace
echo "=== delarte LP ==="
python3 code/out/delsarte_lp.py 2>&1 | tee code/out/delsarte_lp.captured.txt
echo "EXIT=$?"
echo "=== clifford extremal check ==="
python3 code/out/check_clifford_extremal.py 2>&1 | tee code/out/check_clifford_extremal.captured.txt
echo "EXIT=$?"
