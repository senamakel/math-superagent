import subprocess, sys, os
os.chdir("/workspace")
r = subprocess.run([sys.executable, "code/refute/_run_parseval_uniform2.py"], capture_output=True, text=True)
print(r.stdout)
print("ERR", r.stderr[-2000:])
