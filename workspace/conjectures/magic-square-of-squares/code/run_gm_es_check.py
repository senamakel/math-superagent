#!/usr/bin/env python3
"""Run the checks in gm_es_check.py"""
import subprocess, sys
sys.path.insert(0, '/workspace/code')  # noqa: E402  (dev-run only; module
# itself is imported from code/lib elsewhere per house style)
r = subprocess.run([sys.executable, '/workspace/code/gm_es_check.py'],
                   capture_output=True, text=True)
print(r.stdout)
if r.returncode != 0:
    print("STDERR:", r.stderr)
sys.exit(r.returncode)