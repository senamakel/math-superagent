#!/bin/bash
cd /workspace
timeout 540 python3 code/run_refute.py 2>&1
echo EXIT_CODE=$?
