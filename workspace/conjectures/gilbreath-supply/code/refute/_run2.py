import subprocess, sys
r = subprocess.run([sys.executable, "code/refute/verify_endpoint_sign.py"],
                   cwd="/workspace", capture_output=True, text=True)
sys.stdout.write(r.stdout)
sys.stderr.write(r.stderr)
