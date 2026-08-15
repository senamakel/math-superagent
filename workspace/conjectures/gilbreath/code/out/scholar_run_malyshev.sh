#!/usr/bin/env bash
cd /workspace && timeout 540 python3 code/scholar/verify_malyshev_bound.py 2>&1 | tee code/out/verify_malyshev_bound.captured.txt; echo "EXIT_CODE=$?"
