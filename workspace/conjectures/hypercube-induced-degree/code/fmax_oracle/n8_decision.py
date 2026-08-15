#!/usr/bin/env python3
"""Decide f(8)=3 (and f(9)=3): exact ILP feasibility, two independent solvers.

Question: is there S subseteq {0,1}^n with |S| = 2^{n-1}+1 and D(S) <= d
(no vertex of S has more than d neighbours inside S)?  For n=8, d=3 this
decides whether f(8) = ceil(sqrt(8)) = 3.  The lower bound f(8) >= 3 is
already PROVED in this run via the Huang spectral route (A_n^2 = nI,
interlacing; see research/backward/spectral-interlacing-sqrt-lower-bound.md),
so a witness found here is a direct machine-checked confirmation f(8) = 3.
n=9, d=3 is the same decision at the next ceil-sqrt step (size 257).

Two independent solver routes on the SAME exact integer formulation:

  * scipy.optimize.milp (HiGHS MIP) -- big-M linearisation, identical to
    lib.fmax.decision_ilp which was validated against the exhaustive oracle
    on all 13 (n,d) pairs for n=1..4 (code/out/fmax_driver.captured.txt):
        for each vertex v:  sum_{u in N(v)} x_u + n*x_v <= d + n
    M = n is valid because every vertex of Q_n has exactly n neighbours:
    when x_v = 0 the LHS is <= n <= d+n (slack), when x_v = 1 it forces the
    true internal degree sum_{u in N(v)} x_u <= d.  (Applying the bound to
    NON-selected vertices too is the known-broken encoding that produced the
    false "f(10)>4" claims -- code/out/upper_n10_11.py -- and is NOT used.
    The even-weight set + one odd vertex is a valid partial witness for it:
    the odd vertex has degree n inside the set, so the sum over its
    neighbours is n > d, and the broken encoding would wrongly reject it.)

  * ortools CP-SAT -- the same condition, half-reified (exact, no big-M):
        model.Add(sum(x[u] for u in N(v)) <= d).OnlyEnforceIf(x[v])

Both formulations add two PROVABLY SAFE symmetry breaks (they remove no
solution orbit):

  (1) x[0] == 1.  Q_n is vertex-transitive, so WLOG the all-zero vertex is
      in S: for any valid S and any v in S there is an automorphism mapping
      v to 0, and |S| and the degree bounds are invariant.

  (2) e0 - o0 >= 0, e0 = # selected even-weight vertices, o0 = # selected
      odd-weight.  Safe jointly with (1): for the automorphism g_t(v)=v xor
      t (complement on the support of vertex t), g_t maps t to 0, so
      0 in g_t(S) iff t in S; and g_t swaps the parity classes iff |t| is
      odd.  Every valid S contains an even vertex t_e (the odd class has
      only 2^{n-1} = 128 vertices < 129 = |S|) and an odd vertex t_o.  If
      e0(S) >= o0(S), take h = g_{t_e}: parity counts unchanged (|t_e| even)
      and 0 in h(S), so both breaks hold.  Otherwise take h = g_{t_o}
      (|t_o| odd): counts swap, the image has e-count >= o-count, and 0 in
      the image.  Either way h(S) is a valid solution satisfying both
      breaks, so the pair is jointly safe.

Thread caps are set BEFORE numpy/scipy import (prior runs crashed in
OpenBLAS's 28-thread pool -- code/out/c10d4.txt).

Every witness extracted is re-verified by a pure-Python exact degree counter
(third, solver-free route) before being written to code/out/witness_n8.txt
or code/out/witness_n9.txt.  Uses no enumeration of subsets: 2^n binaries
and O(2^n) constraints, polynomial-size ILP.

Usage: python3 n8_decision.py --n 8 --d 3 --highs-tl 380 --sat-tl 600
"""

import os
import sys
import time
import resource
import argparse

os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"

import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from ortools.sat.python import cp_model


def neighbours(n, v):
    """The n neighbours of vertex v in Q_n (exact integer bitlabels)."""
    return [v ^ (1 << k) for k in range(n)]


def parity_of(v):
    return bin(v).count("1") & 1


