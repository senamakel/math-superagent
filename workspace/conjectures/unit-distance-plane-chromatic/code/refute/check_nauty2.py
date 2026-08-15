import subprocess, time
try:
    out = subprocess.run(["nauty-geng"],capture_output=True,text=True)
    print("nauty-geng stderr:", out.stderr[:200])
except FileNotFoundError:
    print("NAUTY NOT FOUND")
