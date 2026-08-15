#!/usr/bin/env python3
import subprocess, sys
for f in ["check_tptp_model.py", "decode_model.py"]:
    print("="*30, f)
    r = subprocess.run([sys.executable, f"/workspace/code/refute/{f}"],
                       capture_output=True, text=True, cwd="/workspace/code")
    print(r.stdout)
    if r.stderr: print("STDERR:", r.stderr)
