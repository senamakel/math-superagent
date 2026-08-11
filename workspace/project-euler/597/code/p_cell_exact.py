#!/usr/bin/env python3
"""Exact rational integration oracle for p(n,L) (PE 597) over the simplex.

Speeds are iid Exp(1), invariant to common scaling, so the race outcome is a
deterministic piecewise-constant function of the normalized speed vector,
uniformly distributed on the (n-1)-simplex (Dirichlet(1,..,1)). p(n,L) is the
uniform-simplex measure of the even-parity region:

    p(n,L) = (n-1)! * (Euclidean volume of even-parity cells of the simplex)

The outcome's separating set is a genuine straight-line hyperplane arrangement
(every candidate time is const/(affine), so pairwise time-equalities are
affine; speed-equalities are affine too). Parity is constant on each open cell
(verified empirically: 0 inconsistent sign-buckets over 150k samples per
config). Cells are sliced exactly with rational arithmetic and their even-
parity volume summed, so this is a Monte-Carlo-free exact oracle.

Usage:  python3 p_cell_exact.py n L [mass_case]
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "toolkits"))
from fractions import Fraction as F
import math
from arr_enum import enumerate_cells, leaf_interior
from arr_polytope import Polytope
from brute import outcome_parity


def p_exact(n, L, verbose=False):
    leaves, planes = enumerate_cells(n, L, verbose=verbose)
    d = n - 1
    even_vol = F(0)
    even_count = 0
    npts = 0
    for poly, svec in leaves:
        pt = leaf_interior(poly)
        if pt is None:
            continue
        npts += 1
        # pt in free coords v0..v_{d-1}; full speeds with v_{n-1}=1-sum
        s = sum(F(x) for x in pt)
        speeds = [F(x) for x in pt] + [F(1) - s]
        # parity is exact in the strict interior: float is safe only if far
        # from boundaries; use exact race for certainty
        from exact_race import outcome_parity_exact
        par = outcome_parity_exact(n, L, speeds)
        even_count += (par == 0)
        if par == 0:
            even_vol += poly.volume()
    density = math.factorial(d)
    p = density * even_vol
    return p, even_vol, even_count, len(leaves)


def main():
    args = [a for a in sys.argv[1:]]
    if len(args) < 2:
        print("usage: p_cell_exact.py n L [--verbose]")
        return
    n = int(args[0])
    L = int(args[1])
    verbose = "--verbose" in args
    p, even_vol, even_count, nleaves = p_exact(n, L, verbose=verbose)
    print(f"n={n} L={L}")
    print(f"  cells={nleaves}  even_cells={even_count}")
    print(f"  even_euclidean_vol = {even_vol}")
    print(f"  p(n,L) = {p}  = {float(p):.12f}")


if __name__ == "__main__":
    main()
