#!/usr/bin/env python3
"""Scholar verification of the fractional-chromatic claims, exact rational.

Reconciles the captured float output (chi_f(C5)=2.5, chi_f(diamond)=3,
chi_f(Moser)=3.5) with an EXACT rational dual vertex scan (the primal and
dual match by strong LP duality, but this computes chi_f = omega_f exactly
over Q by enumerating the vertices of the dual fractional-clique polytope).

Graphs use exactly the calibrated 7-vertex Moser spindle edge list
(11 unit edges, chi=4) so the value is comparable to the captured run.
"""
from itertools import combinations
from fractions import Fraction


def independent_sets(n, edges):
    adj = [0] * n
    for u, v in edges:
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
    out = []
    for mask in range(1 << n):
        ok = True
        for u in range(n):
            if (mask & (1 << u)) and (mask & adj[u]):
                ok = False
                break
        if ok and mask:
            out.append(mask)
    return out


def chi_f_dual_exact(n, edges):
    """chi_f = omega_f via the dual fractional-clique LP, exact over Q.
    max sum w_v s.t. sum_{v in I} w_v <= 1 for every independent set I,
    w >= 0.  Its optimum is attained at a vertex where n independent-set
    (or nonnegativity) constraints are tight; enumerate those vertices.
    Return (exact Fraction optimum, witness w, whether optimum is a vertex)."""
    indep = independent_sets(n, edges)
    # rows: for each independent set I, constraint sum_{v in I} w_v <= 1
    # Plus nonnegativity w_v >= 0. A vertex of R^n has n tight constraints.
    B = []           # list of (label, row) ; row[i] in {0,1}
    for I in indep:
        B.append(('I', [1 if (I >> v) & 1 else 0 for v in range(n)]))
    for v in range(n):  # nonnegativity w_v >= 0 tight -> w_v = 0
        row = [0] * n
        row[v] = 1
        B.append(('W%d' % v, row))

    best = Fraction(-1)
    bestw = None
    bestfrom = None
    mB = len(B)
    for combo in combinations(range(mB), n):
        rows = [B[i][1] for i in combo]
        M = [r[:] + [Fraction(1)] for r in rows]
        # gaussian elimination over Q to solve M w = 1
        ok = True
        for col in range(n):
            piv = None
            for r in range(col, n):
                if M[r][col] != 0:
                    piv = r
                    break
            if piv is None:
                ok = False
                break
            M[col], M[piv] = M[piv], M[col]
            pv = M[col][col]
            M[col] = [x / pv for x in M[col]]
            for r in range(n):
                if r != col and M[r][col] != 0:
                    f = M[r][col]
                    M[r] = [a - f * b for a, b in zip(M[r], M[col])]
        if not ok:
            continue
        sol = [M[r][n] for r in range(n)]
        if any(w < 0 for w in sol):
            continue  # violates w >= 0
        # must be FEASIBLE for the full dual polytope: check all indep constraints
        feas = True
        for I in indep:
            s = sum(sol[v] for v in range(n) if (I >> v) & 1)
            if s > 1 + 1e-30:  # exact: use Fraction comparison
                if s > Fraction(1):
                    feas = False
                    break
        if not feas:
            continue
        s = sum(sol, Fraction(0))
        if s > best:
            best = s
            bestw = sol
            bestfrom = tuple(B[i][0] for i in combo)
    return best, bestw, bestfrom


c5 = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]
diamond = [(0, 1), (0, 2), (1, 2), (0, 3), (1, 3)]
moser = [(0, 1), (0, 2), (0, 4), (0, 5), (1, 2), (1, 3),
         (2, 3), (3, 6), (4, 5), (4, 6), (5, 6)]

for name, n, edges, expect in [("C5", 5, c5, Fraction(5, 2)),
                               ("Diamond", 4, diamond, Fraction(3)),
                               ("Moser", 7, moser, Fraction(7, 2))]:
    best, w, _ = chi_f_dual_exact(n, edges)
    match = (best == expect)
    print(f"{name:8s} chi_f_exact = {best}  expect={expect}  "
          f"{'OK' if match else '**MISMATCH**'}  witness={[str(x) for x in w]}")
