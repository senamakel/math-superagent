import os, subprocess, sys

base = "/workspace/code"
env = dict(os.environ)
env["PYTHONPATH"] = base + os.pathsep + env.get("PYTHONPATH", "")
r = subprocess.run(
    [sys.executable, "/workspace/code/out/bouchard_length_bound_check.py"],
    capture_output=True, text=True, env=env)
print(r.stdout)
if r.stderr:
    print("STDERR:")
    print(r.stderr)
print("exit", r.returncode)
