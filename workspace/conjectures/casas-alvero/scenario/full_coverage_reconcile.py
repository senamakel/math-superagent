"""Reconcile n=96 and n=98 against the FULL m<=7 settled-family coverage,
including the 6p^k and 7p^k families.  Question per research/patterns/
open_degree_complement_and_sequences.md:
  - is 98 the ONLY true discrepancy (covered by 2p^k yet published-open)?
  - is 96 correctly open once 6p^k (p=2 bad for d=6) and 7p^k are included?
d=7 bad primes: source says smallest non-bad prime apart from 7 is 127, so
p in {2,3,5,11} are bad for d=7.  For the 7p^k family we need to know whether
a candidate base p is bad; use the 127-bound (p<127 and p!=7 => bad).
"""
from sympy import factorint

published_open = [20, 24, 28, 30, 35, 36, 40, 42, 45, 48, 55, 56, 60, 63, 66,
                  70, 72, 77, 78, 80, 84, 88, 90, 91, 98, 99, 100]
P = set(published_open)

def is_pp(q):
    return len(factorint(q)) == 1

def base(q):
    return list(factorint(q))[0]

def cover_full(n):
    """Return list of (m, p) with n == m*p^k, m in 1..7, p prime, and whether GOOD."""
    res = []
    for m in range(1, 8):
        if n % m == 0:
            q = n // m
            if is_pp(q):
                p = base(q)
                # bad-prime exclusion by multiplier m
                if m == 1: good = True                 # p^k, no exclusion
                elif m == 2: good = True               # 2p^k, no exclusion
                elif m == 3: good = (p != 2)
                elif m == 4: good = (p not in {3, 5, 7})
                elif m == 5: good = (p not in {2, 3, 7, 11, 131, 193, 599, 3541, 8009})
                elif m == 6: good = (p not in {2, 5, 7, 11, 13, 19, 23, 29, 37, 47,
                                               61, 67, 73, 97, 257, 811, 983, 1069,
                                               1087, 1187, 1487, 1499, 1901, 2287,
                                               3209, 3877, 3881, 4019, 4943, 5471,
                                               6983, 8699, 9337, 15131, 15823, 20771,
                                               21379, 23993, 150203, 266587, 547061,
                                               685177, 885061, 1030951, 7783207,
                                               17250187, 40362599, 9348983563,
                                               70016757407, 2610767527031,
                                               225833117528659, 7390044713023799,
                                               51313000813080529})
                elif m == 7: good = (p == 7) or (p >= 127)   # bad unless p==7 or p>=127
                res.append((m, p, q, good))
    return res

print("=== Full m<=7 coverage test ===")
only_anomaly = []
for n in range(9, 101):
    if n == 12:
        continue
    covs = cover_full(n)
    covered = any(g for (_, _, _, g) in covs)
    pub = n in P
    consistent = (pub == (not covered))
    if not consistent:
        only_anomaly.append((n, covs, pub, covered))
for (n, covs, pub, covered) in only_anomaly:
    print(f"  n={n}: published_open={pub} covered(m<=7)={covered}  "
          f"representations: {[(m,p,good) for (m,p,q,good) in covs]}")
print("\nOnly inconsistent degrees under full m<=7 coverage:", [x[0] for x in only_anomaly])
print("\n== n=98 detail ==")
for c in cover_full(98):
    print("  98:", c)
print("== n=96 detail ==")
for c in cover_full(96):
    print("  96:", c)
