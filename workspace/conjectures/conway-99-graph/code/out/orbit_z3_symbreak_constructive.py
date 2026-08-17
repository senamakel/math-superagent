"""Decisive construction test for the symbreak encoder's canonical break.

The 99 encoder (orbit_z3_enc_g99_run.py) imposes on the orbit matrix M
  A. diag[0] <= diag[1] <= ... <= diag[m-1]
  B. row_0 <=_lex row_i for every i.
The break is SOUND for a class of orbit matrices iff every class has a
representative satisfying A and B.  Since A and B are conjugation-invariant
(row+column permutation), it suffices to construct, for each real orbit matrix
M0, a conjugate satisfying the break and confirm the CP-SAT model accepts it.

For BvLS the diagonal is constant, so A is vacuous and only B matters:
row 0 lex-min.  We construct a conjugate as follows: for each candidate vertex
v to occupy position 0, place v at position 0 and order every other vertex's
position by ascending M0[v, .] (so v's row is lexicographically as small as
that vertex allows), then test whether row 0 is the lex-min row of the
resulting matrix.  This is a constructive witness: if it succeeds on the real
BvLS orbit matrix, the break is confirmed not to reject that real class.

For rook(3) we verify exhaustively (6 conjugates).
Exact integer arithmetic.  No floats.
"""
import numpy as np
from ortools.sat.python import cp_model
from lib.srg import bvls_graph, orbit_matrix


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
    M = np.asarray(M, dtype=np.int64)
    m = M.shape[0]
    diag = [int(M[i, i]) for i in range(m)]
    if diag != sorted(diag):
        return False
    rows = [list(map(int, M[i])) for i in range(m)]
    r0 = rows[0]
    return all(r0 <= list(r) for r in rows)


def conjugate(M, perm):
    m = M.shape[0]
    P = np.zeros((m, m), dtype=np.int64)
    for ni, oi in enumerate(perm):
        P[ni, oi] = 1
    return P @ M @ P.T


def construct_break_conjugate(M0):
    """For each vertex v as position 0 with the other columns sorted by
    M0[v, .] ascending, return (perm, M1) if the result satisfies the break."""
    M0 = np.asarray(M0, dtype=np.int64)
    m = M0.shape[0]
    found = []
    for v in range(m):
        others = [j for j in range(m) if j != v]
        others_sorted = sorted(others, key=lambda j: (int(M0[v, j]), j))
        perm = [v] + others_sorted
        M1 = conjugate(M0, perm)
        if satisfies_break(M1):
            found.append((perm, M1))
    return found


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


def main():
    print("=== constructive soundness witness for the symbreak canonical break ===")

    # rook(3): exhaustive
    M0 = np.array([[0, 2, 2], [2, 0, 2], [2, 2, 0]], dtype=np.int64)
    import itertools
    m, k, lam, mu = 3, 4, 1, 2
    hits = 0
    for perm in itertools.permutations(range(m)):
        if satisfies_break(conjugate(M0, perm)):
            hits += 1
    print(f"rook(3) m=3: conjugates satisfying break = {hits}/6")
    if hits > 0:
        solver, st = build_fixed_with_break(3, 4, 1, 2, M0, 60)
        print(f"  fix M0 (a break-satisfying conjugate) + break: status={solver.StatusName(st)}")

    # BvLS: constructive
    A = bvls_graph()
    orbits, lengths, Mm = orbit_matrix(A, bvls_z3())
    assert set(lengths) == {3}
    M0 = np.asarray(Mm, dtype=np.int64)
    m, k, lam, mu = 81, 22, 1, 2
    print(f"BvLS m=81: diag = {sorted(set(np.diag(M0).tolist()))} "
          f"(constants, so break A is vacuous; only row0 lex-min)")
    found = construct_break_conjugate(M0)
    print(f"constructive search over candidate roots: {len(found)} vertex-root(s) yield a break-satisfying conjugate")
    if found:
        perm, M1 = found[0]
        print(f"  verified satisfies_break(M1): {satisfies_break(M1)}")
        solver, st = build_fixed_with_break(m, k, lam, mu, M1, 60)
        status = solver.StatusName(st)
        wall = solver.WallTime()
        print(f"  fix M1 + break: status={status} (wall {wall:.2f}s)")
        print(f"  -> break admits a REAL BvLS orbit matrix: "
              f"{status in ('FEASIBLE','OPTIMAL')}")
    else:
        print("  NO constructed conjugate satisfies the break (sorted-column construction).")
        print("  -> the break has not been shown to admit the real BvLS class;")

    print()
    print("INTERPRETATION")
    print("  Soundness of the break requires that SOME conjugate satisfies it.  The")
    print("  sorted-column construction is one constructive witness, not an exhaustive")
    print("  proof for BvLS (m=81, 81! conjugates).  If the construction succeeds, the")
    print("  break is confirmed SOUND on the real BvLS class.  If it fails, the break is")
    print("  UNVALIDATED (neither proved sound nor unsound) and a 99 INFEASIBLE from it")
    print("  must be treated as NOT EVIDENCE until resolved, per directive 30.")


if __name__ == "__main__":
    main()
