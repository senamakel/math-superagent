#!/usr/bin/env python3
import subprocess
r = subprocess.run([sys.executable,"/workspace/code/refute/weighted_excess_check.py"], capture_output=True, text=True)
print(r.stdout)
