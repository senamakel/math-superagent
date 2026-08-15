import subprocess
r = subprocess.run(["python3","/workspace/code/refute/weighted_excess_check.py"], capture_output=True, text=True)
print(r.stdout)
