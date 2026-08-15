#!/usr/bin/env python3
"""Time and count nauty-geng at n=12 with the pruning flags that make the
kernel census feasible: connected, min-degree>=4 (-d4), K4-free (-k).

Purpose: determine whether extending the kernel census to n=12 is feasible at
all, and how many candidates stream through, before deciding whether to run
the full 4-colourability scan on a potential counterexample.
"""
import subprocess
import time

def count(n, min_deg, k4free, connected, budget=30):
    cmd = ["nauty-geng", str(n)]
    if connected:
        cmd.append("-c")
    if min_deg:
        cmd.append("-d%d" % min_deg)
    if k4free:
        cmd.append("-k")
    t0 = time.time()
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            text=True, bufsize=1)
    c = 0
    try:
        for ln in proc.stdout:
            if ln and not ln.startswith(">") and not ln.startswith("#") and \
               all(63 <= ord(ch) <= 126 for ch in ln.rstrip("\n")):
                c += 1
                if time.time() - t0 > budget:
                    return c, time.time() - t0, "TIMEOUT"
    finally:
        proc.kill()
        proc.wait()
    return c, time.time() - t0, "done"

if __name__ == "__main__":
    for n, deg, k4 in [(12, 4, True)]:
        c, dt, status = count(n, deg, k4, True, budget=25)
        print(f"n={n} -d{deg} -k connected: count={c} in {dt:.1f}s status={status}")
