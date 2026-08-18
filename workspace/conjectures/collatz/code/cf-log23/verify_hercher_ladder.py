"""Verify that Hercher's m-cycle exclusion ladder is the continued fraction
of log_2(3), evaluated at his epsilon bounds.

Hercher 2022 (arXiv 2201.00406), proof of Theorem 23, states an iteration:

  m2 >= 47:  delta < (K+L)/K < delta + 6.9e-32  =>  K > 5.2e15
  m2 >= 67:  delta < (K+L)/K < delta + 5.1e-36  =>  K > 3.97e17
  m2 >= 77:  delta < (K+L)/K < delta + 4.1e-38  =>  K > 4.64e18
  m2 >= 82:  delta < (K+L)/K < delta + 2.3e-39  =>  K > 2.74e19
  m2 >= 86:  delta < (K+L)/K < delta + 2.3e-40  =>  K > 7.76e19
  m2 >= 88:  delta < (K+L)/K < delta + 5.3e-41  =>  K > 2.05e20
  m2 >= 91:  delta < (K+L)/K < delta + 1.11e-43 =>  K > 7.94e21

where delta = log_2(3).  Each implication is the Diophantine statement:
the smallest denominator of any fraction p/q in the open interval
(delta, delta + eps) is exactly the K lower bound quoted.  This program
computes that minimal denominator for each eps, by continued-fraction
interval arithmetic (Hercher's own Lemma 22), with exact verification that
the constructed fraction lies strictly inside the interval, and compares
against the quoted K bounds.

Lemma (Hercher 2022, Lemma 22): for alpha < beta with CF expansions
alpha = [a_0; a_1, ...], beta = [b_0; b_1, ...], let k be the first index
with a_k != b_k.  Then gamma = [a_0; ...; a_{k-1}; min(a_k, b_k) + 1] has
the smallest denominator among all fractions in the OPEN interval
(alpha, beta) -- provided gamma itself lies in the open interval, which it
always does when both endpoints are irrational (the case here).

Verification of gamma in (delta, delta+eps):
  gamma = p/q > delta  <=>  log2(3) < p/q  <=>  3^q < 2^p   (EXACT, big ints)
  gamma = p/q < delta + eps: checked at high precision (dps 400); the gap
  |gamma - (delta+eps)| is bounded below by ~1/(q * q') with q, q' ~ 1e21,
  i.e. ~1e-42, far above the 400-digit working precision.

Validation of interval_min_denom: brute force over denominators q <= Q on
intervals (sqrt(2), sqrt(2) + eps) with exact integer oracle
  sqrt(2) < p/q  <=>  2 q^2 < p^2
  p/q < sqrt(2) + eps  <=>  (p - eps q)^2 < 2 q^2   (exact, eps rational)
"""
from __future__ import annotations

import math
import sys
from fractions import Fraction

import mpmath as mp

# Hercher's iteration: (eps, quoted K bound) as given in the proof of Thm 23
STEPS = [
    (Fraction("6.9e-32"), "5.2e15"),
    (Fraction("5.1e-36"), "3.97e17"),
    (Fraction("4.1e-38"), "4.64e18"),
    (Fraction("2.3e-39"), "2.74e19"),
    (Fraction("2.3e-40"), "7.76e19"),
    (Fraction("5.3e-41"), "2.05e20"),
    (Fraction("1.11e-43"), "7.94e21"),
]


def cf_of(x: mp.mpf, n_terms: int = 600) -> list[int]:
    terms = []
    for _ in range(n_terms):
        a = int(mp.floor(x))
        terms.append(a)
        frac = x - a
        if frac == 0:
            break
        x = 1 / frac
    return terms


def convergent(terms: list[int]) -> tuple[int, int]:
    """(p, q) of CF [a_0; ...; a_k].  p_{-2}=0, p_{-1}=1; q_{-2}=1, q_{-1}=0."""
    p = [0, 1]
    q = [1, 0]
    for a in terms:
        p.append(a * p[-1] + p[-2])
        q.append(a * q[-1] + q[-2])
    return p[-1], q[-1]


