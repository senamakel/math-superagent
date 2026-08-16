import subprocess, sys, os
os.chdir("/workspace")
r = subprocess.run([sys.executable, "code/refute/_go_uni.py"], capture_output=True, text=True)
print("OUT:\n", r.stdout)
print("ERR:\n", r.stderr[-2000:] if r.stderr else "")
