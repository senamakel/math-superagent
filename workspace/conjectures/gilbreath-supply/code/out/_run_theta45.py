import subprocess, sys, os
r = subprocess.run([sys.executable, '/workspace/code/out/theta45_fit.py'], capture_output=True, text=True)
print(r.stdout)
print(r.stderr)
