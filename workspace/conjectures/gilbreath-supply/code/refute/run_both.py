#!/usr/bin/env python3
"""Run the K* resolution and witness verification; print everything."""
import subprocess, sys
for f in ["code/refute/kstar_resolve.py", "code/refute/verify_witness_n8.py"]:
    print("="*70)
    r = subprocess.run([sys.executable, f], capture_output=True, text=True,
                       cwd="/workspace")
    print(r.stdout)
    if r.stderr:
        print("STDERR:", r.stderr)
