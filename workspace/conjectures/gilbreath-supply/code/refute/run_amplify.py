import subprocess, sys
r = subprocess.run([sys.executable, '/workspace/code/refute/amplify_probe.py'],
                   cwd='/workspace', capture_output=True, text=True)
print(r.stdout)
print('STDERR:', r.stderr)
