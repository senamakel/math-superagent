"""Test the set-bit hypothesis for the F2 Hasse-CA counterexamples.

For popcount-2 n (n = 2^b + 2^c), the counterexamples are conjectured to be
exactly x^a (x+1)^{n-a} for a in {set bits of n as powers} = {2^b, 2^c}.

Generalize and test: are ALL counterexamples of the form x^a (x+1)^{n-a}
for some a?  And which a values occur per popcount class?  Count how many
distinct a occur and whether that explains m(n,2).

m(n,2)=1,2,8 for popcount 1,2,3 (observed).  ce = 2(m-1): pc1->0, pc2->2,
pc3->14.  If all counterexamples were x^a(x+1)^{n-a}, pc2 would give exactly
2 (a = 2 set bits) -> matches!  pc3 would give 3 -> but observed ce=14, so
pc3 has 14 distinct shapes, more than 3.  So the elemental form is only the
pc<=2 story.
"""
from lib.casas_alvero import is_ca_hasse, is_pure_power
from sympy import symbols, Poly, GF
from math import comb

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
    bits = 0
    for j in range(n + 1):
        if comb(n, j) % 2 == 1:
            bits |= 1 << j
    return fbits == bits


def two_term(fbits, n):
    """True if f = x^a + x^b = x^min(x^{diff}+1) i.e. has exactly 2 monomials."""
    bits = [j for j in range(n + 1) if (fbits >> j) & 1]
    return len(bits) == 2


def analyze(n):
    ces = []
    for v in range(1 << n):
        fb = (1 << n) | v
        if is_ca_f2(fb) and not is_pure_f2(fb, n):
            ces.append(fb)
    twoterm = [fb for fb in ces if two_term(fb, n)]
    # extract 'a' index for two-term x^a + x^n (the lower exponent)
    avals = sorted((min(j for j in range(n) if (fb >> j) & 1) for fb in twoterm))
    print(f"n={n:2d} popcount={bin(n).count('1')}: ce={len(ces)} "
          f"two-term={len(twoterm)} a-values={avals}  setbits={[1<<k for k in range(n.bit_length()) if (n>>k)&1]}")


if __name__ == "__main__":
    for n in range(3, 31):
        if 2 ** n > (1 << 28):
            break
        if bin(n).count("1") <= 3 or n in (15, 23, 27):
            analyze(n)
