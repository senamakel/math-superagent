#!/usr/bin/env python3
import subprocess, sys
cmd = ["python3", "code/scholar/threshold_focus.py"]
out = subprocess.run(cmd, capture_output=True, text=True, timeout=3600)
print(out.stdout)
if out.stderr:
    print("STDERR tail:", out.stderr[-4000:])
print("exit:", out.returncode)
