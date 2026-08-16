#!/usr/bin/env python3
import subprocess, sys
name, cmd = "threshold_focus", ["python3", "code/scholar/threshold_focus.py"]
out = subprocess.run(cmd, capture_output=True, text=True, timeout=1800)
print(out.stdout)
if out.stderr:
    print("STDERR:", out.stderr[-4000:])
print("exit:", out.returncode)
