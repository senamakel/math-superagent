#!/bin/bash
cd /workspace/code
echo "=== exact rational dual scan ==="
timeout 540 python3 scholar_verify_frac.py 2>&1 | tee out/scholar_verify_frac.captured.txt
echo "EXIT_CODE=$?"
echo "=== independent primal+dual (scipy highs, separate source) ==="
timeout 540 python3 run_verify_frac_indep.py 2>&1 | tee out/scholar_verify_frac_indep.captured.txt
echo "EXIT_CODE=$?"
