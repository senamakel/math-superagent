#!/usr/bin/env python3
"""Run the minimal k-1 zero-bound oracle; prints output. Used by the host when
executing code/refute/center_ideal_kminus1_oracle.py directly."""
import os, subprocess, sys
os.chdir("/workspace")
cmd = [sys.executable, "code/refute/center_ideal_kminus1_oracle.py"]
p = subprocess.run(cmd, capture_output=True, text=True)
print(p.stdout)
if p.returncode != 0:
    print("EXIT", p.returncode)
    print(p.stderr[-4000:])
