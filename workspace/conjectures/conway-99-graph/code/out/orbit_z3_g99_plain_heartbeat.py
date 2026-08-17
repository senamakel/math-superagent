"""Plain (unbroken) CP-SAT orbit-matrix find-mode for srg(99,14,1,2), m=33
fixed-point-free order-3 automorphism.

This is the SOUND route per directive 35 (the S_33 symmetry break is UNSOUND
and has been dropped). Every bound improvement from the solver is written
through a flushed log_callback heartbeat so that a long/stalled run still
leaves a visible, honest record: a moving bound is evidence, a stalled bound
is evidence too.

Verdict semantics (repeat, from directive 27/35):
  - INFEASIBLE excludes a fixed-point-free order-3 automorphism and nothing
    more (NOT that the graph does not exist).
  - UNKNOWN/TIMEOUT proves nothing; the record is the budget and the boundary.

Ring: exact integer (Z). Encoder equation (validated at rook m=3 OPTIMAL and
BvLS m=81 OPTIMAL in fixed-accept mode):
    M^2 = (k-mu) I + (lam-mu) M + mu*3*J
M symmetric, entries in 0..3, row sums = k, diagonal in {0,2}.
"""
import sys
from ortools.sat.python import cp_model
import numpy as np


def run(m, k, lam, mu, maxseconds, out):
    model = cp_model.CpModel()
    M = {}
    for i in range(m):
        for j in range(i, m):
            M[(i, j)] = model.NewIntVar(0, 3, f"M{i}_{j}")

    def g(i, j):
        return M[(min(i, j), max(i, j))]

    for i in range(m):
        model.AddAllowedAssignments([M[(i, i)]], [(0,), (2,)])
    for i in range(m):
        model.Add(sum(g(i, j) for j in range(m)) == k)

    off = lam - mu
    c1 = k - mu
    c2 = mu * 3
    for i in range(m):
        for j in range(m):
            prods = []
            for t in range(m):
                p = model.NewIntVar(0, 9, f"p_{i}_{j}_{t}")
                model.AddMultiplicationEquality(p, [g(i, t), g(t, j)])
                prods.append(p)
            sq = model.NewIntVar(0, 9 * m, f"sq_{i}_{j}")
            model.Add(sum(prods) == sq)
            rhs = c1 * (1 if i == j else 0) + off * g(i, j) + c2
            model.Add(sq == rhs)

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = maxseconds
    solver.parameters.num_search_workers = 4
    solver.parameters.log_search_progress = True
    solver.log_callback = lambda msg: (out.write(msg + "\n"), out.flush())
    st = solver.Solve(model)
    return solver, st, M, g


def main():
    which = sys.argv[1] if len(sys.argv) > 1 else "g99"
    maxsec = float(sys.argv[2]) if len(sys.argv) > 2 else 600.0
    m, k, lam, mu = 33, 14, 1, 2
    print(f"srg(99,14,1,2) m=33 fixed-point-free order-3 PLAIN (no symbreak) "
          f"maxsec={maxsec}", flush=True)
    solver, st, M, g = run(m, k, lam, mu, maxsec, sys.stdout)
    print(f"final solver status: {solver.StatusName(st)}", flush=True)
    if st in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        rows = [[solver.Value(g(i, j)) for j in range(m)] for i in range(m)]
        Mat = np.array(rows, dtype=np.int64)
        C = Mat @ Mat
        rhs = (k - mu) * np.eye(m) + (lam - mu) * Mat + mu * 3 * np.ones((m, m))
        ok = bool(np.all(C == rhs))
        print(f"SOLUTION FOUND. equation holds: {ok}; "
              f"row sums all==k: {all(Mat[i].sum() == k for i in range(m))}; "
              f"diag present: {sorted(set(Mat[i, i] for i in range(m)))}",
              flush=True)
        return 0
    elif st == cp_model.INFEASIBLE:
        print("INFEASIBLE: no fixed-point-free order-3 orbit matrix exists "
              "(excludes only that automorphism, NOT the graph).", flush=True)
        return 2
    else:
        print("INCONCLUSIVE (timeout/UNKNOWN): no verdict; record is the "
              "budget and the last bound above.", flush=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
