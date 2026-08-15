#!/bin/bash
cd /workspace/code
echo "=== chi_f independent check (frac_chro_verify) ==="
timeout 540 python3 lib/frac_chro_verify.py 2>&1 | tee out/frac_chro_verify.captured.txt
echo "EXIT_CODE=$?"
echo
echo "=== original frac_chro_calib (never executed until now) ==="
timeout 540 python3 frac_chro_calib.py 2>&1 | tee out/frac_chro_calib.captured.txt
echo "EXIT_CODE=$?"
