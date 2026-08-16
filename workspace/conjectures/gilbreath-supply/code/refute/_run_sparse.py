import subprocess
r = subprocess.run(["python", "code/refute/sparse_powers_of_two.py"],
                   cwd="/workspace", capture_output=True, text=True)
out = r.stdout + "\n---STDERR---\n" + r.stderr
print(out)
open("/workspace/code/out/sparse_powers_of_two.txt", "w").write(out)
