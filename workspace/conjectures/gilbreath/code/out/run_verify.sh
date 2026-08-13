#!/usr/bin/env bash
cd /workspace
echo "=== verify_three.py ==="
timeout 540 python3 code/out/verify_three.py 2>&1 | tee code/out/verify_three.captured.txt; echo "EXIT=$?"
echo "=== verify_three_b.py ==="
timeout 540 python3 code/out/verify_three_b.py 2>&1 | tee code/out/verify_three_b.captured.txt; echo "EXIT=$?"
