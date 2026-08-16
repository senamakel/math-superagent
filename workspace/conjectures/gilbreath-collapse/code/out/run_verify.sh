#!/bin/bash
cd /workspace && PYTHONPATH=/workspace/code python3 code/out/verify_multiset.py > code/out/verify_multiset.out 2>&1
echo "exit=$?"