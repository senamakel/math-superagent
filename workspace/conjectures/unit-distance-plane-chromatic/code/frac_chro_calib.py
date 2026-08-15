#!/usr/bin/env python3
"""Compute chi_f (fractional chromatic number, LP over the independent-set
polytope) for the run's exact calibration graphs: C5 (expect 5/2), the diamond
(expect 3, a triangle cover issue), and the Moser spindle (7v, 11e, chi=4).
This is the first time the run computes chi_f on any of its graphs, which is
the central claim of the fractional-chromatic-lp-lower-bound approach.

Exact integer/rational LP via scipy 'highs'. For these tiny graphs the
independent-set enumeration is exhaustive and exact.
"""
import sys
sys.path.insert(0, "/workspace/code")
import scipy.optimize as opt


def independent_sets(n, edges):
    adj = [set() for _ in range(n)]
    for a, b in edges:
        adj[a].add(b); adj[b].add(a)
    indep = []
    for mask in range(1 << n):
        vs = [i for i in range(n) if (mask >> i) & 1]
        ok = True
        for i in range(len(vs)):
            for j in range(i + 1, len(vs)):
                if vs[j] in adj[vs[i]]:
                    ok = False; break
            if not ok:
                break
        if ok:
            indep.append(frozenset(vs))
    return indep


def chi_f(n, edges, name=""):
    indep = independent_sets(n, edges)
    mI = len(indep)
    c = [1.0] * mI
    A, b = [], []
    for v in range(n):
        row = [0.0] * mI
        for j, I in enumerate(indep):
            if v in I:
                row[j] = 1.0
        A.append(row); b.append(1.0)
    res = opt.linprog(c, A_ub=[[-r for r in row] for row in A],
                      b_ub=[-x for x in b],
                      bounds=[(0, None)] * mI, method='highs')
    val = res.fun
    print(f"{name:20s} n={n} |E|={len(edges):2d}  chi_f = {val:.6f}  "
          f"(#indep={mI})")
    return val


# C5 (cycle of 5): chi_f = 5/2
c5 = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]
chi_f(5, c5, "C5")

# Diamond: two triangles on common edge AB, tips C,D at dist sqrt3
# vertices 0=A,1=B,2=C,3=D ; edges ABC (0,1,2), ABD (0,1,3)
diamond = [(0, 1), (0, 2), (1, 2), (0, 3), (1, 3)]
chi_f(4, diamond, "Diamond")

# Moser spindle; edges from brute_calibration (exact, 11 edges)
moser = [(0, 1), (0, 2), (0, 4), (0, 5), (1, 2), (1, 3),
         (2, 3), (3, 6), (4, 5), (4, 6), (5, 6)]
chi_f(7, moser, "Moser spindle")

# Compare: independence number alpha (chi_f >= n/alpha for vertex-transitive only,
# but alpha gives a lower bound chi_f >= n/alpha in general? No — only for
# vertex-transitive. For general graphs chi_f >= n/alpha? Actually chi_f >=
# n/alpha is FALSE in general. We report alpha for completeness.)

def independence_number(n, edges):
    indep = independent_sets(n, edges)
    return max(len(I) for I in indep)

print("\nIndependence numbers for contrast:")
for name, n, edges in [("C5", 5, c5), ("Diamond", 4, diamond), ("Moser", 7, moser)]:
    print(f"  {name}: alpha = {independence_number(n, edges)}")
