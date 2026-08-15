#!/usr/bin/env python3
"""Exact fractional chromatic number chi_f(G) for the run's tiny calibration
graphs, via the DUAL LP (fractional clique):

    chi_f(G) = omega_f(G) = max { sum_v w_v : sum_{v in I} w_v <= 1
                                  for every independent set I, w_v >= 0 }

by strong LP duality (claim fractional-chromatic-lp-duality).  For the graphs
here (n <= 7) the dual polytope lives in R^n and its optimum is attained at a
vertex where n linearly independent constraints are tight.  We enumerate exact
rational vertices by Gaussian elimination over Fractions, taking tight
constraints from BOTH the independent-set rows AND the nonnegativity bounds
w_v >= 0, and keep the max sum w_v.  Thus the value returned is an EXACT
rational, not a float.

Run:  timeout 540 python3 code/scholar_frac_chro_calib.py 2>&1 | tee \
      code/out/scholar_frac_chro_calib.captured.txt

Expected exact values (the source-note claims this calibrates):
    C5        => 5/2   (odd cycle C_{2k+1}: chi_f = (2k+1)/k)
    Diamond   => 3     (chordal hence perfect, chi = omega = 3)
    Moser     => in (3, 4]  (chi(Moser)=4 gives chi_f <= 4; exact value is
                             the OPEN computation this run still owes)
"""
from itertools import combinations
from fractions import Fraction


def independent_sets(n, edges):
    adj = [0] * n
    for a, b in edges:
        adj[a] |= (1 << b)
        adj[b] |= (1 << a)
    indep = []
    for mask in range(1 << n):
        if mask and all(not (mask & (1 << u) and (mask & adj[u])) for u in range(n)):
            indep.append(mask)
    return indep


def gauss_solve(M, b):
    """Solve M x = b over Fractions; M square. Returns list or None if singular."""
    n = len(M)
    aug = [list(M[i]) + [b[i]] for i in range(n)]
    for col in range(n):
        piv = next((r for r in range(col, n) if aug[r][col] != 0), None)
        if piv is None:
            return None
        aug[col], aug[piv] = aug[piv], aug[col]
        pv = aug[col][col]
        aug[col] = [x / pv for x in aug[col]]
        for r in range(n):
            if r != col and aug[r][col] != 0:
                f = aug[r][col]
                aug[r] = [a - f * c for a, c in zip(aug[r], aug[col])]
    return [aug[r][n] for r in range(n)]


def chi_f_exact(n, edges):
    """Exact chi_f via dual vertex enumeration. Returns (value, witness_w, #indep)."""
    indep = independent_sets(n, edges)
    # constraint rows: independent-set rows first, then nonnegativity rows
    rows = []                 # each row = list of n Fractions
    for I in indep:
        rows.append([Fraction(1) if (I >> v) & 1 else Fraction(0) for v in range(n)])
    rows += [[Fraction(-1) if v == j else Fraction(0) for v in range(n)]
             for j in range(n)]   # -w_j <= 0  i.e. w_j >= 0
    mR = len(rows)
    best = None
    bestw = None
    seen = set()
    for combo in combinations(range(mR), n):
        key = tuple(sorted(combo))
        if key in seen:
            continue
        seen.add(key)
        M = [rows[i] for i in combo]
        sol = gauss_solve(M, [Fraction(1)] * n)   # every tight row = 1
        if sol is None:
            continue
        # nonnegativity rows have RHS 1 too; a tight (-w_j<=0) row means
        # -w_j = 1 -> w_j = -1, so it is NOT feasible; only accept it as
        # tightening w_j to 0 is handled below. Instead handle w_j = 0 by
        # forcing the variable: keep this simpler correct scan of vertices
        # is NOT trivial; see note. We instead scan only independent-set
        # rows plus explicit w_j = 0 boundary.
        if any(w < 0 for w in sol):
            continue
        s = sum(sol, Fraction(0))
        if best is None or s > best:
            best = s
            bestw = sol
    return best, bestw, len(indep)


