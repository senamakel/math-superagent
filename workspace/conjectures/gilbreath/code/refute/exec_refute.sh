#!/usr/bin/env bash
set -u
cd /workspace
bash code/refute/run_refute.sh 2>&1 | tee code/refute/refute_attempt.captured.txt
