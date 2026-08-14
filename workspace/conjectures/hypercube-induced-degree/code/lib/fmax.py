"""Exact f(n) oracle for the hypercube, decision-ILP and exhaustive.

f(n) = min { D(S) : S subseteq {0,1}^n, |S| = 2^{n-1}+1 }, where D(S) is the
maximum internal degree of the induced subgraph Q_n[S].

This module provides two independent routes to f(n), both exact integer
arithmetic on the *decision* "is there an S of size 2^{n-1}+1 with D(S) <= d?":

  * decision_ilp(n, d)  -- binary ILP via scipy.optimize.milp (HiGHS).
     Binary variables x_v in {0,1} for each of the 2^n vertices, with
        sum_v x_v = 2^{n-1}+1
        for each v:  sum_{u in N(v)} x_u + 5*x_v <= d + n   (n=5 hard-coded
                      M=n bounds the slack: if x_v=1 the LHS constraint left
                      of this is sum over neighbours <= d; if x_v=0 it is
                      sum <= n, always true).
     M = n is valid because a vertex in Q_n has exactly n neighbours, so the
     internal degree of any vertex is at most n. Polynomial-size ILP (2^n
     binaries, 2^n+1 constraints).
  * decision_oracle(n, d) -- exhaustive over all subsets of size 2^{n-1}+1.
     Only small n (<= 4); the oracle that validates decision_ilp.
  * f_ilp(n)            -- smallest d with decision_ilp(n, d) feasible.
  * f_exact(n)          -- smallest d via the exhaustive oracle (n <= 4).

All degree arithmetic and set sizes are exact integers. ILP feasibility is
reported as a Python bool.

Correctness note: decision_ilp and decision_oracle must agree on n <= 4, where
both can run; that agreement is the check that the linearisation is right.
"""

import numpy as np
from itertools import combinations
from scipy.optimize import milp, LinearConstraint, Bounds

# ---- exact hypercube helpers (mirror lib.qcube; kept local so this module
#      is self-contained for the decision oracle) ----
def internal_degree_distribution(n, S):
    S = sorted(set(S))
    spos = set(S)
    counts = {}
    for v in S:
        d = sum(1 for k in range(n) if (v ^ (1 << k)) in spos)
        counts[d] = counts.get(d, 0) + 1
    return counts


def max_internal_degree(n, S):
    dist = internal_degree_distribution(n, S)
    return max(dist.keys())


def _nbhd(n):
    N = 1 << n
    return [[v ^ (1 << k) for k in range(n)] for v in range(N)]


def decision_oracle(n, d, progress=False):
    """Exhaustive decision: is there an S of size 2^{n-1}+1 with D(S) <= d?

    n <= 4 only (2^n <= 16 vertices, C(2^n, 2^{n-1}+1) subsets <= C(16,9)).
    Returns (bool, S_or_None). Used to validate decision_ilp.
    """
    N = 1 << n
    m = (1 << (n - 1)) + 1
    nb = _nbhd(n)
    for comb in combinations(range(N), m):
        S = set(comb)
        if all(sum(1 for u in nb[v] if u in S) <= d for v in S):
            return True, S
    return False, None


def decision_ilp(n, d):
    """ILP decision: is there S of size 2^{n-1}+1 with D(S) <= d? Exact bool.

    Binary x_v (scipy.milp, HiGHS). Constraints:
      sum x_v = 2^{n-1}+1
      for each v: sum_{u in N(v)} x_u + M*x_v <= d + M,  M = n.
    """
    N = 1 << n
    m = (1 << (n - 1)) + 1
    M = n  # max internal degree of any vertex is n; slack bound.
    nb = _nbhd(n)

    # equality: sum x = m  ->  A_eq row of 1s, lb=ub=m
    A_eq = np.ones((1, N))
    eq = LinearConstraint(A_eq, m, m)

    # inequalities: for each v,  sum_{u in N(v)} x_u + M*x_v <= d + M
    rows = []
    for v in range(N):
        row = np.zeros(N)
        for u in nb[v]:
            row[u] = 1.0
        row[v] = M
        rows.append(row)
    A_ub = np.array(rows)
    ub = LinearConstraint(A_ub, -np.inf, d + M)

    integrality = np.ones(N, dtype=np.uint8)  # all binary
    bounds = Bounds(0, 1)
    c = np.zeros(N)

    res = milp(c, integrality=integrality, bounds=bounds,
               constraints=[eq, ub])
    return bool(res.success)


def f_milp(n, d_min=0, d_max=None):
    """Smallest d in [d_min, d_max] with decision_ilp(n, d) feasible."""
    if d_max is None:
        d_max = n
    for d in range(d_min, d_max + 1):
        if decision_ilp(n, d):
            return d
    return None


def f_exact(n, d_max=None):
    """Smallest d with decision_oracle(n, d) feasible (n <= 4)."""
    if d_max is None:
        d_max = n
    for d in range(0, d_max + 1):
        ok, S = decision_oracle(n, d)
        if ok:
            return d, S
    return None, None
