import subprocess
r = subprocess.run(["python3", "code/out/check_edge_zero_run.py", "20"], capture_output=True, text=True, timeout=600)
print(r.stdout)
print(r.stderr[-2000:] if r.stderr else "")
print("EXIT", r.returncode)
