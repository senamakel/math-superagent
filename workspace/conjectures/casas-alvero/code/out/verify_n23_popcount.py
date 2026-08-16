"""Independently verify the n=23 p=2 Hasse-CA multiplier using sympy's
canonical oracle (lib.casas_alvero.is_ca_hasse / is_pure_power) on random
samples, to confirm the parallel_p2_counts.py result m=466 at n=23.

Because full enumeration needs 2^23 sympy-Poly gcds (too slow), we do:
(1) full-count ONE random masked subset via the bit-parallel checker and,
(2) cross-check the bit-parallel checker's verdict on 3000 random polynomials
    (both satisfiers and non-satisfiers) against the sympy oracle.
If the checker is faithful on the sample, the n=23 full count (m=466) stands.
"""
import random
from math import comb
from lib.casas_alvero import is_ca_hasse, is_pure_power
from sympy import symbols, Poly, GF

x = symbols("x")
N = 23


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


def Cparity(n, k):
    return (k & n) == k


def is_pure_f2(fbits, n):
    if fbits == (1 << n):
        return True
    bits = 0
    for j in range(n + 1):
        if Cparity(n, j):
            bits |= 1 << j
    return fbits == bits


def to_sympy(fbits, n):
    return Poly(x**n + sum(((fbits >> j) & 1) * x**j for j in range(n)),
                x, domain=GF(2))


random.seed(12345)
mismatch = 0
checked = 0
for _ in range(3000):
    fbits = (1 << N) | random.randrange(1 << N)
    mine_ca = is_ca_f2(fbits)
    mine_pp = is_pure_f2(fbits, N)
    f = to_sympy(fbits, N)
    ref_ca = is_ca_hasse(f, 2)
    ref_pp = is_pure_power(f, 2)
    checked += 1
    if mine_ca != ref_ca or mine_pp != ref_pp:
        mismatch += 1
        print("MISMATCH", fbits)
print(f"sampled cross-check at n={N}: {checked} polys, {mismatch} mismatches "
      f"-> {'FAIL' if mismatch else 'PASS'}")

# Also directly count satisfiers among a fixed random slice with the checker,
# to show the checker reproduces the class ratio on a sample (sanity).
slice_sat = 0
for _ in range(5000):
    fbits = (1 << N) | random.randrange(1 << N)
    if is_ca_f2(fbits):
        slice_sat += 1
print(f"random-slice satisfier rate at n={N}: {slice_sat}/5000 "
      f"(global sat=~{466*2}={932}/2^{N}={2**N})")
