#!/usr/bin/env python3
"""Test the honest-language hypothesis: is the reachable-histogram set at each N
EXACTLY the set of walks (a_0=0, ..., a_M=3) that (a) use only observed
transitions, (b) have total sum 2N+1, (c) end value 3?

If so, D(N) = weighted sum over these walks with per-level weights, and the
whole problem is a polynomial (finite-state, sum-constrained) walk DP."""
import glob, collections, itertools

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

# observed transitions (union over all N) = finite-state alphabet hypothesis
trans = set()
for n, hs in all_hists.items():
    for h in hs:
        for k in range(len(h)-1):
            trans.add((h[k], h[k+1]))

# Also test: does simply bounding the jump to <=4 suffice? Build transition
# set as ALL pairs with |a-b|<=4 among values 0..8 to test 'max-jump' hypothesis.
trans_jump4 = set((a,b) for a in range(0,9) for b in range(0,9) if abs(a-b)<=4)

def enumerate_walks(maxlen, transet, target_sum):
    """All walks a_0=0,...,a_L=3, length <= maxlen, using transet, sum==target_sum.
    Bounded: force last == 3. This is just for cross-check on small N."""
    res = []
    def rec(cur, L, s, path):
        if L > maxlen: return
        if cur == 3 and s == target_sum:
            res.append(tuple(path))
            return
        if s > target_sum: return
        for nxt in range(0,9):
            if (cur, nxt) in transet:
                rec(nxt, L+1, s+nxt, path+[nxt])
    rec(0,0,0,[0])
    return set(res)

for n in sorted(all_hists):
    hs = all_hists[n]
    S = 2*n+1
    # honest-language using observed transitions (bounded length by max hist len)
    found_obs = enumerate_walks(13, trans, S)
    eq_obs = (found_obs == hs)
    # max-jump-4 language
    found_j4 = enumerate_walks(13, trans_jump4, S)
    eq_j4 = (found_j4 == hs)
    print(f"N={n}: S={S} reachable_h={len(hs)} "
          f"walk_obs={len(found_obs)} eq_obs={eq_obs} "
          f"walk_jump4={len(found_j4)} eq_jump4={eq_j4}")
    if not eq_obs and n<=5:
        extra = found_obs - hs
        missing = hs - found_obs
        print("   EXTRA (in walk, not reachable):", sorted(extra)[:5])
        print("   MISSING (reachable, not in walk):", sorted(missing)[:5])
