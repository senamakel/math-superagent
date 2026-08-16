#!/usr/bin/env python3
import subprocess, sys
r = subprocess.run([sys.executable, "code/refute/verify_meet_runtelescope.py"],
                   capture_output=True, text=True)
print(r.stdout)
if r.stderr:
    print("STDERR:", r.stderr)
