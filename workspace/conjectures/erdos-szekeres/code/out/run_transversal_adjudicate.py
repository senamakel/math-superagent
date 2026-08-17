#!/usr/bin/env python3
"""Run the transversal-convexity adjudication and capture output."""
import subprocess, sys
cmd = [sys.executable, "code/out/transversal_adjudicate.py"]
r = subprocess.run(cmd, capture_output=True, text=True, cwd="/workspace")
print(r.stdout)
print(r.stderr, file=sys.stderr)
print("EXIT:", r.returncode)
