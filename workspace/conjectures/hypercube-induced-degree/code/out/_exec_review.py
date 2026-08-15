import subprocess, sys
r = subprocess.run(["bash", "code/out/run_review.sh"], capture_output=True, text=True)
print(r.stdout)
print("STDERR:", r.stderr[-3000:] if r.stderr else "")
