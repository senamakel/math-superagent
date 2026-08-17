"""CP-SAT orbit-matrix find-mode for srg(99,14,1,2) (m=33, fixed-point-free
order-3 automorphism), same build() equation as the validated encoder, WITH a
sound S_33 symmetry break.

Symmetry group: simultaneous row+column permutation (conjugation by S_33) of
the orbit indices. Every constraint is conjugation-covariant:
  - M^2 = (k-mu)I + (lam-mu)M + mu*3J is conjugation-invariant,
  - all row sums equal k,
  - "diagonal in {0,2}" is conjugation-invariant (permutes diagonal positions).
Conjugates are equivalent for an EXISTENCE decision (we decide whether ANY
orbit matrix exists; we are not counting), so forcing one canonical
representative discards nothing.

Canonical break (sound, loses no solutions):
  1. Diagonal nondecreasing: diag[0] <= diag[1] <= ... <= diag[m-1].
     (diagonal values lie in {0,2}, so 0-diagonal orbits come first.)
  2. Row 0 is the lexicographically minimal row: row_0 <=_lex row_i, all i.
     Under conjugation we can always move the lex-min row to position 0.

Lex comparator a <=_lex b, m variables each (correct reified encoding):
  - "all equal so far" chain: pf[c] = (a[0..c]==b[0..c]), pf[-1]=true.
  - lt[0] = a[0] < b[0];  lt[c] = pf[c-1] AND a[c] < b[c].
  - a <=_lex b  <=>  pf[m-1] OR (OR_c lt[c]).
Strict int less is half-reified each direction (supported for linear bounds).
"""
import sys
from ortools.sat.python import cp_model
import numpy as np


def _lex_le(model, A, i, j, m):
    """boolvar = (row i <=_lex row j) for symmetric matrix vars A[i][j]."""
    def val(a, b):
        return A[(min(a, b), max(a, b))]
    pf_prev = model.NewBoolVar("pf")
    model.Add(pf_prev == 1)
    or_list = []
    ever_less_before = []
    # we need lt_c and pf chain
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
        lt_and = model.NewBoolVar(f"la_{i}_{j}_{c}")  # pf_prev AND lt_c
        model.AddBoolAnd([pf_prev, lt_c]).OnlyEnforceIf(lt_and)
        model.AddBoolOr([pf_prev.Not(), lt_c.Not()]).OnlyEnforceIf(lt_and.Not())
        or_list.append(lt_and)
        pfs.append(pe_c)
        pf_prev = pe_c
    # result = pf[m-1] OR any(lt_and)
    result = model.NewBoolVar(f"lres_{i}_{j}")
    model.AddBoolOr([pfs[-1]] + or_list).OnlyEnforceIf(result)
    none = []
    # result false => all lt_and false and pf[m-1] false
    model.AddBoolOr([result, pfs[-1].Not()])
    for k_ in or_list:
        model.AddBoolOr([result, k_.Not()])
    # enforce that result is false only when appropriate: half-reify is enough
    # for the direction we need (we force result=1, so OnlyEnforceIf suffices).
    return result


def run(m, k, lam, mu, maxseconds, symbreak=True, out=None):
    model = cp_model.CpModel()
    A = {}
    for i in range(m):
        for j in range(i, m):
            A[(i, j)] = model.NewIntVar(0, 3, f"M{i}_{j}")
    def g(i, j):
        return A[(min(i, j), max(i, j))]

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

    if symbreak:
        for i in range(m - 1):
            model.Add(A[(i, i)] <= A[(i + 1, i + 1)])
        for i in range(1, m):
            lv = _lex_le(model, A, 0, i, m)
            model.Add(lv == 1)   # row 0 <=_lex row i

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = maxseconds
    solver.parameters.num_search_workers = 4
    if out is not None:
        solver.log_callback = lambda msg: out.write(msg + "\n")
    st = solver.Solve(model)
    return solver, st, A, g


def main():
    which = sys.argv[1] if len(sys.argv) > 1 else "g99"
    symstr = sys.argv[2] if len(sys.argv) > 2 else "sb"
    maxsec = float(sys.argv[3]) if len(sys.argv) > 3 else 600
    symbreak = (symstr == "sb")
    if which == "rook":
        m, k, lam, mu = 3, 4, 1, 2
    elif which == "g99":
        m, k, lam, mu = 33, 14, 1, 2
    else:
        print("usage: orbit_z3_enc_g99_run.py {rook|g99} {sb|nosb} [seconds]")
        return
    print(f"m={m} k={k} lam={lam} mu={mu} symbreak={symbreak} maxsec={maxsec}",
          flush=True)
    solver, st, A, g = run(m, k, lam, mu, maxsec, symbreak)
    print(f"solver status: {solver.StatusName(st)}", flush=True)
    if st in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        rows = [[solver.Value(g(i, j)) for j in range(m)] for i in range(m)]
        M = np.array(rows, dtype=np.int64)
        C = M @ M
        rhs = (k - mu) * np.eye(m) + (lam - mu) * M + mu * 3 * np.ones((m, m))
        ok = bool(np.all(C == rhs))
        print(f"SOLUTION FOUND; equation holds: {ok}; "
              f"row sums all k: {all(M[i].sum() == k for i in range(m))}; "
              f"diag values: {sorted(set(M[i, i] for i in range(m)))}")
        if which == "rook":
            print(M.tolist())
        return 0
    elif st == cp_model.INFEASIBLE:
        print("INFEASIBLE: no symmetric orbit matrix satisfies the quotient "
              "equation with these constraints (order-3 automorphism excluded).")
        return 2
    else:
        print("INCONCLUSIVE (timeout/UNKNOWN). No verdict.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
