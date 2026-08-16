#!/usr/bin/env python3
"""Regenerate+verify the threshold-weight exponent capture, and run an
independent fit with error bar, testing against the fold's constants.
Runs the existing scripts via subprocess and reads their stdout."""

import subprocess, sys, os

def run_script(path, cwd="/workspace"):
    r = subprocess.run([sys.executable, path], cwd=cwd,
                       capture_output=True, text=True, timeout=1200)
    return r

# 1. Regenerate the missing capture from the library's own script
print("="*80)
print("RUN 1: extend_threshold_exponent.py  (derives extended weight table)")
r = run_script("/workspace/code/out/extend_threshold_exponent.py")
print(r.stdout)
if r.returncode != 0:
    print("STDERR:", r.stderr)

print("="*80)
print("RUN 2: run_threshold_fit.py  (regenerates threshold_exponent_fit.txt)")
r = run_script("/workspace/code/out/run_threshold_fit.py")
print(r.stdout)
if r.returncode != 0:
    print("STDERR:", r.stderr)
