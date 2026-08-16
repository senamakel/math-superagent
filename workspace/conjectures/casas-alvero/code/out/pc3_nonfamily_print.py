"""Print the actual non-family pc=3 F2 Hasse-CA ce polynomials, factored."""
import sys
from math import comb
from sympy import symbols, Poly, GF

x = symbols("x")

def hasse_deriv(fbits, i):
    out = 0; j = 0; fb = fbits
    while fb:
        if fb & 1:
            if (i & j) == i: out |= 1 << (j - i)
        fb >>= 1; j += 1
    return out

def pmod(a, b):
    bl = b.bit_length()
    while a.bit_length() >= bl:
        a ^= b << (a.bit_length() - bl)
    return a

def pgcd(a, b):
    if a == 0: return b
    if b == 0: return a
    while b:
        a, b = b, pmod(a, b)
    return a

def is_ca_f2(fbits):
    n = fbits.bit_length() - 1
    for i in range(1, n):
        hi = hasse_deriv(fbits, i)
        if hi == 0: continue
        if pgcd(fbits, hi) == 1: return False
    return True

def is_pure_f2(fbits, n):
    if fbits == (1 << n): return True
    bits = 0
    for j in range(n + 1):
        if comb(n, j) % 2 == 1: bits |= 1 << j
    return fbits == bits

def family_bits(a, n):
    fb = 0
    for j in range(n - a + 1):
        if comb(n - a, j) % 2 == 1: fb |= 1 << (a + j)
    return fb

def support(fb):
    return [j for j in range(fb.bit_length()) if (fb >> j) & 1]

for n in (7, 21):
    fam = set(family_bits(a, n) for a in range(1, n) if (a & ~n) == 0)
    nonfam = []
    for v in range(1 << n):
        fr = (1 << n) | v
        if is_ca_f2(fr) and not is_pure_f2(fr, n) and fr not in fam:
            nonfam.append(fr)
    print(f"=== n={n} pc=3, non-family ce: {len(nonfam)} ===")
    for fb in nonfam:
        expr = x**n + sum(((fb >> j) & 1) * x**j for j in range(n))
        f = Poly(expr, x, domain=GF(2))
        cs = f.factor_list()
        facts = ".".join(f"({str(g).replace(chr(39),'')})^{k}" for g, k in cs[1])
        print(f"   support={support(fb)}: {expr} = {facts}")
