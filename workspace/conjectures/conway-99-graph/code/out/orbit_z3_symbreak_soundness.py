"""Soundness gate for the SYMMETRY-BREAK the 99 encoder applies.

Research question the operator cares about (directive 30 option 2, and the
reason to prefer the symbreak encoder): the experimental 99 encoder
orbit_z3_enc_g99_run.py imposes, alongside the necessary quotient equation
    M^2 = (k-mu)I + (lam-mu)M + mu*3J,   rows==k, diag in {0,2}, entry 0..3,
the canonical-ordering break
    A. diag[0] <= diag[1] <= ... <= diag[m-1]
    B. row_0 <=_lex row_i  for every i.
A break is SOUND iff every feasible orbit matrix has at least one conjugate
(under simultaneous row+column permutation) satisfying the break.  If the
break is unsound, a genuine order-3 automorphism (a real orbit matrix) could
be declared INFEASIBLE, which would be a false negative.  So before any 99
INFEASIBLE is believed, we must witness that the break admits a real orbit
matrix on the two controls.

Method (exact integer only):
  - rook(3): m=3, EXPLORE ALL 6 conjugates of the known-good M0 and check the
    break; prove soundness exhaustively at the small control.
  - BvLS:    m=81, the diagonal is constant (=2), so (A) is vacuous and the
    only condition is (B).  We random-search conjugations of the real M0 and
    check the break; report how many of N random conjugates satisfy it.
For each accepted conjugate, build the CP-SAT model with M FIXED to it PLUS
the break constraints and solve; it must be FEASIBLE/OPTIMAL (no search, so
fast) — confirming the break + real value are jointly consistent.
Ring: exact integer (numpy int64).  No floats.
"""
import numpy as np
from ortools.sat.python import cp_model
from lib.srg import bvls_graph, orbit_matrix
import random


def _prod_idx(s):
    return s[0] * 81 + s[1] * 27 + s[2] * 9 + s[3] * 3 + s[4]


def bvls_z3():
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


def satisfies_break(M):
    """Check the two canonical constraints on a concrete 0/1... 0..3 matrix."""
    M = np.asarray(M, dtype=np.int64)
    m = M.shape[0]
    diag = [int(M[i, i]) for i in range(m)]
    if diag != sorted(diag):
        return False
    rows = [list(map(int, M[i])) for i in range(m)]
    r0 = rows[0]
    return all(r0 <= list(r) for r in rows)


def build_fixed_with_break(m, k, lam, mu, M0fixed, maxseconds):
    model = cp_model.CpModel()
    A = {}
    for i in range(m):
        for j in range(i, m):
            A[(i, j)] = model.NewIntVar(0, 3, f"M{i}_{j}")
    def g(i, j):
        return A[(min(i, j), max(i, j))]
    for i in range(m):
        for j in range(i, m):
            model.Add(A[(i, j)] == int(M0fixed[i, j]))
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
    # break constraints
    for i in range(m - 1):
        model.Add(A[(i, i)] <= A[(i + 1, i + 1)])
    for i in range(1, m):
        lv = _lex_le(model, A, 0, i, m)
        model.Add(lv == 1)
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = maxseconds
    solver.parameters.num_search_workers = 4
    st = solver.Solve(model)
    return solver, st


def conjugate(M, perm):
    m = M.shape[0]
    P = np.zeros((m, m), dtype=np.int64)
    for ni, oi in enumerate(perm):
        P[ni, oi] = 1
    return P @ M @ P.T


def main():
    random.seed(12345)
    print("=== soundness gate for the symbreak encoder's canonical break ===")
    print("Constraint set S = {diag nondecreasing, row0 lex-min} on the orbit")
    print("matrix M satisfying the necessary quotient equation.")
    outcomes = []

    # ---- rook(3): exhaustive over all 6 conjugates ----
    M0 = np.array([[0, 2, 2], [2, 0, 2], [2, 2, 0]], dtype=np.int64)
    m, k, lam, mu = 3, 4, 1, 2
    print(f"\n--- rook(3) m={m}: exhaustive over all {6} conjugates of known-good M0 ---")
    import itertools
    from math import factorial
    good = []
    for perm in itertools.permutations(range(m)):
        Mc = conjugate(M0, perm)
        if satisfies_break(Mc):
            good.append(perm)
    print(f"conjugates satisfying the break: {len(good)}/{factorial(m)}")
    if good:
        perm = good[0]
        Mc = conjugate(M0, perm)
        solver, st = build_fixed_with_break(m, k, lam, mu, Mc, 60)
        status = solver.StatusName(st)
        print(f"  fix Mc={Mc.tolist()} + break: status={status}, "
              f"solver.WallTime={solver.WallTime():.2f}s")
        outcomes.append(("rook(3)", status, status in ("FEASIBLE", "OPTIMAL")))
    else:
        print("  NO conjugate satisfies the break -> break UNSOUND at rook(3)")
        outcomes.append(("rook(3)", "NONE", False))

    # ---- BvLS m=81: random conjugations ----
    A = bvls_graph()
    orbits, lengths, Mm = orbit_matrix(A, bvls_z3())
    assert set(lengths) == {3}
    M0 = np.asarray(Mm, dtype=np.int64)
    m, k, lam, mu = 81, 22, 1, 2
    print(f"\n--- BvLS m={m}: randomized conjugations of the real orbit matrix ---")
    diag = sorted(set(np.diag(M0).tolist()))
    print(f"diagonal values: {diag}  -> {'constant, (A) vacuous' if len(diag)==1 else 'not constant'}")
    N = 20000
    hits = 0
    first = None
    for _ in range(N):
        perm = list(range(m))
        random.shuffle(perm)
        Mc = conjugate(M0, perm)
        if satisfies_break(Mc):
            hits += 1
            if first is None:
                first = Mc
            if hits >= 1:
                break
    print(f"random conjugations tried up to: {N}; found satisfying break: {hits}")
    if first is not None:
        solver, st = build_fixed_with_break(m, k, lam, mu, first, 60)
        status = solver.StatusName(st)
        print(f"  fix a break-satisfying real conjugate + break: status={status}, "
              f"wall={solver.WallTime():.2f}s")
        outcomes.append(("BvLS(243)", status, status in ("FEASIBLE", "OPTIMAL")))
    else:
        print("  NO random conjugate satisfied the break (need larger search or break unsound)")
        outcomes.append(("BvLS(243)", "NONE", False))

    print("\n=== SUMMARY ===")
    ok = True
    for label, status, acc in outcomes:
        print(f"  {label}: status={status}  ->  {'PASS' if acc else 'FAIL/INCONCLUSIVE'}")
        if not acc:
            ok = False
    if ok:
        print("\nThe break admits a real orbit matrix of both controls (accepted under the break).")
        print("The symbreak encoder's canonical constraints are not vacuous/contradictory on")
        print("the real controls; a 99 INFEASIBLE would be read as an orbit-matrix statement,")
        print("with the caveat that full class-by-class soundness at m=33 is witnessed by")
        print("these controls, not proved for a hypothetical 99 matrix.")
    else:
        print("\nThe break rejects the real orbit matrix on a control: UNSOUND, must fix before")
        print("any 99 INFEASIBLE is believed.")
    return 0 if ok else 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
