import subprocess, sys, os
# run the directive-45 discrimination and capture stdout exactly
p = subprocess.run([sys.executable, 'librarian_directive45_discriminate.py'],
                   capture_output=True, text=True, cwd=os.path.dirname(__file__))
out = p.stdout + p.stderr
tmp = 'librarian_directive45_capture.txt.tmp'
with open(tmp,'w') as f: f.write(out)
os.replace(tmp, 'librarian_directive45_capture.txt')
print("exit", p.returncode)
