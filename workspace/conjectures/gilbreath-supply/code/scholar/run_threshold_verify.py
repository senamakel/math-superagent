#!/usr/bin/env python3
"""Run the third-pass threshold verification scripts and capture output."""
import subprocess, sys

targets = [
    ("code/scholar/threshold_limit_run.py", ["python3", "code/scholar/threshold_limit_run.py"]),
    ("code/verif/threshold_exact_mean_independent.py", ["python3", "code/verif/threshold_exact_mean_independent.py"]),
    ("code/scholar/threshold_verify_tail.py", ["python3", "code/scholar/threshold_verify_tail.py"]),
]

for name, cmd in targets:
    print("=" * 78)
    print("RUNNING:", name)
    print("=" * 78)
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=1800)
        print(out.stdout)
        if out.stderr:
            print("STDERR:", out.stderr[-3000:])
        print("exit:", out.returncode)
    except Exception as e:
        print("ERROR:", e)
