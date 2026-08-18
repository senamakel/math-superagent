#!/usr/bin/env python3
import os, subprocess, sys
os.chdir("/workspace")
cmd = [sys.executable, "code/refute/bautin_membership_independent.py"]
p = subprocess.run(cmd, capture_output=True, text=True)
print(p.stdout)
if p.returncode != 0:
    print("EXIT", p.returncode)
    print(p.stderr[-4000:])