def evens_odds(n):
    """([even vertices], [odd vertices]) of Q_n, bitlabels 0..2^n-1."""
    evens, odds = [], []
    for v in range(1 << n):
        (evens if parity_of(v) == 0 else odds).append(v)
    return evens, odds


def verify_set(n, S):
    """Pure-Python exact re-verification: (|S|, max deg, {deg: count}).
    Shares no solver code; recomputes every internal degree from scratch."""
    from collections import Counter
    S = set(S)
    deg = Counter()
    for v in S:
        c = 0
        for k in range(n):
            if (v ^ (1 << k)) in S:
                c += 1
        deg[c] += 1
    return len(S), (max(deg) if deg else -1), dict(sorted(deg.items()))


def highs_decision(n, d, time_limit, threads=None):
    """HiGHS MILP decision via scipy.optimize.milp.

    Returns (feasible, S_or_None, status, message, wall_s).  A False return
    is 'proven infeasible / no solution within limit' -- the printed status
    distinguishes 'no feasible solution found' (time limit) from a proof.
    """
    N = 1 << n
    m = (1 << (n - 1)) + 1
    M = n
    t0 = time.time()

    A_eq = np.ones((1, N))
    eq = LinearConstraint(A_eq, m, m)

    rows = []
    for v in range(N):
        row = np.zeros(N)
        for u in neighbours(n, v):
            row[u] = 1.0
        row[v] = M
        rows.append(row)
    A_ub = np.array(rows)
    ub = LinearConstraint(A_ub, -np.inf, d + M)

    x0row = np.zeros(N)
    x0row[0] = 1.0
    x0c = LinearConstraint(x0row, 1, 1)

    evens, odds = evens_odds(n)
    parrow = np.zeros(N)
    for v in evens:
        parrow[v] = 1.0
    for v in odds:
        parrow[v] = -1.0
    pc = LinearConstraint(parrow.reshape(1, -1), 0, np.inf)

    integrality = np.ones(N, dtype=np.uint8)
    bounds = Bounds(0, 1)
    c = np.zeros(N)

    options = {"time_limit": time_limit, "presolve": True}
    if threads is not None:
        options["threads"] = threads
    try:
        res = milp(c, integrality=integrality, bounds=bounds,
                   constraints=[eq, ub, x0c, pc], options=options)
    except (ValueError, TypeError):
        # solver rejected an option (solver-version dependent): retry
        # without the optional ones, still with time limit.
        try:
            res = milp(c, integrality=integrality, bounds=bounds,
                       constraints=[eq, ub, x0c, pc],
                       options={"time_limit": time_limit})
        except (ValueError, TypeError):
            res = milp(c, integrality=integrality, bounds=bounds,
                       constraints=[eq, ub, x0c, pc])
    dt = time.time() - t0

    feasible = bool(getattr(res, "success", False)) and res.x is not None
    S = None
    if feasible:
        S = [v for v in range(N) if res.x[v] > 0.5]
    return feasible, S, getattr(res, "status", None), getattr(res, "message", ""), dt


def cpsat_decision(n, d, time_limit, workers=8, warmstart=True):
    """ortools CP-SAT decision with half-reified degree bounds.

    Returns (feasible, S_or_None, status, wall_s).  Status shows
    OPTIMAL/FEASIBLE vs INFEASIBLE (proof) vs UNKNOWN (time limit).
    """
    N = 1 << n
    m = (1 << (n - 1)) + 1
    t0 = time.time()
    model = cp_model.CpModel()
    x = [model.NewBoolVar(f"x{i}") for i in range(N)]
    model.Add(sum(x) == m)
    for v in range(N):
        model.Add(sum(x[u] for u in neighbours(n, v)) <= d).OnlyEnforceIf(x[v])
    model.Add(x[0] == 1)
    evens, odds = evens_odds(n)
    model.Add(sum(x[v] for v in evens) - sum(x[v] for v in odds) >= 0)
    if warmstart:
        # parity class (2^{n-1} vertices, all internal degree 0) + one odd
        # vertex = 2^{n-1}+1 vertices; only the odd vertex violates the
        # degree bound (it has degree n).  Near-feasible hint guiding CP-SAT
        # search toward the feasible region.
        for v in range(N):
            model.AddHint(x[v], 1 if (parity_of(v) == 0 or v == 1) else 0)
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = time_limit
    solver.parameters.num_search_workers = workers
    solver.parameters.log_search_progress = False
    status = solver.Solve(model)
    dt = time.time() - t0
    feasible = status in (cp_model.OPTIMAL, cp_model.FEASIBLE)
    S = None
    if feasible:
        S = [v for v in range(N) if solver.Value(x[v]) == 1]
    return feasible, S, status, dt


