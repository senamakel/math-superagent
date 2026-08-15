#!/bin/bash
timeout 540 python3 /workspace/research/independent_check_research.py 2>&1 | tee /workspace/code/out/independent_review_research.captured.txt
echo EXIT_CODE=$?