def chi_f_primal_lp(n, edges):
    """Cross-check via the PRIMAL LP with scipy highsover integral data.
    Returns a float approximation (for cross-check only, not the exact verdict)."""
    import numpy as np
    from scipy.optimize import linprog
    indep = independent_sets(n, edges)
    mI = len(indep)
    c = np.ones(mI)
    A = np.array([[-1.0 if (I >> v) & 1 else 0.0 for I in indep]
                  for v in range(n)])
    b = -np.ones(n)
    r = linprog(c, A_ub=A, b_ub=b, bounds=[(0, None)] * mI, method='highs')
    return r.fun if r.success else None


# The exact dual vertex scan above has an explicit-boundary gap: vertices where
# some w_j = 0 are missed because forcing a variable to 0 is not an
# independent-set row.  Fix by ALSO optimising over the face w_j = 0 (repeat the
# scan restricted to the other variables, recursively).  Below is the corrected
# wrapper that recurses on zeroed coordinates.
def chi_f_exact_full(n, edges, forced_zero=frozenset()):
    """Exact chi_f over the independent-set LP via dual vertex enumeration,
    including the boundary faces w_j = 0 (corrected version)."""
    free = [v for v in range(n) if v not in forced_zero]
    indep = independent_sets(n, edges)
    # rows only from free variables; a tight row RHS 1 if it touches no
    # forced-zero var, otherwise it is infeasible for that face.
    rows = []
    for I in indep:
        if any(((I >> v) & 1) for v in forced_zero):
            continue
        rows.append([Fraction(1) if (I >> v) & 1 else Fraction(0) for v in free])
    mR = len(rows)
    k = len(free)
    best = None
    bestw = None
    if k == 0:
        return Fraction(0), {}, len(indep)
    from itertools import combinations as comb
    seen = set()
    for combo in comb(range(mR), k):
        key = tuple(sorted(combo))
        if key in seen:
            continue
        seen.add(key)
        M = [rows[i] for i in combo]
        sol = gauss_solve(M, [Fraction(1)] * k)
        if sol is None:
            continue
        if any(w < 0 for w in sol):
            continue
        s = sum(sol, Fraction(0))
        if best is None or s > best:
            best = s
            bestw = dict(zip(free, sol))
    # faces w_j = 0: recurse
    for j in free:
        sub = chi_f_exact_full(n, edges, forced_zero | {j})
        if sub[0] is not None and (best is None or sub[0] > best):
            best = sub[0]
            bestw = sub[1]
    return best, bestw, len(indep)


# ---- graphs (exact edge lists matching code/frac_chro_calib.py) ----
c5 = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]
diamond = [(0, 1), (0, 2), (1, 2), (0, 3), (1, 3)]      # K4 minus edge (2,3)
moser = [(0, 1), (0, 2), (0, 4), (0, 5), (1, 2), (1, 3),
         (2, 3), (3, 6), (4, 5), (4, 6), (5, 6)]

if __name__ == "__main__":
    for name, n, edges in [("C5", 5, c5), ("Diamond", 4, diamond),
                           ("Moser", 7, moser)]:
        exact, worst_w, nI = chi_f_exact_full(n, edges)
        approx = chi_f_primal_lp(n, edges)
        wstr = "".join(f"w{v}={worst_w[v] if worst_w and v in worst_w else 0} "
                       for v in range(n))
        print(f"{name:8s} n={n} |E|={len(edges):2d} #indep={nI:3d}  "
              f"chi_f EXACT = {exact} = {float(exact):.6f}   "
              f"primal-LP approx = {approx if approx is None else round(approx,6)}")
        if name == "C5":
            print("   [expect 5/2]")
        elif name == "Diamond":
            print("   [expect 3, chordal/perfect]")
        else:
            print("   [expect in (3,4]; OPEN exact value is the run's open computation]")
