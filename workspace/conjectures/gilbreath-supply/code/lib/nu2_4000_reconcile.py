#!/usr/bin/env python3
"""Decisive reconciliation of the exact value of nu2(4000) (and mu_4000) for
the primes, under the canonically floored fold convention d in [2, n-1].

The run debated nu2(4000) == 1975 vs 1976. This script settles it by computing
nu2(4000) THREE independent ways on the SAME input h, so any difference is a
real convention/route discrepancy rather than a difference of inputs:

  (a) lib.nu2.fold_nu2(4000, h)      == lib.supply_fold.s_sos  (SOS transform)
  (b) lib.supply_fold.s_direct(4000, h)[1]  (LITERAL brute submask-XOR oracle)
  (c) a from-scratch literal brute implemented in this script (no lib import
      for the inner loop): for each d in [2, 3999] compute
      T(n,d) = XOR over bitwise submasks o of d of h[n-1-d+o], count ones.

The input h is built once with lib.nu2_guard.prime_h(4002) (the residue-switch
definition h[j] = [q_{j+2} != q_{j+1} mod 4], length 4002), so h is identical
for all three routes.

We also compute nu2(53) and nu2(64) by all routes (guard expects 18 and 27),
and the exact primes mean

    mu_4000 = (1/4000) * sum_{n=2}^{4000} nu2(n)/n

using the canonical fold_nu2 (s_sos).

s_direct signature (confirmed in lib/supply_fold.py): returns (total, ones)
where total = sum_{d=2}^{n-1} (-1)^{T(n,d)} and ones = #{d : T(n,d)=1} = nu2(n).
All arithmetic exact (parities / +-1 products); only the ratio density and the
mean display as floats.

Complexity: route (a) O(4000 log 4000); route (b) O(sum over d of 2^w(d))
with n=4000 bounded (oracle, ~ seconds); route (c) same literal brute as (b)
but written from scratch; the mean loop is 4000 calls to fold_nu2, O(N^2 log N).
"""

from fractions import Fraction

from lib.nu2_guard import prime_h
from lib.nu2 import fold_nu2
from lib.supply_fold import s_direct

N = 4000


def submasks(d):
    """All bitwise submasks of d (including d and 0), descending."""
    s = d
    while True:
        yield s
        if s == 0:
            break
        s = (s - 1) & d


def nu2_literal_scratch(n, h):
    """From-scratch literal brute: for each d in [2, n-1],
    T(n,d) = XOR over bitwise submasks o of d of h[n-1-d+o], count ones.
    No lib import for the inner loop. Exact. Returns (nu2, per-d ones list)."""
    ones = 0
    for d in range(2, n):
        x = 0
        for o in submasks(d):
            x ^= h[n - 1 - d + o]
        ones += x
    return ones


def route(n, h):
    """Return dict of nu2(n) by the three independent routes."""
    a = fold_nu2(n, h[:n])                # s_sos
    b = s_direct(n, h[:n])[1]             # s_direct -> (S, ones); ones == nu2
    c = nu2_literal_scratch(n, h[:n])     # from-scratch literal brute
    return dict(ssos=a, s_direct=b, scratch=c)


def main():
    h = prime_h(N + 2)   # length 4002; residue-switch, identical for all routes
    print("SEQUENCE : primes (residue-switch h, prime_h(4002))")
    print("ORACLE   : s_sos / s_direct / from-scratch literal submask-XOR")
    print("CONVENTION: floored fold d in [2, n-1], T(n,d) = XOR_o submask of d h[n-1-d+o]")
    print("s_direct signature: s_direct(n, h) -> (S, ones); "
          "S=sum (-1)^T over d in [2,n-1], ones=#d with T=1 (== nu2(n)).")
    print()

    for n in (53, 64):
        r = route(n, h)
        agree = r['ssos'] == r['s_direct'] == r['scratch']
        print(f"n={n}: ssos={r['ssos']} s_direct={r['s_direct']} "
              f"scratch={r['scratch']}  agree={agree}")
        assert agree, (n, r)

    print()
    r = route(N, h)
    agree = r['ssos'] == r['s_direct'] == r['scratch']
    print(f"n={N}: ssos={r['ssos']} s_direct={r['s_direct']} "
          f"scratch={r['scratch']}  agree={agree}")
    print(f"nu2(4000) = {r['ssos']}  -> nu2/4000 = {r['ssos']}/4000 = {r['ssos']/4000:.6f}")
    assert agree, r

    # Exact mean mu_4000 = (1/4000) sum_{n=2}^{4000} nu2(n)/n, canonical fold_nu2.
    tot = Fraction(0)
    for n in range(2, N + 1):
        tot += Fraction(fold_nu2(n, h[:n]), n)
    mu = tot / N
    print()
    head = "mu_4000 = (1/4000) * sum_{n=2}^{4000} nu2(n)/n"
    print(f"{head} = {float(mu):.6f}  (exact Fraction num_bits={mu.numerator.bit_length()}, "
          f"den_bits={mu.denominator.bit_length()})")

    # How the 1975-vs-1976 gap arises: the d in {0,1} cells under a [0,n-1]
    # convention. Report the SOS S and ones so the reader sees the relation
    # S = (nd - 2*ones), nd = n-2.
    S, ones = s_direct(N, h[:N])
    nd = N - 2
    print(f"(check) s_direct(4000): S={S}, ones={ones}, nd={nd}, "
          f"S == nd-2*ones: {S == nd - 2*ones}")


if __name__ == "__main__":
    main()