def interval_min_denom(lo: mp.mpf, hi: mp.mpf, dps: int = 400) -> tuple[int, int]:
    """Minimal denominator q of a fraction p/q strictly inside (lo, hi).

    Returns (p, q).  Requires both endpoints irrational (else gamma can sit
    on an endpoint and the bound is not tight).
    """
    mp.mp.dps = dps
    ca = cf_of(lo)
    cb = cf_of(hi)
    k = 0
    while k < min(len(ca), len(cb)) and ca[k] == cb[k]:
        k += 1
    prefix = ca[:k]
    c = min(ca[k], cb[k]) + 1
    p, q = convergent(prefix + [c])
    return p, q


def delta_lt_pq(p: int, q: int) -> bool:
    """log2(3) < p/q, exact: 3^q < 2^p."""
    return pow(3, q) < pow(2, p)


def brute_min_denom_sqrt2(eps: Fraction, Q: int) -> int:
    """Smallest q with p/q in (sqrt2, sqrt2+eps), exact integer oracle."""
    for q in range(1, Q + 1):
        # smallest p with sqrt2 < p/q: p^2 > 2 q^2
        p = math.isqrt(2 * q * q) + 1
        if p * p <= 2 * q * q:
            p += 1
        # p/q < sqrt2 + eps  <=>  (p - eps q)^2 < 2 q^2  (and p - eps q > 0)
        r = Fraction(p, 1) - eps * q
        if r <= 0:
            continue
        # r^2 < 2 q^2
        if r.numerator * r.numerator < 2 * q * q * r.denominator * r.denominator:
            return q
    return -1


def validate() -> None:
    print("=== validation: (sqrt2, sqrt2+eps) CF-method vs exact brute force ===")
    cases = [
        (Fraction(1, 1000), 3000),
        (Fraction(3, 1000), 3000),
        (Fraction(1, 100), 3000),
        (Fraction(7, 1000), 3000),
        (Fraction(1, 10000), 3000),
    ]
    ok_all = True
    for eps, qmax in cases:
        lo = mp.sqrt(2)
        hi = lo + mp.mpf(eps.numerator) / mp.mpf(eps.denominator)
        p, q = interval_min_denom(lo, hi, dps=200)
        b = brute_min_denom_sqrt2(eps, qmax)
        status = "OK" if q == b else "MISMATCH"
        if q != b:
            ok_all = False
        print(f"  eps={float(eps):.2e}: CF-method q={q} (p={p}), brute q={b}, {status}")
    print("validation", "passed" if ok_all else "FAILED")
    assert ok_all, "validation failed"


def main() -> None:
    validate()

    print("\n=== Hercher Theorem 23 iteration ===")
    mp.mp.dps = 400
    delta = mp.log(3) / mp.log(2)
    print(f"delta = log2(3) = {mp.nstr(delta, 30)}")

    print("\n  eps          exact minimal denominator q*   quoted K >   match?")
    for eps, quoted in STEPS:
        hi = delta + mp.mpf(eps.numerator) / mp.mpf(eps.denominator)
        p, q = interval_min_denom(delta, hi)
        # verify gamma strictly inside, exactly
        in_lo = delta_lt_pq(p, q)                      # delta < p/q
        g = mp.mpf(p) / mp.mpf(q)
        in_hi = g < hi                                 # p/q < delta + eps
        ok = in_lo and in_hi
        # compare with quoted: quoted is a rounded value; check q is within
        # the printed order of magnitude and the leading digits
        q_float = float(q)
        quoted_val = float(quoted)
        rel = abs(q_float - quoted_val) / quoted_val
        print(f"  {float(eps):.3e}  q* = {q:,} (p={p})   {quoted:>10}   "
              f"inside={in_lo and in_hi}  rel|q*-quoted|={rel:.3f}")
        if not ok:
            print("    ** gamma NOT strictly inside the interval -- method broken **")
            return
    print("\nIf every rel|q*-quoted| is small (< ~0.15), Hercher's quoted K "
          "bounds ARE the minimal denominators of the CF interval (delta, delta+eps), "
          "confirming the ladder is driven by the continued fraction of log2(3).")


if __name__ == "__main__":
    main()
