import subprocess, sys
r = subprocess.run([sys.executable, '/workspace/code/out/theta45_verify.py'], capture_output=True, text=True)
print(r.stdout)
if r.stderr: print("STDERR:", r.stderr[:4000])
