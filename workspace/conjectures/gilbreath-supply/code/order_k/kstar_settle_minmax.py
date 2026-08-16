#!/usr/bin/env python3
"""Memory-light K*(n) via per-fiber (min,max) of S2, single string pass.

No full s2v dict. For each K, group strings by cumulative C_1..C_K key,
tracking only min & max S2 per fiber; a witness exists iff some fiber has
min != max. This is the exact witness definition, constant memory per fiber.
"""
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

def kstar(n):
    strings = list(product([0, 1], repeat=n))
    # precompute per-string S2 in streaming fashion but store compact result list
    # Memory: store s2 as list parallel to strings (small ints).
    s2list = [S2(n, list(s)) for s in strings]
    prefix = []
    for K in range(1, n):
        fibers = {}
        for idx, h in enumerate(strings):
            key = tuple(hist(h, L) for L in range(2, K + 2))
            s = s2list[idx]
            e = fibers.get(key)
            if e is None:
                fibers[key] = (s, s)
            else:
                lo, hi = e
                if s < lo: lo = s
                if s > hi: hi = s
                fibers[key] = (lo, hi)
        any_w = any(lo != hi for (lo, hi) in fibers.values())
        prefix.append(any_w)
        if not any_w:
            return K, prefix
    return n - 1, prefix

def main():
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 18
    want = [int(x) for x in sys.argv[2:]] if len(sys.argv) > 2 else list(range(2, nmax+1))
    out = []
    sp = out.append
    sp("kstar_settle_minmax: K*(n) via per-fiber (min,max) S2 -- floor-vs-ceil")
    sp("SEQUENCE: all binary strings per n (exhaustive oracle)")
    sp("ORACLE  : S=(n-2)-2*nu2 via lib.supply_fold.s_sos")
    sp("RANGE   : n = %s (2^n states, oracle_bound)" % want)
    table = {}
    for n in want:
        t0 = time.time()
        k, prefix = kstar(n)
        table[n] = k
        sp("  n=%-3d K*=%-3d witness-prefix=%s (%.1fs)" % (n, k, prefix, time.time()-t0))
        sys.stdout.flush()
    sp("")
    floor_ok = ceil_ok = True
    seq = []
    for n in want:
        g = table[n]; fv = n//2; cv = (n+1)//2
        floor_ok &= (g == fv); ceil_ok &= (g == cv); seq.append(g)
        sp("  n=%-3d K*=%d floor(n/2)=%d ceil(n/2)=%d %s" % (
            n, g, fv, cv, "OK" if (g==fv) else "*** floor MISMATCH ***"))
    sp("")
    sp("  K*(n)==floor(n/2): %s  (over %s)" % (floor_ok, want))
    sp("  K*(n)==ceil(n/2):  %s  (over %s)" % (ceil_ok, want))
    sp("  seq = %s" % seq)
    text = "\n".join(out) + "\n"
    capture = "/workspace/code/out/kstar_settle_minmax.captured.txt"
    tmp = capture + ".tmp.%d" % os.getpid()
    with open(tmp, "w") as f: f.write(text)
    os.replace(tmp, capture)
    sys.stdout.write(text)

if __name__ == "__main__":
    main()
