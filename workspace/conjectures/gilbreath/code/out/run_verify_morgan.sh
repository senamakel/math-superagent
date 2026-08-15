#!/bin/bash
cd /workspace && timeout 120 python3 code/out/verify_morgan_corridor.py 2>&1 | tee /workspace/code/out/verify_morgan_corridor.captured.txt
echo "EXIT_CODE=$?"
