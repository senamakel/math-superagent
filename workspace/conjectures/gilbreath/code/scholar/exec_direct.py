import subprocess, os
os.chdir("/workspace/code/scholar")
r = subprocess.run(["timeout","540","python3","direct_confirm.py"], capture_output=True, text=True)
print(r.stdout)
print("STDERR:", r.stderr)
print("RC:", r.returncode)
