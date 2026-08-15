#!/usr/bin/env python3
"""Directive-66 comparison: 2-adic linear complexity growth across three
binary families.

Quantity measured (stated plainly): the EXACT 2-adic linear complexity
lambda_N for N-bit prefixes, computed via the continued-fraction /
Euclidean-algorithm route and validated against a brute-force oracle on all
strings of length <= 8 (code/lib/fcsr.py, fcsr_lambda_bits).  Proxies are
reported alongside and are clearly labelled as proxies:

  * 2-kernel size  (kernel_size)  -- number of distinct dyadic substrings
    s[2^k*m .. 2^k*(m+1)-1] wholly inside the string (automatic-seq test),
  * zero-run stats (zero_run_stats) -- #maximal zero-runs and longest zero-run,
  * w and zero/halved weight of the halved-gap bit string.

Families (all h[j] = j-th halved-gap switch bit, j >= 0):
  (1) Thue-Morse            h[j] = popcount(j) mod 2
  (2) odd-factor periodic   h[j] = (j mod 3 == 1)   [the word 0,0,1 repeated]
  (3) real prime            h[j] = ((p_{j+2} - p_{j+1})/2) mod 2,  p from
                             lib.gilbreath.primes_up_to.

For family 3 we also report the genuine run quantity nu2(N) = #2s in the
maximal {0,2} suffix of the right diagonal (lib.rightdiag.cycle_and_nu2), the
linearity of which is the whole G-supply question, so we can compare the
2-adic complexity / kernel / zero-run behaviour of the switch string with that
genuine supply measure.

Exact integers only (the bit-count popcount is exact; densities are rationals
count/N with a decimal for display).  Complexity: O(N^3) worst-case big-int
ops for the CF route (one per prefix, but prefixes share the single alpha; each
lambda is O(N^2) in practice), O(N) space.
"""
import math
import sys
import time

from lib.fcsr import (fcsr_lambda_bits, fcsr_lambda_prefix, kernel_size,
                      zero_run_stats, hamming_weight)
from lib.gilbreath import primes_up_to


def popcount(j):
    return bin(j).count("1")


def thue_morse(N):
    return [popcount(j) & 1 for j in range(N)]


def periodic_001(N):
    return [1 if (j % 3) == 1 else 0 for j in range(N)]


def prime_switch(N):
    """h[j] = ((p_{j+2} - p_{j+1})/2) mod 2 for j=0..N-1."""
    # need primes beyond the (N+1)-th;  pi(x) > x/log x, solve bound
    limit = max(100, int(N * (math.log(N) + 2)) + 50) if N > 1 else 100
    # generously over-bound: pi(B) ~ B/log B; need pi(B) >= N+2
    # choose B such that B/log B >= N+2  =>  B ~ (N+2)(log B). iterate once.
    B = limit
    for _ in range(3):
        B = int((N + 2) * (math.log(B) + 1.1)) + 10
    B = max(B, 200)
    P = primes_up_to(B)
    while len(P) < N + 2:
        B *= 2
        P = primes_up_to(B)
    return [((P[j + 2] - P[j + 1]) // 2) & 1 for j in range(N)]


def report_lambda_growth(bits, name, maxN):
    """Report lambda_N at several prefix lengths (exact), plus a summary of
    whether it grows faster/slower than linear-in-N (compare lambda_N/N)."""
    N = len(bits)
    print(f"--- {name} : lambda_N (2-adic linear complexity) ---")
    lam_prefix = fcsr_lambda_prefix(bits[:maxN])
    print("  %-8s %-10s %-12s" % ("N", "lambda_N", "lambda_N/N"))
    for Ns in (64, 128, 256, 512, 1024, 2048):
        if Ns > maxN:
            break
        lam = lam_prefix[Ns - 1]
        if Ns:  # lambda>=1 usually
            print("  %-8d %-10d %-12.4f" % (Ns, lam, lam / Ns))
    print()
    return lam_prefix


def main():
    N = 3000            # a few thousand bits for each family
    maxN = 2048         # lambda prefix table length (keeps runtime sane)
    print("=" * 78)
    print("Directive-66 comparison: 2-adic linear complexity + proxies")
    print("Exact lambda_N via continued fraction (validated vs brute force "
          "on N<=8).")
    print("N (prefix bits for lambda table) = %d ; full family length = %d"
          % (maxN, N))
    print("=" * 78)

    families = [
        ("(1) Thue-Morse h[j]=popcount(j) mod 2", thue_morse),
        ("(2) periodic 001 (odd-factor P=3)     ", periodic_001),
        ("(3) real prime halved-gap switch     ", prime_switch),
    ]

    # Build all three families once
    famdata = []
    for name, fn in families:
        t0 = time.time()
        bits = fn(N)
        famdata.append((name, bits, time.time() - t0))

    for name, bits, bt in famdata:
        print("\n### Family %s  (built in %.2fs)" % (name, bt))
        # proxies
        ks = kernel_size(bits)
        nzr, lzr = zero_run_stats(bits)
        w = hamming_weight(bits)
        print("  [proxy] 2-kernel size      : %d" % ks)
        print("  [proxy] #maximal zero-runs : %d" % nzr)
        print("  [proxy] longest zero-run   : %d" % lzr)
        print("  [proxy] Hamming weight w   : %d  (density %.4f)"
              % (w, w / N))
        # exact lambda growth
        t0 = time.time()
        lam = report_lambda_growth(bits, name, maxN)
        print("  (lambda table time %.2fs)" % (time.time() - t0))
        # final lambda value
        lf, wit = fcsr_lambda_bits(bits[:maxN])
        print("  lambda_%d = %d   (witness q=%d)" % (maxN, lf, wit[0]))
        # asymptotic characterisation (heuristic classifier, exact numbers)
        if maxN >= 2048:
            lam2048 = lam[2047]
            lam1024 = lam[1023]
            ratio = lam2048 / lam1024 if lam1024 else float('inf')
            print("  lambda_2048/lambda_1024 = %.3f  (2 = linear/affine; "
                  "1 = constant/log; >2 = superlinear, ~sqrt(2^?)/N)"
                  % ratio)

    # genuine run-nu2 for the prime family (the G-supply quantity)
    print("\n### Genuine run quantity for family (3): nu2(N) on the right "
          "diagonal")
    from lib.rightdiag import incremental_diagonals, cycle_and_nu2
    _, pbits, _ = famdata[2]    # prime switch bits
    # rebuild the 2-then-odds q from the switch bits and track nu2(N)
    q = [2, 3]
    for j in range(N + 2):
        q.append(q[-1] + (2 if pbits[j] else 4))
    nu2s = []
    yielder = incremental_diagonals(q)
    for n in range(0, maxN + 1):
        dd = next(yielder)
        _, nu2 = cycle_and_nu2(dd)
        nu2s.append(nu2)
    print("  %-8s %-10s %-10s %-10s" % ("N", "nu2(N)", "nu2/N", "nu2/w"))
    for Ns in (64, 128, 256, 512, 1024, 2048):
        nu = nu2s[Ns] if Ns < len(nu2s) else nu2s[-1]
        w_N = sum(pbits[:Ns])
        print("  %-8d %-10d %-10.4f %-10.4f" % (
            Ns, nu, nu / Ns, (nu / w_N if w_N else float('nan'))))
    print("  nu2_2048/nu2_1024 = %.3f  (2 = linear; ~1 = collapse)"
          % (nu2s[2048] / nu2s[1024]))


if __name__ == "__main__":
    main()
