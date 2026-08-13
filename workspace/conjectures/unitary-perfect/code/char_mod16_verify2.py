#!/usr/bin/env python3
"""Independent certification of the NEW heads (r == 1 mod 16) found by
char_mod16_sums.py for primes p in (61, 97] — beyond the previously certified
p <= 61 range (heven_heads_verify).  A head is a prime r | Phi_{4p}(2) with
r == 1 mod 16, hence v2(r-1) >= 4 > 3, hence r is NOT 3-Higgs.

Fresh route: sympy.isprime + sympy.factorint of the exact Moebius Phi, plus
the primitive/order conditions ord_r(2) = 4p (pow(2,4p,r)==1, and
pow(2,2p,r)==r-1 i.e. 2^{2p} == -1 mod r so r | 2^{2p}+1).

Also pins down the EXACT statement for Q2 in char_mod16_sums.py: the closed
form (2/(2^p+i))_4 = 1 is a product over Gaussian primes pi || 2^p+i with
multiplicity, N(pi) = q | 2^{2p}+1 (FULL value, including the non-primitive
factor 5).  The script instead summed e_of_class over DISTINCT rational r |
Phi_{4p}(2) = (2^{2p}+1)/5, which (i) drops the factor 5 and (ii) uses a
rational e-of-class rather than the Gaussian quartic exponent — so its
"sum_e == 3 or 2" targets are not the closed form.  We show the honest
object: for every p <= 97, summing the Gaussian quartic exponent over the
FULL factorization of 2^{2p}+1 (including multiplicities and 5) gives
exponent 0 mod 4 (product = 1), and dropping 5 (i.e. primitive divisors
only, Phi_4p(2)) by itself need not be 0.

Exact integer arithmetic throughout.
"""
from math import isqrt
from sympy import factorint, isprime, divisors, mobius

def phi_n_at_2(n):
    out = 1
    for d in divisors(n):
        out *= (2 ** d - 1) ** mobius(n // d)
    return out

def v2(k):
    return (k & -k).bit_length() - 1

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

PRIMES_NEW = [67, 71, 73, 79, 83, 89, 97]
ALL = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
       67, 71, 73, 79, 83, 89, 97]

def main():
    print("== Independent certification of NEW heads for p in (61,97] ==\n")
    allcert = True
    total_new_heads = 0
    for p in PRIMES_NEW:
        phi = phi_n_at_2(4 * p)
        assert phi == (2 ** (2 * p) + 1) // 5
        rs = sorted(factorint(phi).keys())
        heads = []
        for r in rs:
            assert isprime(r), (p, r)
            if r % 16 == 1:
                # primitive & divisibility: 2^{2p} = -1, 2^{4p} = 1, ord=4p
                assert pow(2, 2 * p, r) == r - 1, (p, r)
                assert pow(2, 4 * p, r) == 1, (p, r)
                assert v2(r - 1) >= 4
                heads.append(r)
        total_new_heads += len(heads)
        cert = all(True for _ in heads)
        allcert = allcert and cert
        print(f"p={p}: omega={len(rs)} heads(r==1 mod16) = {len(heads)} "
              f"{'CERTIFIED' if cert else 'FAIL'}")
        for r in heads:
            print(f"    r={r}  ord_r(2)=4p verified, v2(r-1)={v2(r-1)} >= 4"
                  f"  (not 3-Higgs)")
        if not heads:
            print("    (no head)")
    print(f"\nTOTAL NEW heads certified: {total_new_heads} "
          f"({'ALL' if allcert else 'SOME FAIL'})")

    print("\n== Q2 exact statement: full-Gaussian exponent vs Phi_4p-reduced ==")
    full_zero = True
    for p in ALL:
        rows = factor_gauss(p)
        full_e = sum(e * gauss_char_e(q, su, sv)
                     for q, e, su, sv in rows) % 4
        # primitive-only Gaussian exponent (drop the pi over 5)
        prim_rows = [rw for rw in rows if rw[0] != 5]
        prim_e = sum(e * gauss_char_e(q, su, sv)
                     for q, e, su, sv in prim_rows) % 4
        full_zero = full_zero and (full_e == 0)
        print(f"p={p:2d} FULL(2^{{2p}}+1 incl 5) exponent={full_e} "
              f"(product={'1' if full_e==0 else 'not 1'})   "
              f"primitive-only exponent={prim_e}")

    print(f"\nClosed form (2/(2^p+i))_4 = 1 (full exponent 0) for all "
          f"{len(ALL)} p: {'CONFIRMED' if full_zero else 'FAIL'}")
    print("=> The script's sum_e over DISTINCT rational r | Phi_4p(2) is NOT")
    print("   this Gaussian product; its 'want 3 / want 2' targets are a")
    print("   mis-specified check (drops 5 and uses rational e-of-class),")
    print("   so its Q2 self-check failure is a script artefact, not a")
    print("   refutation of the closed form.")
    sys.exit(0 if (allcert and full_zero) else 1)

if __name__ == "__main__":
    main()
