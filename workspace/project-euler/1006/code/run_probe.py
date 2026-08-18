import subprocess, sys
r = subprocess.run([sys.executable, "code/probe_M.py"], capture_output=True, text=True, cwd="/workspace")
print(r.stdout)
print(r.stderr)
