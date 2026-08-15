"""Sanity-check the CP-SAT degree-decision encoding, then bracket f(10), f(11).

The load-bearing re-run is upper_n10_11_recheck.captured.txt: ortools CP-SAT
declares n=10 and n=11 INFEASIBLE at d=4 (i.e. no S of size 2^{n-1}+1 with all
internal degrees <= 4). That refutes the small-n conjecture f(n)=ceil(sqrt(n))
(=4 at 10,11) IF the encoding is sound. Two things could make it unsound and
both are checked here:

1. Encoding correctness: the same `sum(x[u] for u in N(v)) <= d` +
   `sum(x)==2^{n-1}+1` CP-SAT encode must reproduce the KNOWN values
   f(4)=2, f(5)=3, f(6)=3, f(7)=3 (exhaustive/ILP-certified elsewhere).
2. Not-pathologically-infeasible: at n=10 and n=11 the solver must find
   FEASIBLE at SOME d (we test d=5, d=6), proving the infeasibility at d=4 is
   a real threshold and not an artifact (e.g. numerical/thread failure).

We compare the CP-SAT verdict at d=ceil(sqrt(n))-1 (should be infeasible) and
d=ceil(sqrt(n)) (should be feasible where known) for small n, and bracket f(10),
f(11) by scanning d upward from 4.
"""
from ortools.sat.python import cp_model


def decision_cpsat(n, d, timeout_seconds=300):
    N = 1 << n
    m = (1 << (n - 1)) + 1
    model = cp_model.CpModel()
    x = [model.NewBoolVar(f"x{i}") for i in range(N)]
    model.Add(sum(x) == m)
    for v in range(N):
        model.Add(sum(x[v ^ (1 << k)] for k in range(n)) <= d)
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = timeout_seconds
    status = solver.Solve(model)
    feasible = status in (cp_model.OPTIMAL, cp_model.FEASIBLE)
    return feasible, status


# 1. Encoding sanity on known values.
known = {4: 2, 5: 3, 6: 3, 7: 3}
print("== Encoding sanity: CP-SAT vs known f(n) ==", flush=True)
for n, fn in known.items():
    f_inf, _ = decision_cpsat(n, fn - 1, timeout_seconds=60)
    f_feas, _ = decision_cpsat(n, fn, timeout_seconds=60)
    ok = (f_inf is False) and (f_feas is True)
    print(f"  n={n} known f={fn}: d={fn-1} -> {f_inf} (want False), "
          f"d={fn} -> {f_feas} (want True): {'OK' if ok else 'MISMATCH'}", flush=True)

# 2. Bracket f(10), f(11): scan d from 4 (already known infeasible) upward.
print("== Bracket f(10), f(11) ==", flush=True)
for n in (10, 11):
    for d in (4, 5, 6):
        feas, status = decision_cpsat(n, d, timeout_seconds=300)
        print(f"  n={n} d={d} -> feasible={feas} status={status}", flush=True)
print("DONE", flush=True)
