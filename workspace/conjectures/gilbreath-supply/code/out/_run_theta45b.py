import subprocess, sys
r = subprocess.run([sys.executable, '/workspace/code/out/_run_theta45.py'], capture_output=True, text=True)
print(r.stdout)
if r.stderr: print("STDERR:", r.stderr[:3000])
