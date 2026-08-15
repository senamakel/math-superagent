#!/usr/bin/env python3
"""Tightness of the COMBINED supply chain over the dense nu2 data.

Chain (all exact over the stated ranges, conjectures beyond):
  (T) nu2(n) >= w(n)/2                       for all n >= 17   (data 17..30000)
  (S) w(n) >= (n-2)/2                        for all n >= 2    (data 2..1e6)
  =>  (C) nu2(n) >= (n-2)/4                  for all n >= 17   (data 17..30000)
  =>   nu2(n) > n^0.525                      for n >= ~20      (Granville route)

Reports the slack of each link and the tightest points:
  - min (2*nu2 - w) and min (nu2 - w/2) over n in [17,30000], where
  - min (4*nu2 - (n-2)) over n in [17,30000], where (the combined bound slack)
  - the worst implied exponent min log(nu2)/log(n) over n in [4000,30000]
  - where the naive threshold (n-2)/4 > n^0.525 first holds (solve exactly)
"""
import math

nu2 = {}
N = 0
with open("code/out/nu2_dense.txt") as f:
    for line in f:
        n, v = map(int, line.split())
        nu2[n] = v
        N = n

from lib.gilbreath import primes_up_to
P = primes_up_to(1_000_000)
hbits = [((P[i + 1] - P[i]) // 2) % 2 for i in range(len(P) - 1)]
pref = [0] * (len(hbits) + 1)
for i, b in enumerate(hbits):
    pref[i + 1] = pref[i] + b

def w(n):
    return pref[n] - pref[2]

# (T) slack
m1 = 10 ** 18; m1n = 0
m1b = 10 ** 18; m1bn = 0
for n in range(17, N + 1):
    s = 2 * nu2[n] - w(n)
    if s < m1:
        m1 = s; m1n = n
    s2 = nu2[n] - w(n) / 2.0
    if s2 < m1b:
        m1b = s2; m1bn = n
print("transfer (T): min (2*nu2 - w) = %d at n=%d ; min (nu2 - w/2) = %.4f at n=%d"
      % (m1, m1n, m1b, m1bn))
print("  worst ratio nu2/w = %.4f at n=%d (nu2=%d w=%d)"
      % (nu2[m1n] / float(w(m1n)), m1n, nu2[m1n], w(m1n)))

# (S) slack at the same points is known (>=0, equality only at n<=8); report min over [17,N]
m2 = 10 ** 18; m2n = 0
for n in range(17, N + 1):
    s = 2 * w(n) - (n - 2)
    if s < m2:
        m2 = s; m2n = n
print("switch-majority (S): min (2w - (n-2)) over [17,%d] = %d at n=%d"
      % (N, m2, m2n))

# (C) combined slack
m3 = 10 ** 18; m3n = 0
for n in range(17, N + 1):
    s = 4 * nu2[n] - (n - 2)
    if s < m3:
        m3 = s; m3n = n
print("combined (C): min (4*nu2 - (n-2)) over [17,%d] = %d at n=%d (nu2=%d)"
      % (N, m3, m3n, nu2[m3n]))
print("  -> implied nu2 >= (n-2)/4 there: (n-2)/4 = %.1f vs nu2 = %d"
      % ((m3n - 2) / 4.0, nu2[m3n]))

# worst implied exponent
bmin = min(math.log(nu2[n]) / math.log(n) for n in range(4000, N + 1))
bn = min(range(4000, N + 1), key=lambda n: math.log(nu2[n]) / math.log(n))
print("min log(nu2)/log(n) over [4000,%d] = %.4f at n=%d (nu2=%d)"
      % (N, bmin, bn, nu2[bn]))

# where does (n-2)/4 > n^0.525 first hold?  solve numerically/exactly over ints
n0 = next(n for n in range(1, 10 ** 6) if (n - 2) / 4.0 > n ** 0.525)
print("first n with (n-2)/4 > n^0.525 : %d" % n0)

# and what exponent does (n-2)/4 imply asymptotically?  log(nu2)/log(n) if
# nu2 = (n-2)/4 exactly: 1 - log4/log n -> 1
print("exponent implied by (n-2)/4 : 1 - log(4)/log(n) -> 1 as n -> inf")
