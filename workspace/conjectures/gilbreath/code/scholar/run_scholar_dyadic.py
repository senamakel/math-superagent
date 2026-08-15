#!/usr/bin/env python3
"""Run scholar_dyadic_collapse_check.py, capture output."""
import subprocess, sys, time
t0 = time.time()
r = subprocess.run([sys.executable, "scholar_dyadic_collapse_check.py"],
                   capture_output=True, text=True, cwd="/workspace/code/scholar")
print("STDOUT:\n" + r.stdout)
print("STDERR:\n" + r.stderr)
print("EXIT_CODE=%d  time=%.1fs" % (r.returncode, time.time()-t0))
