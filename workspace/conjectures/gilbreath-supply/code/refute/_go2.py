import subprocess, sys, os
os.chdir("/workspace")
r = subprocess.run([sys.executable, "code/refute/_exec_parseval.py"], capture_output=True, text=True)
print(r.stdout)
print("ERR", r.stderr[-3000:])
