import subprocess, sys
result = subprocess.run([sys.executable, "code/scratch/librarian_ground.py"], capture_output=True, text=True)
print(result.stdout)
print(result.stderr)
