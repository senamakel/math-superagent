#!/usr/bin/env python3
"""Run the exhaustive {2,4}-gap search to as large a width as feasible."""
import subprocess, time, sys

t0 = time.time()
r = subprocess.run([sys.executable, "exhaust_carved_gap24.py", "20"],
                   capture_output=True, text=True)
print("exit", r.returncode)
print(r.stdout)
print("STDERR:", r.stderr[-2000:] if r.stderr else "")
print(f"elapsed {time.time()-t0:.1f}s")
