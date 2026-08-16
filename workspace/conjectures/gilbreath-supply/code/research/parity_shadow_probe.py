#!/usr/bin/env python3
"""Probe the parity-shadow candidate (Kruskal-Katona / Harper) central claim.

Question: is the parity shadow of a 'spread' subset S' of the Boolean lattice
linear in n? The parity shadow is exactly the fold weight:

    T(n,d) = |S' ∩ down(d)| mod 2 = XOR_{u submasks of d} h'[n-1-...]
    nu2(S') = #{ d in [2,n-1] : |S' ∩ down(d)| odd }.

where S' = reflected switch positions. We use lib.supply_fold.s_sos on the
indicator string (= h with 1s at the positions of S').

The candidate's falsifier: if a SPREAD set S' (full popcount histogram) has
nu2 = o(n), the shadow bound cannot work. We test random subsets with
various densities and popcount distributions at m = 5..7 (n ~ 2^m).
"""
import random
from lib.supply_fold import s_sos


def parity_shadow(m, S):
    """Parity shadow size for a subset S of the m-cube, using the fold.
    S is a set of integers in [0, 2^m - 1]. n = 2^m so the operative range
    d in [2, n-1] is essentially the whole cube minus 0,1.
    h[j] = 1 iff j in S."""
    n = 1 << m
    h = [0] * n
    for j in S:
        if 0 <= j < n:
            h[j] = 1
    _, ones = s_sos(n, h)
    return ones


def main():
    random.seed(12345)
    print("m | n | type | |S| | density | nu2/n | nu2 (linear?)")
    for m in (5, 6, 7):
        n = 1 << m
        # single point at various popcounts
        for p in range(0, m + 1):
            # a point with exactly p bits set: 2^p-1 has p bits (bits 0..p-1)
            u = (1 << p) - 1 if p else 0
            v = parity_shadow(m, {u})
            # expected: upset of u inside [2,n-1], size 2^{m-p} minus the
            # elements < 2 (d=0,1 excluded) and accounting d>=2
            print(f"{m} | {n} | single pc{p} | 1 | {1/n:.4f} | {v/n:.4f} | v={v}")
        # full-spread random sets at several densities
        for dens in (0.2, 0.5, 0.8):
            trials = 8
            for t in range(trials):
                S = {j for j in range(n) if random.random() < dens}
                v = parity_shadow(m, S)
                print(f"{m} | {n} | random d{dens}t{t} | {len(S)} | {len(S)/n:.4f} | {v/n:.4f} | v={v}")
        # adversarial: a set engineered to cancel - take two upsets that overlap
        # exactly on a large region. e.g. S = {a, b} where b is 'just below' a.
        # Also: S = full set minus small = indicator nearly all-ones.
        Sfull = set(range(n))
        v = parity_shadow(m, Sfull)
        print(f"{m} | {n} | all-ones | {n} | 1.0 | {v/n:.4f} | v={v}")


if __name__ == "__main__":
    main()
