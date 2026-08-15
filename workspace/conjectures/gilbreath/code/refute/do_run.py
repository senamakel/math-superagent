#!/usr/bin/env python3
import subprocess
r = subprocess.run(["bash","/workspace/code/refute/exec_refute_wp.sh"], capture_output=True, text=True)
print(r.stdout)
print(r.stderr)
