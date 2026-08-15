#!/usr/bin/env python3
"""Run the Lipschitz-excess Lyapunov first-step oracle check."""
import subprocess, sys
cmd = ["timeout", "300", "python3", "research_lipschitz_excess_check.py", "200", "2000000"]
r = subprocess.run(cmd, capture_output=True, text=True, cwd="/workspace/code/out")
print(r.stdout)
print(r.stderr)
print("EXIT", r.returncode)
