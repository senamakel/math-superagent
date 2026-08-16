#!/usr/bin/env python3
"""Extend the exact-mean threshold weight w*(n) = min w : mean_n(w)/n >= 0.40
to large n (powers of two), using the grouped Krawtchouk popcount formula.

mean_n(w)/n = (1/(2n)) * sum_p cnt_p * (1 - K_w(2^p; n)/C(n,w)),
where cnt_p = #{d in [2,n-1] : popcount(d)=p} and K_w is the Krawtchouk
polynomial value.  All arithmetic exact rational; only the >= 0.40 compare
uses Fraction so the crossing is exact.

Test: does the per-doubling exponent log2(w*)/log2(n) stay near 0.55
(pure sublinear power) or bend toward 1/2 (the structural prediction)?

Range: n = 2^k for k = 4..22 (16 .. 4194304).
"""
from fractions import Fraction
from math import comb, log2


def popcount_counts(n):
    c = {}
    for d in range(2, n):
        p = bin(d).count('1')
        c[p] = c.get(p, 0) + 1
    return c


def mean_frac(n, w, cnt):
    """mean_n(w)/n as a Fraction.  Exact crossing test (>= 2/5)."""
    Cnw = comb(n, w)
    tot = Fraction(0)
    for p, cntp in cnt.items():
        if cntp == 0:
            continue
        m = 1 << p
        # K_w(m; n) = sum_j (-1)^j C(m,j) C(n-m, w-j)
        K = 0
        jlo = max(0, w - (n - m))
        jhi = min(w, m)
        for j in range(jlo, jhi + 1):
            term = comb(m, j) * comb(n - m, w - j)
            K += -term if (j & 1) else term
        tot += Fraction(cntp, 2) * (1 - Fraction(K, Cnw))
    return tot / n


def main():
    print("w*(n) = min w : mean_n(w)/n >= 0.40  (exact, grouped Krawtchouk)")
    print("range: n = 2^k, k = 4..22")
    rows = []
    for k in range(4, 23):
        n = 1 << k
        cnt = popcount_counts(n)
        # scan w upward.  w* ~ n^0.55: sublinear, so scan is cheap.
        w = None
        # lower bound from previous
        for ww in range(1, n // 2):
            m = mean_frac(n, ww, cnt)
            if m >= Fraction(2, 5):
                w = ww
                me = float(m)
                break
        rows.append((k, n, w, me))
        print("k=%2d  n=%8d  w*=%6d  theta=%.6f  mean=%.4f"
              % (k, n, w, w / n, me) if w else
              "k=%2d  n=%8d  no crossing" % (k, n), flush=True)
    print("")
    print("per-doubling exponent  log2(w*(2n)/w*(n)):")
    prev = None
    for k, n, w, me in rows:
        if prev is not None:
            k0, n0, w0, me0 = prev
            if w and w0 and w0 > 0:
                slope = (log2(w) - log2(w0)) / 1.0
                print("  k=%2d  w* %d -> %d   exponent=%.4f"
                      % (k, w0, w, slope))
        prev = (k, n, w, me)


if __name__ == "__main__":
    main()
