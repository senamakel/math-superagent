#!/bin/bash
cd /workspace
echo "=== refute_runtelescope ==="
python3 code/refute/refute_runtelescope.py 2>&1 | tail -30
