#!/usr/bin/env python3
"""Verify the nu2<->w transfer bounds exactly from on-disk nu2_dense.txt.

nu2_dense.txt holds n, nu2(n) for n=1..30000. We recompute w(n) from first
principles (mod-4 gap bits, window [2,n-1]) and report, EXACTLY over the
30000 terms:
  - smallest c with nu2(n) >= c*w(n) for all n >= threshold, for thresholds
    17, 100, 1000, 4000
  - the first falsifying n for each claimed bound (0.5 for n>=17, 0.75 for
    n>=1005)
  - the exact min ratio nu2/w and where it happens for n>=17
This is a check over the data already on disk, not a new computation of nu2.
"""
from lib.gilbreath import primes_up_to

P = primes_up_to(1_000_000)  # 78498 primes, matches the dense generator's sieve

# histogram of primes: nu2_dense.txt is n=1..30000 -> need 30002 primes, fine

# load nu2
nu2 = {}
with open("code/out/nu2_dense.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        n, v = line.split()
        nu2[int(n)] = int(v)

# recompute w: hbits[i] = ((P[i+1]-P[i])//2) % 2, window i in [2, n-1]
# prefix sums over index i (0-based gap index)
hbits = [((P[i+1] - P[i]) // 2) % 2 for i in range(len(P) - 1)]
# pref[i] = sum_{j=0}^{i-1} hbits[j]
pref = [0]
for b in hbits:
    pref.append(pref[-1] + b)

def w(n):
    # sum hbits[2 .. n-1] inclusive = pref[n] - pref[2]
    return pref[n] - pref[2]

print("n   nu2   w   nu2/w   nu2-0.5w  nu2-0.75w  dev=2nu2-n")
for n in range(17, 30001, 997):
    print(f"{n:6d} {nu2[n]:6d} {w(n):6d} {nu2[n]/w(n):.4f} "
          f"{nu2[n]-0.5*w(n):+8.1f} {nu2[n]-0.75*w(n):+8.1f} {2*nu2[n]-n:+8d}")

for thresh in (1, 2, 17, 100, 1000, 4000):
    best_c = min(nu2[n]/w(n) for n in range(max(thresh, 2), 30001) if w(n) > 0)
    argmin_c = min((n for n in range(max(thresh, 2), 30001) if w(n) > 0),
                   key=lambda n: nu2[n]/w(n))
    print(f"threshold n>={thresh}: min nu2/w = {best_c:.6f} at n={argmin_c}")

# falsifying n for specific claimed bounds
for c, thresh in ((0.5, 17), (0.75, 1005), (0.75, 4000), (0.6, 17)):
    bad = [n for n in range(thresh, 30001) if nu2[n] < c*w(n)]
    print(f"nu2 >= {c}*w for n>={thresh}: {'TRUE' if not bad else 'FAILS'} "
          f"first-falsifier={bad[0] if bad else None} count={len(bad)}")
