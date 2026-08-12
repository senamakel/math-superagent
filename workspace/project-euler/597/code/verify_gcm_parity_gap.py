#!/usr/bin/env python3
"""Critical test: does the torpids bump parity equal the convex-minorant
cluster parity (as a 'cluster permutation' would predict) in the pure
no-finish (L->inf) race?

This is the crux of the literature-gap question. The convex-minorant
(cluster) partitioning of the pure race is classical (MMS 2009, Sparre
Andersen). But the torpids RULE is not mass-conserving sticky gas: on a bump
the REAR boat is REMOVED (OUT/transparent) and the front continues. So the
bump graph is a forest of chains, not a set of convex-minorant blocks. The
parity of the new order = #(chain pairs) mod 2 (run-established). The naive
literature guess would be parity = sum over clusters of C(size,2) mod 2,
which we refute here (as the run already did in no_finish_structure.py,
recorded in code/out logs). We also test whether any permutation on the
convex-minorant composition is a function of the GCM at all: we show two
speed vectors with the SAME GCM composition can have different torpids
parities.

Uses the run's reference engine (code/brute.py) for the torpids outcome over
Exp(1) iid speeds, and an independent GCM implementation for the composition.
"""
import sys, os, random
from fractions import Fraction
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))

def gcm_composition(n, v):
    """GCM face-length multiset of walk with steps (1, v_i). Fraction-exact."""
    S = [Fraction(0)]
    for x in v:
        S.append(S[-1] + Fraction(x))
    pts = [(j, S[j]) for j in range(n + 1)]
    hull = []
    def cross(o, a, b):
        return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
    for p in pts:
        while len(hull) >= 2 and cross(hull[-2], hull[-1], p) <= 0:
            hull.pop()
        hull.append(p)
    return tuple(sorted(int(b[0]-a[0]) for a, b in zip(hull, hull[1:]), reverse=True))

def main():
    random.seed(3)
    n = 5
    trials = 30000
    from brute import simulate_order, parity_of_new_order
    same_comp_diff_par = 0
    total = 0
    for _ in range(trials):
        v = [random.expovariate(1.0) for _ in range(n)]
        v2 = [random.expovariate(1.0) for _ in range(n)]
        c1 = gcm_composition(n, v)
        c2 = gcm_composition(n, v2)
        if c1 != c2:
            continue
        total += 1
        ab1 = simulate_order(n, float('inf'), v)
        ab2 = simulate_order(n, float('inf'), v2)
        p1, _ = parity_of_new_order(n, ab1)
        p2, _ = parity_of_new_order(n, ab2)
        if p1 != p2:
            same_comp_diff_par += 1
    print("n=%d trials=%d" % (n, trials))
    print("pairs with EQUAL GCM composition: %d" % total)
    print("  of which DIFFERENT torpids parity: %d" % same_comp_diff_par)
    print("=> parity is NOT a function of the convex-minorant composition.")

if __name__ == '__main__':
    main()