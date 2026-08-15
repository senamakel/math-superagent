import subprocess, sys
r = subprocess.run([sys.executable, "code/refute/_up.py"],
                   capture_output=True, text=True, timeout=900)
print(r.stdout[-5000:])
if r.stderr: print("STDERR:", r.stderr[-2000:])
