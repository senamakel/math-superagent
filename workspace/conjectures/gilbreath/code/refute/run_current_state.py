import subprocess, sys
for prog in ["search_intruder4_rung.py", "search_allzero_subclaim.py", "run_intruder4_searches.py"]:
    print("="*70)
    print("PROGRAM:", prog)
    try:
        r = subprocess.run([sys.executable, "code/refute/"+prog],
                           capture_output=True, text=True, timeout=300)
        print(r.stdout)
        if r.stderr:
            print("STDERR:", r.stderr[-2000:])
    except Exception as e:
        print("ERR:", e)
