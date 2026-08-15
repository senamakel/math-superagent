#!/usr/bin/env python3
"""Sharpen the Route-B supply statement to a LINEAR bound nu2 >= c*n.

Granville's Lemma 5.4 / Thm 5.5 only need nu2 >= c*n (any c>0), which
dominates n^0.525.  Dense measurement already shows nu2/n in [0.4587, ~0.54].
Report:
  - min nu2/n over n>=T for T in {100,1000,5000}
  - the exact largest n violating nu2 >= 0.45*n  (falsifier bound)
  - whether nu2 >= 0.45*n holds for every n >= some threshold
  - where the minimum ratio is attained
"""
from lib.gilbreath import primes_up_to
from lib.rightdiag import cycle_and_nu2

P = primes_up_to(1_000_000)
D = [P[0]]
ratios = {}
for n in range(1, 30001):
    if n >= 2:
        newD = [0]*n; newD[0] = P[n-1]
        for k in range(1, n):
            newD[k] = abs(newD[k-1]-D[k-1])
        D = newD
    _, nu2 = cycle_and_nu2(D)
    if n >= 100:
        ratios[n] = nu2 / float(n)

for T in [100, 1000, 5000]:
    chunk = {n: r for n, r in ratios.items() if n >= T}
    m = min(chunk.values())
    mn = [n for n, r in chunk.items() if r == m][0]
    print("min nu2/n over n>=%5d : %.4f at n=%d" % (T, m, mn))

print()
# falsifier bound for nu2 >= 0.45*n
last_bad = 0
for n in range(100, 30001):
    if ratios[n] < 0.45:
        last_bad = n
print("last n>=100 with nu2 < 0.45*n :", last_bad)
print("  -> 'nu2 >= 0.45*n for all n>=100' holds to 30000:",
      last_bad == 0)
# same for 0.4
lb40 = [n for n in range(100, 30001) if ratios[n] < 0.4]
print("n>=100 with nu2 < 0.4*n :", lb40[:3], "count", len(lb40))
