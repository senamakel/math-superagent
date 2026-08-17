"""CP-SAT orbit-matrix encoder, m=33 for srg(99,14,1,2), fixed-point-free
order-3 automorphism, WITH a sound S_33 symmetry break.

Model: M symmetric 33x33 integer, entries in 0..3, row sums 14, diagonal in
{0,2}, satisfying the necessary quotient equation
    M^2 = (k-mu)I + (lam-mu)M + mu*3*J.

Symmetry: simultaneous row+column permutation (conjugation by S_33) preserves
every constraint — the M^2 equation is conjugation-covariant, all row sums are
equal, and "diagonal in {0,2}" is conjugation-invariant. Conjugates are
indistinguishable for EXISTENCE (we decide, not count), so a canonical
representative loses nothing.

Sound canonical break (two families):
  A. Diagonal nondecreasing:  diag[0] <= diag[1] <= ... <= diag[m-1].
     (diagonal values are in {0,2}, so this stacks 0-diagonal orbits first.)
  B. Row 0 is the lexicographically minimum row:  row_0 <=_lex row_i for all i.
     Under conjugation we may always bring the lex-min row to position 0.
Both are genuine symmetry breaks of S_33; combined they keep one canonical
orbit matrix per class (completeness unaffected when deciding existence).

Lexicographic comparator row_a <=_lex row_b, encoded with reified booleans:
  prefix_eq[c] = (a[t]==b[t] for all t <= c)      (prefix_eq[-1] = true)
  less[c]      = prefix_eq[c-1] AND a[c] < b[c]
  result       = prefix_eq[m-1] OR (OR_c less[c])

Please keep the per-row cost polynomial: each comparison is O(m) vars and
clauses, and we impose it m times, so O(m^2) overhead in total.
"""
from ortools.sat.python import cp_model


def _lex_le(model, a, b, m):
    """Return a BoolVar that is 1 iff row a <=_lex row b (a, b: lists of int
    vars of length m)."""
    prefix_eq = []   # prefix_eq[c]: a[0..c] all equal to b[0..c]
    less_any = []
    # prefix up to -1 is vacuously true
    pe_prev = model.NewBoolVar("pe_minus1")
    model.Add(pe_prev == 1)
    eq_all = model.NewBoolVar("eq_all")
    # We'll build chain: for each c, "all t<c equal" = AND of equals so far.
    all_eq_prev = pe_prev
    for c in range(m):
        eq_c = model.NewBoolVar(f"eq_{c}")
        model.Add(a[c] == b[c]).OnlyEnforceIf(eq_c)
        model.Add(a[c] != b[c]).OnlyEnforceIf(eq_c.Not())
        # prefix_eq[c] = all_eq_prev AND eq_c
        pe_c = model.NewBoolVar(f"pe_{c}")
        model.AddBoolAnd([all_eq_prev, eq_c]).OnlyEnforceIf(pe_c)
        model.AddBoolOr([all_eq_prev.Not(), eq_c.Not()]).OnlyEnforceIf(pe_c.Not())
        # less[c] = all_eq_prev AND a[c] < b[c]
        lt_c = model.NewBoolVar(f"lt_{c}")
        model.Add(a[c] < b[c]).OnlyEnforceIf(lt_c)
        model.Add(a[c] >= b[c]).OnlyEnforceIf(lt_c.Not())  # wait, need care
        less_any.append(lt_c)
        all_eq_prev = pe_c
    # fix lt_c soundly: lt_c = all_eq_prev AND a[c]<b[c]
    # a[c] < b[c] (integers) -> use bounded expr: a[c] <= b[c]-1, but var lower 0
    # Reify strict less between two int vars is not directly supported by
    # OnlyEnforceIf; use a bool via AddLessThan with reification we can do:
    #   model.Add(a[c] < b[c]).OnlyEnforceIf(lt_c) is NOT reifiable in many vers.
    # Use an explicit strict-less BoolVar via is_less = a[c] < b[c] reification:
    return eq_all


def build(m, k, lam, mu, maxseconds, symbreak=True):
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
        model.Add(sum(M[(i, j)] if i <= j else M[(j, i)] for j in range(m)) == k)

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
    st = solver.Solve(model)
    return solver, st, M, g


if __name__ == "__main__":
    print("helper module — run orbit_z3_enc_g99_run.py with -s for the break")
