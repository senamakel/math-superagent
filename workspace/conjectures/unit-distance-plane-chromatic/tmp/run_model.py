import subprocess, sys
r = subprocess.run([sys.executable, "/workspace/code/refute/check_tptp_model.py"],
                   capture_output=True, text=True, cwd="/workspace/code")
print(r.stdout)
if r.stderr: print("STDERR:", r.stderr)
