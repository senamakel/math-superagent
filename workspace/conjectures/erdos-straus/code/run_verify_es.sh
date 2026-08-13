#!/bin/bash
cd /workspace
timeout 540 python3 code/es_structure/verify_es_structure.py 2>&1 | tee code/out/es_structure.verify.txt
echo "EXIT_CODE=${PIPESTATUS[0]}"