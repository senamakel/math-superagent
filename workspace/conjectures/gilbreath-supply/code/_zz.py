import subprocess, sys, os
os.chdir("/workspace/code")
r = subprocess.run([sys.executable, "_go_parseval_direct.py"], capture_output=True, text=True)
print("OUT:\n", r.stdout)
print("ERR:\n", r.stderr[-2000:] if r.stderr else "")
