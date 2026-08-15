#!/bin/bash
cd /workspace && timeout 300 python3 code/grounding_shifting_test.py 2>&1 | tee code/out/grounding_shifting.captured.txt; echo EXIT=$?
