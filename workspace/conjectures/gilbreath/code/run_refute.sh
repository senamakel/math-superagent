#!/bin/bash
cd /workspace
timeout 540 python3 code/run_refute.py
echo EXIT_CODE=$?
