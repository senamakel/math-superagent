#!/usr/bin/env python3
"""Driver: run the fast refuter checks to ground the current state of the
three open candidates before attacking one."""
import subprocess, sys, os

BASE = "/workspace/code"
def run(rel, cap):
    p = subprocess.run([sys.executable, os.path.join(BASE, rel)],
                       capture_output=True, text=True)
    print(f"===== {rel} (exit {p.returncode}) =====")
    print(p.stdout[-2500:])
    if p.stderr:
        print("STDERR:", p.stderr[-800:])
    print()

run("out/liu_c3_objective_indep.py", "liu_c3_repro")
run("refute/coupling_half_n1_check.py", "n1")
run("refute/two_set_strong_check.py", "two_set")
