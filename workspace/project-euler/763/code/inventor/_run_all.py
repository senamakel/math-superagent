import subprocess
for p in ["code/inventor/check_recurrence.py", "code/inventor/probe_topcap.py",
          "code/inventor/probe_reachable.py"]:
    print("=" * 30, p, "=" * 30)
    r = subprocess.run(["python3", p], capture_output=True, text=True, cwd="/workspace")
    print(r.stdout)
    if r.stderr:
        print("STDERR:", r.stderr)
