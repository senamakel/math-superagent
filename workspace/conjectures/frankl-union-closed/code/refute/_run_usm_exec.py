#!/usr/bin/env python3
"""Run the correct upper-semimodular verifier (intersection-closed enumeration)
on m = 1..4 to establish the baseline small-case coverage, and capture output."""
import subprocess, sys, os
r = subprocess.run([sys.executable, "/workspace/code/refute/_run_usm.py"],
                   capture_output=True, text=True, cwd="/workspace/code/refute")
print(r.stdout)
if r.returncode != 0:
    print("EXIT", r.returncode)
if r.stderr.strip():
    print("STDERR:", r.stderr[:3000])
