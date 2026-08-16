import subprocess, sys, os
os.chdir("/workspace")
r = subprocess.run([sys.executable, "code/refute/check_parseval_uniform.py"], capture_output=True, text=True)
print(r.stdout)
print("ERR", r.stderr[-2000:] if r.stderr else "")
