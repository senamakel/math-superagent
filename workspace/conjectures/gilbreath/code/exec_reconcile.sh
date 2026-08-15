#!/usr/bin/env bash
cd /workspace
timeout 300 python3 code/reconcile_lemma54_violations.py 2>&1 | tee code/out/reconcile_lemma54_violations.captured.txt
echo EXIT_CODE=$?
