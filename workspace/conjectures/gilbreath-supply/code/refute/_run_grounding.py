import subprocess
r = subprocess.run(["python", "code/refute/grounding.py"],
                   cwd="/workspace", capture_output=True, text=True)
out = r.stdout + "\n---STDERR---\n" + r.stderr
print(out)
open("/workspace/code/out/refuter_grounding.txt", "w").write(out)
