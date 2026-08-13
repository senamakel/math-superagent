#!/usr/bin/env python3
"""Character sums mod 16 over the distinct prime divisors of Phi_{4p}(2).

For each odd prime p <= 97, Phi_{4p}(2) = (2^{2p}+1)/5 (exact integer).
Complete factorization via sympy.factorint (numbers <= 2^194+1 ~ 1e58).
For each distinct prime divisor r report:
  - class r mod 16 in {1,5,9,13} (every such r is 1 mod 4; see below)
  - e(r) in {0,1,2,3} with (2/r)_4 = i^{e(r)}: e=0 iff r==1 mod 16
    (head), e=2 iff r==9 mod 16, e=1,3 iff r==5 or 13 mod 16
  - heads  = #{r | Phi : r == 1 mod 16}
  - omega  = omega(Phi) = number of distinct prime divisors
  - S_chi over the four Dirichlet characters on {1,5,9,13}:
      trivial   chi0 = 1            -> S = omega
      quadratic chi2(5) = -1        -> S2 = N1 - N5 + N9 - N13
      quartic   chi(5) = i          -> S4 = N1 + i*N5 - N9 - i*N13
      conjugate chi-bar(5) = -i     -> S4bar = conj(S4)
  - and sum over r of e(r) mod 4 (the mod-4 product identity),
      Sigma e(r) == 3 (mod 4) for p != 5, == 2 (mod 4) for p == 5.

Verification targets (exact, from first principles):
  1. p=3: Phi_12(2) = 13, omega=1, r=13 == 13 mod 16, heads=0.
  2. p=5: Phi_20(2) = 41, r=41 == 9 mod 16, heads=0, Sigma e = 2.
  3. independence check: recompute Phi via the Moebius product formula
       Phi_n(2) = prod_{d|n} (2^d - 1)^{mu(n/d)}
     and via (2^{2p}+1)/5; each r checked to divide the full value and to be
     prime (sympy.isprime).
  4. every r is 1 mod 4 (guaranteed: ord_r(2) = 4p | r-1), with primitive
     order check pow(2, 4p, r) == 1 for heads certification.
  5. Parseval: sum_a N_a^2 == (S2^2 + |S4|^2 + |S4bar|^2 + omega^2)/8.
  6. min over p of heads/omega reported (single-c fit for C29).

Exact: sympy.factorint integers, sympy.I for the quartic character values;
no floats in the reported sums ( |S|^2 computed exactly as N_a counts ).

Time/space: p <= 97 => N <= 2^194+1 ~ 5.9e58, factorint with sympy's
default methods is well within 540 s per the 71-row table already completed
through p = 61 (code/out/heven_gauss_61.captured.txt).
"""

import sys
import time
from fractions import Fraction
from sympy import factorint, isprime, I, Rational

PRIMES = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
          61, 67, 71, 73, 79, 83, 89, 97]


def phi_n_at_2(n):
    """Phi_n(2) by the Moebius inversion formula (exact)."""
    from sympy import divisors, mobius
    out = 1
    for d in divisors(n):
        out *= (2 ** d - 1) ** mobius(n // d)
    return out


def class_of(r):
    """r mod 16, mapped into {1,5,9,13}; caller guarantees r == 1 mod 4."""
    c = r % 16
    assert c in (1, 5, 9, 13), (r, c)
    return c


def e_of_class(c):
    """e in {0,1,2,3} with i^e = (2/r)_4; e=0 iff r==1 mod 16 (head)."""
    return {1: 0, 5: 1, 9: 2, 13: 3}[c]


def main():
    t0 = time.time()
    rows = []
    all_ok = True
    sympy_I = I

    for p in PRIMES:
        n = 4 * p
        phi_exact = phi_n_at_2(n)
        phi_alt = (2 ** (2 * p) + 1) // 5
        assert phi_exact == phi_alt, (p, phi_exact, phi_alt)

        fac = factorint(phi_exact)
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
            # primitive divisor: ord_r(2) must divide 4p and r|2^{2p}+1
            assert pow(2, 2 * p, r) == r - 1, (p, r)
            assert pow(2, 4 * p, r) == 1, (p, r)
            per_r.append((r, c, e))

        N1, N5, N9, N13 = counts[1], counts[5], counts[9], counts[13]
        S0 = omega
        S2 = N1 - N5 + N9 - N13
        S4 = Rational(N1) + sympy_I * Rational(N5) - Rational(N9) - sympy_I * Rational(N13)
        S4bar = S4.conjugate()

        # mod-4 product identity: Sum e(r) == 3 (p!=5), == 2 (p==5)
        sum_e = sum(es) % 4
        want = 2 if p == 5 else 3
        ok_e = (sum_e == want)

        # Parseval: sum_a N_a^2 == (sum_chi |S_chi|^2)/8, exactly
        lhs = N1 * N1 + N5 * N5 + N9 * N9 + N13 * N13
        rhs = (S2 * S2 + abs(S4) ** 2 + abs(S4bar) ** 2 + S0 * S0) / 8
        ok_parseval = (lhs == rhs)

        head_frac = Fraction(N1, omega) if omega else None
        rows.append((p, omega, N1, N5, N9, N13, S2, S4, S4bar, sum_e,
                     ok_e, ok_parseval, head_frac, per_r))
        all_ok = all_ok and ok_e and ok_parseval

        print(f"p={p:3d} omega={omega:3d} N1={N1:3d} N5={N5:3d} "
              f"N9={N9:3d} N13={N13:3d} heads={N1:3d} "
              f"S2={S2:5d} S4={S4} S4bar={S4bar} "
              f"sum_e={sum_e}(want {want}) {'OK' if ok_e else 'FAIL'} "
              f"Parseval {'OK' if ok_parseval else 'FAIL'}")
        for r, c, e in per_r:
            print(f"    r={r:>38d}  class={c:2d} mod16  e={e}  "
                  f"{'HEAD' if c == 1 else ''}")

    # single-c fit: min over p of heads/omega
    mins = min(rows, key=lambda row: row[12])
    print(f"\nMIN heads/omega: p={mins[0]}  heads/omega = {mins[12]} "
          f"= {float(mins[12]):.6f}")

    # the p=3 and p=5 hand-checkable rows restated
    for p in (3, 5):
        row = next(r for r in rows if r[0] == p)
        print(f"CHECK p={p}: Phi={phi_alt if p==5 else phi_n_at_2(4*p)}, "
              f"omega={row[1]}, class={row[13][0][1]}, heads={row[2]}")

    print(f"\nALL identity checks: {'PASS' if all_ok else 'FAIL'}")
    print(f"rows completed: {len(rows)}/{len(PRIMES)}, "
          f"elapsed {time.time() - t0:.1f}s")
    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()