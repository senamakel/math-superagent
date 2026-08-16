import subprocess, sys, os
p = subprocess.run([sys.executable, '_run_d45.py'], cwd=os.path.dirname(__file__), capture_output=True, text=True)
print(p.stdout); print(p.stderr)
t = os.path.join(os.path.dirname(__file__),'librarian_directive45_capture.txt')
print("---capture---")
print(open(t).read())
