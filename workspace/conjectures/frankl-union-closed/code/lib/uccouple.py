#!/usr/bin/env python3
"""uccouple.py — rigorous (interval) arithmetic for the Yu coupling objective
Gamma_hat(t) = sup_alpha inf_{two-atom P_pq: Eh>0} g(P_pq,alpha)/E h(p), and a
branch-and-bound certifier for that inf.

This module is the ONE place the objective is encoded and the inf is certified.
Everything here is exact interval arithmetic (mpmath.iv, directed rounding),
so a reported LOWER bound is a provable lower bound on inf_P g/Eh. Floating
point is used only to locate candidate minima for guiding the search, never to
conclude.

Subjects / functions
--------------------
h_iv(x)                 : interval binary entropy h(x)=-x log2 x -(1-x)log2(1-x)
phi1(p,q)               : median{max(p,q),1/2,p+q} (multiset median)
ratio_lo(P_cell,t,alpha): rigorous LOWER bound of g(P,alpha)/E h(p) over a
                          cell (tuple of 4 intervals for a1,a2,b1,b2)
certify_inf(t,alpha,...): branch-and-bound returning a rigorous LOWER bound on
                          inf_P g/Eh, or a verdict that it could not be
                          certified within the budget.

Feasible region (from Yu Prop 1 / proof of eq (17)):
    a1,a2,b1,b2 in [0,1], a=(a1+a2)/2, b=(b1+b2)/2,
    a <= t < b <= 1,  beta=(t-a)/(b-a) in (0,1], E h(p) > 0.
NOTE: the constraints are on the AVERAGES, not on individual atoms: a1+a2<=2t
and b1+b2>2t.  Individual atoms are free in [0,1].  This is the region used
here; a region that additionally bounds b1,b2>=t is a strict subset (it omits
Yu's minimizer, which has b1=a=0.330<t) and gives an UNSOUND over-estimate of
the inf.
"""
import time

from mpmath import iv, mp


def h_iv(x):
    """Rigorous enclosure of h(z) for z an interval in [0,1].

    h is concave on [0,1], so its minimum on an interval is at an endpoint
    (h(0)=h(1)=0) and its maximum <= 1 (attained near 1/2).  Return the
    interval [lo, hi] that provably contains {h(z): z in x}.
    """
    one = iv.mpf(1)
    zero = iv.mpf(0)
    lo = x.a
    hi = x.b
    lo = max(lo, zero)
    hi = min(hi, one)
    if hi <= zero or lo >= one:
        return iv.mpf(0)

    def hv(z):
        # z is an mpf scalar in [0,1].
        ln2 = mp.log(mp.mpf(2))
        zm = mp.mpf(z)
        one_m_z = mp.mpf(1) - zm
        if zm <= 0 or zm >= 1 or one_m_z <= 0 or one_m_z >= 1:
            return mp.mpf(0)
        return -zm * mp.log(zm) / ln2 - one_m_z * mp.log(one_m_z) / ln2

    hlo = min(hv(mp.mpf(lo)), hv(mp.mpf(hi)))
    hhi = max(hv(mp.mpf(lo)), hv(mp.mpf(hi)))
    if lo <= iv.mpf("0.5") <= hi:
        hhi = max(hhi, iv.mpf(1))
    return iv.mpf([hlo, hhi])


def phi1(p, q):
    """median{max(p,q), 1/2, p+q} on intervals -> enclosing interval."""
    one_half = iv.mpf("0.5")

    def corner_minmax(f):
        vs = []
        for pp in (p.a, p.b):
            for qq in (q.a, q.b):
                vs.append(f(pp, qq))
        return min(vs), max(vs)

    m1 = corner_minmax(lambda pp, qq: max(pp, qq))       # max(p,q)
    m2 = (iv.mpf("0.5"), iv.mpf("0.5"))                  # 1/2 constant
    m3 = corner_minmax(lambda pp, qq: pp + qq)           # p+q
    lo = sorted([m1[0], m2[0], m3[0]])[1]
    hi = sorted([m1[1], m2[1], m3[1]])[1]
    return iv.mpf([lo, hi])


