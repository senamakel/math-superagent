import sys
sys.argv = ['x']
import subprocess
r = subprocess.run([sys.executable, "code/out/refute_check_counts.py"],
                   capture_output=True, text=True, cwd="/workspace")
print(r.stdout)
print(r.stderr)
