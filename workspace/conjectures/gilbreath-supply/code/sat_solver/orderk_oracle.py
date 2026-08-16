#!/usr/bin/env python3
"""CORRECTED brute-force oracle for K*(n) — authoritative definition.

DEFINITION (fixed, no off-by-one):
  C_m(h)  = histogram of (m+1)-grams of h (overlapping windows), so
            C_1 = 2-gram histogram, C_2 = 3-gram, ..., C_K = (K+1)-gram.
  "Order-K correlation vector" C_1..C_K = histograms of word-lengths 2..K+1.
  K*(n) = min{K >= 1 : S^2 is constant on every C_1..C_K fiber}
        = min{K : no pair h,h' with equal C_1..C_K but S^2(h) != S^2(h')}.

  This matches REOPENED.md (C_1=(5,1,1,0) = 2-grams) and the imported table.

Oracle = exhaustive over all 2^n strings (n = 2..14); S via canonical
lib.supply_fold.s_sos.

Also verifies the REDUCTION used by the SAT encoding:
  equal C_1..C_K   <=>   equal C_K histogram AND equal length-K prefix
(two equivalence relations coincide iff same fiber-S2-sets).
"""
import sys, os
from itertools import product
from lib.supply_fold import s_sos

OUT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    "..", "out", "orderk_oracle_check.txt"))

def hist(h, L):
    """histogram of length-L words over overlapping windows."""
    n = len(h); size = 1 << L; cnt = [0]*size
    for p in range(n-L+1):
        w = 0
        for b in range(L): w = (w<<1) | h[p+b]
        cnt[w] += 1
    return tuple(cnt)

def CK(h, K):
    """C_1..C_K as a tuple (histograms of word-lengths 2..K+1)."""
    return tuple(hist(h, L) for L in range(2, K+2))

def S2(n, h):
    S, _ = s_sos(n, list(h)); return S*S

def run():
    lines = []
    lines.append("SEQUENCE : all binary strings per n (brute, exhaustive); "
                 "K* = min{K: S^2 const on every C_1..C_K fiber}")
    lines.append("ORACLE   : lib.supply_fold.s_sos (canonical floored)")
    lines.append("N-RANGE  : n = 2..14")
    lines.append("")
    imported = {2:1,3:1,4:2,5:2,6:3,7:4,8:4,9:5,10:5,11:6,12:6,13:7,14:7,
                15:8,16:8,17:9,18:9,19:10,20:10}

    lines.append("== (A) K*(n) from full C_1..C_K grouping ==")
    kstar = {}
    for n in range(2, 15):
        strings = [tuple(x) for x in product([0,1], repeat=n)]
        s2v = {h: S2(n, h) for h in strings}
        found = None
        for K in range(1, n):
            g = {}
            for h in strings:
                g.setdefault(CK(h,K), set()).add(s2v[h])
            if all(len(v)==1 for v in g.values()):
                found = K; break
        kstar[n] = found
        lines.append("  n=%2d  K*=%s" % (n, found))

    lines.append("")
    lines.append("== (B) REDUCTION CHECK: equal C_1..C_K <=> equal C_K + prefix_K ==")
    red_ok = True
    for n in range(2, 14):
        strings = [tuple(x) for x in product([0,1], repeat=n)]
        s2v = {h: S2(n, h) for h in strings}
        for K in range(1, n):
            g_full = {}
            g_red = {}
            for h in strings:
                g_full.setdefault(CK(h,K), set()).add(s2v[h])
                g_red.setdefault((hist(h,K+1), tuple(h[:K])), set()).add(s2v[h])
            fs = sorted([tuple(sorted(v)) for v in g_full.values()])
            rs = sorted([tuple(sorted(v)) for v in g_red.values()])
            if fs != rs:
                red_ok = False
                lines.append("  MISMATCH n=%d K=%d #cells full=%d red=%d" %
                             (n,K,len(g_full),len(g_red)))
    lines.append("  reduction HOLDS: %s" % red_ok)

    lines.append("")
    lines.append("== (C) Compare to imported table & ceil(n/2) ==")
    for n in range(2, 15):
        iv = imported.get(n)
        kv = kstar[n]
        lines.append("  n=%2d imported=%s oracle=%s  ceil(n/2)=%s  %s" %
                     (n, iv, kv, (n+1)//2,
                      "OK" if kv==iv else "*** DISAGREE ***"))
    text = "\n".join(lines)+"\n"
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    tmp = OUT+".tmp.%d"%os.getpid()
    open(tmp,"w").write(text); os.replace(tmp,OUT)
    sys.stdout.write(text)
    return 0

if __name__ == "__main__":
    sys.exit(run())
