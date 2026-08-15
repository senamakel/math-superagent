import subprocess, os
os.chdir("/workspace/code/scholar")
r = subprocess.run(["bash", "confirm_exec2.sh"], capture_output=True, text=True)
print(r.stdout)
