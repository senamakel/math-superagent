import subprocess, sys, os
os.chdir("/workspace")
r = subprocess.run([sys.executable, "code/refute/_run_uni.py"], capture_output=True, text=True)
print(r.stdout)
print("ERR", r.stderr[-2000:] if r.stderr else "")
