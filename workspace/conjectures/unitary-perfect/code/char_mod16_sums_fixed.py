#!/usr/bin/env python3
"""FIXED character-sums-mod-16 measurement over the prime divisors of Phi_{4p}(2).

Corrected from code/char_mod16_sums.py per the reviewer directives:

(1) PARSEVAL with divisor 4.  For the four Dirichlet characters on the
    classes G = {1,5,9,13} (group (Z/16Z)* of order 4), with
       chi0 = 1 (trivial) -> S0 = omega
       chi2 = quadratic, chi2(5) = -1 -> S2 = N1 - N5 + N9 - N13
       chi4 = quartic, chi4(5) = i   -> S4 = N1 + i*N5 - N9 - i*N13
       chi4bar (conjugate)           -> S4bar = conj(S4),
    Parseval / orthogonality of the Fourier vector
       N_a = #{r | Phi_4p(2) : r == a (mod 16)}
    reads  sum_a N_a^2  ==  (S0^2 + S2^2 + |S4|^2 + |S4bar|^2) / 4.
    (The old script's /8 was wrong; it treated S0 as a separate 8th
    character.  The normalized |S_chi|^2 = |sum_a N_a chi(a)|^2 / |G| and
    there are 4 characters so the denominator is 4.)  Verified on every row
    and on the hand-row p=3: Phi_12 = 13, only class 13:  N13=1 => sum N_a^2
    = 1;  S0=1, S2=1, |S4|^2=|i^3|^2=1, |S4bar|^2=1 => (1+1+1+1)/4 = 1.  PASS.

(2) BOGUS CLOSED-FORM CHECK REMOVED.  The old 'sum_e == 3 (p!=5) / 2 (p==5)'
    target over DISTINCT rational r | Phi_{4p}(2) with a rational e-of-class
    is not the honest closed form: it drops the non-primitive factor 5 and
    mis-uses a rational e rather than the Gaussian exponent.  The honest
    closed form is the FULL Gaussian product over pi^e || 2^p + i of
       (2/pi)_4^e = +1  for every odd prime p,
    equivalently the total Gaussian exponent  sum_e e*(2/pi)_4  == 0 (mod 4)
    over the FULL factorization of 2^{2p}+1 (including 5 and multiplicities).
    We reuse the exact factor_gauss + gauss_char_e route from
    char_mod16_verify2.py and cross-check with the supplementary-formula
    route from directive14_quartic_closed_form.py.  The per-row Phi-REDUCED
    rational e-sum is printed as INFORMATIONAL ONLY (labelled 'info') and is
    not a pass/fail target.

MEASUREMENT LOOP (identical to the original): for each odd prime p <= 97,
   Phi_4p(2) = (2^{2p}+1)/5, complete factorint, classes {1,5,9,13}, heads
   (N1), omega, S2, S4, N1..N13.

SECOND-MOMENT MEASUREMENT VERDICT:
   (a) min over p of N1/omega and the achieving p;
   (b) N1 for the seven H_even members p in {3,5,13,23,31,41,61} and N1/omega;
   (c) which 3-Higgs primes p <= 97 have N1 == 0 with 2p NOT in H_even;
   (d) rows with |S2| == omega (p=3,13,61,89,...): these violate any
       |S2| <= delta*omega with delta < 1, i.e. the L4 second-moment premise
       fails on small p.

Exact integer/rational arithmetic throughout (sympy.factorint; Fraction for
the N1/omega ratios; sympy.I only in the reported S4 symbol value).
Time/space: p <= 97 => Phi_4p(2) = (2^{2p}+1)/5 < 2^194 ~ 3e58; factorint is
well within 540 s (the 71-row complete table through p=61 already passed).
"""
import sys
import time
from fractions import Fraction
from sympy import factorint, isprime, divisors, mobius, I, Rational

# exact Gaussian helpers reused from char_mod16_verify2 (module import safe:
# guarded by __main__).  factor_gauss(p) -> [(q,e,su,sv)] for 2^p + i;
# gauss_char_e(q,su,sv) -> k with (2/pi)_4 = i^k.
from char_mod16_verify2 import factor_gauss, gauss_char_e

