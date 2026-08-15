#!/usr/bin/env python3
"""Attack S-universe-4color: every graph on <= N vertices with
min-deg>=4, K4-free, K2,3-free is 4-colourable (NO neighbourhood-max-degree
condition). This is the weakened universe U_N the run still commits to in
research/backward/5chromatic-size-lower-bound.md (gap S-universe-4color),
which is strictly LARGER than the verified C_N census universe (which adds the
neighbourhood-maxdeg<=2 condition). A 5-chromatic member of U_N REFUTES
S-universe-4color directly — and is a candidate 5-critical unit-distance graph.

We enumerate connected graphs on n vertices with min-deg>=4 via nauty-geng,
filter K4-free and K2,3-free (the (b),(c) conditions but NOT (d)), and run the
calibrated complete SAT oracle at k=4. UNSAT at k=4 = 5-chromatic = refutation.
"""
import subprocess, sys, time, itertools, argparse
sys.path.insert(0, "/workspace/code")
from lib.satcolor import is_k_colorable


def graph6_to_edges(s):
    n = 0
    i = 0
    if ord(s[0]) < 126:
        n = ord(s[0]) - 63
        i = 1
    elif ord(s[0]) == 126 and len(s) > 1:
        n = (ord(s[1]) - 63) * 16 + (ord(s[2]) - 63) + 63
        i = 3
    else:
        raise ValueError
    bits = []
    for c in s[i:]:
        v = ord(c) - 63
        bits.extend((v >> sh) & 1 for sh in range(5, -1, -1))
    edges = []
    k = 0
    for j in range(1, n):
        for r in range(0, j):
            if k < len(bits) and bits[k]:
                edges.append((r, j))
            k += 1
    return n, edges


def kernel_conditions(n, edges, check_nbhd_deg=True):
    """Return (min_deg_ok, k4free, k23free, nbhd_ok, min_deg)."""
    adj = [set() for _ in range(n)]
    for a, b in edges:
        adj[a].add(b); adj[b].add(a)
    md = min((len(adj[v]) for v in range(n)), default=0)
    # K4
    k4 = False
    for a in range(n):
        for b in adj[a]:
            if b <= a: continue
            inter = adj[a] & adj[b]
            for c in inter:
                if c <= b: continue
                for d in inter:
                    if d > c and d in adj[c]:
                        k4 = True; break
                if k4: break
            if k4: break
        if k4: break
    # K2,3: two vertices share >=3 common neighbours
    k23 = False
    for a in range(n):
        for b in range(a+1, n):
            if len(adj[a] & adj[b]) >= 3:
                k23 = True; break
        if k23: break
    # nbhd max degree <= 2
    nd = True
    if check_nbhd_deg:
        for v in range(n):
            nb = sorted(adj[v])
            for x in nb:
                if sum(1 for y in nb if y in adj[x]) > 2:
                    nd = False; break
            if not nd: break
    return (md >= 4, not k4, not k23, nd, md)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--maxn", type=int, default=13)
    ap.add_argument("--use_nbhd", action="store_true",
                    help="also require nbhd-maxdeg<=2 (the C_N census universe)")
    args = ap.parse_args()
    label = "C_N (with nbhd cond)" if args.use_nbhd else "U_N (weakened, no nbhd cond)"
    print(f"Attacking S-universe-4color over {label}", flush=True)
    for n in range(8, args.maxn + 1):
        cmd = ["nauty-geng", str(n), "-c", "-d4", "-k"]  # connected, min-deg 4, K4-free
        t0 = time.time()
        total = 0; members = 0; five_chrom = []
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                text=True, bufsize=1)
        try:
            for ln in proc.stdout:
                ln = ln.rstrip("\n")
                if not ln or ln[0] in ">#":
                    continue
                if not all(63 <= ord(c) <= 126 for c in ln):
                    continue
                total += 1
                m, edges = graph6_to_edges(ln)
                md4, k4f, k23f, nd, md = kernel_conditions(n, edges, args.use_nbhd)
                if not (md4 and k4f and k23f):
                    continue
                if args.use_nbhd and not nd:
                    continue
                members += 1
                sat, witness = is_k_colorable(edges, 4, n)
                if not sat:
                    five_chrom.append(edges)
        finally:
            proc.stdout.close()
            try: proc.wait(timeout=300)
            except subprocess.TimeoutExpired:
                proc.kill(); proc.wait()
        dt = time.time() - t0
        print(f"n={n}: processed {total}, {members} in-universe, "
              f"5-chromatic={len(five_chrom)}, {dt:.1f}s", flush=True)
        if five_chrom:
            for e in five_chrom:
                print(f"  REFUTED: 5-chromatic member edges={e}", flush=True)
            return
    print("No 5-chromatic member found in the searched universe range.", flush=True)


if __name__ == "__main__":
    main()
