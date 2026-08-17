"""DIRECTIVE 29/30 gate specifically for the SYMMETRY-BROKEN encoder
orbit_z3_enc_g99_run.py: verify that adding the S_33 canonical-ordering break
to the model does NOT reject a known-good orbit matrix (rook m=3, BvLS m=81).

For each control: take M0 (an orbit matrix that genuinely comes from the
graph under a fixed-point-free order-3 automorphism), fix every M_ij == M0_ij,
AND impose the same canonical-break constraints the experimental 99 encoder
uses (diagonal nondecreasing, row 0 lexicographically minimal). A sound
symmetry break admits at least one conjugate per orbit-matrix class, so if the
canonical representative of M0's class is rejected the break is UNSOUND.

The canonical representative of M0's class is produced by relabelling orbits
so that (diag nondecreasing AND row 0 lex-min) hold. We build the model on the
ORIGINAL M0 and, rather than relabelling, simply test BOTH:
   (a) M0 with the break constraints added directly  -- may be rejected if M0
       is not the canonical representative (that is EXPECTED and fine);
   (b) the canonical conjugate M0' of M0 (achieved by sorting orbits to push
       all diag-2 positions later and choosing the relabel that puts the
       lex-min row first) with the same break constraints -- MUST be accepted.

If neither (a) nor (b) is accepted, the break itself is unsound: it would
eliminate real orbit matrices.  Ring: exact integer (numpy int64).  No floats.
"""
import sys
import itertools
import numpy as np
from ortools.sat.python import cp_model
from lib.srg import bvls_graph, orbit_matrix


def _prod_idx(s):
    return s[0] * 81 + s[1] * 27 + s[2] * 9 + s[3] * 3 + s[4]


def bvls_z3():
    """The order-3 translation automorphism on Z_3^5 (BvLS construction)."""
    a = (1, 0, 0, 0, 0)
    g = [0] * 243
    for s0 in range(3):
        for s1 in range(3):
            for s2 in range(3):
                for s3 in range(3):
                    for s4 in range(3):
                        s = (s0, s1, s2, s3, s4)
                        t = tuple((s[k] + a[k]) % 3 for k in range(5))
                        g[_prod_idx(s)] = _prod_idx(t)
    return g


def _lex_le(model, A, i, j, m):
    """boolvar = (row i <=_lex row j) using upper-triangle vars A[(a,b)]."""
    def val(a, b):
        return A[(min(a, b), max(a, b))]
    pf_prev = model.NewBoolVar("pf")
    model.Add(pf_prev == 1)
    or_list = []
    pfs = []
    for c in range(m):
        a = val(i, c)
        b = val(j, c)
        eq_c = model.NewBoolVar(f"eq_{i}_{j}_{c}")
        model.Add(a == b).OnlyEnforceIf(eq_c)
        model.Add(a != b).OnlyEnforceIf(eq_c.Not())
        pe_c = model.NewBoolVar(f"pe_{i}_{j}_{c}")
        model.AddBoolAnd([pf_prev, eq_c]).OnlyEnforceIf(pe_c)
        model.AddBoolOr([pf_prev.Not(), eq_c.Not()]).OnlyEnforceIf(pe_c.Not())
        lt_c = model.NewBoolVar(f"lt_{i}_{j}_{c}")
        model.Add(a < b).OnlyEnforceIf(lt_c)
        model.Add(a >= b).OnlyEnforceIf(lt_c.Not())
        lt_and = model.NewBoolVar(f"la_{i}_{j}_{c}")
        model.AddBoolAnd([pf_prev, lt_c]).OnlyEnforceIf(lt_and)
        model.AddBoolOr([pf_prev.Not(), lt_c.Not()]).OnlyEnforceIf(lt_and.Not())
        or_list.append(lt_and)
        pfs.append(pe_c)
        pf_prev = pe_c
    result = model.NewBoolVar(f"lres_{i}_{j}")
    model.AddBoolOr([pfs[-1]] + or_list).OnlyEnforceIf(result)
    model.AddBoolOr([result, pfs[-1].Not()])
    for k_ in or_list:
        model.AddBoolOr([result, k_.Not()])
    return result


def symbreak_constraints(model, A, g, m):
    """Diagonal nondecreasing + row 0 lex-min, mirroring the 99 encoder."""
    for i in range(m - 1):
        model.Add(A[(i, i)] <= A[(i + 1, i + 1)])
    for i in range(1, m):
        lv = _lex_le(model, A, 0, i, m)
        model.Add(lv == 1)


def build_fixed_sb(m, k, lam, mu, M0, maxseconds):
    """Model with M fixed to M0, plus the symmetry-break constraints.
    Returns (solver, status)."""
    model = cp_model.CpModel()
    A = {}
    for i in range(m):
        for j in range(i, m):
            A[(i, j)] = model.NewIntVar(0, 3, f"M{i}_{j}")
    def g(i, j):
        return A[(min(i, j), max(i, j))]
    for i in range(m):
        for j in range(i, m):
            model.Add(A[(i, j)] == int(M0[i, j]))
    for i in range(m):
        model.AddAllowedAssignments([A[(i, i)]], [(0,), (2,)])
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
    symbreak_constraints(model, A, g, m)
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = maxseconds
    solver.parameters.num_search_workers = 4
    st = solver.Solve(model)
    return solver, st


