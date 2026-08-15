import subprocess, sys
r2 = subprocess.run([sys.executable, "code/run_refute_kernel_independent.py"], capture_output=True, text=True, timeout=300)
print("=== independent ===")
print(r2.stdout); print(r2.stderr); print("EXIT", r2.returncode)
