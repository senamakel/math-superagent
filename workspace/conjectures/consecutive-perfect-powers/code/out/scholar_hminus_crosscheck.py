"""sympy-exact twin of the mpmath verification of the relative class number
formula h^-(Q(zeta_p)) = 2p * prod_{chi odd mod p} (-1/2 * B_{1,chi}),
B_{1,chi} = (1/p) sum_{a=1}^{p-1} chi(a) a.  This is a THIRD independent route
to the already-checked h^- values, using exact rational/cyclotomic arithmetic
rather than high-precision mpmath (see code/out/hminus_exact.py and
code/out/verify_claims.py for the other two).

Characters: g a primitive root mod p, chi_k(g^e) = exp(2 pi i k e/(p-1)),
k odd (odd character).  With exp(2 pi i /(p-1)) represented as the sympy
I-root of unity, the product lands in Q(zeta_(p-1)) and the imaginary part
cancels; we read off the real part as the exact integer.

Known values (OEIS A061653 / Washington): p=3->1,...,43->211.
"""
from sympy import Rational, exp, I, pi, expand, nsimplify

KNOWN = {3:1, 5:1, 7:1, 11:1, 13:1, 17:1, 19:1, 23:3, 29:8, 31:9,
         37:37, 41:121, 43:211}

def primitive_root(p):
    n = p - 1
    prime_divs = []
    d = 2; m = n
    while d * d <= m:
        if m % d == 0:
            prime_divs.append(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        prime_divs.append(m)
    for g in range(2, p):
        if all(pow(g, n // r, p) != 1 for r in prime_divs):
            return g
    raise ValueError("no primitive root")

def rel_class_number(p):
    g = primitive_root(p)
    logtab = {}
    v = 1
    for e in range(p - 1):
        logtab[v] = e
        v = (v * g) % p
    rho = exp(2 * I * pi / (p - 1))          # generator of (p-1)-th roots
    total = Rational(2) * p
    for k in range(1, p - 1, 2):             # odd characters
        s = sum(rho ** (k * logtab[a]) * Rational(a) for a in range(1, p))
        B1 = s / p
        total *= (-Rational(1) / 2) * B1
    # total is a Gaussian rational (imag part 0); read real part, cleanly.
    real = expand(total).as_real_imag()[0]
    return nsimplify(real)

ok = True
for p, known in KNOWN.items():
    try:
        val = rel_class_number(p)
        good = (val == known)
        ok = ok and good
        print(f"p={p:3d}  h^- computed = {val!s:>8}   known={known:>5}   match={good}")
    except Exception as e:
        print(f"p={p:3d}  ERROR {type(e).__name__}: {e}")
print("ALL MATCH:", ok)
