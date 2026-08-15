import subprocess, sys
r = subprocess.run([sys.executable, "code/refute/run_current_state.py"],
                   capture_output=True, text=True, timeout=600)
print(r.stdout)
if r.stderr: print("STDERR:", r.stderr[-3000:])
