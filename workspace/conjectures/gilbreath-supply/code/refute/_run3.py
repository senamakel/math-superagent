import subprocess, sys
r = subprocess.run([sys.executable, "code/refute/endpoint_sign_check.py"],
                   cwd="/workspace", capture_output=True, text=True)
sys.stdout.write(r.stdout)
sys.stderr.write(r.stderr)
