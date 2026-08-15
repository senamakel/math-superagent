import subprocess, time
# quick: confirm nauty-geng is present and version
try:
    out = subprocess.run(["nauty-geng","--version"],capture_output=True,text=True)
    print("nauty-geng present:", out.stdout.strip() or out.stderr.strip()[:100])
except FileNotFoundError:
    print("NAUTY NOT FOUND")
