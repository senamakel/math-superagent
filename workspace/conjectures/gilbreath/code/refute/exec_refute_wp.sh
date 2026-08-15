#!/bin/bash
cd /workspace/code/refute
echo "=== weighted_excess_check.py ==="
python3 weighted_excess_check.py 2>&1 | tee /workspace/code/out/weighted_excess_refuted.captured.txt
echo "EXIT=$?"
echo ""
echo "=== weighted_excess_potential.py ==="
python3 weighted_excess_potential.py 2>&1 | tee /workspace/code/out/weighted_excess_spike.captured.txt
echo "EXIT=$?"
