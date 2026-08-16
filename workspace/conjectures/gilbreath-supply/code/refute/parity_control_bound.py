#!/usr/bin/env python3
"""Attack the engine lemma of G-threshold-parity-control, EXACT integer form.

Claim: for X ~ Hypergeometric(n,m,w),
    |E[(-1)^X]|  <=  max_j P[X=j].

E[(-1)^X] = sum_j (-1)^j P[X=j], P[X=j] = C(w,j) C(n-w,m-j) / C(n,m).
The comparison is scale-free: define
    A = sum_j (-1)^j C(w,j) C(n-w,m-j)   (integer)
    M = max_j C(w,j) C(n-w,m-j)          (integer)
Then  |E[(-1)^X]| <= max_j P[X=j]  <=>  |A| <= M.
"""
from math import comb

def alt_and_max(n, m, w):
    lo = max(0, m - (n - w))
    hi = min(w, m)
    A = 0
    M = 0
    for j in range(lo, hi + 1):
        term = comb(w, j) * comb(n - w, m - j)
        A += (-1)**j * term
        if term > M:
            M = term
    return A, M

fails = []
count = 0
for n in range(1, 81):
    for m in range(0, n + 1):
        for w in range(0, n + 1):
            count += 1
            A, M = alt_and_max(n, m, w)
            if abs(A) > M:
                fails.append((n, m, w, abs(A), M))

print("grid: n in 1..80, m in 0..n, w in 0..n  ->", count, "combos")
print("violations of |E[(-1)^X]| <= max_j P[X=j]:", len(fails))
for f in fails[:30]:
    print("   n=%d m=%d w=%d  |A|=%d  M=%d  ratio=%.3f" % (f[0], f[1], f[2], f[3], f[4], f[3]/f[4]))
if not fails:
    print("NO VIOLATIONS in grid")
