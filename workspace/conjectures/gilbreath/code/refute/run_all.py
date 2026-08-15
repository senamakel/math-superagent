#!/usr/bin/env python3
import subprocess
for f in ["weighted_excess_potential.py", "weighted_excess_quick.py", "weighted_excess_check.py"]:
    print("="*60)
    print("RUN", f)
    print("="*60)
    r = subprocess.run(["python3", f], capture_output=True, text=True)
    print(r.stdout)
    if r.returncode != 0:
        print("STDERR:", r.stderr)
