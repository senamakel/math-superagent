import subprocess, os
os.chdir("/workspace/code/scholar")
r = subprocess.run(["python3", "scholar_dyadic_collapse_check.py"],
                   capture_output=True, text=True)
print(r.stdout)
print(r.stderr)
print("EXIT_CODE=%d" % r.returncode)
