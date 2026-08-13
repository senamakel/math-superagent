#!/usr/bin/env python3
"""Run the mod-6 claim verification with a bounded timeout, capturing output."""
import subprocess, sys, os

cmd = [sys.executable, "verify_mod6_claims.py"]
env = dict(os.environ)
try:
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=300, cwd=os.path.dirname(os.path.abspath(__file__)), env=env)
    print(r.stdout)
    print("STDERR:", r.stderr[-2000:] if r.stderr else "(none)")
    print("EXIT_CODE:", r.returncode)
except subprocess.TimeoutExpired:
    print("TIMEOUT after 300s")