# verify Harper edge-isoperimetric on small cubes
import subprocess, sys
r = subprocess.run(["timeout","540","python3","verify_harper_edgemini.py"],
                   capture_output=True, text=True, cwd="/workspace/code")
print(r.stdout)
print(r.stderr)
print("EXIT_CODE=", r.returncode)
