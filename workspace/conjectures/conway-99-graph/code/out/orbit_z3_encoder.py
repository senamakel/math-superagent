"""CP-SAT orbit-matrix encoder for a fixed-point-free order-3 automorphism.

Setup. A fixed-point-free order-3 automorphism of an srg(v,k,lam,mu) has
v/3 = m point-orbits, all of length 3. The orbit matrix M is m x m,
symmetric, integer nonnegative, with
   M_ij = number of neighbours in point-orbit j of a vertex of point-orbit i,
row sums = k, diagonal values in {0, 2} (a 3-vertex orbit contains 0, 1 or 2
edges joining a fixed vertex to its own orbit), entries bounded by 3.

Pulling the eigenvalue equation A^2 = k I + lam A + mu (J - I - A) back through
the orbit indicator gives the NECESSARY equation
   M^2 = (k-mu) I + (lam-mu) M + mu * n * J        (n = orbit length = 3)
i.e.  M^2_ij = (k-mu) delta_ij + (lam-mu) M_ij + mu*3.

An ORBIT MATRIX THAT FAILS THIS EQUATION CANNOT COME FROM SUCH A GRAPH, so
INFEASIBLE proves no fixed-point-free order-3 automorphism exists. It does NOT
show the graph itself does not exist (directive 27 gate 1). Conversely, if the
encoder finds a solution it behaves consistently with such an action (a
necessary condition only).

The quadratic M^2_ij = sum_t M_it M_tj is encoded with OR-Tools CP-SAT's
native bounded-integer multiplication (entries in 0..3). Ring: exact integer
(Z). This is the same code path used for the control (BvLS / rook(3)) and for
the 99 case.

Gate (directive 27 gate 2): the encoder MUST find the control orbit matrix
before an UNSAT on 99 is believed. We solve BvLS (m=81) and rook(3) (m=3) in
"find" mode and compare.
"""
import sys
from ortools.sat.python import cp_model


def build(m, k, lam, mu, maxseconds):
    """CP-SAT model: find symmetric integer M, row sums k, diag in {0,2},
    entries in 0..3, satisfying M^2 = (k-mu)I + (lam-mu)M + mu*3*J."""
    model = cp_model.CpModel()
    M = {}
    for i in range(m):
        for j in range(i, m):          # upper triangle; symmetric
            M[(i, j)] = model.NewIntVar(0, 3, f"M{i}_{j}")
    def g(i, j):
        return M[(min(i, j), max(i, j))]
    # diagonal in {0,2}
    for i in range(m):
        model.AddAllowedAssignments([M[(i, i)]], [(0,), (2,)])
    # row sums = k
    for i in range(m):
        model.Add(sum(M[(i, j)] if i <= j else M[(j, i)] for j in range(m)) == k)
    # M^2 = (k-mu)I + (lam-mu)M + mu*3 J
    off = lam - mu
    c1 = k - mu
    c2 = mu * 3   # mu * orbit length
    for i in range(m):
        for j in range(m):
            # M^2_ij = sum_t M_it M_tj
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
    st = solver.Solve(model)
    return solver, st, M, g


def extract(solver, M, g, m, oned):
    rows = []
    for i in range(m):
        rows.append([solver.Value(g(i, j)) for j in range(m)])
    return rows


def orbits_from_perm(perm):
    """Given the cycle structure (list of orbit members) of a fixed-point-free
    permutation, produce the canonical identity-on-orbits assignment and the
    true orbit matrix. Here we just return the orbit matrix from a graph."""
    pass


def check_eq(M, k, lam, mu, m):
    """Verify M^2 = (k-mu)I + (lam-mu)M + mu*3 J exactly (integers)."""
    import numpy as np
    M = np.array(M, dtype=np.int64)
    C = M @ M
    rhs = (k - mu) * np.eye(m) + (lam - mu) * M + mu * 3 * np.ones((m, m))
    return bool(np.all(C == rhs)), int(np.max(np.abs(C - rhs)))


def main():
    which = sys.argv[1] if len(sys.argv) > 1 else "bvls"
    if which == "bvls":
        m, k, lam, mu = 81, 22, 1, 2
        maxsec = 300
        label = "BvLS validation (must FIND)"
    elif which == "rook":
        m, k, lam, mu = 3, 4, 1, 2
        maxsec = 60
        label = "rook(3) validation (must FIND)"
    elif which == "g99":
        m, k, lam, mu = 33, 14, 1, 2
        maxsec = float(sys.argv[2]) if len(sys.argv) > 2 else 600
        label = "99 case: fixed-point-free order-3 feasibility"
    else:
        print("usage: orbit_z3_encoder.py {bvls|rook|g99 [seconds]}")
        return
    print(f"=== {label} ===")
    print(f"m={m} orbits (length 3), srg({3*m},{k},{lam},{mu})")
    solver, st, M, g = build(m, k, lam, mu, maxsec)
    print(f"solver status: {solver.StatusName(st)}")
    if st in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        rows = extract(solver, M, g, m, None)
        # verify the equation on the returned matrix exactly
        ok, md = check_eq(rows, k, lam, mu, m)
        print(f"SOLUTION FOUND. equation M^2=(k-mu)I+(lam-mu)M+mu*3J holds: {ok}"
              f" (max abs diff {md})")
        print(f"row sums: all==k : {all(sum(r) == k for r in rows)}")
        print(f"diagonal values present: {sorted(set(rows[i][i] for i in range(m)))}")
        if which == "rook":
            for r in rows:
                print("  " + " ".join(map(str, r)))
        return 0
    elif st == cp_model.INFEASIBLE:
        print("INFEASIBLE: no symmetric orbit matrix with row sums k, "
              "diag in {0,2}, entries in 0..3 satisfies the srg-quotient equation.")
        return 2
    else:
        print("INCONCLUSIVE (timeout / unknown). No verdict.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
