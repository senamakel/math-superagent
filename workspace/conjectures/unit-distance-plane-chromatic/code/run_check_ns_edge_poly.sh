#!/usr/bin/env bash
cd /workspace && timeout 60 python3 code/check_ns_edge_poly.py 2>&1 | tee code/out/check_ns_edge_poly.captured.txt; echo EXIT_CODE=$?
