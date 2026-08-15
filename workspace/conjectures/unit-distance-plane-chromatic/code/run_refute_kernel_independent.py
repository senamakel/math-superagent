#!/usr/bin/env python3
"""Run the independent brute-force check and capture output."""
import subprocess, sys
p = subprocess.run([sys.executable, "code/refute_kernel_independent.py"],
                   capture_output=True, text=True, timeout=200)
out = p.stdout + p.stderr
open("code/out/refute_kernel_independent.captured.txt", "w").write(out)
print(out)
print("EXIT=", p.returncode)
