#!/usr/bin/env python3
"""Benchmark the exact Phi primitives in code/lib/phi.py, so the search
programs in code/phi_triple_variety/ are tuned to a feasible bound.

Measures:
  1. phi_pairs(M) generation time for several M.
  2. in_phi exact membership-test rate.
  3. The sum>1 / plus_one_is_square prefilter pass rate on candidate pairs
     (how many candidate sums survive the cheap necessary condition and
     actually reach the expensive exact membership test).
No floats in the logic; wall-clock timing is printed for honesty only.
"""
import time
from math import gcd, isqrt
from lib.phi import phi_pairs, in_phi, plus_one_is_square, sum_in_phi_prefilter


def rate_phi_pairs(Ms=(200, 400, 800, 1500)):
    for M in Ms:
        t0 = time.time()
        Phi = phi_pairs(M)
        dt = time.time() - t0
        print(f"  phi_pairs({M}): |Phi|={len(Phi)} in {dt:.2f}s")


def rate_in_phi(n=200_000):
    # build a pool of reduced fractions with ~sizes appearing in sums near M=1000
    Phi = phi_pairs(400)
    pool = list(Phi)
    import random
    rng = random.Random(1)
    t0 = time.time()
    cnt = 0
    P = len(pool)
    hits = 0
    for _ in range(n):
        A1, B1 = pool[rng.randrange(P)]
        A2, B2 = pool[rng.randrange(P)]
        num = A1 * B2 + A2 * B1
        den = B1 * B2
        g = gcd(num, den)
        A, B = num // g, den // g
        if A >= B or A <= 0:
            continue
        if in_phi(A, B):
            hits += 1
        cnt += 1
    dt = time.time() - t0
    print(f"  in_phi on {cnt} valid candidate sums: {dt:.2f}s "
          f"({cnt/max(dt,1e-9):.0f}/s), hits={hits}")


def rate_prefilter(n=200_000):
    Phi = phi_pairs(400)
    pool = list(Phi)
    import random
    rng = random.Random(2)
    P = len(pool)
    t0 = time.time()
    nvalid = 0
    nsurvive = 0
    for _ in range(n):
        A1, B1 = pool[rng.randrange(P)]
        A2, B2 = pool[rng.randrange(P)]
        num = A1 * B2 + A2 * B1
        den = B1 * B2
        g = gcd(num, den)
        A, B = num // g, den // g
        if A >= B or A <= 0:
            continue
        nvalid += 1
        if plus_one_is_square((A, B)):
            nsurvive += 1
    dt = time.time() - t0
    print(f"  prefilter on {nvalid} valid sums: {dt:.2f}s; "
          f"{nsurvive} survive (1+sum a rational square) = "
          f"{100.0*nsurvive/max(nvalid,1):.3f}%")


if __name__ == "__main__":
    print("[1] phi_pairs generation (exact distinct values)")
    rate_phi_pairs()
    print("[2] exact membership test in_phi rate")
    rate_in_phi()
    print("[3] plus_one_is_square prefilter pass rate")
    rate_prefilter()
