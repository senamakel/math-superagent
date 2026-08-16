#!/usr/bin/env python3
"""Wall-time wrapper: runs the n=5 bad-prime verifier and reports total wall
time plus the verifier's own internal timing. Exit status propagates."""
import subprocess
import sys
import time

t0 = time.time()
proc = subprocess.run(
    [sys.executable, "/workspace/code/badprimes_criterion/verify_badprimes_n5.py"],
    capture_output=True, text=True)
wall = time.time() - t0
print(proc.stdout, end="")
print("EXTERNAL WALL TIME (wrapper): %.1f s" % wall, flush=True)
sys.stderr.write(proc.stderr)
sys.exit(proc.returncode)