def _feas_cell(c, t_mp):
    """Is the whole cell (a1,a2,b1,b2 intervals) inside the feasible region?
    Used only to prune entirely-infeasible cells from the search; cells
    partially inside/outside are kept and split (they cost a bit more).
    Here we keep cells unless they are DISJOINT from feasibility:
      a1+a2<=2t must be possibly true  -> a1.a+a2.a <= 2t
      b1+b2 > 2t    must be possibly true -> b1.b+b2.b > 2t
    """
    a1, a2, b1, b2 = c
    if (a1.a + a2.a) > 2 * t_mp:
        return False
    if (b1.b + b2.b) <= 2 * t_mp:
        return False
    return True


def ratio_lo(c, t, alpha):
    """Rigorous LOWER bound on g(P,alpha)/E h(p) over cell c=(a1,a2,b1,b2
    intervals) at fixed (t,alpha).  Returns (lo, eh_lo, ok) where ok=False when
    E h(p) may be <= 0 inside the cell (then no ratio lower bound is valid).
    """
    t_iv = iv.mpf(t)
    alpha_iv = iv.mpf(alpha)
    one = iv.mpf(1)
    half = iv.mpf("0.5")
    a1, a2, b1, b2 = c
    a_iv = (a1 + a2) * half
    b_iv = (b1 + b2) * half

    # beta = (t-a)/(b-a); need enclosures of beta.  b-a may cross zero -> wide.
    bma = b_iv - a_iv
    if bma.a <= 0:
        # cell may have b<=a; cannot certify.  Return an air-tightly invalid
        # value so the caller treats it as unexplorable (must split).
        return None, None, False
    beta = (t_iv - a_iv) / bma
    beta_lo = beta.a
    beta_hi = beta.b
    wa_lo = (one - beta_hi) * half
    wb_lo = beta_lo * half

    atoms = [a1, a2, b1, b2]
    wts_lo = [wa_lo, wa_lo, wb_lo, wb_lo]

    # E h(p) lower bound
    eh_hi = iv.mpf(0)
    for i in range(4):
        eh_hi += wts_lo[i] * h_iv(atoms[i]).b
    if eh_hi <= 0:
        return None, None, False   # may be E h(p)<=0 -> Eh>0 violated
    # For the RATIO lower bound we divide g_lo by an UPPER bound of Eh.
    eh_ul = iv.mpf(0)
    for i in range(4):
        eh_ul += _wts_hi(atoms, beta_hi, beta_lo, i) * h_iv(atoms[i]).b

    # g_lo = (1-alpha) E_indep_lo + alpha E_coup_lo  (alpha,1-alpha >=0)
    e_ind_lo = iv.mpf(0)
    for i in range(4):
        for j in range(4):
            wi = wts_lo[i]
            wj = wts_lo[j]
            arg = atoms[i] + atoms[j] - atoms[i] * atoms[j]
            e_ind_lo += wi * wj * h_iv(arg).a
    # coupled term: 2 wa h(phi(a1,a2)) + 2 wb h(phi(b1,b2)) lower bound
    g45 = phi1(a2, a1)
    g67 = phi1(b2, b1)
    e_coup_lo = (2 * wa_lo * h_iv(g45).a) + (2 * wb_lo * h_iv(g67).a)

    g_lo = (one - alpha_iv) * e_ind_lo + alpha_iv * e_coup_lo
    if eh_ul <= 0:
        return None, None, False
    lo = g_lo / eh_ul
    return lo.a, eh_ul.a, True


def _wts_hi(atoms, beta_hi, beta_lo, i):
    """Upper bound of the weight of atom i (0,1 -> wa; 2,3 -> wb)."""
    if i < 2:
        return (1 - beta_lo) / 2  # wa_hi = (1-beta_min)/2
    return beta_hi / 2  # wb_hi = beta_max/2


