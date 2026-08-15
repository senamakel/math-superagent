#!/bin/sh
cd /workspace && timeout 300 python3 code/out/attack4.py 2>&1 | tee code/out/attack_torus_6col.captured.txt; echo EXIT=$?
