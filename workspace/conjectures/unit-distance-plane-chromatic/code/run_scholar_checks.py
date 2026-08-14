#!/usr/bin/env python3
"""Run the scholar check harness and capture its output."""
import subprocess, sys, os

cmd = [sys.executable, "/workspace/code/check_scholar.py"]
res = subprocess.run(cmd, capture_output=True, text=True, cwd="/workspace")
out = res.stdout + res.stderr

with open("/workspace/code/out/scholar_checks.captured.txt", "w") as f:
    f.write(out)
    f.write(f"\nEXIT_CODE={res.returncode}\n")

print(out)
print(f"EXIT_CODE={res.returncode}")