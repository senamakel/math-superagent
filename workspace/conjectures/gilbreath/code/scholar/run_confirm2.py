import subprocess, os, sys
os.chdir("/workspace/code/scholar")
env = dict(os.environ)
env["PYTHONPATH"] = "/workspace/code:" + env.get("PYTHONPATH","")
r = subprocess.run([sys.executable, "confirm_contradiction.py"],
                   capture_output=True, text=True, env=env)
print(r.stdout)
print(r.stderr)
print("RC=", r.returncode)
