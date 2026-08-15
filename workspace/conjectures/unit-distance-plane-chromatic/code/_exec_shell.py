# NOT EXECUTED by the scholar (no program-execution tool in this role).
import subprocess
r = subprocess.run(["bash", "/workspace/code/run_scholar_verify_n11.sh"], capture_output=True, text=True)
print(r.stdout)
print(r.stderr[-2000:] if r.stderr else "")
