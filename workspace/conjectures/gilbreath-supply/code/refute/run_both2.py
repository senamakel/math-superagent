#!/usr/bin/env python3
"""Execute code in /workspace/code/refute files via subprocess."""
import subprocess, sys
root = "/workspace"
for f in ["code/refute/kstar_resolve.py", "code/refute/verify_witness_n8.py"]:
    print("=" * 70)
    r = subprocess.run([sys.executable, f], capture_output=True, text=True,
                       cwd=root)
    print(r.stdout)
    if r.stderr:
        print("STDERR:", r.stderr)
