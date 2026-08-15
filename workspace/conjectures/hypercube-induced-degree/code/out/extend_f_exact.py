"""Extend f(n) exact values to n=6,7,8 via the decision ILP.

Conjecture under test: f(n) = ceil(sqrt(n)) for all n.  Already verified
n=1..5 = 1,2,2,2,3.  Huang's spectral lower bound gives f(n) >= ceil(sqrt(n))
(RECALLED/MECHANICALLY-VERIFIED in this run's research before I take it on),
so the question is whether the matching upper construction exists: does there
exist S of size 2^{n-1}+1 with D(S) <= ceil(sqrt(n))?

ceil(sqrt(6))=3, ceil(sqrt(7))=3, ceil(sqrt(8))=3, ceil(sqrt(9))=3,
ceil(sqrt(10))=4, ceil(sqrt(11))=4, ceil(sqrt(12))=4, ceil(sqrt(13))=4,
ceil(sqrt(14))=4, ceil(sqrt(15))=4, ceil(sqrt(16))=4.

I report infeasibility/feasibility of the decision ILP for each (n, d) around
the conjecture, on exact integer arithmetic (scipy.optimize.milp, HiGHS).
"""
import sys, time
sys.path.insert(0, "/workspace/code")
from lib.fmax import decision_ilp

def ceil_sqrt(n):
    r = 1
    while r*r < n:
        r += 1
    return r

for n in [6, 7, 8, 9, 10]:
    m = (1 << (n - 1)) + 1
    t0 = time.time()
    cs = ceil_sqrt(n)
    row = []
    # check every d from 1 up to cs+1 so we can bracket f(n) even if conjecture fails
    for d in range(1, min(n, cs + 2) + 1):
        t1 = time.time()
        ok = decision_ilp(n, d)
        row.append((d, ok))
        print(f"n={n} |S|={m} d={d} feasible={ok}  [{time.time()-t1:.2f}s]",
              flush=True)
    # f(n) = smallest feasible d
    fn = min((d for d, ok in row if ok), default=None)
    print(f"  -> n={n}: f(n)={fn}  conj=ceil(sqrt(n))={cs}  match={fn==cs}",
          flush=True)
    print(f"  n={n} total {time.time()-t0:.2f}s", flush=True)
