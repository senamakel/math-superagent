import subprocess, os
os.chdir("/workspace/code/scholar")
r = subprocess.run(["bash", "exec_confirm.sh"], capture_output=True, text=True)
print(r.stdout)
print(r.stderr)
print("RC=", r.returncode)
