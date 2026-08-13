"""Execute the structural checks and print results to a file."""
import subprocess, sys, os
code = open('research/notes/verify_three_candidates.py').read()
out = subprocess.run([sys.executable, '-c', code], capture_output=True, text=True, cwd='.')
print(out.stdout)
print("STDERR:", out.stderr)
with open('research/notes/verify_three_candidates_output.txt','w') as f:
    f.write(out.stdout + "\n" + out.stderr)
