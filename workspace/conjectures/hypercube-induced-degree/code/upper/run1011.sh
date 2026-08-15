#!/bin/bash
cd /workspace/code/upper
timeout 540 python3 upper_build.py 10 11 2>&1 | tee /workspace/code/out/upper_build_n1011.captured.txt
echo "EXIT=$?"
