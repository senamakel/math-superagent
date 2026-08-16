import subprocess, sys, os
os.chdir("/workspace")
sys.path.insert(0, "/workspace")
r = subprocess.run([sys.executable, "code/refute/delta_ladder_verify_simple.py"], cwd="/workspace", capture_output=True, text=True)
print("STDOUT:", r.stdout)
print("STDERR:", r.stderr)
print("RC:", r.returncode)
