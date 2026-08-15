#!/bin/bash
echo "=== R-intruder-4-always searches ==="
timeout 500 python3 code/refute/run_intruder4_searches.py 2>&1
echo "EXIT=$?"
echo
echo "=== R-carved-gap24 exhaustive (free gaps <=22 in {2,4}) ==="
timeout 500 python3 code/refute/run_carved24_big.py 2>&1
echo "EXIT=$?"
