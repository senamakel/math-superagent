"""Orbit-matrix feasibility for a fixed-point-free order-3 automorphism,
encoded for OR-Tools CP-SAT (exact integer).

Mitigates both the lambda=1,mu=2 srg condition and the De Winter-Kamischke-Wang
congruence to orbit level. For an order-3 fixed-point-free action the orbit
matrix M (m x m, symmetric, integer) must satisfy:
    MM^T = 6J + (k-2) I - M          (srg condition, validated on controls)
    row sums M[i,:] = k              (regularity)
    M[i][i] in {0,2}                 (orbit = triangle or independent set)
    M[i][j] in {0..3} off-diagonal   (orbit size 3)
    DKW: 3T = g = #vertices mapped to adjacent vertex; g -= 4 is 0 mod 7.

We enforce the MM^T identity by requiring, for the symmetric M, the unique
satisfier of MM^T = 6J + c I - M: since for adjacent-in-orbit entries this is
exactly what a real srg orbit matrix must satisfy (validated), we constrain the
quadratic sums.

Rather than a full quadratic product over large domains, we exploit that the
sum block identity is the *necessary* condition; we post the diagonal sums
directly as CP-SAT integers and the off-diagonal sums as integers, adding
element/table constraints for the (M_li * M_lj) products where needed.

ENTRY POINT: python3 code/out/orbit_matrix_z3.py  <bvls|99>
Writes a captured report to code/out/orbit_matrix_z3_<tag>.captured.txt
"""
import sys
import time
import numpy as np
from ortools.sat.python import cp_model


def encode(m, k, c, ts, timeout, label):
    """Return (model, M) solving orbit-matrix feasibility, or None if UNSAT.

    m    : number of size-3 orbits
    k    : degree
    c    : (k-2)
    ts   : allowed triangle-orbit counts (DKW), or None for no DKW constraint
    """
    model = cp_model.CpModel()
    # upper bound on any M[i][j]: off-diag 3, diag 2
    ub = 3
    M = [[model.NewIntVar(0, ub, f"M_{i}_{j}") for j in range(m)]
         for i in range(m)]
    # symmetry + diagonal type + off-diagonal range
    for i in range(m):
        for j in range(i, m):
            if i != j:
                model.Add(M[i][j] <= 3)
                model.Add(M[j][i] == M[i][j])
            else:
                model.Add(M[i][i] == M[j][i])  # trivial self
                # diagonal in {0,2}
                b = model.NewBoolVar(f"diag_{i}")
                model.Add(M[i][i] == 0).OnlyEnforceIf(b)
                model.Add(M[i][i] == 2).OnlyEnforceIf(b.Not())
    # regular: row sums = k
    for i in range(m):
        model.Add(sum(M[i][j] for j in range(m)) == k)

    # MM^T = 6J + c I - M, entrywise, via AddMultiplicationEquality (CP-SAT
    # does not multiply two IntVars directly).
    Jc = 6
    # helper: sum over l of M[a][l] * M[b][l]  == target
    def block_sum(a, b, target):
        terms = []
        for l in range(m):
            p = model.NewIntVar(0, 9, f"p_{a}_{b}_{l}")
            model.AddMultiplicationEquality(p, M[a][l], M[b][l])
            terms.append(p)
        model.Add(sum(terms) == target)

    for i in range(m):
        block_sum(i, i, Jc + c - M[i][i])          # diagonal
        for j in range(i + 1, m):
            block_sum(i, j, Jc - M[i][j])          # off-diagonal

    # DKW triangle-orbit count constraint (for the DKW target)
    if ts is not None:
        # diagonal entries are orbit-type indicators in {0,2}; T = #triangles.
        T = model.NewIntVar(0, m, "T")
        diagb = []
        for i in range(m):
            tb = model.NewBoolVar(f"TRI_{i}")
            model.Add(M[i][i] == 2).OnlyEnforceIf(tb)
            model.Add(M[i][i] == 0).OnlyEnforceIf(tb.Not())
            diagb.append(tb)
        model.Add(sum(diagb) == T)
        allowed = []
        for t in ts:
            b = model.NewBoolVar(f"T_eq_{t}")
            model.Add(T == t).OnlyEnforceIf(b)
            allowed.append(b)
        model.AddBoolOr(allowed)

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = timeout
    solver.parameters.num_search_workers = 8
    status = solver.Solve(model)
    return solver, status, M


