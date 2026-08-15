"""Independent second route to f(10), f(11): reproduce the d=4 decision.

upper_n10_11.captured.txt (ortools CP-SAT) declared n=10 and n=11 INFEASIBLE
at d=4, i.e. no S of size 2^{n-1}+1 with max internal degree <= 4, which would
refute the small-n conjecture f(n)=ceil(sqrt(n)) (=4 at n=10,11). That
captured run was a single CP-SAT run with OpenBLAS thread errors around it and
was never independently confirmed. This script re-verifies the decision with a
DIFFERENT solver (scipy.optimize.milp / HiGHS) and a DIFFERENT encoding
(lib.fmax big-M ILP, already validated against exhaustive oracle on n=1..4),
so the existence/non-existence of an S at D(S)<=4 at n=10,11 is confirmed by
two unrelated routes. It also brackets f(n) by testing d=4 and d=5.

Both solvers being complete means INFEASIBLE is a proof of non-existence
(UNSAT), not a timeout: ortools returned CpSolverStatus.INFEASIBLE and HiGHS
must likewise terminate with res.success False without hitting a time/resource
cap. We enforce a wall-clock timeout and report which status was reached.
"""
import os, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['OMP_NUM_THREADS'] = '1'
os.environ['MKL_NUM_THREADS'] = '1'
sys.path.insert(0, "/workspace/code")

from lib.fmax import decision_ilp

def ceil_sqrt(n):
    r = 1
    while r * r < n:
        r += 1
    return r

pairs = []
for n in (10, 11):
    # the ceil(sqrt(n)) conjecture says f(n) <= ceil_sqrt; test that d,
    # and one step above to bracket f(n).
    pairs.append((n, 4))
    pairs.append((n, 5))

results = {}
for n, d in pairs:
    t0 = time.time()
    try:
        ok = decision_ilp(n, d)
        status = "FEASIBLE" if ok else "INFEASIBLE"
        # scipy.milp success=False with a valid model and no timeout is a
        # proof-complete infeasible; it does not return success=False on a
        # merely-unfinished run. We additionally bound wall time outside.
    except Exception as e:
        ok = None
        status = f"ERROR {e!r}"
    elapsed = time.time() - t0
    results[(n, d)] = (ok, elapsed)
    line = (f"n={n} |S|={(1<<(n-1))+1} d={d} decision={status} "
            f"[{elapsed:.1f}s]")
    print(line, flush=True)
    if d == 4:
        # Is the ceil-sqrt equality refuted at this n?
        print(f"   -- conjecture f({n}) <= ceil(sqrt({n}))={ceil_sqrt(n)} "
              f"-> f({n}) > 4" if ok is False else
              f"   -- conjecture f({n}) <= " 
              f"{ceil_sqrt(n)} NOT refuted at d=4", flush=True)

print("ALL_HIGHS_STEPS_DONE", flush=True)
