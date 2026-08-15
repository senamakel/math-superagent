#!/usr/bin/env python3
"""Run the Mycielski kernel refutation and capture output."""
import subprocess, sys
p = subprocess.run([sys.executable, "code/refute_mycielski_kernel.py"],
                   capture_output=True, text=True, timeout=540)
out = p.stdout + p.stderr
open("code/out/refute_kernel.captured.txt", "w").write(out)
print(out)
print("EXIT=", p.returncode)
