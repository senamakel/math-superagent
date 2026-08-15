import subprocess, sys, os
env = dict(os.environ)
# run the shell script directly via bash in workspace
r = subprocess.run(["bash", "code/out/run_oeis_check.sh"], capture_output=True, text=True, cwd="/workspace")
print("STDOUT:\n", r.stdout)
print("STDERR:\n", r.stderr)
print("RC:", r.returncode)
