#!/usr/bin/env python3
"""
ATTACK the claimed periodic 6-colouring of the plane.

The sweep in torus_margin.py builds the separation graph on the 7 coset
REPRESENTATIVES and decides edges by the physical distance between those two
representatives.  A periodic colouring of the plane by radius-rho cells is
proper only if NO two same-coloured cosets have ANY pair of lattice points
within 1+2*rho.  So the correct edge test is the MINIMUM distance between the
two cosets over the WHOLE lattice, not the representative distance.

Hypothesis: representative-distance undercounts edges (two cosets can be close
in the plane while their canonical reps are far apart), so the reported
6-colourings are spurious: the true minimum-distance separation graph is NOT
6-colourable at these (L, sublattice) parameters.

We test D=7, row=(1,-2) (the first reported 6-colouring) and a couple more.
"""
import math
import sympy as sp
from lib.satcolor import is_k_colorable

THREE_HALF = sp.Rational(3, 2)

def a2_centre(u, v, Lv):
    x = sp.sqrt(3) * Lv * (u - sp.Rational(v, 2))
    y = THREE_HALF * Lv * v
    return sp.simplify(x), sp.simplify(y)

def sqdist(c1, c2):
    return sp.expand((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2)

def sublattice_reps_row(p, q, D):
    reps = []
    for r in range(D):
        cand = None
        for u in range(D):
            for v in range(D):
                if (p*u + q*v) % D == r:
                    if cand is None or (u*u+v*v) < (cand[0]*cand[0]+cand[1]*cand[1]):
                        cand = (u, v)
        reps.append(cand)
    return reps

def coset_dist_min(p, q, D, r1, r2, Lv, R=12):
    """Minimum physical distance between two cosets r1,r2 of the kernel of
    (u,v)->p u+q v mod D, minimized over lattice vector difference delta with
    p*du+q*dv ≡ (r2-r1) mod D.  Exact physical distance in Q(sqrt3)."""
    c1 = a2_centre(*(reps[r1]), Lv)
    best = None
    for du in range(-R, R+1):
        for dv in range(-R, R+1):
            if ((p*du + q*dv) - (r2-r1)) % D != 0:
                continue
            c2 = a2_centre(reps[r1][0]+du, reps[r1][1]+dv, Lv)
            d2 = sqdist(c1, c2)
            if best is None or sp.simplify(d2 - best) < 0:
                best = d2
    return best

def build_graph(p, q, D, Lv, mode, R=12):
    """mode='rep' uses rep-rep distance; mode='min' uses min coset distance."""
    T2 = sp.expand((1+2*Lv)**2)
    edges = []
    for i in range(D):
        for j in range(i+1, D):
            if mode == 'rep':
                d2 = sqdist(a2_centre(*reps[i], Lv), a2_centre(*reps[j], Lv))
            else:
                d2 = coset_dist_min(p, q, D, i, j, Lv, R)
            if sp.simplify(d2 - T2) <= 0:
                edges.append((i, j))
    return edges

def count_min_dist_under_R(p, q, D, Lv, R):
    """Count pairs of cosets whose min distance <= 1+2L, as a function of search
    radius R - to confirm R is large enough that the min has stabilized."""
    T2 = sp.expand((1+2*Lv)**2)
    cnt = 0
    pairs = []
    for i in range(D):
        for j in range(i+1, D):
            best = coset_dist_min(p, q, D, i, j, Lv, R)
            if sp.simplify(best - T2) <= 0:
                cnt += 1
                pairs.append((i, j))
    return cnt, pairs

if __name__ == "__main__":
    for (p, q, D, Lv) in [(1,-2,7,sp.Rational(2,5)),
                          (1,-1,7,sp.Rational(2,5)),
                          (1,2,13,sp.Rational(2,5))]:
        reps = sublattice_reps_row(p, q, D)
        print("="*70)
        print(f"Sublattice kernel row=({p},{q}) mod {D}, L={Lv}")
        print(f"  reps = {reps}")
        T2 = sp.expand((1+2*Lv)**2)
        print(f"  (1+2L)^2 = {T2}")
        # check R convergence on min distances
        for R in [3, 6, 9, 12]:
            cnt, pairs = count_min_dist_under_R(p, q, D, Lv, R)
            print(f"  min-distance pairs <=1+2L with R={R}: {cnt} {pairs}")
        # representative graph
        e_rep = build_graph(p, q, D, Lv, 'rep', R=12)
        e_min = build_graph(p, q, D, Lv, 'min', R=12)
        print(f"  rep-distance graph: {len(e_rep)} edges  -> 6-col? {is_k_colorable(e_rep,6,D)[0]}")
        print(f"  min-distance graph: {len(e_min)} edges  -> 6-col? {is_k_colorable(e_min,6,D)[0]}")
        print(f"     rep-only edges (missed by min) = {sorted(set(e_rep)-set(e_min))}")
        print(f"     min-only edges (missed by rep) = {sorted(set(e_min)-set(e_rep))}")
