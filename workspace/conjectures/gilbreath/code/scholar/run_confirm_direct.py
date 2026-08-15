import os, sys, subprocess
os.chdir("/workspace/code/scholar")
py = sys.executable
script = "/workspace/code/scholar/confirm_contradiction.py"
r = subprocess.run([py, script], capture_output=True, text=True,
                   cwd="/workspace/code/scholar",
                   env={**os.environ, "PYTHONPATH": "/workspace/code"})
print(r.stdout)
print("STDERR:", r.stderr)
print("RC:", r.returncode)
