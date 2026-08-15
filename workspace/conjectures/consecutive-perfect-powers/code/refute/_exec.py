import os, subprocess, sys
os.chdir("/workspace/code/refute")
r = subprocess.run([sys.executable, "run_hminus_exact.py"], capture_output=True, text=True)
print("STDOUT:\n", r.stdout)
if r.stderr:
    print("STDERR:\n", r.stderr[-3000:])
