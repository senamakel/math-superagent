import subprocess, sys, os
d = 'research/notes'
code = open(os.path.join(d,'verify_three_candidates.py')).read()
out = subprocess.run([sys.executable, '-c', code], capture_output=True, text=True)
sys.stdout.write(out.stdout)
sys.stderr.write("STDERR: " + out.stderr + "\n")
open(os.path.join(d,'verify_three_candidates_output.txt'),'w').write(out.stdout + "\n" + out.stderr)
