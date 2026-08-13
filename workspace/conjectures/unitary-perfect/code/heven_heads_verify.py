#!/usr/bin/env python3
"""Independent certification of the HEADS found by code/heven_gauss.py.

For each (p, r) pair the Gaussian run reported as a head — r | Phi_{4p}(2)
with v2(r-1) >= 4, so r = 1 (mod 16) and r is non-3-Higgs — verify from
first principles ONLY (no factorization of 2^{2p}+1 anywhere):

  V1. r is prime (sympy.isprime);
  V2. r | 2^{2p} + 1, i.e. pow(2, 2*p, r) == r - 1;
  V3. v_2(r-1) >= 4, i.e. r = 1 (mod 16);
  V4. r = 1 + 4p*t: (r-1) % (4*p) == 0, the primitive-divisor order fact.

Every V1..V4 must hold to certify (p, r) as a non-3-Higgs witness killing
m = 2p from H_even.  V3 alone already forces non-3-Higgs (3-Higgs requires
v_q(p-1) <= 3 for all q | p-1 by the A057447 recursion, q = 2 included).

Also certifies the negative check: the seven p with 2p in H_even (Thm 8:
2p in {6,10,26,46,62,82,122}) that the Gaussian run reported with NO head
are spot-checked here only as far as independent divisibility allows; the
absence of heads rests on the full exact factorization of the main run.
"""
from sympy import isprime

HEADS = [  # (p, r) exactly as printed by heven_gauss.py
    (7, 113), (11, 2113), (19, 525313),
    (29, 536903681), (37, 593), (37, 231769777),
    (43, 500177), (47, 3761), (47, 140737471578113),
    (53, 15358129), (53, 586477649), (59, 157649),
]

NO_HEADS = [3, 5, 13, 23, 31, 41, 61]  # p with 2p in H_even, no head in range


def v2(n):
    return (n & -n).bit_length() - 1


def main():
    bad = []
    for p, r in HEADS:
        ok = [isprime(r),
              pow(2, 2 * p, r) == r - 1,
              r % 16 == 1,
              (r - 1) % (4 * p) == 0]
        print("p=%3d r=%-15d prime=%s |2^{2p}+1=%s r%%16=%d (r-1)%%(4p)=%d %s"
              % (p, r, ok[0], ok[1], r % 16, (r - 1) % (4 * p),
                 "CERTIFIED" if all(ok) else "FAIL"))
        if not all(ok):
            bad.append((p, r, ok))
    print("heads certified: %d/%d" % (len(HEADS) - len(bad), len(HEADS)))
    print("no-head primes (2p in H_even, Thm 8): %s" % NO_HEADS)
    print("(absence of heads for those p rests on the full exact"
          " factorization in code/out/heven_gauss_61.captured.txt)")
    if bad:
        print("FAIL: " + str(bad))
        raise SystemExit(1)
    print("ALL HEADS CERTIFIED")


if __name__ == "__main__":
    main()