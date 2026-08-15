"""First step of the adopted approach: settle the exact-value question.

Is { |S| = 2^{n-1}+1, D(S) <= ceil(sqrt n) } feasible at n = 6, 7, 8?
Feasible => f(n) = ceil(sqrt n) there (upper construction / witness).
INFEASIBLE => f(n) > ceil(sqrt n) (first counterexample to the conjecture).

Uses the existing decision ILP (code/lib/fmax.py). Bounded; n=8 is 256
binaries, 257 constraints, a polynomial-size ILP (HiGHS via scipy.milp).
"""

import math
import time
import sys
from lib.fmax import decision_ilp

for n in range(6, 9):
    d = math.ceil(math.sqrt(n))
    t0 = time.time()
    feasible = decision_ilp(n, d)
    dt = time.time() - t0
    print(f"n={n}  |S|={2**(n-1)+1}  d=ceil(sqrt(n))={d}  feasible={feasible}  "
          f"({dt:.1f}s)", flush=True)
    if not feasible:
        print(f"  -> COUNTEREXAMPLE: f({n}) > {d}", flush=True)
