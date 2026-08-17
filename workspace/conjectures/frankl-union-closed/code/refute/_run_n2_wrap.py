import subprocess, sys, os
# run the n=2 coupling check from its own dir so relative imports work
r = subprocess.run([sys.executable, "/workspace/code/refute/_run_n2_exec.py"],
                   capture_output=True, text=True, cwd="/workspace/code/refute")
print(r.stdout)
if r.returncode != 0:
    print("EXIT", r.returncode)
if r.stderr.strip():
    print("STDERR:", r.stderr[:4000])
