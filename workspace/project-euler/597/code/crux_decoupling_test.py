#!/usr/bin/env python3
"""Crux test: does the race's final relative order DECOUPLE across the root?

Questions, all answered by the TRUE race oracle (no treap assumption):

  D1. parity(left) = sub-race parity of boats [a..r-1] ALONE?  (decoupling)
  D2. parity(right) = sub-race parity of boats [r+1..b] ALONE?
  D3. cross = #(left,right) inverted pairs in FINAL permutation =
      |left|*|right| ?   (the specific 'always = L*R' claim)
  D4. does cross depend only on the root identity r?

We take root r = argmin_i W_i = v_i/(L-40i) over the full range [0,n-1], per
the library. parity(left) for the recursion = inv count of the FINAL
permutation restricted to left-indices, mod 2. Sub-race parity = oracle on the
corresponding contiguous slice with same geometry. Compare.
"""
import sys, os, random
from collections import defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brute import simulate_order, outcome_parity, parity_of_new_order


def W(speeds, L, i):
    return speeds[i] / (L - 40.0 * i)


def analyze(n, L, speeds):
    above = simulate_order(n, L, speeds)
    par, order = parity_of_new_order(n, above)
    r = min(range(n), key=lambda i: W(speeds, L, i))
    left = list(range(r))
    right = list(range(r + 1, n))
    # inversions within left subset of the full final permutation
    def inv_of_subset(sub):
        pos = {boat: i for i, boat in enumerate(order)}
        c = 0
        for x in range(len(sub)):
            for y in range(x + 1, len(sub)):
                i, j = sub[x], sub[y]
                if i < j and pos[i] > pos[j]:
                    c += 1
        return c % 2
    pinv_left = inv_of_subset(left) if len(left) >= 2 else 0
    pinv_right = inv_of_subset(right) if len(right) >= 2 else 0
    # sub-race oracle parity for each slice
    subleft = outcome_parity(len(left), L, speeds[:r]) if len(left) >= 2 else 0
    subright = outcome_parity(len(right), L, speeds[r + 1:]) if len(right) >= 2 else 0
    # true cross: inverted left-right pairs in final permutation
    cross = 0
    for i in left:
        for j in right:
            if i < j and j in above[i]:
                cross += 1
    d1 = (pinv_left == subleft)
    d2 = (pinv_right == subright)
    d3 = (cross == len(left) * len(right))
    # recursion with TRUE cross and TRUE sub-race parities:
    rec_par = (subleft + subright + cross) % 2
    d4 = (rec_par == par)
    return r, d1, d2, d3, d4, cross


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 300000
    rng = random.Random(777)
    for (n, L) in [(3, 160.0), (4, 160.0), (4, 400.0), (5, 400.0), (5, 1800.0)]:
        d1b = d2b = d3b = d4b = 0
        per_root = defaultdict(set)
        for _ in range(N):
            speeds = [rng.expovariate(1.0) for _ in range(n)]
            r, d1, d2, d3, d4, cross = analyze(n, L, speeds)
            if not d1: d1b += 1
            if not d2: d2b += 1
            if not d3: d3b += 1
            if not d4: d4b += 1
            per_root[r].add(cross)
        print(f"n={n} L={L}:")
        print(f"  D1 left sub-range parity == sub-race: {'OK' if d1b==0 else str(d1b)+' FAIL'}")
        print(f"  D2 right sub-range parity == sub-race: {'OK' if d2b==0 else str(d2b)+' FAIL'}")
        print(f"  D3 cross == |L|*|R| : FAIL in {d3b}/{N}")
        print(f"  D4 recursion(true cross,true sub-race) == full parity: "
              f"{'OK' if d4b==0 else str(d4b)+' FAIL'}")
        multi = {k: v for k, v in per_root.items() if len(v) > 1}
        print(f"  D-cross-per-root: roots with multiple cross values: "
              f"{len(multi)} {dict(multi) if multi else ''}")


if __name__ == '__main__':
    main()
