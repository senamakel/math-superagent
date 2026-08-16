import subprocess
r = subprocess.run(["python", "code/refute/gen_n8.py"],
                   cwd="/workspace", capture_output=True, text=True)
out = r.stdout + "\n---STDERR---\n" + r.stderr
print(out)
open("/workspace/code/out/n8_gen.txt", "w").write(out)
