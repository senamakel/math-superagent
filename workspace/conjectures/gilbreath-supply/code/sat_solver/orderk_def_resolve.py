#!/usr/bin/env python3
"""Decide which definition of K*(n) reproduces the imported table.

Test interpretations against research/witness-hunt-n20-imported.txt:
  K*:  n=4:2 5:2 6:3 7:4 8:4 9:5 10:5 11:6 12:6 13:7 14:7 15:8 16:8 17:9 18:9 19:10 20:10

Interpretation A: single C_K histogram (length K+1 grams). K* = largest K with
   a witness pair (equal single C_K histogram, different S^2).
Interpretation B: single C_K histogram. K* = min K with S^2 constant on every
   single-C_K fiber.
Interpretation C: cumulative C_1..C_K. K* = min K constant on every fiber.
   (what I tried first)

Also print, for n=8, the witness booleans at each K under each interpretation,
to see which matches "witness@K=True K=1,2,3 / False at K=n-1".
"""
import sys, os
from itertools import product
from lib.supply_fold import s_sos

OUT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    "..", "out", "orderk_def_resolve.txt"))

def hist(h, L):
    n = len(h); size = 1 << L; cnt = [0]*size
    for p in range(n - L + 1):
        w = 0
        for b in range(L): w = (w << 1) | h[p+b]
        cnt[w] += 1
    return tuple(cnt)

def S2(n, h):
    S, _ = s_sos(n, h); return S*S

def run():
    lines = []
    lines.append("SEQUENCE : all binary strings per n (brute); K* definition resolution")
    lines.append("ORACLE   : lib.supply_fold.s_sos")
    lines.append("N-RANGE  : n=4..12")
    lines.append("")
    imported = {4:2,5:2,6:3,7:4,8:4,9:5,10:5,11:6,12:6,13:7,14:7}
    for n in range(4, 13):
        strings = [tuple(x) for x in product([0,1], repeat=n)]
        # precompute S2 per string once
        s2 = {h: S2(n, list(h)) for h in strings}
        # Interpretation A: single C_K histogram; largest K with witness
        best_A = None
        witness_A = {}
        for K in range(1, n-1):
            g = {}
            for h in strings:
                g.setdefault(hist(h, K+1), set()).add(s2[h])
            has = any(len(v) > 1 for v in g.values())
            witness_A[K] = has
            if not has: best_A = K; break
        # A: largest K with witness = best_A - 1
        Kstar_A = (best_A - 1) if best_A else None
        # Interpretation B: single C_K; min K with constancy
        Kstar_B = None
        for K in range(1, n-1):
            g = {}
            for h in strings: g.setdefault(hist(h,K+1),set()).add(s2[h])
            if all(len(v)==1 for v in g.values()):
                Kstar_B = K; break
        lines.append("n=%2d imported=%s  A(largestK witness)=%s  B(minK const on single)=%s"
                     % (n, imported.get(n), Kstar_A, Kstar_B))
        if n == 8:
            lines.append("     n=8 witness_true_at: " +
                         ",".join("K=%d:%s"%(k,witness_A[k]) for k in sorted(witness_A)))
    # full-cumulative (C) for comparison
    lines.append("")
    lines.append("C (cumulative C_1..C_K, minK const):")
    for n in range(4, 13):
        strings = [tuple(x) for x in product([0,1], repeat=n)]
        s2 = {h: S2(n, list(h)) for h in strings}
        Kc = None
        for K in range(1, n-1):
            def fsig(h): return tuple(hist(h,L) for L in range(2,K+1))
            g = {}
            for h in strings: g.setdefault(fsig(h),set()).add(s2[h])
            if all(len(v)==1 for v in g.values()): Kc=K; break
        lines.append("  n=%2d imported=%s cumulative-minK=%s" % (n, imported.get(n), Kc))
    text = "\n".join(lines) + "\n"
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    tmp = OUT+".tmp.%d"%os.getpid()
    open(tmp,"w").write(text); os.replace(tmp,OUT)
    sys.stdout.write(text)
    return 0

if __name__ == "__main__":
    sys.exit(run())
