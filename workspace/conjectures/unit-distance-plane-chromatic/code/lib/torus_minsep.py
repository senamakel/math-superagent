#!/usr/bin/env python3
"""
CORRECTED separation-graph construction for the flat-torus periodic-colouring
approach (see code/correct_torus_sweep.py for the driver and the bug report).

The bug this module fixes: code/lib/torus_margin.py measured the Euclidean
distance between *chosen representatives* of two cosets.  For a periodic
colouring a coset is the whole translate of the sublattice, so the correct
edge condition is the translation-invariant minimum distance between the two
full cosets:

        min_{s in Lambda'} |rep_i - rep_j + s|  <=  1 + 2*rho.

Representative-only distances UNDERSHOOT the true coset-to-coset distance
(picking the closest rep-pair), i.e. they *undercount edges*, producing false
periodic 6-colourings.  This module computes the true minimum exactly in
Q(sqrt3).

Spectrum: the triangular (A2/Eisenstein) lattice, physical map
   centre(u,v) = ( sqrt3*L*(u - v/2),  3/2*L*v ),
so squared physical distance between lattice-coordinate difference (du,dv) is
   3*L^2 * N(du,dv),  N(du,dv) = du^2 - du*dv + dv^2.

For a pair of cosets with reps p,q the min squared physical distance is
   min_{a,b in Z} 3*L^2 * N((p-q) + a*g1 + b*g2).
N is positive-definite, so its integer minimum over the sublattice is attained
near the unique continuous minimum in R^2; we compute the continuous optimum
exactly (rational), scan a growing integer box of shifts around it, and stop
when the winning shift is *strictly interior* and the continuous optimum lies
inside the box.  Then it is provably the global minimum (a convex
positive-definite form has no other local minima).  All arithmetic exact.
"""
import sympy as sp

THREE = sp.Integer(3)


def N(u, v):
    """Squared A2 lattice norm (integer)."""
    return u * u - u * v + v * v


def in_sublattice(dx, dy, g1, g2):
    """True iff (dx,dy) = a*g1 + b*g2 for some integers a,b."""
    det = g1[0] * g2[1] - g1[1] * g2[0]
    if det == 0:
        raise ValueError("degenerate sublattice generators")
    a_num = dx * g2[1] - dy * g2[0]
    b_num = g1[0] * dy - g1[1] * dx
    return (a_num % det == 0) and (b_num % det == 0)


def _sigma_min(g1, g2):
    """Smallest singular value of M = [[g1u,g2u],[g1v,g2v]] (exact real).

    |shift vector| >= sigma_min * |(a,b)|  for shift = a*g1 + b*g2.
    Returns a sympy exact real."""
    g1u, g1v = sp.Integer(g1[0]), sp.Integer(g1[1])
    g2u, g2v = sp.Integer(g2[0]), sp.Integer(g2[1])
    # M^T M = [[|g1|^2, g1.g2],[g1.g2, |g2|^2]]
    a11 = g1u * g1u + g1v * g1v
    a12 = g1u * g2u + g1v * g2v
    a22 = g2u * g2u + g2v * g2v
    # eigenvalues: (a11+a22)/2 +/- sqrt(((a11-a22)/2)^2 + a12^2)
    disc = sp.sqrt(((a11 - a22) / 2) ** 2 + a12 ** 2)
    s2 = (a11 + a22) / 2 - disc
    return sp.sqrt(sp.nsimplify(sp.simplify(s2)))


def min_sublattice_N(g1, g2, p, q):
    """Exact integer minimum of N((p-q) + a*g1 + b*g2) over (a,b) in Z^2 —
    the squared A2-norm coset-to-coset distance.  Rep-independent.

    Returns (minN, (a,b)).  Provably the global minimum: we grow a box of
    shifts whose radius R is *certified* (from the current best and the
    lattice's smallest singular value) to contain every shift that could beat
    the current best; when a scan finds no improvement, the box provably held
    the global min.  All comparisons exact in integers."""
    du = p[0] - q[0]
    dv = p[1] - q[1]
    d_norm = sp.sqrt(sp.Integer(du * du + dv * dv))
    smin = _sigma_min(g1, g2)
    best = N(du, dv)              # shift (0,0)
    best_ab = (0, 0)
    MARGIN = sp.Integer(4)        # safety in the certified radius
    while True:
        # Any shift with N <= best has (1/2)|shift+d|^2 <= best  (N>=(1/2)|.|^2),
        #   |shift+d| <= sqrt(2*best), and |a g1 + b g2| >= smin |(a,b)|, so
        #   smin |(a,b)| <= sqrt(2*best) + |d|  =>  bound on |(a,b)|.
        R = sp.ceiling((sp.sqrt(sp.Rational(2 * best, 1)) + d_norm) / smin) + MARGIN
        R = int(R)
        improved = False
        for a in range(-R, R + 1):
            for b in range(-R, R + 1):
                val = N(du + a * g1[0] + b * g2[0],
                        dv + a * g1[1] + b * g2[1])
                if val < best:
                    best = val
                    best_ab = (a, b)
                    improved = True
        if not improved:
            break
    return best, best_ab


