#!/usr/bin/env python3
"""Run the minimal k-1 counterexample oracle and capture to out/."""
import subprocess, sys, os, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, os.pardir))
SCRIPT = os.path.join(ROOT, 'refute', 'center_ideal_kminus1_oracle.py')
OUT = os.path.normpath(os.path.join(ROOT, 'out',
                                    'center_ideal_kminus1_oracle.captured.txt'))
env = dict(os.environ)
env['PYTHONPATH'] = ROOT + os.pathsep + env.get('PYTHONPATH', '')
r = subprocess.run([sys.executable, SCRIPT], capture_output=True, text=True, env=env)
if r.returncode != 0:
    print('FAILED run'); print(r.stdout); print(r.stderr); sys.exit(r.returncode)
fd, tmp = tempfile.mkstemp(dir=os.path.dirname(OUT), prefix='.kminus1.', suffix='.tmp')
with os.fdopen(fd, 'w') as f:
    f.write(r.stdout)
os.replace(tmp, OUT)
print(r.stdout)
print('captured to', OUT)
