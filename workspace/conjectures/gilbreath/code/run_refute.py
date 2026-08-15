#!/usr/bin/env python3
import sys, subprocess, os
os.chdir('/workspace')
cmd = [sys.executable, '-c',
       "import sys; sys.path.insert(0,'/workspace/code'); from refute.leftmost_decides import main; main()",
       '5', '45']
r = subprocess.run(cmd, capture_output=True, text=True, timeout=540)
with open('code/out/refute_leftmost_decides.captured.txt','w') as f:
    f.write(r.stdout + "\n---\n" + r.stderr)
print(r.stdout)
print("STDERR tail:", (r.stderr or "")[-1000:])
