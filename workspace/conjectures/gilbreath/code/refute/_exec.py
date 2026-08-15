#!/usr/bin/env python3
import sys, subprocess, os
os.chdir('/workspace')
r = subprocess.run([sys.executable, 'code/refute/leftmost_decides.py', '5', '45'],
                   capture_output=True, text=True, timeout=540)
with open('code/out/refute_leftmost_decides.captured.txt', 'w') as f:
    f.write(r.stdout)
print(r.stdout)
print("STDERR:", (r.stderr or "")[-2000:])
