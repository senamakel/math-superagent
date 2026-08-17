#!/bin/bash
cd /workspace && python3 code/refute/check_regularity.py 7 | tee code/out/refute_check_regularity.captured.txt
