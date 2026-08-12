#!/usr/bin/env python3
"""Fast DP test of the honest-language hypothesis.

Language hypothesis: reachable histograms at N are exactly the walks
(0=a_0,...,a_M=3) with (i) consecutive pairs in a transition set T,
(ii) total sum 2N+1. Test with T = observed union transition set, and
T = all pairs with |a-b|<=4 (jump-4 language).

Uses a DP by (last value, total sum, length) and counts/collects walks of a
given sum when last value == 3.  Exact integer arithmetic. Track counts; for
mismatch diagnosis on small N also collect actual walk sets by memoized
set-recursion capped at length 13.
"""
import glob, collections, functools

def sorted_key(p):
    return int(p.split('level_')[1].split('.')[0])

all_hists = {}
for path in sorted(glob.glob('data/level_*.txt'), key=sorted_key):
    n = sorted_key(path)
    hs = set()
    for line in open(path):
        hist, M, bbox = line.rstrip().split('|')
        hs.add(tuple(map(int, hist.strip().split())))
    all_hists[n] = hs

trans = set()
for n, hs in all_hists.items():
    for h in hs:
        for k in range(len(h)-1):
            trans.add((h[k], h[k+1]))

trans_jump4 = set((a,b) for a in range(0,9) for b in range(0,9) if abs(a-b)<=4)

def count_walks(T, target_sum, maxlen):
    """DP: number of walks (0->...->3) using T, length<=maxlen, sum==target_sum.
    Returns dict sum->count."""
    # dp[val] = dict sum->count for walks ending at val at current length
    dp = collections.defaultdict(int)
    dp[(0,0)] = 1   # (last_val, sum)
    total = 0
    for length in range(1, maxlen+1):
        ndp = collections.defaultdict(int)
        for (v, s), c in dp.items():
            for nxt in range(0,9):
                if (v, nxt) in T:
                    ns = s + nxt
                    if ns > target_sum: continue
                    ndp[(nxt, ns)] += c
        dp = ndp
        # walks of exactly this length ending at 3
        for (v, s), c in dp.items():
            if v == 3 and s == target_sum:
                total += c
    return total

for n in sorted(all_hists):
    S = 2*n+1
    hs = all_hists[n]
    c_obs = count_walks(trans, S, 13)
    c_j4 = count_walks(trans_jump4, S, 13)
    print(f"N={n}: reachable_h={len(hs)}  walks_obs={c_obs}  eq={c_obs==len(hs)}   "
          f"walks_jump4={c_j4}  eq={c_j4==len(hs)}")