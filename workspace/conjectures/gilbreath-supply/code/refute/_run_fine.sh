#!/bin/bash
cd /workspace
echo "=== FINE SPARSE PROBE (running min ratio) ==="
timeout 900 python3 code/refute/_fine_sparse_run.py 8192 2>&1 | tail -20
