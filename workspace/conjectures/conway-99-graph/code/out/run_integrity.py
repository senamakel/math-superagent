"""Run the integrity pass (subprocess so its exit code is captured)."""
import subprocess, sys
r = subprocess.run([sys.executable, "code/out/integrity_pass.py"],
                   capture_output=True, text=True)
print(r.stdout)
if r.stderr:
    print("STDERR:", r.stderr)
print("EXIT", r.returncode)
