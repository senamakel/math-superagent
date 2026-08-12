#!/usr/bin/env python3
"""Independent THIRD route to Project Euler 185 (Number Mind) via OR-tools CP-SAT.

This is *not* the recursive backtracking solver (solution.py) and *not* the
scipy MILP (solution2.py): it is a constraint-programming formulation solved by
Google OR-tools cp_model (CP-SAT), a completely separate solver engine with a
distinct branch-and-bound/conflict-driven search. It therefore gives an
independent numerical check on the reported L=16 secret.

MODEL
-----
Integer variables  digit[p] in 0..9   for p in 0..L-1   (one digit per position).

All 10**L strings are legal a priori (positions may repeat digits), so there is
no all-different constraint.

For each guess i with required count c_i we introduce L boolean variables
    match[i][p]  <->  (digit[p] == guess_i[p])
and post
    sum_p match[i][p] == c_i
i.e. exactly c_i correctly placed digits. This is exactly the required
semantics: only digits equal in value AND in position count.

Cost: L position vars + N*L boolean match vars, ~ L + 16*22 booleans, solved by
CP-SAT. Independent of 10**L — no enumeration of candidate strings.

UNIQUENESS
----------
After CP-SAT finds a solution, we post a "no-good" cut that at least one
position must differ from the found assignment (OR_p digit[p] != found[p]) and
solve again; infeasibility proves the found string is the unique answer.
"""

import sys
import time

try:
    from ortools.sat.python import cp_model
except ImportError as e:  # pragma: no cover - OR-tools is verified installed
    sys.exit(f"OR-tools not importable and pip install did not help: {e}")

from lib.pe185 import L5, CONSTRAINTS5, L16, CONSTRAINTS16


class _SolutionSet(cp_model.CpSolverSolutionCallback):
    """Collects up to `limit` solutions found by the enumeration search."""

    def __init__(self, digit_vars, limit):
        super().__init__()
        self._vars = digit_vars
        self._limit = limit
        self.solutions = []

    def on_solution_callback(self):
        if len(self.solutions) >= self._limit:
            return
        self.solutions.append("".join(str(self.Value(v)) for v in self._vars))


def build_model(L, constraints, extra_forbid=None):
    """Return (model, digit_vars) for the given instance.

    extra_forbid: optional list of digit-strings that must NOT be produced
    (used for the uniqueness re-solve). The model forbids each by requiring
    at least one position to differ.
    """
    model = cp_model.CpModel()
    digit = [model.NewIntVar(0, 9, f"digit_{p}") for p in range(L)]

    for gi, (guess, ci) in enumerate(constraints):
        matches = []
        for p in range(L):
            b = model.NewBoolVar(f"m{gi}_{p}")
            # b == 1  iff  digit[p] == guess[p]
            model.Add(digit[p] == int(guess[p])).OnlyEnforceIf(b)
            model.Add(digit[p] != int(guess[p])).OnlyEnforceIf(b.Not())
            matches.append(b)
        model.Add(sum(matches) == ci)

    if extra_forbid:
        for s in extra_forbid:
            diffs = []
            for p in range(L):
                dvar = model.NewBoolVar(f"ne_{p}")
                model.Add(digit[p] != int(s[p])).OnlyEnforceIf(dvar)
                model.Add(digit[p] == int(s[p])).OnlyEnforceIf(dvar.Not())
                diffs.append(dvar)
            model.Add(sum(diffs) >= 1)  # at least one position differs

    return model, digit


def solve(L, constraints, extra_forbid=None, time_limit=3600.0, find_all=False):
    """Solve the CP-SAT model.

    Returns (secret_string or None, status_name, solver, digit_vars).
    If find_all, enumerates every solution (used for uniqueness); otherwise
    returns the first solution CP-SAT finds.
    """
    model, digit = build_model(L, constraints, extra_forbid=extra_forbid)
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = time_limit
    if find_all:
        solver.parameters.enumerate_all_solutions = True
        cb = _SolutionSet(digit, limit=10_000_000)
        status = solver.Solve(model, cb)
        sols = cb.solutions
        return sols, status, solver, digit
    status = solver.Solve(model)
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        secret = "".join(str(solver.Value(v)) for v in digit)
        return secret, status, solver, digit
    return None, status, solver, digit


