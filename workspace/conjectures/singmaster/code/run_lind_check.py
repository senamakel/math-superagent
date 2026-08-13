#!/usr/bin/env python3
"""Run the Lind index-alignment check and capture output."""
import subprocess, sys
p = subprocess.run([sys.executable, "check_lind_index_alignment.py"],
                   capture_output=True, text=True, cwd="/workspace/code")
print(p.stdout)
print(p.stderr, file=sys.stderr)
sys.exit(p.returncode)