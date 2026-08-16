#!/usr/bin/env python3
"""Run the exact fold-distance-enumerator adversarial check and capture output."""
import subprocess, sys
p = "code/refute/fold_distance_enumerator_on.py"
out = subprocess.run([sys.executable, p], capture_output=True, text=True)
print(out.stdout)
print(out.stderr)
