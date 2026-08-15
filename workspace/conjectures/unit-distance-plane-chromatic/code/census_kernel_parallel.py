#!/usr/bin/env python3
"""Count kernel members of C_11 exhaustively, parallelised over geng's
res/mod residue split across all 28 CPUs.

Each worker runs `nauty-geng 11 -d4 res/mod` — only 1/mod of the search
space — streams and filters, writes its found kernel members to a per-worker
file. So the total wall time is that of one slice (not 28x it), and the
per-worker graph count is 1/mod of 187M. This keeps the exhaustive scan
complete (all residue classes together cover every graph exactly once) while
making each slice small enough to filter in pure Python within the timeout.
"""
import subprocess, sys, os, time
sys.path.insert(0, "/workspace/code")
from census_kernel import graph6_to_edges, check_kernel

OUTDIR = "/workspace/code/out/kernel_slices"
os.makedirs(OUTDIR, exist_ok=True)

MOD = int(sys.argv[1]) if len(sys.argv) > 1 else 28
RES = int(sys.argv[2]) if len(sys.argv) > 2 else int(sys.argv[1])

n = 11
cmd = ["nauty-geng", str(n), "-d4", f"{RES}/{MOD}"]
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                        text=True, bufsize=1)
count = 0
members = []
start = time.time()
try:
    for ln in proc.stdout:
        ln = ln.rstrip("\n")
        if not ln or ln[0] in ">#":
            continue
        m, edges = graph6_to_edges(ln)
        ok, reason = check_kernel(n, edges)
        count += 1
        if ok:
            members.append(edges)
finally:
    proc.stdout.close()
    proc.wait()

# write members (canonical sorted edge tuples) to per-residue file
with open(f"{OUTDIR}/res{RES}_of{MOD}.txt", "w") as f:
    for e in members:
        f.write(repr(sorted(e)) + "\n")
d = time.time() - start
print(f"RES={RES}/{MOD}: processed {count} graphs, {len(members)} kernel members, {d:.1f}s", flush=True)
