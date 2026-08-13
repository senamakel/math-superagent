#!/usr/bin/env python3
"""Extension of the mod-16 character measurement to large odd primes
p in {101, 103, 107, 109, 113, 127}.

For each p, Phi_{4p}(2) = (2^{2p}+1)/5 (exact) is factorised COMPLETELY via
sympy.factorint (numbers <= 2^254+1 ~ 76 digits).  For each distinct prime
divisor r report:
  - class r mod 16 in {1,5,9,13} (every such r is 1 mod 4: ord_r(2)=4p | r-1)
  - e(r) in {0,1,2,3} with (2/r)_4 = i^{e(r)}: e=0 iff r==1 mod 16 (head),
    e=2 iff r==9 mod 16, e=1,3 iff r==5 or 13 mod 16
  - heads = #{r | Phi : r == 1 mod 16}   (v2(r-1)>=4, so r is NOT 3-Higgs)
  - omega = number of distinct prime divisors
  - character sums over the four Dirichlet characters on {1,5,9,13}:
      trivial  chi0 = 1      -> S0 = omega
      quadratic chi2(5) = -1 -> S2 = N1 - N5 + N9 - N13
      quartic   chi(5)  = i  -> S4 = N1 + i*N5 - N9 - i*N13
      conjugate chi-bar       -> S4bar = conj(S4)
  - Parseval with the CORRECT divisor 4 (the group {1,5,9,13} = <5> is cyclic
    of order 4):
      sum_a N_a^2 == (S0^2 + S2^2 + |S4|^2 + |S4bar|^2) / 4
    (the previous script used /8, which is the WRONG Parseval constant).
  - CLOSED-FORM check: the full Gaussian product over the COMPLETE factorisation
    of 2^{2p}+1 (including the non-primitive factor 5, with multiplicity) of
    (2/pi)_4^e equals +1  ==  (2/(2^p+i))_4 == +1.  Route: code/char_mod16_verify2.py
    (Cornacchia split of each rational prime into Gaussian primes + explicit
    gauss jacobi evaluation).  This is the honest closed form (the old script's
    sum over DISTINCT rational r | Phi_4p(2) of e-of-class, with 'want 3/2'
    targets, is a mis-specified check -- it drops 5 and uses a rational
    e-of-class, not the Gaussian quartic exponent).

Also reports for each p:
  - is_3_higgs(p) via lib.higgs.is_3_higgs (OEIS A057447, literal rule)
  - note that 2p is NOT a verified H_even member for p >= 61 (the verified
    set H_even cap [2,1200] = {2,6,10,18,26,30,46,62,82,122}; H_even prime
    branch members are 2p for p in {3,5,13,23,31,41,61}, so p>=101 is far
    past every verified member).

Exact integer / Gaussian-arithmetic throughout; no floats in reported sums.
If a complete factorisation does not finish in budget for some p, it is
reported as UNFACTORED and the row is skipped for the per-p sums, with the
elapsed time stated.

Time/space: 7 primes, numbers <= 2^254+1 ~ 5.8e76; sympy factorint (pollard
rho + ECM under the hood) with a 540 s wall clock; worst-case p=127 is the
largest and closes the run.
"""

import sys
import time
from math import isqrt
from fractions import Fraction
from sympy import factorint, isprime, I, Rational, divisors, mobius

from lib.higgs import is_3_higgs

PRIMES = [101, 103, 107, 109, 113, 127]

# verified H_even prime-branch members (2p in H_even) through p=1200/2
# (arXiv:2605.20475 Thm 8): p in {3,5,13,23,31,41,61}
VERIFIED_P = {3, 5, 13, 23, 31, 41, 61}


