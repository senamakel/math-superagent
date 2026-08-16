import subprocess
r = subprocess.run(["python", "code/refute/powers_two_check.py"],
                   cwd="/workspace", capture_output=True, text=True)
out = r.stdout + "\n---STDERR---\n" + r.stderr
print(out)
open("/workspace/code/out/powers_two_check.txt", "w").write(out)
