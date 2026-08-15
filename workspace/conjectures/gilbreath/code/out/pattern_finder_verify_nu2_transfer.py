#!/usr/bin/env python3
"""Independent verification of the nu2 transfer/fluctuation claims, from the
on-disk exact data (nu2_dense.txt = exact nu2(n), recomputed sieve for w(n)).

Checks, all exact over the 30000 supplied terms:
  (1) transfer lower bounds: nu2 >= c*w(n) for c in {0.5 (n>=17), 0.75,
      and the pointwise min ratio},
      w(n) = Hamming weight of halved mod-4 gap bits over j in [2,n-1].
  (2) fluctuation concentration |2*nu2 - n| <= C*sqrt(n) (report: C=5 max).
  (3) supply-beta check nu2 > n^0.525 on n in [4000, 30000].
  (4) does nu2 >= n/2 - sqrt(n log n) hold? (deviation margin)
"""
import math
from lib.gilbreath import primes_up_to

NMAX = 30000
P = primes_up_to(1_000_000)
assert len(P) > NMAX + 2

# halved mod-4 gap bits, hbits[i] = bit of gap g_{i+1} (i.e. g_{i+1}==2 mod4)
hbits = [((P[i+1] - P[i]) // 2) % 2 for i in range(len(P) - 1)]
# prefix sums of hbits for fast interval queries
pref = [0]*(len(hbits)+1)
for i, b in enumerate(hbits):
    pref[i+1] = pref[i] + b
def w(n):
    # sum over j in [2, n-1]: hbits[j] corresponds to j-th index => pref[n] - pref[2]
    return pref[n] - pref[2]   # pref index = count of first idx entries; hbits[2..n-1] = pref[n]-pref[2]

# read nu2
nu2 = []
with open("code/out/nu2_dense.txt") as f:
    for line in f:
        parts = line.split()
        if len(parts) == 2:
            nu2.append(int(parts[1]))
assert len(nu2) == NMAX, len(nu2)

print(f"loaded {NMAX} terms of nu2, w window = hbits[2..n-1]")

# (1) transfer
min_ratio_all = (1e9, 0)
min_ratio_17 = (1e9, 0)
viol_05 = []; viol_075 = []; viol_075_from1005 = []
for n in range(2, NMAX+1):
    wn = w(n)
    if wn > 0:
        r = nu2[n-1]/wn
        if r < min_ratio_all[0]: min_ratio_all = (r, n)
        if n >= 17 and r < min_ratio_17[0]: min_ratio_17 = (r, n)
        if nu2[n-1] < 0.5*wn and n >= 17: viol_05.append(n)
        if nu2[n-1] < 0.75*wn: viol_075.append(n)
        if n >= 1005 and nu2[n-1] < 0.75*wn: viol_075_from1005.append(n)
print("min nu2/w over ALL n:", min_ratio_all)
print("min nu2/w over n>=17:", min_ratio_17)
print("nu2<0.5w for n>=17: count=%d first=%s" % (len(viol_05), viol_05[:5]))
print("nu2<0.75w for n>=2: count=%d first=%s" % (len(viol_075), viol_075[:5]))
print("nu2<0.75w for n>=1005: count=%d first=%s" % (len(viol_075_from1005), viol_075_from1005[:5]))

# (2) fluctuation
max_fluc_over_sqrt = (0, 0)  # (value, n)
max_absdev = (0, 0)
max_fluc_over_sqrtern = (0,0)
min_margin_nlogn = (1e9, 0)
for n in range(1000, NMAX+1):
    dev = 2*nu2[n-1] - n
    if abs(dev) > max_absdev[0]: max_absdev = (abs(dev), n)
    r = abs(dev)/math.sqrt(n)
    if r > max_fluc_over_sqrt[0]: max_fluc_over_sqrt = (r, n)
    r2 = abs(dev)/math.sqrt(n*math.log(n))
    if r2 > max_fluc_over_sqrtern[0]: max_fluc_over_sqrtern = (r2, n)
    margin = nu2[n-1] - (n/2 - math.sqrt(n*math.log(n)))
    if margin < min_margin_nlogn[0]: min_margin_nlogn = (margin, n)
print("max_abs_dev(2nu2-n) n>=1000: %.1f at n=%d" % max_absdev)
print("max |2nu2-n|/sqrt(n) n>=1000: %.3f at n=%d" % max_fluc_over_sqrt)
print("max |2nu2-n|/sqrt(n log n) n>=1000: %.3f at n=%d" % max_fluc_over_sqrtern)
print("min of (nu2 - (n/2 - sqrt(n log n))): %.2f at n=%d (positive => nu2+sqrt(nlogn) > n/2 always)" % min_margin_nlogn)

# (3) supply-beta
below = [n for n in range(4000, NMAX+1) if nu2[n-1] <= n**0.525]
print("n in [4000,30000] with nu2 <= n^0.525: %d first=%s" % (len(below), below[:5]))
# also margin: min nu2/n^0.525
minbeta = (1e9, 0)
for n in range(4000, NMAX+1):
    r = nu2[n-1]/n**0.525
    if r < minbeta[0]: minbeta = (r, n)
print("min nu2/n^0.525 over n>=4000: %.3f at n=%d" % minbeta)
