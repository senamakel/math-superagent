import subprocess, sys
for prog in ["search_intruder4_rung.py", "search_allzero_subclaim.py"]:
    print("="*70)
    print("PROGRAM:", prog)
    try:
        r = subprocess.run([sys.executable, "code/refute/"+prog],
                           capture_output=True, text=True, timeout=500)
        print(r.stdout[-4000:])
        if r.stderr: print("STDERR:", r.stderr[-1000:])
    except Exception as e:
        print("ERR:", e)
