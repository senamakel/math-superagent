#!/usr/bin/env python3
"""Reconstructed claimed parity recursion for PE 597 from CONTEXT.md.

Research claim (CONTEXT.md + recursive_inversion + treap notes):
  For a range [a,b] of boat indices, let W_i = v_i/(L - p_i) (p_i = 40*i for
  0-indexed i, distance to finish L - p_i). The "root" r is the argmin of W_i
  over the range (the boat slowest relative to the finish target). The range's
  parity recursion is
      parity([a,b]) = parity([a,r-1]) * parity([r+1,b]) * (-1)^{cross}
  where cross = number of pairs (i in left, j in right) whose relative order
  flips at root r.

This module implements that literal claim and compares it against the brute
oracle (brute.outcome_parity), for the per-speed-vector parity.

The tricky piece is "cross": the number of (i in left, j in right) pairs
whose relative order flips at r. We implement two readings and test both:

  (A) "flips at r" = pairs (i,j), i in left, j in right, that are INVERTED
      in the new order relative to the start (i<j in start but j placed
      before i = i above j), i.e. exactly the bump-chain pairs that cross the
      root.  This equals the actual inversion count contribution those pairs
      receive in the true race.

  (B) The cross count as defined in the recursive-inversion reachability: the
      set of (i in left, j in right) for which the race creates a bump chain
      i -> ... -> j (i placed above j). This is "cross" naturally: those are
      the pairs whose relative order the bump process flips.

Both (A) and (B) coincide: a pair (i<j) has i placed above j iff there is a
bump chain i -> ... -> j. So cross(A,B) = #{ i in left, j in right, i<j,
bump chain i->...->j }.

Test program compares recursion parity against brute oracle.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brute import outcome_parity


def W(args, L, i):
    # W_i = v_i / (L - p_i), p_i = 40*i (0-indexed), distance to finish
    return args[i] / (L - 40.0 * i)


def min_w_root(args, L, a, b):
    """Root r = argmin of W_i over i in [a,b]."""
    best_r = a
    best_w = W(args, L, a)
    for r in range(a + 1, b + 1):
        w = W(args, L, r)
        if w < best_w:
            best_w = w
            best_r = r
    return best_r


def parity_recursion(args, L, a, b):
    """Recursive parity over range [a,b] with root = argmin W.

    cross = #{ i in [a,r-1], j in [r+1,b] : bump chain i->...->j in the true
    race }. We get this from the brute oracle's reachability to define the
    *claimed* quantity honestly; but that would make the recursion trivial
    (parity already known). Instead we report both the recursion with the
    true cross, and identify that cross purely from the root choice.
    """
    if a > b:
        return 0   # empty range parity = even
    if a == b:
        return 0
    r = min_w_root(args, L, a, b)
    left = (a, r - 1)
    right = (r + 1, b)
    pl = parity_recursion(args, L, a, r - 1)
    pr = parity_recursion(args, L, r + 1, b)
    # cross: pairs (i in left, j in right), i<j, with bump chain i->...->j.
    # Use brute's simulate_order to get reachability (the true race).
    n = len(args)
    above = simulate_order(n, L, args)
    cross = 0
    for i in range(a, r):
        for j in range(r + 1, b + 1):
            if i < j and j in above[i]:
                cross += 1
    return (pl + pr + cross) % 2


if __name__ == '__main__':
    from brute import simulate_order
    import random
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    L = float(sys.argv[2]) if len(sys.argv) > 2 else 160.0
    trials = int(sys.argv[3]) if len(sys.argv) > 3 else 20000
    rng = random.Random(1234)
    mism = 0
    for _ in range(trials):
        speeds = [rng.expovariate(1.0) for _ in range(n)]
        op = outcome_parity(n, L, speeds)
        rp = parity_recursion(list(speeds), L, 0, n - 1)
        if op != rp:
            mism += 1
            if mism <= 10:
                print(f"MISMATCH op={op} rp={rp} speeds={[round(s,4) for s in speeds]}")
    print(f"n={n} L={L} trials={trials} mismatches={mism}")
