import subprocess, sys
r1 = subprocess.run([sys.executable, "code/run_refute_kernel.py"], capture_output=True, text=True, timeout=600)
print("=== main refute ===")
print(r1.stdout); print(r1.stderr); print("EXIT", r1.returncode)
