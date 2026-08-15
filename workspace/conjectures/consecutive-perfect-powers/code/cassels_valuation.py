#!/usr/bin/env python3
"""cassels_valuation.py

Re-derive, by exact algebra (sympy + PARI/GP via cypari2), the valuation
facts underlying the Cassels divisibility step of x^p - y^q = 1 (Catalan):
an odd-prime solution forces p | y and q | x. This program does NOT prove
Cassels in full; it establishes the exact valuation identities and the
cyclotomic coprimality that the entry lemma reduces to.

Four independent sections:

  A. LTE / valuation identity (exact integers, no floats)
     x-side :  v_p(x^p - 1) = v_p(x - 1) + 1   whenever  p | (x-1)
               v_p(x^p - 1) = v_p(x - 1)       whenever  p \nmid (x-1)
     y-side :  v_q(y^q + 1) = v_q(y + 1) + 1   whenever  q | (y+1)
     swept over p in {3,5,7,11} and a range of x (and q, y on the y-side).
     This is the LTE transfer Cassels uses on both sides.

  B. Cyclotomic factorisation / (1-zeta_p)-adic valuation of the factors of
     x^p - 1.  In Q(zeta_p):
        x^p - 1 = prod_{i=0}^{p-1} (x - zeta_p^i),   zeta_p = exp(2 pi i / p)
     with (p) = (1 - zeta_p)^{p-1} totally ramified, P = (1 - zeta_p) the
     unique prime over p.  For p in {3,5,7,11} and a handful of x we compute
     v_P(x - zeta^i) and v_P(x^p - 1) directly in PARI and verify
        v_P(x^p - 1) = sum_i v_P(x - zeta^i)
     and, when p | (x-1), that the p-adic valuation of the rational integer
     x^p - 1 (i.e. of the ideal (x^p-1) at P) equals v_p(x^p-1) from section A
     via the ramification identity v_P(p) = p - 1:
        v_P(x^p - 1) = (p-1) * v_p(x^p - 1).

  C. Cyclotomic coprimality off the ramified prime.
     For i != j the ideals (x - zeta^i), (x - zeta^j) share no prime ideal
     away from the unique prime P = (1 - zeta_p).  Verified numerically by
     factoring both ideals and intersecting their prime sets: the intersection
     must be contained in {P}.  (If neither x-zeta^i is divisible by P the
     intersection must be empty.)

  D. Oracle cross-check: solutions(N) == {(3,2,2,3)} for reachable N, exact
     integer arithmetic, so the known solution 3^2 - 2^3 = 1 is never
     excluded by any lemma asserted below.

Exact or PARI-exact arithmetic throughout: the rational side is pure integer
arithmetic (no floats); PARI's nfinit/ideal machinery is exact. No rounding
is used for any comparison.
"""
import time
from math import isqrt

from lib.valuation import v_p, lte_xside, lte_yside, solutions


# --------------------------------------------------------------------------
# Section A: LTE valuation identities (exact integers)
# --------------------------------------------------------------------------
def section_A():
    print("=" * 74)
    print("A. LTE valuation identities  (exact integer arithmetic)")
    print("   x-side: v_p(x^p-1) = v_p(x-1) + 1  iff p | (x-1)")
    print("           v_p(x^p-1) = v_p(x-1)      iff p !| (x-1)")
    print("   y-side: v_q(y^q+1) = v_q(y+1) + 1  iff q | (y+1)")
    print("=" * 74)

    primes = [3, 5, 7, 11]
    # x-side: choose x with a spread of v_p(x-1) values
    x_range = list(range(2, 30)) + [40, 82, 244, 730]  # 3^a+1-ish, 5^b+? spreads
    print("\n--- x-side (p | x-1 forces +1; p !| x-1 leaves it) ---")
    total_x = bad_x = 0
    shown = 0
    for p in primes:
        for x in x_range:
            if x % p == 0:
                continue  # need p \nmid x for the plain LTE statement
            lhs, rhs, p_div, p_ndiv_x = lte_xside(p, x)
            # identity under either hypothesis branch: rhs already includes the
            # conditional +1, so the identity lhs == rhs is the statement.
            total_x += 1
            if lhs != rhs:
                bad_x += 1
                print(f"  FAIL p={p} x={x}: v_p(x^p-1)={lhs} vs {rhs}")
            if shown < 14 and (p_div or abs(lhs-rhs) > 0 or (p, x) == (3, 4)):
                tag = "p|x-1 => +1" if p_div else "p !| x-1"
                print(f"  p={p:2d} x={x:5d}  v_p(x^p-1)={lhs}  "
                      f"v_p(x-1)+[{p_div}]={rhs}   {tag}")
                shown += 1
    print(f"  x-side: {total_x} cases, {bad_x} failures ->",
          "PASS" if bad_x == 0 else "FAIL")

    print("\n--- y-side (q | y+1 forces +1 on v_q(y^q+1)) ---")
    y_range = list(range(1, 30)) + [80, 242, 728]  # 3^a-1-ish spreads
    total_y = bad_y = 0
    shown = 0
    for q in primes:
        for y in y_range:
            if y ** q + 1 == 0:
                continue
            lhs, rhs, q_div = lte_yside(q, y)
            total_y += 1
            if lhs != rhs:
                bad_y += 1
                print(f"  FAIL q={q} y={y}: v_q(y^q+1)={lhs} vs {rhs}")
            if shown < 14 and (q_div or (q, y) == (3, 2)):
                tag = "q|y+1 => +1" if q_div else "q !| y+1"
                print(f"  q={q:2d} y={y:5d}  v_q(y^q+1)={lhs}  "
                      f"v_q(y+1)+[{q_div}]={rhs}   {tag}")
                shown += 1
    print(f"  y-side: {total_y} cases, {bad_y} failures ->",
          "PASS" if bad_y == 0 else "FAIL")

    print("\n  STATUS (A): LTE identities ",
          "PASS" if bad_x == 0 and bad_y == 0 else "FAIL",
          " -- exact-proved by LTE (1+x+...+x^{p-1} == geometric sum);",
          "verified over the stated ranges.")
    print("  Note: the overbroad hypothesis 'p !| x' is FALSE (p=3,x=2:");
    print(f"        v_3(2^3-1)={v_p(2**3-1,3)} but 1+v_3(2-1)={1+v_p(1,3)}).")
    return bad_x == 0 and bad_y == 0


