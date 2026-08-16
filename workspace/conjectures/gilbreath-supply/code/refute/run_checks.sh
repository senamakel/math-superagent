#!/bin/bash
cd /workspace
echo "=== run-telescope verify ==="
python3 code/gfold/g_run_telescope_verify.py 2>&1 | tail -20
echo ""
echo "=== refute_runtelescope ==="
python3 code/refute/refute_runtelescope.py 2>&1 | tail -30
