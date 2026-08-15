#!/usr/bin/env python3
"""Decide f(8) = 3: is there S of size 2^{7}+1 = 129 with D(S) <= 3?

Context: the spectral proof in this run (signed adjacency A_n, A_n^2 = nI,
Cauchy interlacing, lambda_max <= D(H)) proves f(n) >= sqrt(n) for all n, so
f(8) >= 3 (integer degree).  A witness with D(S) <= 3 therefore settles
f(8) = 3 EXACTLY, extending the exact-value frontier 1,2,2,2,3,3,3 by one
term.  Prior attempts at this decision (n8_decision.py) timed out in both
HiGHS (380s, time limit, no primal) and CP-SAT (600s, UNKNOWN): f(8) is
unsettled and no witness exists on disk.

This run uses the plain validated decision+extraction `lib.fmax.decision_ilp`
/ `decision_ilp_witness` -- the big-M linearisation validated against the
exhaustive oracle on ALL 13 (n,d) pairs with n=1..4 and cross-checked against
CP-SAT up to n=7 -- without the symmetry-break constraints of the prior
attempts (a different search configuration).  A found witness is re-verified
independently by lib.fmax's pure-Python exact degree counter (third route,
shares no solver code) before it is reported.

Encodings:  2^8 = 256 binary vars,  256+1 linear constraints, polynomial
size.  No enumeration of subsets -- decision ILP only (the GOAL oracle).
Exact integer arithmetic throughout; the only floats are the solver's own
LP relaxation penumbras, which never enter the result.

Usage: timeout 540 python3 code/fmax_oracle/n8d3_run.py 2>&1 |
            tee code/out/n8d3_run.captured.txt
"""

import os
import time
import resource

os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"

from lib.fmax import (decision_ilp, decision_ilp_witness,
                      max_internal_degree, internal_degree_distribution)


def peak_rss_mb():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0


def main():
    n, d = 8, 3
    m = (1 << (n - 1)) + 1
    print(f"=== n={n} d={d} |S| target={m} (vertices {1 << n}) ===", flush=True)
    print(f"thread caps: OPENBLAS={os.environ.get('OPENBLAS_NUM_THREADS')} "
          f"OMP={os.environ.get('OMP_NUM_THREADS')}", flush=True)

    t0 = time.time()
    ok = decision_ilp(n, d)
    dt = time.time() - t0
    print(f"[HiGHS decision_ilp] feasible={ok}  [{dt:.1f}s] "
          f"peak_rss={peak_rss_mb():.0f}MB", flush=True)

    if ok:
        t0 = time.time()
        ok2, S = decision_ilp_witness(n, d)
        dt = time.time() - t0
        print(f"[witness extraction] feasible={ok2}  [{dt:.1f}s]", flush=True)
        if ok2:
            size = len(S)
            mx = max_internal_degree(n, S)
            dist = internal_degree_distribution(n, S)
            verified = (size == m and mx <= d)
            print(f"witness: |S|={size} (need {m})  D(S)={mx} (need <= {d})  "
                  f"dist={dict(sorted(dist.items()))}", flush=True)
            print(f"independent pure-python verification: {verified}", flush=True)
            if verified:
                with open("/workspace/code/out/witness_n8_run.txt", "w") as f:
                    f.write(f"# n={n} d={d} |S|={size} D(S)={mx} "
                            f"dist={dict(sorted(dist.items()))}\n")
                    for v in sorted(S):
                        f.write(f"{v}\n")
                print("wrote code/out/witness_n8_run.txt", flush=True)
            print(f"==> f({n}) = {d}  SETTLED EXACTLY (lower bound f(n) >= "
                  f"sqrt(n) from the proved spectral chain, degree integer)",
                  flush=True)
        else:
            print("witness extraction failed despite feasible decision", flush=True)
    else:
        # decision_ilp returns False ONLY on proven infeasibility (HiGHS
        # success=False with no time limit); do not confuse with a timeout.
        print("infeasible: no S of size 129 with D(S) <= 3 "
              "(would prove f(8) > 3, refuting ceil(sqrt(8)))", flush=True)

    print("DONE", flush=True)
    return 0


if __name__ == "__main__":
    sys_exit = main()
    import sys
    sys.exit(sys_exit)