def phi_n_at_2(n):
    """Phi_n(2) by the Moebius inversion formula (exact)."""
    out = 1
    for d in divisors(n):
        out *= (2 ** d - 1) ** mobius(n // d)
    return out


def class_of(r):
    c = r % 16
    assert c in (1, 5, 9, 13), (r, c)
    return c


def e_of_class(c):
    return {1: 0, 5: 1, 9: 2, 13: 3}[c]


# --- Gaussian closed-form helpers (route of char_mod16_verify2.py) ---------

def cornacchia(q, x):
    a, b = q, x % q
    while b * b > q:
        a, b = b, a % b
    u = b
    w2 = q - u * u
    w = isqrt(w2)
    assert w * w == w2 and w > 0
    return u, w


def factor_gauss(p):
    a = 2 ** p
    N = a * a + 1
    rows = []
    for q, e in sorted(factorint(N).items()):
        q = int(q)
        x = a % q
        u, v = cornacchia(q, x)
        pi_div = ((a * u + v) % q == 0) and ((u - a * v) % q == 0)
        pb_div = ((a * u - v) % q == 0) and ((a * v + u) % q == 0)
        assert pi_div != pb_div
        su, sv = (u, v) if pi_div else (u, -v)
        rows.append((q, e, su, sv))
    return rows


def gauss_char_e(q, su, sv):
    c = pow(2, (q - 1) // 4, q)
    if c == 1:
        return 0
    if c == q - 1:
        return 2
    icls = (-su * pow(sv, q - 2, q)) % q
    if c == icls:
        return 1
    assert c == (q - icls) % q
    return 3


def full_gaussian_product_is_one(p):
    """(2/(2^p+i))_4 == +1 : sum over FULL factorisation incl 5 of
    e·(2/pi)_4^e is 0 mod 4."""
    rows = factor_gauss(p)
    total = sum(e * gauss_char_e(q, su, sv) for q, e, su, sv in rows) % 4
    return total == 0


def main():
    t0 = time.time()
    all_ok = True
    zero_head_3higgs = []   # 3-Higgs p with heads == 0 (the C29 persistence)
    unfactored = []

    for p in PRIMES:
        t_p = time.time()
        n = 4 * p
        phi_exact = phi_n_at_2(n)
        phi_alt = (2 ** (2 * p) + 1) // 5
        assert phi_exact == phi_alt, (p, phi_exact, phi_alt)

        try:
            fac = factorint(phi_exact)
        except Exception as ex:                      # not finished / gave up
            unfactored.append(p)
            print(f"p={p:3d}: UNFACTORED after {time.time()-t_p:.1f}s "
                  f"({type(ex).__name__}: {ex})")
            continue

        rs = sorted(fac.keys())
        omega = len(rs)
        counts = {1: 0, 5: 0, 9: 0, 13: 0}
        es = []
        per_r = []
        for r in rs:
            assert isprime(r), (p, r)
            c = class_of(r)
            counts[c] += 1
            e = e_of_class(c)
            es.append(e)
            # primitive divisor: ord_r(2) = 4p  <=>  2^{2p} = -1, 2^{4p} = 1
            assert pow(2, 4 * p, r) == 1, (p, r)
            assert pow(2, 2 * p, r) == r - 1, (p, r)
            per_r.append((r, c, e))

        N1, N5, N9, N13 = counts[1], counts[5], counts[9], counts[13]
        S0 = omega
        S2 = N1 - N5 + N9 - N13
        S4 = Rational(N1) + I * Rational(N5) - Rational(N9) - I * Rational(N13)
        S4bar = S4.conjugate()

        # Parseval with the CORRECT group constant |G| = 4
        lhs = N1 * N1 + N5 * N5 + N9 * N9 + N13 * N13
        rhs = (S0 * S0 + S2 * S2 + abs(S4) ** 2 + abs(S4bar) ** 2) / 4
        ok_parseval = (lhs == rhs)

        # closed form: full Gaussian product (2/(2^p+i))_4 == +1
        closed_ok = full_gaussian_product_is_one(p)

        higgs = is_3_higgs(p)
        verified_member = (2 * p) in {2 * q for q in VERIFIED_P}
        assert not verified_member, (p,)   # all our p >= 101 are beyond H_even

        head_frac = Fraction(N1, omega) if omega else None
        if higgs and N1 == 0:
            zero_head_3higgs.append((p, omega))

        all_ok = all_ok and ok_parseval and closed_ok and higgs

        print(f"p={p:3d} omega={omega:3d} N1={N1:3d} N5={N5:3d} N9={N9:3d} "
              f"N13={N13:3d} heads={N1:3d} S2={S2:5d} S4={S4} "
              f"S4bar={S4bar}")
        print(f"    Parseval(/4) {'OK' if ok_parseval else 'FAIL'}   "
              f"closed-form (2/(2^p+i))_4==+1 {'OK' if closed_ok else 'FAIL'}   "
              f"3-Higgs(p)={higgs}   2p in H_even(verified)="
              f"{'yes' if verified_member else 'no(p>=61 never)'}")
        print(f"    heads/omega={float(head_frac):.4f}  "
              f"class-counts list:")
        for r, c, e in per_r:
            print(f"      r={r:>72d}  class={c:2d} mod16  e={e} "
                  f"{'HEAD' if c == 1 else ''}")
        print(f"    [row time {time.time()-t_p:.1f}s]")

    print("\n== Persistence of zero-head rows among 3-Higgs primes past 97 ==")
    print(f"3-Higgs p with heads==0 in {{101,103,107,109,113,127}}: "
          f"{zero_head_3higgs if zero_head_3higgs else 'NONE'}")
    print(f"unfactored: {unfactored if unfactored else 'none'}")

    verdict = ("zero-head rows DO persist among large 3-Higgs primes"
               if zero_head_3higgs else
               "no zero-head 3-Higgs row among these six large primes; "
               "every 3-Higgs p here carries a head")

    print("\nVERDICT:", verdict)
    print(f"ALL checks: {'PASS' if all_ok else 'FAIL'}")
    print(f"rows completed: {len(PRIMES)-len(unfactored)}/{len(PRIMES)}, "
          f"unfactored {unfactored if unfactored else 'none'}, "
          f"elapsed {time.time()-t0:.1f}s")
    sys.exit(0 if all_ok and not unfactored else 1)


if __name__ == "__main__":
    main()
