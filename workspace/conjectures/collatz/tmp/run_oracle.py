import subprocess, sys
r = subprocess.run([sys.executable, "/workspace/code/cycles/run_oracle.py"],
                   capture_output=True, text=True, timeout=120)
print("STDOUT:\n", r.stdout)
print("STDERR:\n", r.stderr)
print("rc:", r.returncode)
