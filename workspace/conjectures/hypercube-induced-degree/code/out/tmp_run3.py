import subprocess, sys
r = subprocess.run([sys.executable, "code/out/indep_research_check.py"], capture_output=True, text=True)
print(r.stdout)
print(r.stderr)
print("EXIT", r.returncode)
