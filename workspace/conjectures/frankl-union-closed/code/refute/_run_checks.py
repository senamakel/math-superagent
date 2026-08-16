#!/usr/bin/env python3
"""Run the two coupling-half verification scripts in code/refute.
"""
import subprocess, sys, os
here = os.path.dirname(os.path.abspath(__file__))
for script in ["coupling_half_n1_verify.py", "coupling_half_n1_check.py"]:
    print("#"*70)
    print("#", script)
    print("#"*70)
    r = subprocess.run([sys.executable, os.path.join(here, script)], capture_output=True, text=True)
    print(r.stdout)
    if r.returncode != 0 or r.stderr:
        print("STDERR:", r.stderr)