PRIMES = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
          61, 67, 71, 73, 79, 83, 89, 97]

# the seven H_even members {2p} and which p they correspond to
HEVEN_P = {3, 5, 13, 23, 31, 41, 61}

# 3-Higgs p <= 97 (hard-independent from lib.higgs.is_3_higgs computed below)
from lib.higgs import is_3_higgs


def phi_n_at_2(n):
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


def supplementary_closed_form(p):
    """[2/alpha]_4 exponent k mod 4, alpha = -i*(2^p+i) primary, a=1,b=-2^p.
    Closed form k = (2a - b - 2 - b^2)/2 mod 4; identically 0 for p>=3 odd."""
    two_p = 2 ** p
    a, b = 1, -two_p
    num = 2 * a - b - 2 - b * b
    assert num % 2 == 0
    return (num // 2) % 4


def main():
    t0 = time.time()
    rows = []
    all_parseval = True

    for p in PRIMES:
        n = 4 * p
        phi_exact = phi_n_at_2(n)
        phi_alt = (2 ** (2 * p) + 1) // 5
        assert phi_exact == phi_alt, (p, phi_exact, phi_alt)

        fac = factorint(phi_exact)
        rs = sorted(fac.keys())
        omega = len(rs)

        counts = {1: 0, 5: 0, 9: 0, 13: 0}
        for r in rs:
            assert isprime(r), (p, r)
            c = class_of(r)
            counts[c] += 1
            assert pow(2, 2 * p, r) == r - 1, (p, r)
            assert pow(2, 4 * p, r) == 1, (p, r)

        N1, N5, N9, N13 = counts[1], counts[5], counts[9], counts[13]
        S0 = omega
        S2 = N1 - N5 + N9 - N13
        S4 = Rational(N1) + I * Rational(N5) - Rational(N9) - I * Rational(N13)
        S4bar = S4.conjugate()

        # ---- (1) Parseval with divisor 4 (exact) ----
        lhs = N1 * N1 + N5 * N5 + N9 * N9 + N13 * N13
        rhs = (S0 * S0 + S2 * S2 + abs(S4) ** 2 + abs(S4bar) ** 2) / 4
        ok_parseval = (lhs == rhs)
        all_parseval = all_parseval and ok_parseval

        # ---- (2) honest closed form: full Gaussian product = +1 ----
        grows = factor_gauss(p)
        full_k = sum(e * gauss_char_e(q, su, sv) for q, e, su, sv in grows) % 4
        ok_closed = (full_k == 0)
        # cross-check: supplementary closed form matches direct product
        sup_k = supplementary_closed_form(p)
        ok_sup = (sup_k == full_k)

        # informational only: Phi-REDUCED rational e-sum (not a target)
        info_sum_e = sum(e_of_class(class_of(r)) for r in rs) % 4

        head_frac = Fraction(N1, omega) if omega else None
        rows.append(dict(p=p, omega=omega, N1=N1, N5=N5, N9=N9, N13=N13,
                         S2=S2, S4=S4, S4bar=S4bar,
                         ok_parseval=ok_parseval, head_frac=head_frac,
                         full_k=full_k, ok_closed=ok_closed, ok_sup=ok_sup,
                         info_sum_e=info_sum_e, sup_k=sup_k))

        print(f"p={p:3d} omega={omega:3d} N1={N1:3d} N5={N5:3d} "
              f"N9={N9:3d} N13={N13:3d} heads={N1:3d} S2={S2:5d} "
              f"S4={S4} S4bar={S4bar}")
        print(f"     Parseval: sum N_a^2={lhs} == ({S0}^2+{S2}^2+|S4|^2"
              f"+|S4bar|^2)/4={rhs} "
              f"{'OK' if ok_parseval else 'FAIL'}"
              f"   |S2|={abs(S2)} vs omega={omega}"
              f"{'  [|S2|==omega!]' if abs(S2) == omega else ''}")
        print(f"     closed form: FULL Gaussian prod (2/(2^p+i))_4 = i^{full_k}"
              f" {'= 1 OK' if ok_closed else 'FAIL'}"
              f"  supplementary sup_k=i^{sup_k}"
              f" {'OK' if ok_sup else 'FAIL'}"
              f"   [info only] Phi-reduced e-sum = {info_sum_e}")

    ok_closed_all = all(r['ok_closed'] for r in rows)
    ok_sup_all = all(r['ok_sup'] for r in rows)

    print("\n================ SECOND-MOMENT MEASUREMENT VERDICT ================")

    # (a) min over p of N1/omega
    by_frac = sorted(rows, key=lambda r: Fraction(r['N1'], r['omega']))
    m = by_frac[0]
    print(f"(a) min N1/omega = {m['N1']}/{m['omega']} "
          f"(= {float(m['head_frac']):.4f}) at p={m['p']}")

    # (b) N1 for the seven H_even members
    print("(b) H_even members (2p in {6,10,26,46,62,82,122}, p in "
          f"{sorted(HEVEN_P)}):")
    for p in sorted(HEVEN_P):
        r = next(x for x in rows if x['p'] == p)
        print(f"    p={p:2d} (2p={2*p:3d}): N1={r['N1']:2d}  "
              f"N1/omega={r['N1']}/{r['omega']} "
              f"(= {float(Fraction(r['N1'], r['omega'])):.4f})")

    # (c) 3-Higgs p <= 97 with N1==0 and 2p NOT in H_even
    print("(c) 3-Higgs primes p<=97 with N1==0 AND 2p NOT in H_even:")
    c_rows = []
    for r in rows:
        p = r['p']
        if is_3_higgs(p) and r['N1'] == 0 and p not in HEVEN_P:
            c_rows.append(p)
            print(f"    p={p:2d} (2p={2*p:3d})  N1=0  (3-Higgs, not in H_even)")
    print(f"    count={len(c_rows)}  {sorted(c_rows)}")

    # (d) rows with |S2| == omega
    print("(d) rows with |S2| == omega (violate |S2| <= delta*omega, delta<1):")
    d_rows = [r for r in rows if abs(r['S2']) == r['omega']]
    for r in d_rows:
        print(f"    p={r['p']:3d} omega={r['omega']:3d} |S2|={abs(r['S2'])}"
              f"  N1={r['N1']} N5={r['N5']} N9={r['N9']} N13={r['N13']}")
    print(f"    count={len(d_rows)}  p={sorted(r['p'] for r in d_rows)}")

    # final verdict line
    heven_n1 = {r['p']: r['N1'] for r in rows if r['p'] in HEVEN_P}
    min_heven = min(Fraction(r['N1'], r['omega']) for r in rows
                    if r['p'] in HEVEN_P)
    min_global = by_frac[0]['head_frac']
    fails_n1 = all(heven_n1[p] == 0 for p in HEVEN_P)
    print("\nH_even slice N1 values:", {p: heven_n1[p] for p in sorted(HEVEN_P)})
    print("min N1/omega on H_even slice =", min_heven,
          f"(= {float(min_heven):.4f})")
    print("min N1/omega over ALL p =", min_global,
          f"(= {float(min_global):.4f})")
    if fails_n1 and min_global == 0:
        print("SECOND-MOMENT MEASUREMENT: FAILS "
              "(N1=0 on entire H_even slice; min N1/omega = 0)")
    else:
        print("SECOND-MOMENT MEASUREMENT: (not the fails branch)")

    print("\nidentity checks: Parseval(div4) %s  closed-form-full=1 %s  "
          "supplementary-match %s"
          % ("PASS" if all_parseval else "FAIL",
             "PASS" if ok_closed_all else "FAIL",
             "PASS" if ok_sup_all else "FAIL"))
    print(f"rows completed: {len(rows)}/{len(PRIMES)}, "
          f"elapsed {time.time() - t0:.1f}s")

    ok_all = all_parseval and ok_closed_all and ok_sup_all
    sys.exit(0 if ok_all else 1)


if __name__ == "__main__":
    main()