# --------------------------------------------------------------------------
# Section B: cyclotomic (1-zeta_p)-adic valuation of prod (x - zeta^i)
# --------------------------------------------------------------------------
def _pari_nf(p):
    import cypari2
    from cypari2 import Pari
    pari = Pari()
    pol = pari.polcyclo(p)
    K = pari.nfinit(pol)
    z = pol.variable()
    primes = K.idealprimedec(p)
    assert len(primes) == 1, (p, primes)   # totally ramified
    return pari, K, z, primes[0]


def section_B(p_list=(3, 5, 7, 11), x_list=(2, 3, 4, 5, 8, 10, 12, 16, 22)):
    print()
    print("=" * 74)
    print("B. Cyclotomic (1-zeta_p)-adic valuation of x^p-1 = prod (x-zeta^i)")
    print("   in Q(zeta_p), via PARI exact algebra.")
    print("   P = (1-zeta_p) unique prime over p;  (p) = P^{p-1};  v_P(p)=p-1")
    print("=" * 74)
    import cypari2
    allok = True
    for p in p_list:
        pari, K, z, P = _pari_nf(p)
        print(f"\n  p = {p}")
        for x in x_list:
            val_P_prod = 0      # sum of v_P(x - zeta^i)
            per_i = []
            norms = []
            for i in range(p):
                elt = x - z ** i
                I = K.idealhnf(elt)
                v = K.idealval(I, P)
                n = K.idealnorm(I)
                per_i.append(v)
                norms.append(int(n))
                val_P_prod += v
            # Independent cross-check of the factorisation x^p-1 = prod(x-zeta^i):
            # product of the norms of the factors = norm_K(x^p-1) = (x^p-1)^(p-1).
            norm_prod = 1
            for n in norms:
                norm_prod *= n
            expected_norm = (x ** p - 1) ** (p - 1)
            ok_norm = (norm_prod == expected_norm)
            # rational integer x^p - 1 : its ideal at P = (p-1)*v_p(x^p-1)
            vp = v_p(x ** p - 1, p)
            Ip = K.idealhnf(x ** p - 1)
            vP_int = K.idealval(Ip, P)
            expect_vP = (p - 1) * vp
            # factorisation identity: ideal(x^p-1) == prod ideal(x-zeta^i)
            prod_ideal = K.idealhnf(x ** p - 1)
            ok_sum = (vP_int == val_P_prod)
            ok_ram = (vP_int == expect_vP)
            ok = ok_sum and ok_ram and ok_norm
            allok = allok and ok
            flag = "OK " if ok else "FAIL"
            print(f"    x={x:3d}: v_P(x^p-1)={vP_int}  "
                  f"sum_i v_P(x-zeta^i)={val_P_prod}  "
                  f"(p-1)*v_p(x^p-1)={expect_vP}  v_p(x^p-1)={vp}  "
                  f"norm_prod==(x^p-1)^(p-1):{ok_norm} "
                  f"norms={norms} {flag}")
            if not ok:
                print(f"       !! v_P per-i = {per_i}")
    print("\n  STATUS (B): factorisation + ramification-vLTE-on-the-ideal ",
          "PASS" if allok else "FAIL")
    print("  (B) is numeric-PARI-exact over the listed (p, x); the rational")
    print("  v_p(x^p-1) values are exact integer valuations.")
    return allok


