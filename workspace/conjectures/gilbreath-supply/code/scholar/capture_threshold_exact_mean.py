#!/usr/bin/env python3
"""Capture runner for code/scholar/threshold_exact_mean.py.

Runs the script (which imports lib.supply_fold) and writes stdout to a capture,
but only on exit 0 (temp-file-then-move; a failure leaves prior capture intact).
The exact-mean work is the scholar's verification of the pass's one computation.
"""
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET = os.path.join(HERE, "..", "out", "scholar_threshold_exact_mean.captured.txt")
SCRIPT = os.path.join(HERE, "threshold_exact_mean.py")

env = dict(os.environ)
# put /workspace/code on PYTHONPATH so `lib.supply_fold` resolves
code_root = os.path.abspath(os.path.join(HERE, ".."))
if "PYTHONPATH" in env:
    env["PYTHONPATH"] = code_root + os.pathsep + env["PYTHONPATH"]
else:
    env["PYTHONPATH"] = code_root

# header
header_lines = [
    "=" * 78,
    "sequence = weight-w binary strings over F2^n (all weights, exact)",
    "oracle   = exact closed-form mean (no sampling) + brute s_sos cross-check",
    "range    = n in {6..16 exhaustive cross-check; 32..1024 exact mean}",
    "=" * 78,
    "",
]

fd, tmp = tempfile.mkstemp(prefix="capture_", suffix=".tmp")
try:
    with os.fdopen(fd, "w") as f:
        f.write("\n".join(header_lines))
    with open(tmp, "a") as f:
        r = subprocess.run([sys.executable, SCRIPT], env=env, stdout=f, stderr=subprocess.STDOUT)
    if r.returncode != 0:
        os.remove(tmp)
        print(f"capture FAILED (exit {r.returncode}); prior capture preserved.")
        sys.exit(1)
    os.replace(tmp, TARGET)
    print(f"wrote {TARGET}")
except Exception:
    if os.path.exists(tmp):
        os.remove(tmp)
    raise
