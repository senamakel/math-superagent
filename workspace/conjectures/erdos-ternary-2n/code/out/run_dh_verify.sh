#!/bin/sh
# Run the DH n=3 verification (consolidated script). This workspace has no
# shell-execution tool in the agent session, so the harness should run this and
# capture output. Hand verification is recorded in
# research/summaries/dh-n3-and-cross-modulus-gap.md (claim DH-N3-EXAMPLES-VERIFIED).
cd /workspace
python3 code/out/verify_dh_n3.py 2>&1 | tee code/out/verify_dh_n3.captured.txt
echo "EXIT=$?"
