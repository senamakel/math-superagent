import sys, subprocess, os
# Run the off-by-one check and capture
r = subprocess.run([sys.executable, "code/scholar/check_offbyone.py"],
                   capture_output=True, text=True, cwd="/workspace")
print(r.stdout)
print(r.stderr, file=sys.stderr)
print("exit", r.returncode)
