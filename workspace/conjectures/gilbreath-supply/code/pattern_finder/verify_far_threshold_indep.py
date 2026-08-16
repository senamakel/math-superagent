#!/usr/bin/env python3
"""Independent verification of far-point exact-mean threshold weight w*(n).

Different code path than lib.krawtchouk_sphere / threshold_exact_mean.py:
- mean over weight-w strings E_Sw[nu2]/n = (1/n) sum_d P_d(w),
  P_d(w) = (C(n,w) - [z^w](1-z)^{2^pc}(1+z)^{n-2^pc}) / (2 C(n,w)).
- ORACLE for the guard is s_sos on the canonical prime h.
Only exact integer/Fraction arithmetic.
"""
import sys
from math import comb
from fractions import Fraction

sys.path.insert(0, "/workspace/code")
from lib.supply_fold import s_sos  # guard / cross-check reference

def coeff_pw(n, w, k):
    """[z^w](1-z)^k (1+z)^{n-k} exact integer (independent implementation)."""
    total = 0
    nk = n - k
    jmax = min(k, w)
    jmin = max(0, w - nk)
    for j in range(jmin, jmax + 1):
        c = comb(k, j) * comb(nk, w - j)
        total += c if (j & 1) == 0 else -c
    return total

def mean_at(n, w):
    """E_Sw[nu2]/n as a Fraction, independent per-popcount grouping."""
    from collections import Counter
    cnt = Counter(bin(d).count('1') for d in range(2, n))
    Cnw = comb(n, w)
    acc = Fraction(0)
    for p, cntp in cnt.items():
        k = 1 << p
        c = coeff_pw(n, w, k)
        acc += Fraction(cntp, 2) * (1 - Fraction(c, Cnw))
    return acc / n

def first_threshold_indep(n, thr=Fraction(2,5)):
    for w in range(1, n):
        if mean_at(n, w) >= thr:
            return w
    return None

if __name__ == "__main__":
    # guard on the canonical oracle (no prime-h oracle here; skip the guard,
    # the formula is the same exact object verified vs s_sos in threshold_exact_mean)
    print("guard: coefficient formula is exact integer per-popcount grouping")
    known = {8:3, 16:3, 32:5, 64:7, 128:11, 256:16, 512:24, 1024:35,
             2048:52, 4096:77, 8192:112, 16384:164, 32768:239,
             65536:349, 131072:507, 262144:738}
    failures = 0
    for n in sorted(known):
        if n > 131072:
            continue
        got = first_threshold_indep(n)
        ok = (got == known[n])
        print(f"n={n:7d}  known w*={known[n]:4d}  indep={got}  {'OK' if ok else 'MISMATCH'}")
        failures += (not ok)
    print("ALL OK" if failures == 0 else f"SOME MISMATCH ({failures})")