def verify(L, secret, constraints):
    """Exact re-check that secret satisfies every (guess, c_i) constraint."""
    all_ok = True
    rows = []
    for guess, ci in constraints:
        hit = sum(1 for p in range(L) if secret[p] == guess[p])
        ok = hit == ci
        all_ok &= ok
        rows.append((guess, hit, ci, ok))
    return all_ok, rows


def run_instance(L, constraints, label):
    print(f"=== {label} ===")
    t0 = time.perf_counter()
    secret, status, solver, _ = solve(L, constraints)
    t1 = time.perf_counter()
    print(f"CP-SAT status : {solver.StatusName(status)}")
    print(f"secret        : {secret}")
    print(f"solve runtime : {t1 - t0:.3f} s")
    if secret is None:
        print("  no solution found / infeasible")
        return
    all_ok, rows = verify(L, secret, constraints)
    print(f"verification  : all {len(constraints)} counts correct -> {all_ok}")
    bad = [g for g, h, c, ok in rows if not ok]
    if bad:
        for g, h, c, ok in rows:
            if not ok:
                print(f"   WRONG  {g}: {h} != {c}")
    # ---- uniqueness via no-good cut ----
    t2 = time.perf_counter()
    sol2, status2, solver2, _ = solve(L, constraints, extra_forbid=[secret])
    t3 = time.perf_counter()
    if sol2 is None and status2 in (cp_model.INFEASIBLE, cp_model.MODEL_INVALID):
        uniq = "UNIQUE: forbidding the found string makes the problem infeasible"
    elif sol2 is None:
        uniq = f"UNKNOWN (re-solve status {solver2.StatusName(status2)})"
    else:
        uniq = f"MULTIPLE: found another solution {sol2}"
    print(f"uniqueness    : {uniq}  (re-solve {t3 - t2:.3f} s)")
    print()


def main():
    # ---- L=5 worked example (brute-oracle cross-check) ----
    t0 = time.perf_counter()
    run_instance(L5, CONSTRAINTS5, "L=5 example")
    t5 = time.perf_counter()

    # ---- L=16 main instance ----
    t6 = time.perf_counter()
    sol16, status16, solver16, digit16 = solve(L16, CONSTRAINTS16)
    t7 = time.perf_counter()
    print("=== L=16 instance (top-level) ===")
    print(f"CP-SAT status       : {solver16.StatusName(status16)}")
    print(f"secret (CP-SAT)     : {sol16}")
    print(f"solve runtime       : {t7 - t6:.3f} s")
    if sol16 is None:
        print("no solution")
        return
    all_ok, rows = verify(L16, sol16, CONSTRAINTS16)
    print(f"verification        : all 22 counts correct -> {all_ok}")
    for g, h, c, ok in rows:
        if not ok:
            print(f"   WRONG {g}: {h} != {c}")
    # uniqueness via no-good cut
    t8 = time.perf_counter()
    sol16b, status16b, solver16b, _ = solve(L16, CONSTRAINTS16, extra_forbid=[sol16])
    t9 = time.perf_counter()
    print(f"uniqueness          : " +
          ("UNIQUE (forbidding it is infeasible)"
           if sol16b is None and status16b == cp_model.INFEASIBLE
           else f"another solution {sol16b} (status {solver16b.StatusName(status16b)})"))
    print(f"uniqueness runtime  : {t9 - t8:.3f} s")

    print()
    print("CROSS-CHECK vs expected 4640261571849533:", "AGREE" if sol16 == "4640261571849533" else "DISAGREE")


if __name__ == "__main__":
    main()
