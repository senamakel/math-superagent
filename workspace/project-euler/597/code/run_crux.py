import subprocess, sys
for f in [("code/cross_direct_test.py", 40000),
          ("code/crux_decoupling_test.py", 30000)]:
    print("="*70)
    print("RUN:", f[0])
    print("="*70)
    r = subprocess.run([sys.executable, f[0], str(f[1])], capture_output=True, text=True)
    print(r.stdout)
    if r.stderr:
        print("STDERR:", r.stderr[-3000:])
