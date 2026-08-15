#!/bin/bash
cd /workspace
timeout 120 python3 code/verify_huang_signing.py 2>&1 | tee code/out/verify_huang_signing.captured.txt
echo EXIT_CODE=$?
