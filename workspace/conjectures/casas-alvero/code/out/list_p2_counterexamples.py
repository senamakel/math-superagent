"""List the actual Hasse-CA monic polynomials over F2 (both pure powers and
counterexamples) for small n, to find the structural form behind m(n,2).

A monic F2 deg-n poly as int (bit j = coeff of x^j, bit n = 1).  Hasse-CA iff
gcd(f, H_i) non-constant for all i=1..n-1 (vanishing H_i passes).
"""
from lib.casas_alvero import is_ca_hasse, is_pure_power
from sympy import symbols, Poly, GF

x = symbols("x")


def hasse_deriv(fbits, i):
    out = 0
    j = 0
    fb = fbits
    while fb:
        if fb & 1:
            if (i & j) == i:
                out |= 1 << (j - i)
        fb >>= 1
        j += 1
    return out


def pmod(a, b):
    bl = b.bit_length()
    while a.bit_length() >= bl:
        a ^= b << (a.bit_length() - bl)
    return a


def pgcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    while b:
        a, b = b, pmod(a, b)
    return a


def is_ca_f2(fbits):
    n = fbits.bit_length() - 1
    for i in range(1, n):
        hi = hasse_deriv(fbits, i)
        if hi == 0:
            continue
        if pgcd(fbits, hi) == 1:
            return False
    return True


def is_pure_f2(fbits, n):
    if fbits == (1 << n):
        return True
    from math import comb
    bits = 0
    for j in range(n + 1):
        if (comb(n, j) % 2) == 1:
            bits |= 1 << j
    return fbits == bits


def show(n):
    print(f"=== n={n} (popcount={bin(n).count('1')}) over F2 ===")
    cepoly = []
    pure = []
    for v in range(1 << n):
        fb = (1 << n) | v
        if is_ca_f2(fb):
            if is_pure_f2(fb, n):
                pure.append(fb)
            else:
                cepoly.append(fb)
    print(f"  pure powers: {len(pure)}")
    print(f"  counterexamples (not pure powers): {len(cepoly)}")
    # factor each counterexample over F2
    for fb in cepoly:
        expr = x**n + sum(((fb >> j) & 1) * x**j for j in range(n))
        f = Poly(expr, x, domain=GF(2))
        cs = f.factor_list()
        facts = "*".join(f"({str(g).replace(chr(39),'')})^{k}" for g, k in cs[1])
        print(f"    ce: {str(expr)} = {facts}")


if __name__ == "__main__":
    for n in (3, 5, 6, 7, 9, 10, 11, 15):
        show(n)
