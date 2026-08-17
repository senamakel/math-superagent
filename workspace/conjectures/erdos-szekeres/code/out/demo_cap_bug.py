#!/usr/bin/env python3
"""Minimal demonstrator of the longest_cap skip-bug in lib.es_geom.

The DP stores best[i] = best cup/cap ENDING AT i and returns max over i, but a
cup/cap is a SUBSET and may legitimately skip points: the best chain ending at
i need not be obtained by appending i to the best chain ending at each j,
because "best ending at j" keeps a particular last slope, and a longer chain
for j with a worse last slope may be the one that extends.  Also the final max
over best[i] is taken as if the chain must END at i -- but a cup/cap does not
need to end anywhere special, so the best-so-far must be carried forward.

Construct a set where the bug bites: points on a convex arc, so the WHOLE set
is a cap of length m.  longest_cap should return m, but if the DP cannot skip
and/or loses the best-so-far it returns less.
"""
from fractions import Fraction
from itertools import combinations
from lib.es_geom import longest_cap, longest_cup


def brute_cap(S):
    pts = sorted(S, key=lambda p: p[0])
    m = len(pts)
    for r in range(m, 1, -1):
        for comb in combinations(range(m), r):
            ok = all((pts[comb[t+1]][1]-pts[comb[t]][1])/(pts[comb[t+1]][0]-pts[comb[t]][0])
                     > (pts[comb[t+2]][1]-pts[comb[t+1]][1])/(pts[comb[t+2]][0]-pts[comb[t+1]][0])
                     for t in range(r-2))
            if ok:
                return r
    return 0


# convex arc: y = 3 + 3i - i^2 -> slopes 3-2i-1 = ... decreasing => whole set a cap
S = [(Fraction(i), Fraction(3) + Fraction(3)*i - i*i) for i in range(5)]
print("convex arc (descending slopes), 5 pts:")
print("  brute cap =", brute_cap(S), " lib longest_cap =", longest_cap(S))
print("  lib longest_cup =", longest_cup(S))
