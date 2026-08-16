#!/usr/bin/env python3
"""Independent re-derivation of the exact threshold weight w*(n).

Third route to the value (the two existing are scholar gen-func and verif
direct hypergeometric). Here: mean_n(w) = (1/n) sum_{d=2}^{n-1} P_d(w) where
P_d(w) = #weight-w strings with an odd number of ones among the fixed k-set
        = sum_{r odd} C(k,r) C(n-k, w-r) / C(n,w),  k = 2^popcount(d).

We also cross-check P against the literal brute fold s_sos for small n.
Everything exact Fraction; w*(n) = min w : mean_n(w) >= 0.40.
"""
from math import comb
from fractions import Fraction
from collections import Counter

def popcount_dist(n):
    c = Counter()
    for d in range(2, n):
        c[d.bit_count()] += 1
    return c

def odd_count(k, n, w):
    lo = max(0, w - (n - k))
    hi = min(k, w)
    s = 0
    for r in range(lo, hi + 1):
        if r & 1:
            s += comb(k, r) * comb(n - k, w - r)
    return s

def P(n, k, w):
    return Fraction(odd_count(k, n, w), comb(n, w))

def mean_direct(n, w, Np):
    tot = Fraction(0)
    for p, cnt in Np.items():
        tot += cnt * P(n, 1 << p, w)
    return tot / n

def main():
    # brute cross-check vs literal fold
    from lib.supply_fold import s_sos
    from itertools import combinations
    def brute_mean(n, w):
        tot = 0; cnt = 0
        for ones in combinations(range(n), w):
            h = [0]*n
            for j in ones: h[j] = 1
            _, c1 = s_sos(n, h)
            tot += c1; cnt += 1
        return Fraction(tot, cnt)/n
    print("PASS1 brute cross-check (mean_n(w) formula vs literal s_sos):")
    for n, w in [(6,1),(6,2),(8,3),(8,4),(10,3),(12,5),(14,4),(16,5)]:
        Np = popcount_dist(n)
        m = mean_direct(n, w, Np)
        b = brute_mean(n, w)
        ok = (m == b)
        print(f"  n={n} w={w}: formula={float(m):.5f} brute={float(b):.5f} {'OK' if ok else 'MISMATCH'}")

    print("\nPASS2 exact threshold weight w*(n) = min w mean>=0.40 :")
    rows = []
    THR = Fraction(2,5)
    ns = [8,10,12,14,16,24,32,48,64,96,128,192,256,384,512,768,1024,
          1536,2048,3072,4096,6144,8192,12288,16384,24576,32768]
    for n in ns:
        Np = popcount_dist(n)
        first = None
        for w in range(1, n):
            if mean_direct(n, w, Np) >= THR:
                first = w
                break
        rows.append((n, first))
        print(f"  n={n:>6}  w*={first:>5}  theta=w*/n={first/n:.6f}")

    print("\nw* sequence:", [w for _,w in rows])
    print("theta    :", [w/n for n,w in rows])

if __name__ == "__main__":
    main()