def solver_status_name(s):
    return {cp_model.OPTIMAL: "OPTIMAL", cp_model.FEASIBLE: "FEASIBLE",
            cp_model.INFEASIBLE: "INFEASIBLE", cp_model.MODEL_INVALID: "MODEL_INVALID",
            cp_model.UNKNOWN: "UNKNOWN"}.get(s, str(s))


def main():
    tag = sys.argv[1] if len(sys.argv) > 1 else "99"
    if tag not in ("bvls", "99"):
        print("usage: orbit_matrix_z3.py <bvls|99>")
        sys.exit(2)
    t0 = time.time()

    if tag == "bvls":
        m, k, c = 81, 22, 20
        # DKW for bvls: 3T = g, g ≡ k-s (mod 9) with s=-5 => g≡27≡0 => 3T≡0=>T≡0 (mod 3)
        ts = list(range(0, m + 1, 3))  # T in {0,3,...}
        timeout = 600
    else:
        m, k, c = 33, 14, 12
        ts = [6, 13, 20, 27]          # DKW: T ≡ 6 (mod 7)
        timeout = 600

    n_vars = m * (m + 1) // 2
    solver, status, M = encode(m, k, c, ts, timeout, tag)

    wall = time.time() - t0
    lines = []
    lines.append(f"orbit_matrix_z3_{tag}: orbit-matrix feasibility, fixed-point-free Z3")
    lines.append(f"  m (size-3 orbits)          = {m}")
    lines.append(f"  k (degree)                 = {k}")
    lines.append(f"  orbit-level MM^T identity  = 6J + {k-2}I - M")
    lines.append(f"  search variables           = {n_vars}")
    lines.append(f"  MM^T constraints           = {m*m}")
    lines.append(f"  DKW T values allowed       = {ts}")
    lines.append(f"  CP-SAT status              = {solver_status_name(status)}")
    lines.append(f"  wall clock (s)             = {wall:.2f}")

    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        Mv = np.array([[solver.Value(M[i][j]) for j in range(m)] for i in range(m)])
        rowsums = Mv.sum(axis=1)
        diag = np.diag(Mv)
        T = int(np.sum(diag == 2))
        lines.append(f"  FEASIBLE: T (#triangle orbits) = {T}")
        lines.append(f"  row sums all == {k}: {bool(np.all(rowsums == k))} "
                     f"(min {rowsums.min()}, max {rowsums.max()})")
        lines.append(f"  diagonal set {{0,2}}: {set(diag.tolist()) <= {0,2}}")
        # verify the identity on the assignment
        Mf = Mv.astype(np.int64)
        lhs = Mf @ Mf.T
        rhs = 6 * np.ones((m, m), dtype=np.int64) + (k - 2) * np.eye(m, dtype=np.int64) - Mf
        lines.append(f"  MM^T == 6J + {k-2}I - M on assignment: {np.array_equal(lhs, rhs)}")
        lines.append("  orbit matrix M:")
        for i in range(m):
            lines.append("    " + " ".join(f"{int(x)}" for x in Mv[i]))
    elif status == cp_model.INFEASIBLE:
        lines.append("  INFEASIBLE: no orbit matrix of this shape exists "
                     f"(excludes order-3 fixed-point-free automorphism for {tag}).")
    elif status == cp_model.UNKNOWN:
        lines.append("  UNKNOWN: solver timed out; establishes nothing.")
    else:
        lines.append(f"  {solver_status_name(status)}: model problem.")

    report = "\n".join(lines)
    print(report)
    out = f"code/out/orbit_matrix_z3_{tag}.captured.txt"
    with open(out, "w") as f:
        f.write(report + "\n")
    print(f"\n[wrote {out}]")


if __name__ == "__main__":
    main()
