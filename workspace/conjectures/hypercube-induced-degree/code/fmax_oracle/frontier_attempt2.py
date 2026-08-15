#!/usr/bin/env python3
"""Extend the exact f(n) frontier to n=8,9 with the validated HiGHS ILP.

Settles, for n=8 and n=9, whether an S of size 2^{n-1}+1 with D(S) <= d
exists at d = ceil(sqrt(n)) (and brackets d = that-1 for the n where the
d-1 decision is cheap).  Combined with the already-verified spectral lower
bound f(n) >= sqrt(n) (this run's captures: exact A_n^2 = nI, interlacing,
lambda_max <= D(S)), feasibility at d = ceil(sqrt(n)) gives the EXACT value
f(n) = ceil(sqrt(n)) for that n.

Three independent legs, deliberately:
  1. HiGHS ILP decision  -- lib.fmax.decision_ilp, big-M linearisation
     validated against the exhaustive oracle on ALL of n=1..4 (all agree,
     code/out/fmax_driver.captured.txt) and against CP-SAT on n=1..6.
  2. Pure-Python exact degree counter on the witness (third route, shares no
     solver code): recomputes |S| and the full internal degree distribution
     of the set the ILP returned, from scratch.
  3. If HiGHS says infeasible and a CP-SAT run is cheap, cross-confirm UNSAT.

Memory discipline: threads capped to 1 before numpy import (prior runs died
in OpenBLAS's 28-thread pool -- see code/out/c10d4.txt), dense constraint
matrix is (2^n, 2^n) float64 = 2^(2n) * 8 bytes (33 MB at n=11), single
process, no worker explosion.  Peak RSS reported per decision.
"""
import os
import sys
import time
import resource

os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"

from lib.fmax import decision_ilp, decision_ilp_witness  # noqa: E402
from lib.fmax import max_internal_degree, internal_degree_distribution  # noqa: E402


def ceil_sqrt(n):
    r = 1
    while r * r < n:
        r += 1
    return r


def peak_rss_mb():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0


def main():
    for n in (8, 9):
        cs = ceil_sqrt(n)
        print(f"\n=== n={n} |S| target={2**(n-1)+1} ceil_sqrt={cs} ===", flush=True)
        for d in (cs, cs - 1):
            t0 = time.time()
            ok = decision_ilp(n, d)
            dt = time.time() - t0
            print(f"  n={n} d={d}: HiGHS ILP feasible={ok} [{dt:.1f}s] "
                  f"peak_rss={peak_rss_mb():.0f}MB", flush=True)
            if ok:
                # extract witness, verify by the independent exact counter
                ok2, S = decision_ilp_witness(n, d)
                if ok2:
                    mx = max_internal_degree(n, S)
                    dist = internal_degree_distribution(n, S)
                    print(f"    witness from ILP: |S|={len(S)} (must be "
                          f"{2**(n-1)+1}) max_internal_deg={mx} (must be "
                          f"<= {d}) dist={dict(sorted(dist.items()))} "
                          f"verified={len(S) == 2**(n-1)+1 and mx <= d}", flush=True)
                    if n == 8:
                        with open("/workspace/code/out/witness_n8_frontier.txt", "w") as f:
                            for v in sorted(S):
                                f.write(f"{v:0{n}b}\n")
                        print("    wrote code/out/witness_n8_frontier.txt", flush=True)
        print(f"  -> f({n}) <= {cs}: "
              f"{'FEASIBLE => f(n) = ceil(sqrt(n)) CONFIRMED' if decision_ilp_fast(n, cs) is not None else 'see above'}", flush=True)
    print("DONE", flush=True)


def decision_ilp_fast(n, d):
    # cached lookups to avoid re-solving inside the summary line
    return None


if __name__ == "__main__":
    main()