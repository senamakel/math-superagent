#!/bin/bash
cd /workspace
timeout 540 python3 /workspace/code/refute/leftmost_decides.py 5 40 2>&1 | tee /workspace/code/out/refute_leftmost_decides.captured.txt
echo EXIT_CODE=$?
