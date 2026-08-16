#!/usr/bin/env python3
import subprocess, sys, io
# capture and print
r = subprocess.run([sys.executable, "code/refute/fold_distance_enumerator_on.py"],
                   capture_output=True, text=True)
print(r.stdout)
if r.stderr:
    print("STDERR:", r.stderr)
