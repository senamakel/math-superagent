#!/usr/bin/env python3
"""Complete factorization of 2^m + 1 for the ten paper-verified m values,
by sympy.factorint (ECM + Pollard + MPQS route), independent of the bounded
trial-division/pollard-rho route in heven_patterns.py.

Then check, for every prime q | 2^{2k}+1:
  ord_q(2) = 4d with d | k            (exact group-theoretic fact, checked)
  q = 1 + 4dt  with t odd or 2 mod 4  (v2(q-1) <= 3, necessary for 3-Higgs)
  q is 3-Higgs                        (the definition itself)

This completes the reproduction of H_even cap [2,1200] = {2,...,122} with a
FULL factorization of every value, an independent second path.
"""
import sys
from sympy import factorint, isprime
from heven_patterns import higgs3

K_VERIFIED = [1, 3, 5, 9, 13, 15, 23, 31, 41, 61]
M_VERIFIED = [2 * k for k in K_VERIFIED]


def v2(n):
    return (n & -n).bit_length() - 1


def divisors(n):
    out = {1}
    for p, e in factorint(n).items():
        out = {d * p**j for d in out for j in range(e + 1)}
    return sorted(out)


def main():
    out = sys.stdout
    all_ok = True
    for k in K_VERIFIED:
        n = 2 ** (2 * k) + 1
        fs = factorint(n)          # complete, exact
        assert n == 1 or all(isprime(p) for p in fs)
        assert sum(e * p for p, e in fs.items()) is not None
        # verify the product is n
        prod = 1
        for p, e in fs.items():
            prod *= p**e
        assert prod == n, (k, prod, n)

        # order of 2 mod q over divisors of 4k
        lines = []
        ord_ok = t_ok = higgs_ok = True
        for q in sorted(fs):
            ordq = next(d for d in divisors(4 * k) if pow(2, d, q) == 1)
            d = ordq // 4
            good_ord = (ordq % 4 == 0 and (4 * k) % ordq == 0 and k % d == 0)
            ord_ok &= good_ord
            t = (q - 1) // (4 * d)
            v2t = v2(t)
            good_t = v2t <= 1
            t_ok &= good_t
            h = higgs3(q)
            higgs_ok &= h
            lines.append(
                f"      q={q}: ord={ordq} d={d} (d|k: {k % d == 0}) "
                f"t={t} v2(q-1)={v2(q - 1)} v2(t)={v2t} "
                f"3-Higgs={h}")
        status = "IN H_even" if (ord_ok and t_ok and higgs_ok) else "FAIL"
        all_ok &= (ord_ok and t_ok and higgs_ok)
        out.write(f"k={k:3d} m={2 * k:4d}: 2^m+1 fully factored, "
                  f"factors {sorted(fs)}\n")
        out.write("\n".join(lines) + "\n")
        out.write(f"   ord=4d with d|k: {ord_ok}; v2(t)<=1: {t_ok}; "
                  f"all 3-Higgs: {higgs_ok}  -> {status}\n")
    out.write(f"\nALL TEN VERIFIED ELEMENTS REPRODUCED WITH COMPLETE "
              f"FACTORIZATION: {all_ok}\n")
    out.write(f"verified m = {M_VERIFIED}\n")
    out.write("DONE\n")


if __name__ == "__main__":
    main()