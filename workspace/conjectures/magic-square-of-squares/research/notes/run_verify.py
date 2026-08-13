import subprocess, sys, os
d = 'research/notes'
code = open(os.path.join(d,'verify_three_candidates.py')).read()
out = subprocess.run([sys.executable, '-c', code], capture_output=True, text=True)
print(out.stdout)
print("STDERR:", out.stderr)
open(os.path.join(d,'verify_three_candidates_output.txt'),'w').write(out.stdout + "\n" + out.stderr)