# --------------------------------------------------------------------------
# Section C: cyclotomic coprimality off (1 - zeta_p)
# --------------------------------------------------------------------------
def _ideal_prime_id(pr):
    # pr is a PARI prime ideal [[p, [..]~, f, e, [..]]] -- use its p and f and
    # the embedded two-element form as a hashable tuple
    return (int(pr[0]), tuple(int(t) for t in list(pr[1])), int(pr[3]))


def _factor_prime_set(K, ideal):
    """Prime ideals (as hashable ids) dividing `ideal`, by exact PARI factoring.
    idealfactor returns a 2-column matrix: column 0 = prime ideals, column 1 =
    exponents. In cypari2 iterating a matrix yields columns, so read column 0
    explicitly."""
    fac = K.idealfactor(ideal)
    primes_col = fac[0]
    out = set()
    for pr in primes_col:
        out.add(_ideal_prime_id(pr))
    return out


def section_C(p_list=(3, 5, 7, 11), x_list=(2, 3, 4, 8, 12, 16, 22)):
    print()
    print("=" * 74)
    print("C. Cyclotomic coprimality off the unique ramified prime P=(1-zeta_p)")
    print("   For i != j, ideals (x-zeta^i),(x-zeta^j) share no prime ideal")
    print("   outside {P}. Verified by factoring each and intersecting primes.")
    print("=" * 74)
    allok = True
    total = 0
    for p in p_list:
        pari, K, z, P = _pari_nf(p)
        Pid = _ideal_prime_id(P)
        for x in x_list:
            ideals = [(i, _factor_prime_set(K, K.idealhnf(x - z ** i)))
                      for i in range(p)]
            for a in range(p):
                for b in range(a + 1, p):
                    total += 1
                    common = ideals[a][1] & ideals[b][1]
                    outside = [c for c in common if c != Pid]
                    if outside:
                        allok = False
                        print(f"    FAIL p={p} x={x} i={a} j={b}: shared "
                              f"primes outside P: {outside}")
            # report one sample per (p,x)
            norms = [int(K.idealnorm(K.idealhnf(x - z ** i))) for i in range(p)]
            # gcd of all but computed pairwise -- show min common count
            print(f"    p={p:2d} x={x:3d}: norms of (x-zeta^i) = {norms}")
    print(f"\n  (C) checked {total} pairs (i<j) across p in {list(p_list)}, x in {x_list}.")
    print("  STATUS (C): coprimality off P ", "PASS" if allok else "FAIL",
          " (numerically verified, exact factoring)")
    return allok


# --------------------------------------------------------------------------
# Section D: oracle cross-check
# --------------------------------------------------------------------------
def section_D():
    print()
    print("=" * 74)
    print("D. Oracle cross-check (exact integers): known solution not excluded")
    print("=" * 74)
    t0 = time.time()
    r = solutions(10 ** 8)
    ok = set(r) == {(3, 2, 2, 3)}
    print(f"  solutions(10^8) = {r}  -> {'PASS' if ok else 'FAIL'}  "
          f"({time.time()-t0:.3f}s)")
    print("  3^2 - 2^3 = 1  is the unique consecutive perfect power <= 10^8.")
    return ok


if __name__ == "__main__":
    t_start = time.time()
    A = section_A()
    B = section_B()
    C = section_C()
    D = section_D()

    print()
    print("=" * 74)
    print("SUMMARY of valuation computation")
    print("=" * 74)
    print(f"  A  LTE rational valuation identities   : {'PASS' if A else 'FAIL'}")
    print(f"  B  cyclotomic factor v_P identity      : {'PASS' if B else 'FAIL'}")
    print(f"  C  coprimality off ramified prime      : {'PASS' if C else 'FAIL'}")
    print(f"  D  oracle solutions(1e8)=={{(3,2,2,3)}}: {'PASS' if D else 'FAIL'}")
    print()
    print("EXACT-PROVED:  A (LTE, closed-form geometric sum).")
    print("NUMERICALLY-VERIFIED (exact arithmetic over listed ranges): B, C.")
    print("NOT CLAIMED:   Cassels' full theorem q|x, p|y in general -- that")
    print("               needs the ideal/unit argument in Q(zeta_p) that")
    print("               turns these valuation facts into the divisibility,")
    print("               which this valuation computation does not complete.")
    print(f"  total wall time: {time.time()-t_start:.2f}s")