def peak_rss_mb():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, required=True)
    ap.add_argument("--d", type=int, required=True)
    ap.add_argument("--highs-tl", type=float, default=380)
    ap.add_argument("--sat-tl", type=float, default=600)
    ap.add_argument("--highs-threads", type=int, default=None)
    ap.add_argument("--sat-workers", type=int, default=8)
    ap.add_argument("--witness", type=str, default=None)
    args = ap.parse_args()

    n, d = args.n, args.d
    m = (1 << (n - 1)) + 1
    print(f"=== n={n} d={d} |S| target={m} (vertices {1 << n}) ===", flush=True)
    print(f"thread caps: OPENBLAS={os.environ.get('OPENBLAS_NUM_THREADS')} "
          f"OMP={os.environ.get('OMP_NUM_THREADS')}", flush=True)

    print(f"\n[HiGHS milp] time_limit={args.highs_tl}s", flush=True)
    feas_h, S_h, status_h, msg_h, dt_h = highs_decision(
        n, d, args.highs_tl, threads=args.highs_threads)
    print(f"  feasible={feas_h} status={status_h} [{dt_h:.1f}s] "
          f"peak_rss={peak_rss_mb():.0f}MB", flush=True)
    if not feas_h:
        print(f"  message: {str(msg_h)[:200]}", flush=True)
    if feas_h and S_h is not None:
        size, mx, dist = verify_set(n, S_h)
        print(f"  witness: |S|={size} need={m} D(S)={mx} "
              f"dist={dist} verified={size == m and mx <= d}", flush=True)

    print(f"\n[CP-SAT] time_limit={args.sat_tl}s workers={args.sat_workers} ", flush=True)
    feas_s, S_s, status_s, dt_s = cpsat_decision(
        n, d, args.sat_tl, workers=args.sat_workers)
    print(f"  feasible={feas_s} status={status_s} [{dt_s:.1f}s] "
          f"peak_rss={peak_rss_mb():.0f}MB", flush=True)
    if feas_s and S_s is not None:
        size, mx, dist = verify_set(n, S_s)
        print(f"  witness: |S|={size} need={m} D(S)={mx} "
              f"dist={dist} verified={size == m and mx <= d}", flush=True)

    if feas_h is not None and feas_s is not None and not (feas_h and feas_s):
        agree = "AGREE" if feas_h == feas_s else "*** DISAGREE ***"
        print(f"\n-> solvers {agree} (HiGHS={feas_h}, CP-SAT={feas_s})", flush=True)
    if feas_h and feas_s:
        print(f"\n-> both solvers FEASIBLE: AGREE", flush=True)

    S = S_s if (feas_s and S_s is not None) else S_h
    if S is not None:
        size, mx, dist = verify_set(n, S)
        if size != m or mx > d:
            print(f"*** WITNESS FAILED verification: |S|={size} D(S)={mx} ***", flush=True)
            return 1
        out = args.witness or f"/workspace/code/out/witness_n{n}.txt"
        with open(out, "w") as f:
            f.write(f"# n={n} d={d} |S|={size} D(S)={mx} dist={dist}\n")
            for v in sorted(S):
                f.write(f"{v}\n")
        print(f"\nwrote {out} (|S|={size}, D(S)={mx}, dist={dist})", flush=True)
    else:
        print(f"\nno witness: n={n} d={d} undecided or infeasible "
              f"(statuses above: HiGHS={status_h} CP-SAT={status_s})", flush=True)

    print("\nDONE", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())