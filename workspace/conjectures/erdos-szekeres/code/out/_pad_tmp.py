import subprocess, sys, os
r = subprocess.run([sys.executable, "code/out/transversal_adjudicate.py"],
                   capture_output=True, text=True, cwd="/workspace")
print(r.stdout)
print(r.stderr, file=sys.stderr)
print("EXIT:", r.returncode)
