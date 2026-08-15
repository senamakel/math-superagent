#!/usr/bin/env python3
"""Verify chi_f (fractional chromatic number) by exact LP over the
independent-set polytope for the small calibration graphs: C5, the diamond
(K4 minus an edge), and the Moser spindle (7v, 11e). Uses scipy.optimize.linprog
(floating, but rational small integers so exact enough; the values are rational).

This is an independent check of the source-note's claims about chi_f:
  chi_f(C5) = 5/2
  chi_f(diamond) = 3   (NOT 2.5 — some secondary sources are wrong here)
and a calibration of the never-executed code/frac_chro_calib.py expectation.

The dual (fractional clique) and primal (fractional colouring) must agree.
"""
from itertools import combinations
import numpy as np
from scipy.optimize import linprog


def independent_sets(n, edges):
    """All independent sets of the graph on {0..n-1} with given edge list."""
    adj = [0]*n
    for u, v in edges:
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
    indep = []
    for mask in range(1 << n):
        ok = True
        for u in range(n):
            if mask & (1 << u) and (mask & adj[u]):
                ok = False
                break
        if ok and mask:
            indep.append(mask)
    return indep


def chi_f(n, edges):
    """chi_f as the primal LP over the independent-set polytope (minimum total
    weight of independent sets covering every vertex)."""
    indep = independent_sets(n, edges)
    m = len(indep)
    # variables x_I >= 0, minimize sum x_I
    c = np.ones(m)
    # constraints: for each vertex v, sum_{I contains v} x_I >= 1
    A_ub = []
    b_ub = []
    for v in range(n):
        row = np.zeros(m)
        for j, I in enumerate(indep):
            if I & (1 << v):
                row[j] = -1.0   # -sum >= -1  =>  sum <= 1 for dual; here use >=
        # linprog default is <=; convert >= to <= by negation
        A_ub.append(-row)
        b_ub.append(-1.0)
    res = linprog(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub),
                  bounds=[(0, None)]*m, method='highs')
    return res.fun if res.success else None


def chi_f_dual(n, edges):
    """chi_f via the dual fraction-clique LP: maximize sum_v w_v s.t.
    for every independent set I, sum_{v in I} w_v <= 1, w_v >= 0."""
    indep = independent_sets(n, edges)
    # variables w_v, maximize sum
    c = -np.ones(n)
    A_ub = []
    b_ub = []
    for I in indep:
        row = np.zeros(n)
        for v in range(n):
            if I & (1 << v):
                row[v] = 1.0
        A_ub.append(row)
        b_ub.append(1.0)
    res = linprog(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub),
                  bounds=[(0, None)]*n, method='highs')
    return -res.fun if res.success else None


def test(name, n, edges, expect):
    p = chi_f(n, edges)
    d = chi_f_dual(n, edges)
    match = abs((p or 0) - (d or 0)) < 1e-9
    print(f"{name}: primal={p:.6f} dual={d:.6f} agree={match} expect={expect} "
          f"({'OK' if abs(p-expect)<1e-9 else 'MISMATCH'})")
    return p, d


# C5
edges_c5 = [(0,1),(1,2),(2,3),(3,4),(4,0)]
# Diamond = K4 minus edge (0,1): tips 0,1 non-adjacent; 2,3 form the shared edge
edges_diamond = [(0,2),(0,3),(1,2),(1,3),(2,3)]
# Moser spindle: 7 vertices, the 11 unit edges from the calibrated graph.
# Use the abstract edge list (independently derived graph structure): the
# spindle is two K4-e (diamonds) sharing a vertex; edges below reproduce the
# 11-edge / chi=4 structure up to relabelling.
# From code/out brute_calibration (the run's calibrated Moser): 
#   O,P1,P2,Q,P1',P2',Q'; edges (O,P1),(O,P2),(P1,P2),(P1,Q),(P2,Q),
#   (O,P1'),(O,P2'),(P1',P2'),(P1',Q'),(P2',Q'),(Q,Q').
edges_moser = [(0,1),(0,2),(1,2),(1,3),(2,3),
               (0,4),(0,5),(4,5),(4,6),(5,6),(3,6)]

test("C5", 5, edges_c5, 2.5)
test("diamond", 4, edges_diamond, 3.0)
test("moser", 7, edges_moser, None)  # expect chi_f <= 4, >= omega=3? spindle has omega=2 (triangle-free!) 
