"""Exact checks of the block structure of PE156 fixed-point sets.

Reads the run's complete per-digit solution files (produced by code/solution.py,
cross-checked by code/verify.py and the brute oracle) and tests, for every
digit d = 1..9 and EVERY solution in the files:

  (B1) S_d == disjoint union over k=0..d-1 of {k*10^10 + x : x in block0}
       where block0 = S_d intersect [0, 10^10)   (sorted set equality)
  (B2) k*10^10 is a solution of f(n,d)=n  <=>  0 <= k <= d-1
  (B3) counts(d) = d * N0(d)   (the OEIS A130432 divisibility-by-d fact,
       re-derived from the run's own data)
  (B4) s(d) = d*S0 + (d-1)*d/2 * 10^10 * N0
       (closed form: block k contributes k*10^10 per block-0 solution x,
       so s(d) = sum_k sum_x (k*10^10 + x) )

Also reports the derived sequences N0(d), S0(d), and the last solution of
each block (block maxima), plus run-length structure of block-0 solutions
(consecutive-run sizes, matching the OEIS "runs of ten / pairs / isolated"
description for d=1, computed here for every d).
"""
import os
from collections import defaultdict

BASE = "/workspace/code/out"
reported = {1:22786974071,2:73737982962,3:372647999625,4:741999999540,
            5:100000000000,6:2434703999430,7:1876917059570,
            8:15312327487352,9:360000000000}

all_ok = True
N0s, S0s = [], []
MAXES = {}
print(f"{'d':>2} {'N0':>4} {'S0':>14} {'blocks':>8}  B1  B2  B3  B4")
for d in range(1, 10):
    sols = sorted(int(x) for x in open(f"{BASE}/solutions-d{d}.txt").read().split())
    # sanity: sorted, unique
    assert sols == sorted(set(sols)), f"d={d}: solution file not sorted-unique"
    block0 = [x for x in sols if x < 10**10]
    S0 = sum(block0); N0 = len(block0)
    N0s.append(N0); S0s.append(S0)

    # B1: group by block index; blocks present should be 0..d-1
    grp = defaultdict(list)
    for n in sols: grp[n // 10**10].append(n)
    ks = sorted(grp)
    B1 = (ks == list(range(d)))
    B1b = all(grp[k] == sorted([k*10**10 + x for x in block0]) for k in ks)
    B1c = (len(sols) == d * N0)
    B1 = B1 and B1b and B1c

    # B2: k*10^10 in S_d iff k <= d-1  (check k=0..9)
    Sset = set(sols)
    B2 = all((k*10**10 in Sset) == (k <= d-1) for k in range(10))

    # B3
    B3 = (len(sols) == d * N0)

    # B4
    decomp = d*S0 + ((d-1)*d//2) * 10**10 * N0
    B4 = (decomp == reported[d])
    assert B4 == (decomp == sum(sols)), f"d={d}: reported sum mismatch"

    ok = B1 and B2 and B3 and B4
    all_ok &= ok
    MAXES[d] = sols[-1]
    print(f"{d:>2} {N0:>4} {S0:>14} {ks!s:>18}  {B1!s:>2}  {B2!s:>2}  {B3!s:>2}  {B4!s:>2}")

print("\nAll block-structure checks (B1-B4) hold for every digit:", all_ok)

# run-length structure of the block-0 solution sets
print("\nBlock-0 solutions grouped into maximal consecutive runs (run length -> count):")
for d in range(1, 10):
    sols = sorted(int(x) for x in open(f"{BASE}/solutions-d{d}.txt").read().split())
    block0 = sorted(x for x in sols if x < 10**10)
    runs = []
    start = prev = block0[0]
    for x in block0[1:]:
        if x == prev + 1:
            prev = x
        else:
            runs.append((start, prev)); start = prev = x
    runs.append((start, prev))
    from collections import Counter
    lens = Counter(b - a + 1 for a, b in runs)
    print(f"  d={d}: {len(block0):>3} b0-sols, {len(runs)} runs, run lengths {dict(sorted(lens.items()))}")

print("\nDerived sequences (d=1..9):")
print("  N0(d) =", N0s)
print("  S0(d) =", S0s)
print("  last solution per digit =", [MAXES[d] for d in range(1,10)])
print("  last block-0 solution  =", [max(int(x) for x in open(f'{BASE}/solutions-d{d}.txt').read().split() if x.strip() and int(x) < 10**10) for d in range(1,10)])