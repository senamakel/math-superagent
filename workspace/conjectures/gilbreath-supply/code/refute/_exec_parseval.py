import subprocess, sys, os
os.chdir("/workspace")
r = subprocess.run([sys.executable, "-c",
    "import sys; sys.path.insert(0,'code'); sys.path.insert(0,'.'); exec(open('code/refute/check_parseval_uniform.py').read())"],
    capture_output=True, text=True)
print(r.stdout)
print("ERR", r.stderr[-3000:])
