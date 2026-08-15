#!/bin/bash
cd /workspace/code/upper
timeout 540 python3 upper_build.py 7 8 9 2>&1 | tee /workspace/code/out/upper_build_n789.captured.txt
echo "EXIT=$?"
