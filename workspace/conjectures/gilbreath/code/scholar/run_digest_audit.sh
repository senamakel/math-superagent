#!/usr/bin/env bash
# Scholar digest audit — pairing full sources to digests.
cd /workspace && timeout 60 python3 code/scholar/digest_audit.py 2>&1 | tee code/scholar/digest_audit.captured.txt
echo EXIT_CODE=$?
