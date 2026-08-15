#!/usr/bin/env python3
import subprocess, sys, os
# run the transfer test by executing the module file directly
here = os.path.dirname(os.path.abspath(__file__))
code_root = os.path.dirname(here)
env = dict(os.environ)
env['PYTHONPATH'] = code_root + os.pathsep + env.get('PYTHONPATH','')
r = subprocess.run([sys.executable, os.path.join(here,'run_transfer.py')],
                   env=env, capture_output=True, text=True)
print(r.stdout)
print(r.stderr)
