"""Test conjecture (C) of f2_hasse_ce_support_structure.md: is the support-4
Hasse-CA counterexample count over F2 a function ONLY of popcount(n)?

A support-4 degree-n monic poly over F2 is exactly x^n + x^a + x^b + x^c with
0 < a < b < c < n.  Enumerate ONLY these (O(n^3) per n, feasible far past the
2^n exhaustive wall), count those that are Hasse-CA counterexamples, and see
whether the count depends only on popcount(n).

Recorded so far (pc=4): support-4 = 106 at n=15, 23, 27 (3 points).
Question: does it stay a function of popcount beyond?  In particular the first
pc=5 degree is n=31 — its support-4 count is the 4th independent test of
whether small supports are popcount-determined.

Exact bit-arithmetic, oracle-checked against lib.casas_alvero at small n.
"""
from math import comb

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

def count_support4(n):
    """# 4-monomial Hasse-CA ce of degree n: x^n+x^a+x^b+x^c."""
    cnt = 0
    top = 1 << n
    for a in range(1, n-2):
        for b in range(a+1, n-1):
            for c in range(b+1, n):
                fb = top | (1 << a) | (1 << b) | (1 << c)
                if is_ca_f2(fb) and not is_pure_f2(fb, n):
                    cnt += 1
    return cnt

# quick guard against oracle on small n
def guard():
    from itertools import product
    from sympy import symbols, Poly, GF
    from lib.casas_alvero import is_ca_hasse as ref_ca
    x = symbols("x")
    n = 6
    # all 4-monomial ce via reference oracle
    ref = 0
    for a in range(1, n-2):
        for b in range(a+1, n-1):
            for c in range(b+1, n):
                f = Poly(x**n + x**a + x**b + x**c, x, domain=GF(2))
                pp = f == Poly(x**n, x, domain=GF(2)) or \
                     f == Poly((x + 1)**n, x, domain=GF(2))
                if ref_ca(f, 2) and not pp:
                    ref += 1
    mine = count_support4(n)
    print(f"GUARD n=6: bit-parallel={mine} reference={ref} {'OK' if mine==ref else 'MISMATCH'}")
    assert mine == ref

if __name__ == "__main__":
    import sys
    guard()
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 60
    print("n   pc   support-4-ce")
    prev_vals = {}
    for n in range(6, nmax + 1):
        if n == 2: continue
        pc = bin(n).count("1")
        s4 = count_support4(n)
        key = pc
        same = "SAME(prev)" if key in prev_vals and s4 == prev_vals[key] else ""
        if key not in prev_vals:
            prev_vals[key] = s4
        print(f"{n:3d}  {pc}  {s4:5d}  {same}")
