#!/usr/bin/env python3
import subprocess, sys, os
r = subprocess.run([sys.executable, "code/scholar_verify_oeis_mycielski.py"],
                   capture_output=True, text=True, cwd="/workspace")
print(r.stdout)
print(r.stderr)
print("EXIT=", r.returncode)
