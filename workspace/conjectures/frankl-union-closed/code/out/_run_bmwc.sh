#!/bin/bash
cd /workspace
python3 code/out/bm_weight_criterion_verify.py > code/out/bm_weight_criterion.captured.txt 2>&1
cat code/out/bm_weight_criterion.captured.txt
