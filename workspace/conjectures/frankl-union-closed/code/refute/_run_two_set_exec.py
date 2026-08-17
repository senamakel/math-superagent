import subprocess, sys
r = subprocess.run([sys.executable, "/workspace/code/refute/two_set_strong_check.py"],
                   capture_output=True, text=True)
print(r.stdout)
if r.returncode != 0:
    print("EXIT", r.returncode)
if r.stderr.strip():
    print("STDERR:", r.stderr[:3000])
