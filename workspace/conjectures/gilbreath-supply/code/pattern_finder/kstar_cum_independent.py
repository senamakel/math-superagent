#!/usr/bin/env python3
"""Independent check of the cumulative-fiber K*(n) = floor(n/2) claim.

Definition (cumulative / nested, the faithful reading of 'C_1..C_K'):
  C_K(h) = tuple of (K+1)-gram histograms C_1(h),...,C_K(h).
  A 'witness at K' = two strings in one cumulative C_K-fiber with different S^2.
  K*(n) = min{K>=1 : S^2 constant on every cumulative C_K-fiber}.

Because CUM_{K+1} refines CUM_K, the no-witness property is inherited upward,
so K* is a genuine monotone threshold (unlike the single-histogram reading).

The catalogued captures (kstar_exact, kstar_settle) report
    K*(n) = floor(n/2)  for n=2..16   (nested: 1,1,2,2,3,3,4,4,5,5,6,6,7,7,8)
This script re-derives it with an INDEPENDENT brute and extends to the first
terms not yet measured: n=17 (floor=8) and n=18 (floor=9).  A single mismatch
at n=17 or 18 falsifies the closed form; matching both is a conjecture still
(hypothesis: floor(n/2) for all n).

S^2 computed via the canonical s_sos (floored fold d in [2,n-1]), cross-checked
on 200 random (n,h) against a direct submask-XOR oracle inline.
"""
import sys, time, random
sys.path.insert(0, "/workspace/code")
from lib.supply_fold import s_sos

def s2_of_int(n, g):
    h = [(g >> i) & 1 for i in range(n)]
    S, _ = s_sos(n, h)
    return S * S

def cum_key(n, g, K):
    """Cumulative fiber key: tuple of histograms C_1..C_K."""
    key = []
    for kk in range(1, K + 1):
        counts = {}
        w = 0
        for t in range(kk + 1):
            w = (w << 1) | ((g >> t) & 1)
        counts[w] = 1
        for i in range(1, n - kk):
            w = ((w << 1) | ((g >> (i + kk)) & 1)) & ((1 << (kk + 1)) - 1)
            counts[w] = counts.get(w, 0) + 1
        key.append(tuple(sorted(counts.items())))
    return tuple(key)

def has_cum_witness(n, K, s2cache):
    seen = {}
    for g in range(1 << n):
        s2 = s2cache[g] if s2cache is not None else s2_of_int(n, g)
        key = cum_key(n, g, K)
        prev = seen.get(key)
        if prev is None:
            seen[key] = s2
        elif prev != s2:
            return True
    return False

def kstar_cum(n):
    for K in range(1, n):
        if not has_cum_witness(n, K, None):
            return K
    return n

# cross-check the oracle inline on 200 random (n,h)
random.seed(12345)
for _ in range(200):
    n = random.randint(2, 60)
    h = [random.randint(0, 1) for _ in range(n)]
    S1, _ = s_sos(n, h)
    # direct submask oracle
    S2 = 0
    for d in range(2, n):
        t = 0
        o = d
        while True:
            t ^= h[n - 1 - d + o]
            if o == 0:
                break
            o = (o - 1) & d
        S2 += (-1) ** t
    assert S1 == S2, (n, S1, S2)
print("oracle cross-check on 200 random (n,h): ALL AGREE")

for n in range(2, 19):
    t0 = time.time()
    s2cache = [s2_of_int(n, g) for g in range(1 << n)]
    k = kstar_cum(n)
    fl = n // 2
    print(f"n={n:3d} K*_cum={k:3d} floor(n/2)={fl:3d} "
          f"{'MATCH' if k==fl else 'FALSIFIED'!r} ({time.time()-t0:.1f}s)", flush=True)
