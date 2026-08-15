#!/usr/bin/env python3
"""Independent second-route verification of the dense nu2<->w transfer to 1e5.

Uses lib.rightdiag.delta_diagonal (a DIFFERENT code path from the incremental
in-place loop in nu2_dense_transfer_1e5.py) to recompute nu2 at
  - the n>=4000 min-ratio point (reported n=4278, ratio 0.800473),
  - the n>=17 min-ratio point (reported n=44, ratio 0.5),
  - several n>=4000 samples where the 0.75 bound must hold,
  - the n=44, n=1005 reference points.
Cross-checks w(n) from the same mod-4 bits.  Exact integers.
"""
import math
from lib.gilbreath import primes_up_to
from lib.rightdiag import cycle_and_nu2, delta_diagonal

P = primes_up_to(1_500_000)
hbits = [((P[i + 1] - P[i]) // 2) % 2 for i in range(len(P) - 1)]
WS = [0] * (len(hbits) + 1)
for i in range(len(hbits)):
    WS[i + 1] = WS[i] + hbits[i]

def w(n):
    return WS[n] - WS[2]

def nu2_at(n):
    d = delta_diagonal(P, n - 1)   # delta(q_n), length n
    return cycle_and_nu2(d)[1]

# reported points
points = {44, 1005, 4278, 4000, 5000, 10000, 50000, 100000, 30000, 70000}
print("%-8s %-7s %-7s %-9s %-9s" % ("n", "nu2", "w", "nu2/w", "0.5b/0.75b"))
for n in sorted(points):
    nu2 = nu2_at(n)
    wn = w(n)
    r = nu2 / float(wn)
    ok5 = (2 * nu2 >= wn)
    ok75 = (4 * nu2 >= 3 * wn)
    print("%-8d %-7d %-7d %-9.5f %-9s" % (n, nu2, wn, r,
          "0.5:%s" % ok5 if n < 17 else "0.5:%s" % ok5 + " 0.75:%s" % ok75))

# exact-min-ratio search over n>=4000 via delta_diagonal for a dense sample
# (delta_diagonal is O(N^2) per call, so sample every 5th n only as a check
#  on the shape, not a replacement for the exhaustive incremental run)
print("\nsampled n>=4000 min ratio (every 10th n):")
best = (1e9, 0)
for n in range(4000, 100001, 10):
    nu2 = nu2_at(n)
    wn = w(n)
    if wn > 0:
        r = nu2 / float(wn)
        if r < best[0]:
            best = (r, n)
        if 4 * nu2 < 3 * wn:
            print("  !!! 0.75 violation at n=%d nu2=%d w=%d" % (n, nu2, wn))
print("  sampled min ratio n>=4000: %.6f at n=%d" % (best[0], best[1]))
