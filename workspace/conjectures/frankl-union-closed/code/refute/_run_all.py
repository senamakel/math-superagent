#!/usr/bin/env python3
"""Run every verification/analysis script under code/refute whose name is in
the list, capturing stdout.  Everything runs from this folder on PATH.
"""
import subprocess, sys, os
here = os.path.dirname(os.path.abspath(__file__))
scripts = [
    "coupling_half_n1_verify.py",
    "coupling_half_n1_check.py",
    "collapse_recheck.py",
]
for s in scripts:
    print("#"*72)
    print("#", s)
    print("#"*72)
    r = subprocess.run([sys.executable, os.path.join(here, s)],
                       capture_output=True, text=True)
    print(r.stdout)
    if r.returncode != 0:
        print("EXIT", r.returncode)
    if r.stderr.strip():
        print("STDERR:", r.stderr[:2000])
