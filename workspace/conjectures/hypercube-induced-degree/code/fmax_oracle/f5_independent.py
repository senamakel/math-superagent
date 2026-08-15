"""Independent n=5 verification: ortools CP-SAT decision + explicit set.

Two independent checks on the scipy/HiGHS ILP result f(5)=3:

  (1) CP-SAT decision 'is there S of size 17 with D(S) <= 3?' must be True,
      and 'D(S) <= 2?' and 'D(S) <= 1?' must be False (independence from
      scipy.optimize.milp).
  (2) Extract an explicit achieving S for (5, d=3), then verify |S|=17 and
      recompute the full internal degree profile and D(S) with the pure-python
      exact oracle (lib.fmax.internal_degree_distribution) — a third route
      that shares no code with the solver.

All degree values and sizes are exact integers from the python oracle.
"""

import time
from ortools.sat.python import cp_model

from lib.fmax import internal_degree_distribution, max_internal_degree


def _nbhd(n):
    N = 1 << n
    return [[v ^ (1 << k) for k in range(n)] for v in range(N)]


def car_sat_decision(n, d, time_limit=60.0):
    """Return (feasible: bool, S_or_None) via CP-SAT."""
    N = 1 << n
    m = (1 << (n - 1)) + 1
    nb = _nbhd(n)
    model = cp_model.CpModel()
    x = [model.NewBoolVar(f"x{i}") for i in range(N)]
    model.Add(sum(x) == m)
    M = n
    for v in range(N):
        model.Add(sum(x[u] for u in nb[v]) + M * x[v] <= d + M)
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = time_limit
    status = solver.Solve(model)
    if status in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        return True, [v for v in range(N) if solver.Value(x[v]) == 1]
    return False, None


def main():
    n = 5
    m = (1 << (n - 1)) + 1
    t0 = time.time()

    print("=== Independent CP-SAT decision (n=5) ===")
    for d in (1, 2, 3):
        ta = time.time()
        fe, S = car_sat_decision(n, d)
        if S is not None:
            prof = internal_degree_distribution(n, S)
            print(f"  d={d}: feasible={fe}  |S|={len(S)}  D(S)="
                  f"{max_internal_degree(n,S)}  "
                  f"profile={dict(sorted(prof.items()))}  [{time.time()-ta:.2f}s]")
        else:
            print(f"  d={d}: feasible={fe}  [{time.time()-ta:.2f}s]")

    print()
    print("=== Cross-check the scipy/HiGHS f(5)=3 claim ===")
    # scipy said feas(d=1)=F, feas(d=2)=F, feas(d=3)=T.
    # CP-SAT must reproduce exactly that, and the d=3 set must be a true witness.
    results = {}
    for d in (1, 2, 3):
        fe, S = car_sat_decision(n, d)
        results[d] = (fe, S)
    expected = {1: False, 2: False, 3: True}
    agree = all(results[d][0] == expected[d] for d in (1, 2, 3))
    print(f"  CP-SAT agrees with scipy/HiGHS on f(5)=3: {agree}")
    if results[3][1] is not None:
        S = results[3][1]
        assert len(S) == m, f"|S|={len(S)} != {m}"
        prof = internal_degree_distribution(n, S)
        dmax = max(prof.keys())
        print(f"  explicit witness S={sorted(S)}")
        print(f"  |S|={len(S)}  D(S)={dmax}  profile={dict(sorted(prof.items()))}")
        assert dmax <= 3
        # show it is tight for f(5)=3 by confirming degree 3 is present
        has3 = prof.get(3, 0)
        print(f"  degree-3 vertices in the flat extremal set: {has3}")
    print(f"\n  total wall time: {time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()
