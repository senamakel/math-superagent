#!/usr/bin/env python3
"""Memory-light K*(n): recompute cumulative-fiber grouping per K, keep only dict."""
import sys, os, time
from itertools import product
sys.path.insert(0, "/workspace/code")
from lib.supply_fold import s_sos

def hist(h, L):
    n = len(h); size = 1 << L; cnt = [0]*size
    for p in range(n - L + 1):
        w = 0
        for b in range(L): w = (w << 1) | h[p+b]
        cnt[w] += 1
    return tuple(cnt)

def S2(n, h):
    S, _ = s_sos(n, list(h)); return S*S

def kstar(n, strings, s2v):
    prefix = []
    for K in range(1, n):
        cells = {}
        for h in strings:
            # cumulative key = tuple of histograms for lengths 2..K+1
            # build up incrementally per h (recompute hist; cheap enough)
            key = tuple(hist(h, L) for L in range(2, K + 2))
            s = cells.get(key)
            if s is None:
                cells[key] = {s2v[h]}
            else:
                s.add(s2v[h])
        any_w = any(len(v) > 1 for v in cells.values())
        prefix.append(any_w)
        if not any_w:
            return K, prefix
    return n - 1, prefix

def main():
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 18
    out = []
    sp = out.append
    sp("kstar_settle_ml: memory-light K*(n) floor-vs-ceil (GOAL priority 3)")
    sp("SEQUENCE: all binary strings per n (exhaustive oracle)")
    sp("ORACLE  : S=(n-2)-2*nu2 via lib.supply_fold.s_sos")
    sp("RANGE   : n = 2..%d (2^n states, oracle_bound=%d)" % (nmax, nmax))
    table = {}
    for n in range(2, nmax + 1):
        strings = [tuple(x) for x in product([0, 1], repeat=n)]
        s2v = {h: S2(n, h) for h in strings}
        t0 = time.time()
        k, prefix = kstar(n, strings, s2v)
        table[n] = k
        sp("  n=%-3d K*=%-3d witness-prefix=%s (%.1fs)" % (n, k, prefix, time.time() - t0))
    sp("")
    floor_ok = ceil_ok = True
    seq = []
    for n in range(2, nmax + 1):
        g = table[n]; fv = n//2; cv = (n+1)//2
        floor_ok &= (g == fv); ceil_ok &= (g == cv); seq.append(g)
        sp("  n=%-3d K*=%d floor=%d ceil=%d" % (n, g, fv, cv))
    sp("")
    sp("  K*(n)==floor(n/2) for [2,%d]: %s" % (nmax, floor_ok))
    sp("  K*(n)==ceil(n/2)  for [2,%d]: %s" % (nmax, ceil_ok))
    sp("  seq = %s" % seq)
    text = "\n".join(out) + "\n"
    capture = "/workspace/code/out/kstar_settle_ml.captured.txt"
    tmp = capture + ".tmp.%d" % os.getpid()
    with open(tmp, "w") as f: f.write(text)
    os.replace(tmp, capture)
    sys.stdout.write(text)

if __name__ == "__main__":
    main()
