#!/bin/bash
cd /workspace
timeout 540 python3 code/out/independent_review_huang.py 2>&1 | tee code/out/independent_review_huang.captured.txt
echo EXIT_CODE=$?
