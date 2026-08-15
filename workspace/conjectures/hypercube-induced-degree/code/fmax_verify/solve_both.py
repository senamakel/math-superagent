#!/usr/bin/env python3
"""Independent two-solver verification of f(n) = min D(S), |S|=2^{n-1}+1.

For each requested (n, d) pair, decide "is there S of size 2^{n-1}+1 with
internal-degree maximum D(S) <= d?" by TWO independent exact solvers:

  * HiGHS binary ILP  -- lib.fmax.decision_ilp (scipy.optimize.milp)
  * ortools CP-SAT    -- reimplementation below of the same decision form

Both are polynomial-size decision ILPs (2^n binaries, 2^n+1 linear
constraints), never an enumeration of subsets. The two solvers must agree on
every pair; a disagreement is flagged loudly and is the thing under test.

Threads are pinned to 1 BEFORE numpy/scipy import (prior runs OOM-crashed).

Usage: python3 solve_both.py n1:n d1[,d2,...] ...   e.g.
       python3 solve_both.py 8:3,2  9:3,2  10:4,3  11:4,3
"""

import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"

import sys
import time
from collections import Counter

from ortools.sat.python import cp_model
from lib.fmax import decision_ilp, decision_ilp_witness


def cpsat_decision(n, d, timeout_seconds=520):
    """CP-SAT decision: is there S of size 2^{n-1}+1 with D(S) <= d?
    Returns (feasible, witness_or_None).

    Big-M device (same linearisation as lib.fmax.decision_ilp): the internal
    degree bound may only bite a vertex that is SELECTED (x_v = 1).  For every
    vertex v the constraint is
        sum(x[u] for u in N(v)) + n*x_v <= d + n
    which, when x_v = 1, gives sum over selected neighbours <= d (the internal
    degree bound), and when x_v = 0 is slack by n (always true since a vertex
    has at most n neighbours).  Applying `sum(x[N(v)]) <= d` to non-selected
    vertices -- the form in code/out/upper_n10_11.py -- is WRONG: it forbids
    any non-selected vertex from having d+1 selected neighbours, a condition
    the definition does not impose, and it falsified even known-feasible
    witnesses in this workspace (n=3,d=2, n=4,d=2)."""
    N = 1 << n
    m = (1 << (n - 1)) + 1
    model = cp_model.CpModel()
    x = [model.NewBoolVar(f"x{i}") for i in range(N)]
    model.Add(sum(x) == m)
    for v in range(N):
        model.Add(sum(x[v ^ (1 << k)] for k in range(n)) + n * x[v] <= d + n)
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = timeout_seconds
    solver.parameters.num_search_workers = 8
    status = solver.Solve(model)
    feasible = status in (cp_model.OPTIMAL, cp_model.FEASIBLE)
    S = None
    if feasible:
        S = {v for v in range(N) if solver.Value(x[v]) == 1}
    return feasible, S


def max_degree(S, n):
    """(max_internal_degree, distribution) of S in Q_n; exact ints."""
    S = set(S)
    if not S:
        return (0, Counter())
    deg = Counter()
    for v in S:
        c = 0
        for k in range(n):
            if (v ^ (1 << k)) in S:
                c += 1
        deg[c] += 1
    return (max(deg), deg)


def parse(spec):
    pairs = []
    for tok in spec:
        npart, _, dpart = tok.partition(":")
        n = int(npart)
        for d in dpart.split(","):
            d = d.strip()
            if d:
                pairs.append((n, int(d)))
    return pairs


def main():
    specs = sys.argv[1:]
    pairs = parse(specs)
    if not pairs:
        print("no (n,d) pairs given"); return 1

    for (n, d) in pairs:
        line = f"\n=== n={n} d={d}  (|S| target = {2**(n-1)+1}) ==="
        print(line, flush=True)

        # route 1: HiGHS ILP
        t0 = time.time()
        feas_highs = decision_ilp(n, d)
        t_highs = time.time() - t0
        print(f"  HiGHS ILP : feasible={feas_highs}  [{t_highs:.1f}s]", flush=True)

        # route 2: CP-SAT
        t0 = time.time()
        feas_sat, S = cpsat_decision(n, d)
        t_sat = time.time() - t0
        print(f"  CP-SAT    : feasible={feas_sat}  [{t_sat:.1f}s]", flush=True)

        agree = (feas_highs == feas_sat)
        verdict = "AGREE" if agree else "*** DISAGREE ***"
        print(f"  -> {verdict}", flush=True)

        # independent confirmation of a witness's degree profile (third route)
        if feas_sat and S is not None:
            mx, dist = max_degree(S, n)
            ok_size = len(S) == 2 ** (n - 1) + 1
            ok_deg = mx <= d
            print(f"  witness: |S|={len(S)} (ok={ok_size}) max_deg={mx} (<=d ok={ok_deg}) "
                  f"dist={dict(sorted(dist.items()))}", flush=True)

    print("\nDONE", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
