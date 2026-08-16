#!/usr/bin/env python3
"""Canonical oracle + mandatory entry guard for every averaged/statistical
SUPPLY script (directive 11/12).

The problem.md operative definition is the FLOORED submask fold:
    T(n,d) = XOR over submasks o of d of h[n-1-d+o],  d in [2, n-1],
    nu2(n) = #{ d in [2,n-1] : T(n,d)=1 }  = wt(Phi_n h),
h the prime gap-parity string h[j] = [q_{j+2} != q_{j+1} mod 4].

Roles must not write a fresh nu2 implementation: import `fold_nu2` from
lib.nu2 (which is s_sos, cross-checked against the literal submask-XOR oracle
s_direct on n=4..200 plus spots 53,64,100). Every averaged script calls
`assert_supply_guard(...)` at entry so a zeroed/literal/wrong-convention oracle
aborts instead of printing a table.

Guard values (canonical oracle fold_nu2 = s_sos on d in [2,n-1]):
    nu2(53) == 18      (nu2_extended, smax_report, refuter trajectory)
    nu2(64) == 27      (smax_report)
    primes mu_N(4000) within 0.01 of 0.4977
    nu2(4000) == 1975  (canonical oracle + brute.py; see assert_supply_guard
                        note on the 1975/1976 convention collision — the mean
                        tolerance is the asserted guard, not this count)
"""
from fractions import Fraction

from lib.nu2 import fold_nu2
from lib.supply_fold import s_sos, s_direct
from lib.primes import h_string


def prime_h(n):
    """h[j] = [q_{j+2} != q_{j+1} mod 4] for j=0..n-1 (length n)."""
    return h_string(n + 2)[:n]


def scene_header(label, oracle, nlo, nhi):
    """First-three-lines campaign marker (directive 12.3): which sequence this
    capture ran, which oracle+function, and the exact n-range."""
    return ("SEQUENCE : %s\nORACLE   : %s\nN-RANGE  : [%d, %d]"
            % (label, oracle, nlo, nhi))


def verify_oracle_cross(h, spots=(53, 64, 100)):
    """s_sos == s_direct on n=4..200 and at the given spots (prime h)."""
    for n in range(4, 201):
        Sd, od = s_direct(n, h)
        Ss, os_ = s_sos(n, h)
        assert Sd == Ss and od == os_, (n, Sd, Ss, od, os_)
    for n in spots:
        Sd, od = s_direct(n, h)
        Ss, os_ = s_sos(n, h)
        assert Sd == Ss and od == os_, (n, Sd, Ss, od, os_)
    return True


def assert_supply_guard(N, tol_mu=Fraction(1, 100)):
    """Mandatory entry guard (directive 11/12). Aborts (assert) rather than
    printing a table if the canonical oracle returns the degenerate value.

    Guards exactly the operator's spec (directive 11/12): nu2(53)==18,
    nu2(64)==27, and (if N>=4000) the primes mean mu_4000 within 0.01 of
    0.4977. If N>=4000 it also asserts the absolute count nu2(4000)==1975.
    All exact — the magic numbers 18 and 27 are the ones traceable to three
    independent exact routes (smax_report, nu2_extended, refuter trajectory),
    and 1975 is the floored d in [2, n-1] count (s_sos == s_direct ==
    fold_nu2 all give 1975; the 1976 that appears in some earlier captures is
    the unfloored d in [0, n-2] column of code/out/averaged_mean_capture.txt
    — a floored-vs-unfloored offset, not a discrepancy; problem.md's operative
    floor is d in [2, n-1]).

    NOTE (a real convention collision, settled by the oracle itself): the
    absolute count at n=4000 is convention-sensitive. The operative row floor
    d in [2, n-1] implemented by s_sos/fold_nu2 gives nu2(4000) = 1975; some
    earlier captures (avg_nu2_out.txt, brute.py docstring) quoted 1976 under a
    d in [0, n-2] or boundary convention. The guard therefore asserts the
    operator's mean tolerance (the robust statistic) rather than a single
    n=4000 count, and the count is reported contextually, not asserted.
    """
    h = prime_h(max(N + 1, 4001))
    assert fold_nu2(53, h) == 18, "nu2(53) != 18 — oracle is degenerate/wrong"
    assert fold_nu2(64, h) == 27, "nu2(64) != 27 — oracle is degenerate/wrong"
    if N >= 4000:
        # directive 16: re-add the absolute count assert. 1975 is the
        # operative floored d in [2, n-1] count (s_sos == s_direct ==
        # fold_nu2); 1976 is the unfloored d in [0, n-2] reading and is NOT
        # the operative value. (guard_failure_report.md, board post
        # guard_failure_nu2_4000_1975.md.)
        assert fold_nu2(4000, h) == 1975, \
            "nu2(4000) != 1975 — loose convention / stale constant"
    if N >= 4000:
        # mean over n=2..4000 of nu2(n)/n (exact Fractions)
        tot = Fraction(0)
        for n in range(2, 4001):
            tot += Fraction(fold_nu2(n, h), n)
        mu = tot / 4000
        assert abs(mu - Fraction(4977, 10000)) <= tol_mu, \
            "primes mu_4000 = %s not within %s of 0.4977" % (float(mu), tol_mu)
    return True


def fair_var_ratio(N, nu2):
    """s2_N and its ratio to the fair-model per-n variance 1/(4N).

    Under h uniform on the cube, Phi_n is surjective (full row rank n-2,
    nullity 2, proved) so wt(Phi_n h) ~ Binomial(n-2, 1/2) EXACTLY and, if the
    X_n = nu2(n)/n were decoupled, the sample variance over n would be
    s2_N ~ (1/N) sum_{n<=N} Var(X_n) = (1/N) sum_{n<=N} (n-2)/(4n^2)
          ~ (ln N + gamma)/(4N).
    This function prints the empirical s2_N and the ratio s2_N * 4 * N (and,
    for reference, s2_N * 4 * N / ln N) so the reader can see whether the
    primes track the decoupled random model or deviate.
    Returns (mu_N, s2_N, ratio_4N)."""
    Nn = N
    S1 = Fraction(0)
    S2 = Fraction(0)
    for n in range(2, Nn + 1):
        r = Fraction(nu2[n], n)
        S1 += r
        S2 += r * r
    mu = S1 / Nn
    ex2 = S2 / Nn
    s2 = ex2 - mu * mu
    ratio = float(s2) * 4.0 * Nn
    import math
    lnN = math.log(Nn)
    return (float(mu), float(s2), ratio, ratio / lnN)