def certify_inf(t, alpha, max_splits=400000, min_width=2e-4, wall_sec=10.0,
                atom_floor=0.1):
    """Rigorous branch-and-bound for inf_P g(P,alpha)/Eh over the feasible
    two-atom class at fixed (t,alpha).

    Also enforces the degenerate-atom guard (directive 11): all atoms required
    in [atom_floor, 1].  Cells wholly below atom_floor are infeasible by guard.

    Returns a dict:
      verdict: 'certifiable' | 'not-certifiable' | 'inconclusive (time/splits)'
      lower_bound: the tightest certified lower bound of inf_P g/Eh found
                   (a rigorous lower bound over the whole region), = min of the
                   cell lower bounds over all kept cells.
      stats...
    """
    t_mp = mp.mpf(t)
    zero = iv.mpf(0)
    one = iv.mpf(1)
    fl = mp.mpf(atom_floor)
    root = (iv.mpf([fl, 1]), iv.mpf([fl, 1]), iv.mpf([fl, 1]), iv.mpf([fl, 1]))
    stack = [root]
    splits = 0
    cells = 0
    infeasible_cells = 0
    worst = None            # smallest lower bound seen over a kept feasible cell
    worst_cell = None
    unexplorable = 0
    t0 = time.time()

    def width(c):
        return max(c[i].b - c[i].a for i in range(4))

    while stack:
        if time.time() - t0 > wall_sec:
            return {"verdict": "inconclusive (time)", "splits": splits,
                    "cells": cells, "lower_bound": worst, "worst_cell": worst_cell,
                    "infeasible_cells": infeasible_cells, "unexplorable": unexplorable}
        if splits >= max_splits:
            return {"verdict": "inconclusive (splits)", "splits": splits,
                    "cells": cells, "lower_bound": worst, "worst_cell": worst_cell,
                    "infeasible_cells": infeasible_cells, "unexplorable": unexplorable}
        c = stack.pop()
        # prune the whole-cell-feasibility checks
        if not _feas_cell(c, t_mp):
            infeasible_cells += 1
            continue
        lo, eh, ok = ratio_lo(c, t, alpha)
        if not ok:
            # cell may violate Eh>0 or b>a inside — need finer splits
            if width(c) < min_width:
                unexplorable += 1
                continue
            splits += 1
            dim = max(range(4), key=lambda i: c[i].b - c[i].a)
            mid = (c[dim].a + c[dim].b) / 2
            for rep in (0, 1):
                nb = list(c)
                nb[dim] = iv.mpf([c[dim].a, mid]) if rep == 0 else iv.mpf([mid, c[dim].b])
                stack.append(tuple(nb))
            continue
        cells += 1
        if worst is None or lo < worst:
            worst = lo
            worst_cell = c
        if lo >= 1:
            continue            # this cell fully certified
        if width(c) < min_width:
            unexplorable += 1
            continue
        # not certified & wide enough -> split the widest dimension
        splits += 1
        dim = max(range(4), key=lambda i: c[i].b - c[i].a)
        mid = (c[dim].a + c[dim].b) / 2
        for rep in (0, 1):
            nb = list(c)
            nb[dim] = iv.mpf([c[dim].a, mid]) if rep == 0 else iv.mpf([mid, c[dim].b])
            stack.append(tuple(nb))

    if unexplorable:
        return {"verdict": "not-certifiable", "splits": splits, "cells": cells,
                "lower_bound": worst, "worst_cell": worst_cell,
                "infeasible_cells": infeasible_cells, "unexplorable": unexplorable}
    # every feasible cell had lower bound >= 1 (worst >= 1)
    return {"verdict": "certifiable", "splits": splits, "cells": cells,
            "lower_bound": worst, "worst_cell": worst_cell,
            "infeasible_cells": infeasible_cells, "unexplorable": unexplorable}
