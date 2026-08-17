import subprocess
r = subprocess.run(["python", "code/out/nonconvex4_cover.py"],
                   capture_output=True, text=True, cwd="/workspace")
print(r.stdout)
print(r.stderr)
