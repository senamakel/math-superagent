#!/usr/bin/env python3
"""Exact worst-case statistics over the full 30000 dense terms, focused on
the structure the run's derivation would need:

(1) w(n) = # mod-4 switches among gaps 2..n-1, i.e. # i in [2,n-1] with
    gap_i = 2 (mod 4).  Check whether w(n) >= (n-2)/2 holds for every n
    (switch density > 1/2 is the Lemke-Oliver-Soundararajan bias direction:
    consecutive primes switching residue class mod 4 more often than staying).

(2) The combined supply bound: nu2 >= (1/2)*w for n>=17 (transfer, exact over
    data) + w >= (n-2)/2  =>  nu2 >= (n-2)/4.  Check the implied bound on
    every n >= 17.

(3) Exact minima for the theorem threshold: min nu2/n over n>=4000 (where),
    min nu2/n^0.525 over n>=4000 (where), max |2nu2-n|/sqrt(n log n) (where),
    min nu2/w over n>=17 and n>=1000 (where).

All exact integers / exact rational arithmetic; floats only for ratios.
"""
import math

# --- load dense nu2 ---
nu2 = {}
N = 0
with open("code/out/nu2_dense.txt") as f:
    for line in f:
        n, v = map(int, line.split())
        nu2[n] = v
        N = n

from lib.gilbreath import primes_up_to
P = primes_up_to(1_000_000)
assert len(P) >= N + 2
hbits = [((P[i + 1] - P[i]) // 2) % 2 for i in range(len(P) - 1)]
pref = [0] * (len(hbits) + 1)
for i, b in enumerate(hbits):
    pref[i + 1] = pref[i] + b

def w(n):
    return pref[n] - pref[2]   # sum hbits[2..n-1]

print("== exact worst-case statistics, n <= %d ==" % N)

# (1) w(n) >= (n-2)/2 ?
bad_w = [n for n in range(2, N + 1) if 2 * w(n) < (n - 2)]
print("w(n) >= (n-2)/2 for ALL n in [2,%d]: %s (violations: %d, first %s)"
      % (N, "YES" if not bad_w else "NO", len(bad_w), bad_w[:5]))
# w(n)/n range over n>=1000
min_wr = min(w(n) / n for n in range(1000, N + 1))
max_wr = max(w(n) / n for n in range(1000, N + 1))
print("w(n)/n over n>=1000: min=%.4f max=%.4f" % (min_wr, max_wr))

# (2) combined: nu2 >= (n-2)/4 for n >= 17 ?
bad_c = [n for n in range(17, N + 1) if 4 * nu2[n] < (n - 2)]
print("nu2 >= (n-2)/4 for ALL n in [17,%d]: %s (violations: %d, first %s)"
      % (N, "YES" if not bad_c else "NO", len(bad_c), bad_c[:5]))
# implied exponent at the worst such n: min over n>=17 of log(nu2)/log(n)
bmin = min(math.log(nu2[n]) / math.log(n) for n in range(17, N + 1) if nu2[n] > 0)
bn = min(range(17, N + 1), key=lambda n: math.log(nu2[n]) / math.log(n) if nu2[n] > 0 else 9)
print("min log(nu2)/log(n) over n in [17,%d]: %.4f at n=%d (nu2=%d)"
      % (N, bmin, bn, nu2[bn]))

# (3) theorem-threshold statistics
mn_ratio = 1.0; mn_n = 0
for n in range(4000, N + 1):
    r = nu2[n] / n
    if r < mn_ratio:
        mn_ratio = r; mn_n = n
print("\nmin nu2/n over n in [4000,%d]: %.4f at n=%d (nu2=%d)"
      % (N, mn_ratio, mn_n, nu2[mn_n]))

marg = 1e9; marg_n = 0
for n in range(4000, N + 1):
    v = nu2[n] / (n ** 0.525)
    if v < marg:
        marg = v; marg_n = n
print("min nu2/n^0.525 over n in [4000,%d]: %.3f at n=%d" % (N, marg, marg_n))

wdev = 0.0; wdev_n = 0
for n in range(1000, N + 1):
    v = abs(2 * nu2[n] - n) / math.sqrt(n * math.log(n))
    if v > wdev:
        wdev = v; wdev_n = n
print("max |2nu2-n|/sqrt(n log n) over n in [1000,%d]: %.3f at n=%d"
      % (N, wdev, wdev_n))

mnw = 1.0; mnw_n = 0
for n in range(17, N + 1):
    wv = w(n)
    if wv > 0:
        r = nu2[n] / wv
        if r < mnw:
            mnw = r; mnw_n = n
print("min nu2/w over n in [17,%d]: %.4f at n=%d" % (N, mnw, mnw_n))
mnw2 = 1.0; mnw2_n = 0
for n in range(1000, N + 1):
    wv = w(n)
    if wv > 0:
        r = nu2[n] / wv
        if r < mnw2:
            mnw2 = r; mnw2_n = n
print("min nu2/w over n in [1000,%d]: %.4f at n=%d" % (N, mnw2, mnw2_n))

# smallest nu2/w ratio at all, over n>=2 with w>0 (record the transfer's worst)
mnwa = 1.0; mnwa_n = 0
for n in range(2, N + 1):
    wv = w(n)
    if wv > 0:
        r = nu2[n] / wv
        if r < mnwa:
            mnwa = r; mnwa_n = n
print("min nu2/w over ALL n in [2,%d] with w>0: %.4f at n=%d" % (N, mnwa, mnwa_n))

# implied threshold: how small a c in nu2 >= c*w survives on n>=4000?
last = None
for n in range(4000, N + 1):
    wv = w(n)
    if wv > 0 and nu2[n] < 0.8 * wv:
        last = n
print("last n in [4000,%d] with nu2 < 0.8*w : %s" % (N, last))
