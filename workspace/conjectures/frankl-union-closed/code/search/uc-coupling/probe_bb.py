#!/usr/bin/env python3
"""Probe: how much work does a correct 4D interval B&B need to certify
inf_P g(P,alpha)/Eh >= 1 at a t where the true inf is comfortably above 1?

Uses a COHERENT interval computation of the ratio (all quantities intervals,
division interval/interval outward), then B&B.  The certified target is the
interval LOWER endpoint of the ratio over each cell; a cell certifies when that
lower endpoint >= 1.  Reports how many cells/splits/time are needed,
and the worst (minimum) lower endpoint seen.
"""
import sys, time
import mpmath as mp
from mpmath import iv

mp.mp.prec = 220


def h_iv(x):
    """Interval binary entropy: h concavity -> min at endpoint, max<=1."""
    zero = mp.mpf(0); one = mp.mpf(1); half = mp.mpf("0.5")
    lo = max(mp.mpf(x.a), zero); hi = min(mp.mpf(x.b), one)
    if hi <= zero or lo >= one:
        return iv.mpf([0, 0])
    def hv(z):
        z = mp.mpf(z)
        omz = one - z
        if z <= 0 or z >= 1 or omz <= 0 or omz >= 1:
            return mp.mpf(0)
        ln2 = mp.log(mp.mpf(2))
        return -z*mp.log(z)/ln2 - omz*mp.log(omz)/ln2
    l = min(hv(lo), hv(hi)); h = max(hv(lo), hv(hi))
    if lo <= half <= hi:
        h = max(h, one)
    return iv.mpf([l, h])


def ivmin(iv): return iv.a
def ivmax(iv): return iv.b


def cell_ratio_iv(c, t, alpha):
    """Coherent interval of the ratio g(P,alpha)/Eh over cell c=(a1,a2,b1,b2).
    Everything is one interval expression with outward rounding.  Returns
    (ratio_iv, Eh_interval) or (None) if infeasible (E h(p) may be <=0 or
    b-a may cross 0 so beta unbounded)."""
    t_iv = iv.mpf([t, t])
    al = iv.mpf([alpha, alpha])
    one = iv.mpf([1, 1]); two = iv.mpf([2, 2]); half = iv.mpf([0.5, 0.5])
    a1, a2, b1, b2 = c
    a_iv = (a1 + a2) * half
    b_iv = (b1 + b2) * half
    bma = b_iv - a_iv
    if bma.a <= 0:
        return None
    beta = (t_iv - a_iv) / bma
    if beta.a < 0 or beta.b > 1:
        return None   # beta outside [0,1] somewhere -> infeasible cell portion
    wa = (one - beta) * half
    wb = beta * half
    atoms = [a1, a2, b1, b2]
    wts = [wa, wa, wb, wb]
    eh = iv.mpf([0, 0])
    for i in range(4):
        eh = eh + wts[i] * h_iv(atoms[i])
    if eh.b <= 0:
        return None
    e_ind = iv.mpf([0, 0])
    for i in range(4):
        for j in range(4):
            arg = atoms[i] + atoms[j] - atoms[i]*atoms[j]
            e_ind = e_ind + wts[i]*wts[j]*h_iv(arg)
    e_coup = (two*wa*h_iv(phi1(a2, a1))) + (two*wb*h_iv(phi1(b2, b1)))
    g = (one - al)*e_ind + al*e_coup
    return g / eh, eh


def phi1(p, q):
    half = mp.mpf("0.5")
    def rng(f):
        vs = [f(pp, qq) for pp in (p.a, p.b) for qq in (q.a, q.b)]
        return min(vs), max(vs)
    m1 = rng(lambda pp, qq: max(pp, qq))
    m2 = (half, half)
    m3 = rng(lambda pp, qq: pp + qq)
    return iv.mpf([sorted([m1[0], m2[0], m3[0]])[1],
                   sorted([m1[1], m2[1], m3[1]])[1]])


def feas_root(t, floor):
    """Root box: all four atoms in [floor,1]; feasibility (a1+a2<=2t, b1+b2>2t)
    checked lazily as cells are kept/split."""
    fl = iv.mpf([floor, floor]); one = iv.mpf([1, 1])
    return (fl.copy, 0)[0] if False else (iv.mpf([floor,1]), iv.mpf([floor,1]),
                                          iv.mpf([floor,1]), iv.mpf([floor,1]))


def certify(t, alpha, max_splits=2000000, min_width=2e-4, wall=10.0, floor=0.1):
    t_mp = mp.mpf(t)
    root = (iv.mpf([floor,1]), iv.mpf([floor,1]), iv.mpf([floor,1]), iv.mpf([floor,1]))
    stack = [root]
    splits = 0; cells = 0; infeas = 0; unexpl = 0
    worst = None; worst_cell = None
    t0 = time.time()

    while stack:
        if time.time()-t0 > wall:
            return dict(verdict="time", splits=splits, cells=cells, infeas=infeas,
                        unexpl=unexpl, worst=worst, worst_cell=worst_cell)
        if splits >= max_splits:
            return dict(verdict="splits", splits=splits, cells=cells, infeas=infeas,
                        unexpl=unexpl, worst=worst, worst_cell=worst_cell)
        c = stack.pop()
        # whole-cell feasibility pruning
        if (c[0].a + c[1].a) > 2*t_mp:
            infeas += 1; continue
        if (c[2].b + c[3].b) <= 2*t_mp:
            infeas += 1; continue
        r = cell_ratio_iv(c, t, alpha)
        w = max(c[i].b - c[i].a for i in range(4))
        if r is None:
            if w < min_width:
                unexpl += 1; continue
            # mixed infeasibility -> split
            splits += 1
            dim = max(range(4), key=lambda i: c[i].b-c[i].a)
            mid = (c[dim].a + c[dim].b)/2
            for s in (0,1):
                nb = list(c)
                nb[dim] = iv.mpf([c[dim].a, mid]) if s==0 else iv.mpf([mid, c[dim].b])
                stack.append(tuple(nb))
            continue
        ratio_iv, eh = r
        lo = ivmin(ratio_iv)
        cells += 1
        if worst is None or lo < worst:
            worst = lo; worst_cell = c
        if lo >= 1:
            continue
        if w < min_width:
            unexpl += 1; continue
        splits += 1
        dim = max(range(4), key=lambda i: c[i].b-c[i].a)
        mid = (c[dim].a + c[dim].b)/2
        for s in (0,1):
            nb = list(c)
            nb[dim] = iv.mpf([c[dim].a, mid]) if s==0 else iv.mpf([mid, c[dim].b])
            stack.append(tuple(nb))
    if unexpl:
        return dict(verdict="unexplorable", splits=splits, cells=cells, infeas=infeas,
                    unexpl=unexpl, worst=worst, worst_cell=worst_cell)
    return dict(verdict="certifiable", splits=splits, cells=cells, infeas=infeas,
                unexpl=unexpl, worst=worst, worst_cell=worst_cell)


if __name__ == "__main__":
    t = float(sys.argv[1]) if len(sys.argv) > 1 else 0.3820
    alpha = float(sys.argv[2]) if len(sys.argv) > 2 else 0.035
    res = certify(t, alpha, max_splits=2000000, min_width=2e-4, wall=15.0, floor=0.1)
    print("verdict", res["verdict"])
    print("splits", res["splits"], "cells", res["cells"], "infeas", res["infeas"],
          "unexpl", res["unexpl"])
    print("worst lower bound", mp.nstr(res["worst"], 12))
    if res["worst_cell"]:
        print("worst cell", res["worst_cell"])
