#!/usr/bin/env python3
"""Run check_candidate_premises.py and capture output."""
import subprocess, sys, os
cmd = [sys.executable, "code/out/check_candidate_premises.py"]
r = subprocess.run(cmd, capture_output=True, text=True)
print(r.stdout)
print(r.stderr)
