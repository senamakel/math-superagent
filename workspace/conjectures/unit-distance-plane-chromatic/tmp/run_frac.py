import subprocess
r = subprocess.run(["bash", "/workspace/code/run_frac_chro.sh"], capture_output=True, text=True, timeout=720)
print(r.stdout)
if r.stderr: print("STDERR", r.stderr)
