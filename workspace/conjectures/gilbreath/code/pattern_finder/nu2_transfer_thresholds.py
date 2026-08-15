#!/usr/bin/env python3
"""Exact thresholds for the nu2>=c*w transfer bound (dense, n=2..30000).

For each constant c, report the LARGEST n at which nu2(n) < c*w(n), so the
claim "nu2 >= c*w for all n > N_c" is stated precisely with its falsifier
bound.  Over the full range we can also report any n>=1000 violation.
"""
from lib.gilbreath import primes_up_to
from lib.rightdiag import cycle_and_nu2

P = primes_up_to(1_000_000)
hbits = [((P[i+1]-P[i])//2) % 2 for i in range(len(P)-1)]

D = [P[0]]
worst = {}          # c -> (largest n with nu2 < c*w, that nu2/w)
for c in [0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85]:
    worst[c] = (0, 1.0)
for n in range(2, 30001):
    if n >= 2:
        newD = [0]*n; newD[0] = P[n-1]
        for k in range(1, n):
            newD[k] = abs(newD[k-1]-D[k-1])
        D = newD
    _, nu2 = cycle_and_nu2(D)
    w = sum(hbits[2:n])
    if w == 0:
        continue
    for c in worst:
        if nu2 < c*w:
            worst[c] = (n, nu2/float(w))

print("c      last n with nu2<c*w     (nu2/w there)")
for c in [0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85]:
    n, r = worst[c]
    print("%.2f   %d        %.4f" % (c, n, r))
print()
print("Interpretation: 'nu2 >= c*w for all n > last_n' holds densely to 30000.")
