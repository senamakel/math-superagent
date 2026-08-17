#!/usr/bin/env python3
import sys, os, subprocess, time

cmd = [
    sys.executable, "-u", "code/refute/pattern_triangular_n8_attack.py"
]
start = time.time()
with open("code/out/pattern_triangular_n8_attack.captured.txt", "w") as f:
    f.write("$ " + " ".join(cmd) + "\n")
    p = subprocess.run(cmd, cwd="/workspace", stdout=f, stderr=subprocess.STDOUT)
    f.write(f"\nEXIT: {p.returncode}  wall={time.time()-start:.1f}s\n")
print("done exit", p.returncode)