def min_coset_physical_sqdist(g1, g2, p, q, Lv):
    """Exact min squared PHYSICAL distance between two cosets (reps p,q) of
    Lambda'=<g1,g2> for tiling side Lv: = 3*L^2*minN.  Exact in Q(sqrt3)."""
    Lv = sp.sympify(Lv)
    minN, _ = min_sublattice_N(g1, g2, p, q)
    return sp.simplify(THREE * Lv ** 2 * sp.Integer(minN))


def coset_reps_closest(g1, g2, D):
    """The D coset representatives of Z^2/<g1,g2>, each as (u,v).  Any choice
    works for the corrected (min-over-shifts) edges; we take the closest point
    to the origin (smallest A2 norm) within each coset for stability."""
    M = g1[0] * g2[1] - g1[1] * g2[0]
    D2 = abs(M)
    assert D2 == D, (D2, D)
    best = {}
    R = 2 * (abs(g1[0]) + abs(g2[0]) + abs(g1[1]) + abs(g2[1]) + 2)
    for u in range(-R, R + 1):
        for v in range(-R, R + 1):
            key = None
            for (r0, r1) in best:
                if in_sublattice(u - r0, v - r1, g1, g2):
                    key = (r0, r1)
                    break
            if key is None:
                key = (u, v)
                best[key] = (N(u, v), (u, v))
            else:
                nv = N(u, v)
                if nv < best[key][0]:
                    best[key] = (nv, (u, v))
    reps = list(v[1] for v in best.values())
    assert len(reps) == D, (len(reps), D)
    return reps


def corrected_separation_graph(g1, g2, D, Lv):
    """Correct coset-to-coset separation graph on the D cosets of
    Lambda'=<g1,g2>: edge (i,j) iff min_s|rep_i-rep_j+s| <= 1+2*Lv.
    Returns (n, edges, reps).  Exact in Q(sqrt3)."""
    Lv = sp.sympify(Lv)
    reps = coset_reps_closest(g1, g2, D)
    T2 = sp.expand((1 + 2 * Lv) ** 2)
    edges = []
    for i in range(D):
        for j in range(i + 1, D):
            d2 = min_coset_physical_sqdist(g1, g2, reps[i], reps[j], Lv)
            if sp.simplify(d2 - T2) <= 0:
                edges.append((i, j))
    return D, edges, reps


def row_kernel_generators(p, q, D):
    """Two integer generators of the index-D kernel sublattice
        Lambda' = { (u,v) : p*u + q*v = 0 (mod D) }.
    Requires gcd(p,q,D)=1 (then the kernel has index D).  Returns
    (g1, g2) with |det| = D.  Exact integers.

    Construction: reduce (p,q) by g = gcd(p,q) (g is coprime to D since
    gcd(p,q,D)=1, so both congruences have the same solution set).  For
    gcd(p,q)=1, the kernel is generated by (q,-p) (maps to 0) and any
    solution (u0,v0) of p*u0 + q*v0 = D (maps to D ≡ 0 mod D, so also in the
    kernel); their determinant p*u0 + q*v0 = D, giving index D, so they span
    the whole kernel."""
    import math
    g = math.gcd(p, q)
    p_, q_ = p // g, q // g
    assert math.gcd(p_, q_) == 1
    # Bezout coefficients x0*p_ + y0*q_ = 1, sign-robust.
    if q_ != 0:
        x0 = pow(p_ % q_, -1, q_)   # x0*p_ ≡ 1 (mod q_)
        y0 = (1 - p_ * x0) // q_
        assert p_ * x0 + q_ * y0 == 1
    else:
        # q_ == 0 => p_ = +-1
        x0, y0 = p_, 0
        assert p_ * x0 == 1
    # g1 = (q_, -p_) is in the kernel; g2 = D*(x0,y0) maps to D ≡ 0 mod D.
    g1 = (q_, -p_)
    g2 = (D * x0, D * y0)
    det = g1[0] * g2[1] - g1[1] * g2[0]
    assert abs(det) == D, (det, D, p, q)
    assert (p * g1[0] + q * g1[1]) % D == 0
    assert (p * g2[0] + q * g2[1]) % D == 0
    return (g1, g2)
