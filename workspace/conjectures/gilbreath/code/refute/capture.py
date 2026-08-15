#!/usr/bin/env python3
import subprocess, sys, os
# Run the two decisive scripts and capture to a file
for f in ["weighted_excess_check.py", "weighted_excess_potential.py"]:
    path = os.path.join("/workspace/code/refute", f)
    print("#"*70)
    print("#", f)
    print("#"*70)
    r = subprocess.run(["python3", path], capture_output=True, text=True)
    print(r.stdout)
    if r.returncode != 0:
        print("STDERR:", r.stderr)
        print("RC:", r.returncode)
