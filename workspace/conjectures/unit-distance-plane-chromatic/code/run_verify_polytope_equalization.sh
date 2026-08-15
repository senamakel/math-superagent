#!/bin/bash
cd /workspace
timeout 120 python3 code/verify_polytope_equalization.py 2>&1 | tee code/out/verify_polytope_equalization.captured.txt
echo "EXIT_CODE=$?"
