#!/usr/bin/env python3
import subprocess, sys, os
os.chdir("/workspace")
r = subprocess.run([sys.executable, "code/scholar/descent_check.py"], capture_output=True, text=True)
print(r.stdout)
print(r.stderr)
print("EXIT", r.returncode)
