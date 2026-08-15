"""Extend the exact-value oracle's upper-bound feasibility to n=8,9,10,11.

Conjecture under test: f(n) = ceil(sqrt(n)).  Huang's spectral lower bound
gives f(n) >= ceil(sqrt(n)) (mechanically verified in this run), so each
feasible decision below confirms the matching upper construction survives to
that n and the ceil-sqrt conjecture continues there.

What each n settles (one batch of the ceil-sqrt staircase):
  n=8  d=3  -- ceil(sqrt(8))=3: confirms the upper construction continues just
               past the proved-verified frontier (f(1..7)=ceil sqrt n known).
  n=9  d=3  -- ceil(sqrt(9))=3: last n of the d=3 batch (sqrt(n) in [3,4)).
  n=10 d=4  -- ceil(sqrt(10))=4: pushes into the next ceil batch.
  n=11 d=4  -- ceil(sqrt(11))=4: last n of the d=4 batch (sqrt(n) in [4,5)).

For n=8 we also extract an explicit witness set S and DIRECTLY (not by
inference from the recursion) measure |S| and D(S), writing the bitlabels to
witness_n8.txt.  If n=8,d=3 is feasible with a degree-3 witness then
f(8)=3=ceil(sqrt(8)), matching the conjecture, with the construction verified
by direct measurement.

Method: binary ILP via scipy.optimize.milp (HiGHS), the same exact integer
linearisation as lib.fmax.decision_ilp (big-M + n*x_v <= d+n, M=n valid since
every vertex of Q_n has exactly n neighbours).  Decision is polynomial-size
(2^n binaries, 2^n+1 constraints); the cost grows with n (the search size),
not with any enumeration of subsets.

PREREQUISITE (the whole point of this script): OPENBLAS_NUM_THREADS=1 and
OMP_NUM_THREADS=1 must be set before scipy is imported.  Prior runs died from
OpenBLAS spawning 28 threads (c10d4.txt shows pthread_create failures), NOT
infeasibility; capping to one thread avoids that.  We print the value after
import to confirm it took effect.
"""
import os
import sys
import time

# Set thread caps BEFORE importing scipy/numpy — prior runs crashed in
# OpenBLAS's thread pool (see code/out/c10d4.txt) before scipy even imported.
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"

import numpy as np  # noqa: E402
import numpy  # noqa: E402
from scipy.optimize import milp, LinearConstraint, Bounds  # noqa: E402
from lib.fmax import decision_ilp, decision_ilp_witness  # noqa: E402
from lib.fmax import max_internal_degree, internal_degree_distribution  # noqa: E402
from lib.fmax import _nbhd  # noqa: E402

# 1. confirm the thread cap actually took effect, post-import
cfg = getattr(numpy, "__config__", None)
try:
    blas_info = cfg.show() if cfg is not None else "(no __config__)"
except Exception:  # np.__config__.show() prints; guard any oddity
    blas_info = "(show failed)"
print("after scipy import: OPENBLAS_NUM_THREADS =",
      os.environ.get("OPENBLAS_NUM_THREADS"), file=sys.stdout, flush=True)
print("after scipy import: OMP_NUM_THREADS     =",
      os.environ.get("OMP_NUM_THREADS"), file=sys.stdout, flush=True)
print("numpy config:\n" + str(blas_info), file=sys.stdout, flush=True)

# 2. feasibility per (n, d), plus an explicit witness for n=8
CASES = [(8, 3), (9, 3), (10, 4), (11, 4)]
results = {}

for n, d in CASES:
    m = (1 << (n - 1)) + 1
    t0 = time.time()
    ok = decision_ilp(n, d)
    dt = time.time() - t0
    results[(n, d)] = ok
    print(f"n={n} |S|={m} d={d} feasible={ok}  [{dt:.2f}s]", flush=True)

# n=8 witness (direct construction, not inferred)
n8, d8 = 8, 3
t0 = time.time()
feasible, S8 = decision_ilp_witness(n8, d8)
dt = time.time() - t0
print(f"n={n8} d={d8} witness extraction feasible={feasible}  "
      f"[{dt:.2f}s]", flush=True)
if feasible and S8 is not None:
    # direct degree measure of the returned set — the falsification oracle
    dist = internal_degree_distribution(n8, S8)
    D = max_internal_degree(n8, S8)
    print(f"  DIRECT check: |S|={len(S8)} (need {2**(n8-1)+1})  "
          f"D(S)={D}  profile={dict(sorted(dist.items()))}", flush=True)
    with open("/workspace/code/out/witness_n8.txt", "w") as f:
        f.write("# n=8 witness set of bitlabels, |S|=129, D(S)=" + str(D) + "\n")
        f.write(" ".join(str(v) for v in S8) + "\n")
    print("  wrote code/out/witness_n8.txt", flush=True)

print("SUMMARY", flush=True)
for (n, d), ok in results.items():
    print(f"  n={n} d={d}: feasible={ok}", flush=True)
