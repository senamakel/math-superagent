#!/usr/bin/env python3
"""Independent second route to Project Euler 185 (Number Mind) via MILP.

This is the *independent verification* of the backtracking solver
(/workspace/solution.py). Instead of recursive search over candidate digit
strings, we model the problem as an integer linear program and solve it with
scipy.optimize.milp (branch-and-bound), so the cost scales with the constraint
structure, never with 10**L.

MODEL
-----
Binary variables  x[p][d] in {0,1}   for p in 0..L-1 (positions), d in 0..9.
x[p][d] = 1  iff  secret[p] == d.

Constraints:
  (position)   for each p:      sum_d x[p][d] == 1
                 (every position holds exactly one digit)
  (guess)      for each guess i: sum_p x[p][ guess_i[p] ] == c_i
                 (exactly c_i correctly placed digits)

All x are binary (integrality = 1), bounds [0,1]. There is no objective; it is
a feasibility problem (branch-and-bound stops at the first feasible solution,
or minimises the zero objective and returns an optimal feasible point).

Uniqueness: after finding a solution we add a "no-good" cut forbidding exactly
that assignment (at least one currently-zero entry must become 1) and re-solve;
infeasibility then proves the found solution is unique.

Cost: (10L binary vars) + (L + N) equality constraints, solved by
branch-and-bound. Independent of 10**L.
"""

import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

from lib.pe185 import L5, CONSTRAINTS5, L16, CONSTRAINTS16


def build_model(L, constraints):
    """Return (c, integrality, bounds, constraint_matrix, lb, ub) for the MILP.

    constraints: iterable of (guess_string, c_i). Variable index = p*10 + d.
    """
    nvars = 10 * L
    c = np.zeros(nvars)                      # feasibility: zero objective
    integrality = np.ones(nvars)             # all binary
    bounds = Bounds(np.zeros(nvars), np.ones(nvars))

    rows = []
    lb = []
    ub = []

    # one row per position: sum_d x[p][d] == 1
    for p in range(L):
        row = np.zeros(nvars)
        row[p * 10:(p + 1) * 10] = 1.0
        rows.append(row)
        lb.append(1.0)
        ub.append(1.0)

    # one row per guess: sum_p x[p][ guess[p] ] == c_i
    for guess, ci in constraints:
        row = np.zeros(nvars)
        for p, ch in enumerate(guess):
            d = int(ch)
            row[p * 10 + d] = 1.0
        rows.append(row)
        lb.append(float(ci))
        ub.append(float(ci))

    A = np.array(rows)
    return c, integrality, bounds, LinearConstraint(A, np.array(lb), np.array(ub))


def solve(L, constraints, extra_cuts=None):
    """Solve the MILP; return (secret_string, res) or (None, res) if
    infeasible/unsolved. extra_cuts are extra no-good rows to forbid prior
    solutions (used for uniqueness checking)."""
    c, integrality, bounds, lc = build_model(L, constraints)
    if extra_cuts:
        # append no-good rows (>= 1): at least one excluded variable flips to 1
        A0 = np.zeros((len(extra_cuts), 10 * L))
        for k, sol in enumerate(extra_cuts):
            for p in range(L):
                d = int(sol[p])
                # forbid (p,d): require sum of the OTHER nine digits' vars >= 1
                for dd in range(10):
                    if dd != d:
                        A0[k, p * 10 + dd] = 1.0
        lc0 = LinearConstraint(A0, np.ones(len(extra_cuts)), np.inf)
        from scipy.optimize import LinearConstraint as _LC
        # combine
        A = np.vstack([lc.A, A0])
        lb = np.concatenate([lc.lb, np.ones(len(extra_cuts))])
        ub = np.concatenate([lc.ub, np.full(len(extra_cuts), np.inf)])
        lc = _LC(A, lb, ub)

    res = milp(c=c, integrality=integrality, bounds=bounds, constraints=lc,
               options={"time_limit": 3600})
    if not res.success:
        return None, res
    x = res.x
    # exactly one d per position has x[p*10+d] == 1; emit that digit
    secret = "".join(str(d) for p in range(L)
                     for d in range(10) if x[p * 10 + d] > 0.5)
    return secret, res


def main():
    # ---------------- L=5 example ----------------
    print("=== L=5 instance ===")
    sol5, res5 = solve(L5, CONSTRAINTS5)
    print(f"status             : {res5.message}")
    print(f"secret (MILP)      : {sol5}")
    if sol5 == "39542":
        print("CONFIRMED: L=5 answer 39542 (matches brute oracle 100000-check).")
    else:
        print("MISMATCH with expected 39542.")
    # uniqueness check for L=5 (extra cut forbids the found solution)
    sol5b, res5b = solve(L5, CONSTRAINTS5, extra_cuts=[sol5])
    print(f"L=5 uniqueness     : "
          f"{'UNIQUE (no second solution)' if sol5b is None and not res5b.success else 'multiple'}")

    # ---------------- L=16 main instance ----------------
    cons16 = CONSTRAINTS16
    print()
    print("=== L=16 instance ===")
    from time import perf_counter
    t0 = perf_counter()
    sol16, res16 = solve(L16, cons16)
    t1 = perf_counter()
    print(f"status          : {res16.message}")
    print(f"secret (MILP)   : {sol16}")
    print(f"runtime (solve) : {t1 - t0:.3f} s")
    if sol16 is not None:
        # ---- verify the solution independently (exact count check) ----
        print("verification    :")
        all_ok = True
        for guess, ci in cons16:
            hit = sum(1 for p in range(L16) if sol16[p] == guess[p])
            flag = "" if hit == ci else "  <-- WRONG"
            if hit != ci:
                all_ok = False
            print(f"   {guess} : {hit} == {ci}{flag}")
        print(f"   all counts correct: {all_ok}")

        # uniqueness check (forbid this solution, re-solve)
        t2 = perf_counter()
        sol16b, res16b = solve(L16, cons16, extra_cuts=[sol16])
        t3 = perf_counter()
        if sol16b is None and not res16b.success:
            print(f"uniqueness      : UNIQUE (no second solution; re-solve took "
                  f"{t3 - t2:.3f} s)")
        else:
            print(f"uniqueness      : MULTIPLE — found another solution {sol16b}")


if __name__ == "__main__":
    main()
