#!/usr/bin/env python3
"""Extend exact f(n) via the VALIDATED HiGHS ILP oracle (agrees with exhaustive
oracle on n=1..4, unlike the CP-SAT route which failed known small cases).

f(n) = min{ D(S) : S subset {0,1}^n, |S| = 2^{n-1}+1 }, D(S)=max internal deg.

The user's question: is f(n) = ceil(sqrt(n)) for ALL n (tight construction),
or only for perfect squares / asymptotically?  Each value below is the exact
answer at that n from a proof-complete ILP.
"""
import os, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['OMP_NUM_THREADS'] = '1'
os.environ['MKL_NUM_THREADS'] = '1'
sys.path.insert(0, "/workspace/code")

from lib.fmax import decision_ilp, decision_ilp_witness

def ceil_sqrt(n):
    r = 1
    while r*r < n:
        r += 1
    return r

def f_milp_threaded(n, d_max=None, timeout=500):
    """Smallest d (bracketing from d=ceil_sqrt-1 up) with decision_ilp feasible."""
    start = ceil_sqrt(n)
    dmax = d_max if d_max is not None else start + 2
    # d=start-1 must be infeasible (lower bound f(n)>=ceil_sqrt); verify quickly
    for d in range(max(0, start-1), dmax+1):
        t0 = time.time()
        ok = decision_ilp(n, d)
        dt = time.time()-t0
        print(f"  n={n} d={d} feasible={ok}  [{dt:.1f}s]", flush=True)
        if ok:
            return d
    return None

if __name__ == "__main__":
    # Only run a subset per invocation to stay within timeout budget.
    import sys as _s
    ns = [int(x) for x in _s.argv[1:]] or [7, 8, 9]
    for n in ns:
        print(f"=== f({n}): |S|={(1<<(n-1))+1}, conjectured ceil(sqrt({n}))={ceil_sqrt(n)} ===", flush=True)
        val = f_milp_threaded(n)
        print(f">>> f({n}) = {val}  (conjecture ceil(sqrt)={ceil_sqrt(n)}, match={val==ceil_sqrt(n)})", flush=True)
