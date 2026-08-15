#!/usr/bin/env python3
"""Independent check of chi_f on the calibration graphs, with edge lists EXACTLY
matching code/frac_chro_calib.py so the values are directly comparable.

Diamond edges (0,1),(0,2),(1,2),(0,3),(1,3): that's K4 minus edge (2,3), i.e.
the two triangles are (0,1,2) and (0,1,3). FRACTIONAL chromatic number.

Also compute, for the Moser spindle, the fractional clique dual to confirm
chi_f = omega_f by LP duality.
"""
import numpy as np
from scipy.optimize import linprog


def independent_sets(n, edges):
    adj = [0]*n
    for u, v in edges:
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
    indep = []
    for mask in range(1 << n):
        ok = all(not (mask & (1 << u) and (mask & adj[u])) for u in range(n))
        if ok and mask:
            indep.append(mask)
    return indep


def chi_f_primal(n, edges):
    indep = independent_sets(n, edges)
    m = len(indep)
    c = np.ones(m)
    A = np.array([[-1.0 if (I & (1 << v)) else 0.0 for I in indep]
                  for v in range(n)])
    b = -np.ones(n)
    r = linprog(c, A_ub=A, b_ub=b, bounds=[(0, None)]*m, method='highs')
    return r.fun


def chi_f_dual(n, edges):
    indep = independent_sets(n, edges)
    c = -np.ones(n)
    A = np.array([[1.0 if (I & (1 << v)) else 0.0 for v in range(n)]
                  for I in indep])
    b = np.ones(len(indep))
    r = linprog(c, A_ub=A, b_ub=b, bounds=[(0, None)]*n, method='highs')
    return -r.fun


def alpha(n, edges):
    return max(x.bit_count() for x in independent_sets(n, edges))


# Exact edge lists from frac_chro_calib.py
c5 = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]
diamond = [(0, 1), (0, 2), (1, 2), (0, 3), (1, 3)]
moser = [(0, 1), (0, 2), (0, 4), (0, 5), (1, 2), (1, 3),
         (2, 3), (3, 6), (4, 5), (4, 6), (5, 6)]

for name, n, edges, expect in [("C5", 5, c5, 2.5),
                               ("diamond", 4, diamond, 3.0),
                               ("moser", 7, moser, None)]:
    p = chi_f_primal(n, edges)
    d = chi_f_dual(n, edges)
    a = alpha(n, edges)
    agree = abs(p - d) < 1e-9
    line = (f"{name:10s} n={n} |E|={len(edges):2d} alpha={a}  "
            f"chi_f_primal={p:.6f} chi_f_dual={d:.6f} agree={agree}")
    if expect is not None:
        line += f"  expect={expect} {'OK' if abs(p-expect)<1e-9 else '**WRONG**'}"
    print(line)
