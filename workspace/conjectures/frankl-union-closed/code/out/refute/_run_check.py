import subprocess, sys
r = subprocess.run([sys.executable, "/workspace/code/out/refute/check_three_set_model.py"],
                   capture_output=True, text=True, cwd="/workspace")
print(r.stdout)
print("STDERR:", r.stderr)
