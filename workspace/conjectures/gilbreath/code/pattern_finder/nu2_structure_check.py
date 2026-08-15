#!/usr/bin/env python3
"""Fresh exact check of the nu2/w transfer claims + structure of the
fluctuation sequence F_n = nu2(n) - floor(n/2), over the FULL 30000 dense
terms (code/out/nu2_dense.txt), independent of the prior postprocessors.

Recomputes w(n) = sum of mod-4 switch bits over the ancestor window
hbits[2:n] from the primes themselves (sieve 1e6), so the transfer ratios
and thresholds are recomputed, not re-read.  Then:
  - thresholds: last n with nu2 < c*w, for c in 0.5..0.9
  - min nu2/n over n>=1000 and where
  - F_n sign-run structure: longest deficit run (F<0... using nu2-n/2)
  - increments d_n = nu2(n) - nu2(n-1): distribution, runs, odd/even bias
Writes F (first 512) and d (first 512) to files for the sequence tools.

Exact integers throughout. O(N) after reading nu2_dense.txt.
"""
import math
from lib.gilbreath import primes_up_to

# --- load dense nu2 ---
nu2 = {}
N = 0
with open("code/out/nu2_dense.txt") as f:
    for line in f:
        n, v = map(int, line.split())
        nu2[n] = v
        N = n
print("loaded nu2 for n=1..%d" % N)

# --- recompute mod-4 switch bits and w(n) ---
P = primes_up_to(1_000_000)
print("primes up to 1e6: %d" % len(P))
assert len(P) >= N + 2
# hbits[i] = 1 iff gap g_{i+1} = P[i+1]-P[i] is 2 mod 4  (equiv p_{i+1} !~ p_i mod 4)
hbits = [((P[i + 1] - P[i]) // 2) % 2 for i in range(len(P) - 1)]
# prefix sums for O(1) window sums
pref = [0] * (len(hbits) + 1)
for i, b in enumerate(hbits):
    pref[i + 1] = pref[i] + b

def w(n):
    # sum of hbits[2:n]  (indices 2..n-1), n>=2
    return pref[n] - pref[2]

# --- transfer thresholds ---
print("\n== transfer nu2 >= c*w: last n with violation ==")
for c in [0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9]:
    last = None; ratio_at = None
    nviol = 0
    for n in range(2, N + 1):
        wv = w(n)
        if wv > 0 and nu2[n] < c * wv:
            nviol += 1
            last = n; ratio_at = nu2[n] / float(wv)
    print("c=%.2f : violations=%d  last_violating_n=%s (nu2/w=%.4f there)"
          % (c, nviol, last, ratio_at if ratio_at is not None else -1))

# --- min nu2/n over n>=1000 ---
mn = 1.0; mn_n = 0
for n in range(1000, N + 1):
    r = nu2[n] / float(n)
    if r < mn:
        mn = r; mn_n = n
print("\nmin nu2/n over n>=1000 : %.4f at n=%d" % (mn, mn_n))

# --- the actual theorem-threshold check: nu2 > n^0.525 for n in [4000,N] ---
below = [n for n in range(4000, N + 1) if nu2[n] <= n ** 0.525]
print("n in [4000,%d] with nu2 <= n^0.525 : %d first: %s" % (N, len(below), below[:5]))

# --- fluctuation F_n = nu2 - floor(n/2) ---
F = [nu2[n] - n // 2 for n in range(1, N + 1)]
maxF = max(F); minF = min(F)
maxF_n = F.index(maxF) + 1; minF_n = F.index(minF) + 1
print("\nF_n = nu2 - floor(n/2): min=%d at n=%d, max=%d at n=%d"
      % (minF, minF_n, maxF, maxF_n))

# dev_n = 2*nu2 - n (the signed deviation from n/2)
dev = [2 * nu2[n] - n for n in range(1, N + 1)]
maxdev = max(dev); maxdev_n = dev.index(maxdev) + 1
print("dev = 2*nu2 - n : max=%d at n=%d" % (maxdev, maxdev_n))
neg = sum(1 for v in dev if v < 0)
print("dev<0 on %d/%d = %.1f%% of n" % (neg, N, 100.0 * neg / N))

# sign runs of dev (deficit runs: dev<0)
best_def = 0; best_def_span = None
best_sur = 0; best_sur_span = None
cur = 0; start = None
for n in range(1, N + 1):
    if dev[n - 1] < 0:
        if cur == 0:
            start = n
        cur += 1
        if cur > best_def:
            best_def = cur; best_def_span = (start, n)
    else:
        cur = 0
cur = 0
for n in range(1, N + 1):
    if dev[n - 1] > 0:
        if cur == 0:
            start = n
        cur += 1
        if cur > best_sur:
            best_sur = cur; best_sur_span = (start, n)
    else:
        cur = 0
print("longest deficit run (dev<0): %d at n=%s" % (best_def, best_def_span))
print("longest surplus run (dev>0): %d at n=%s" % (best_sur, best_sur_span))

# --- increments d_n = nu2(n) - nu2(n-1) ---
d = [nu2[n] - nu2[n - 1] for n in range(2, N + 1)]
from collections import Counter
cnt = Counter(d)
print("\nincrements d_n = nu2(n)-nu2(n-1), n=2..%d :" % N)
print("  values: %s" % dict(sorted(cnt.items())))
print("  max consecutive identical increments (longest flat run):")
best_flat = 0; cur = 1
for i in range(1, len(d)):
    if d[i] == d[i - 1]:
        cur += 1
        best_flat = max(best_flat, cur)
    else:
        cur = 1
print("   %d" % best_flat)

# --- write first 512 terms of F and d for the sequence tools ---
with open("code/out/pattern_finder_outputs/F_first512.txt", "w") as f:
    f.write(" ".join(map(str, F[:512])))
with open("code/out/pattern_finder_outputs/d_first512.txt", "w") as f:
    f.write(" ".join(map(str, d[:512])))
print("\nwrote F_first512.txt, d_first512.txt (512 terms each)")

# also: ratio nu2/w at the largest n, for the record
for n in [1000, 5000, 10000, 20000, 30000]:
    wv = w(n)
    print("n=%6d nu2=%6d w=%6d nu2/w=%.4f nu2/n=%.4f" %
          (n, nu2[n], wv, nu2[n] / wv, nu2[n] / n))
