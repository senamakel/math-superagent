"""Independent exact verification of h^-(Q(zeta_p)) = 2p prod_{chi odd} (-1/2 B_{1,chi}).

Fully exact rational-algebraic: character values are exact (p-1)-th roots of
unity represented by sympy exp(I*2*pi/(p-1)); the whole product is built in
exact symbolic arithmetic and the final simplification to a rational is done
by nsimplify on real and imaginary parts. No floating-point anywhere.
"""
from sympy import Rational, I, pi, exp, nsimplify, expand_complex
from sympy import re as sym_re, im as sym_im
from sympy import primitive_root as sp_primitive_root
from sympy import floor

KNOWN = {3:1, 5:1, 7:1, 11:1, 13:1, 23:3, 31:9, 37:37, 43:211}

def hminus_exact(p):
    g = sp_primitive_root(p)
    n = p - 1
    logtab = {}
    v = 1
    for e in range(n):
        logtab[v] = e
        v = (v * g) % p
    zeta = exp(I * 2 * pi / n)           # exact n-th root of unity
    P = 2 * p
    for k in range(1, n, 2):             # odd characters
        s = 0
        for a in range(1, p):
            e = logtab[a]
            s += zeta ** (k * e) * a
        B1 = s / p
        P = P * (Rational(-1, 2) * B1)
    P = expand_complex(P)
    r = nsimplify(sym_re(P), rational=True)
    i = nsimplify(sym_im(P), rational=True)
    return r, i, g


if __name__ == "__main__":
    all_ok = True
    for p in sorted(KNOWN):
        r, i, g = hminus_exact(p)
        ok = (i == 0) and (r == KNOWN[p])
        all_ok = all_ok and ok
        print(f"p={p:3d} root={g}  hmin(claim)={KNOWN[p]:>5}  exact_real={r}  imag={i}  match={ok}")
    print("ALL_MATCH:", all_ok)