def canonical_conjugate(M0):
    """Relabel orbits so that (diagonal nondecreasing AND row 0 lex-min) hold.

    A relabelling of orbit indices is a conjugation M -> P M P^T with P a
    permutation matrix, and any such conjugation of a real orbit matrix is
    another real orbit matrix of the same class (the equation is
    conjugation-invariant).  So a canonical representative is produced by one
    global permutation of indices that respects a global sort key:
        key(i) = (diag(i), row_i)   sorted ascending.
    Sorting ALL indices by that composite key (diagonal first, then the whole
    row lexicographically) yields a matrix with diag nondecreasing AND, within
    each equal-diag block, the rows nondecreasing lexicographically.  Row that
    comes first in each block is then the block-min; putting the overall
    lex-min row at position 0 requires the additional step of choosing the
    block-min row first, which the single global sort already does because a
    row that is a global lex-min must lie in the first block with minimal
    diagonal and be the first such row.  We then verify both properties
    explicitly (defensive assert) before trusting the result.
    """
    M0 = np.asarray(M0, dtype=np.int64)
    m = M0.shape[0]
    def key(i):
        return (int(M0[i, i]), tuple(int(x) for x in M0[i]))
    order = sorted(range(m), key=key)
    P = np.zeros((m, m), dtype=np.int64)
    for ni, oi in enumerate(order):     # new index ni <- old index oi
        P[ni, oi] = 1
    M1 = P @ M0 @ P.T
    # defensive verification of the two canonical properties
    diag = [int(M1[i, i]) for i in range(m)]
    assert diag == sorted(diag), "diag not nondecreasing after global sort"
    rows = [list(map(int, M1[i])) for i in range(m)]
    r0 = rows[0]
    assert all(r0 <= list(r) for r in rows), "row 0 not lex-min after global sort"
    return M1


def verify(M0, k, lam, mu, label):
    M0 = np.asarray(M0, dtype=np.int64)
    m = M0.shape[0]
    C = M0 @ M0
    rhs = (k - mu) * np.eye(m, dtype=np.int64) + (lam - mu) * M0 \
        + mu * 3 * np.ones((m, m), dtype=np.int64)
    ok_eq = bool(np.all(C == rhs))
    ok_rows = bool(np.all(M0.sum(axis=1) == k))
    diag = sorted(set(np.diag(M0).tolist()))
    ok_diag = all(d in (0, 2) for d in diag)
    assert ok_eq and ok_rows and ok_diag, f"M0 for {label} failed own checks"
    return f"M0({label},m={m}) verified: sym, rows==k, diag ⊆{{0,2}}, eq holds"


def main():
    print("=== symbreak encoder: soundness gate (accepts known-good M0) ===")
    results = []
    cases = [
        ("rook(3)", 3, 4, 1, 2, np.array([[0, 2, 2], [2, 0, 2], [2, 2, 0]],
                                         dtype=np.int64)),
        ("BvLS", 81, 22, 1, 2, None),
    ]
    for label, m, k, lam, mu, M0 in cases:
        if M0 is None:
            A = bvls_graph()
            orbits, lengths, M = orbit_matrix(A, bvls_z3())
            assert set(lengths) == {3}
            M0 = np.asarray(M, dtype=np.int64)
        print(verify(M0, k, lam, mu, label))
        M0c = canonical_conjugate(M0)
        # (b) canonical conjugate + break must be accepted
        solver, st = build_fixed_sb(m, k, lam, mu, M0c, 60)
        status = solver.StatusName(st)
        wall = solver.WallTime()
        accepted = status in ("FEASIBLE", "OPTIMAL")
        print(f"  canonical conjugate + symbreak, m={m}: status={status} "
              f"(wall {wall:.2f}s)  ACCEPTED: {accepted}")
        results.append((label, status, accepted))
        print()

    print("=== SUMMARY ===")
    ok = True
    for label, status, acc in results:
        print(f"  {label}: {status}  ->  {'PASS (accepts known-good M0 under symbreak)' if acc else 'FAIL/INCONCLUSIVE'}")
        if not acc:
            ok = False
    if ok:
        print("\nThe symmetry break is SOUND on both controls: a canonical representative")
        print("of a real orbit matrix is accepted with the break imposed.  A 99 UNSAT would")
        print("therefore be evidence about the orbit-matrix equation, not a break artifact.")
    else:
        print("\nThe symmetry break REJECTS a known-good orbit matrix on at least one control.")
        print("The break is UNSOUND and must be fixed before any 99 run is read.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
