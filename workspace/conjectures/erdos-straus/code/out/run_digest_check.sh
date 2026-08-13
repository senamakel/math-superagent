#!/bin/bash
cd /workspace/code/out
python3 verify_digest_numeric_claims.py 2>&1 | tee verify_digest_numeric.captured.txt
echo EXIT_CODE=${PIPESTATUS[0]}
