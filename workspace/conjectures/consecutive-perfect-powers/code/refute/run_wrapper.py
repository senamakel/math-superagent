import os, subprocess, sys
os.chdir("/workspace/code/refute")
r = subprocess.run(["bash", "run.sh"], capture_output=True, text=True)
print(r.stdout)
if r.stderr:
    print("STDERR:", r.stderr[-3000:])
sys.exit(r.returncode)
