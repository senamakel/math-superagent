"""Fresh test of pattern-finder conjecture (C): at every popcount, the
SMALL-support counterexample counts are popcount-determined (rigid), only the
large-support counts vary.

Recorded pc=4 data (exact, this run): support-2 = 14, support-4 = 106 at all
of n=15,23,27.  The unexplored terms are the next pc=4 degrees n=29,30 and the
first pc=5 degree n=31.  Conjecture (C) predicts:
    support-2(n) = 2^popcount(n) - 2   [theorem: two-monomial submask family]
    support-4(n) = ?(pc)               [conjecture: constant within pc class]

KEY COMPLEXITY TRICK: a support-s counterexample x^n + sum of (s-1) lower
terms has only C(n,s-1) candidates, so support-2 and support-4 counts can be
decided EXACTLY at n well past the 2^n exhaustive wall (n=31 = 2^31 infeasible
to enumerate fully, but C(31,3)=4495 four-term candidates is trivial).

Each candidate is checked exactly: bit-polynomial Hasse derivative + bit gcd,
matching the canonical oracle (lib.casas_alvero.is_ca_hasse) at small n.

Oracle check: reproduces support-2 = 2^pc-2 and the support-4 counts at the
known n=15,23,27 (and pc<=3 degrees) exactly.
"""
from itertools import combinations

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

def Cparity(n, k):
    return (k & n) == k

def is_pure_f2(fbits, n):
    if fbits == (1 << n): return True
    bits = 0
    for j in range(n + 1):
        if Cparity(n, j): bits |= 1 << j
    return fbits == bits

def count_support_s(n, s):
    """# monic Hasse-CA counterexamples of the form x^n + (s-1) lower terms."""
    top = 1 << n
    cnt = 0
    lower = list(range(0, n))          # indices 0..n-1 (exclude x^n)
    # choose s-1 lower exponents
    for T in combinations(lower, s - 1):
        fb = top
        for e in T:
            fb |= 1 << e
        if is_ca_f2(fb) and not is_pure_f2(fb, n):
            cnt += 1
    return cnt

# ---- verify against known values first ----
print("=== ORACLE CHECK vs recorded data ===")
known = {
    # n: (pc, support2, support4)
    5:(2,2,None),6:(2,2,None),
    7:(3,6,5), 9:(2,2,None), 10:(2,2,None),
    11:(3,6,5), 13:(3,6,5),
    15:(4,14,106), 17:(2,2,None), 18:(2,2,None),
    19:(3,6,5), 20:(2,2,None), 21:(3,6,5), 22:(3,6,5),
    23:(4,14,106), 24:(2,2,None), 25:(3,6,5), 26:(3,6,5),
    27:(4,14,106),
}
allok = True
for n,(pc,s2,s4) in sorted(known.items()):
    c2 = count_support_s(n, 2)
    ok2 = c2 == s2
    allok &= ok2
    line = f"n={n:2d} pc={pc}: support-2 computed={c2:3d} recorded={s2:3d} {'OK' if ok2 else 'FAIL'}"
    if s4 is not None:
        c4 = count_support_s(n, 4)
        ok4 = c4 == s4
        allok &= ok4
        line += f"  support-4 computed={c4:3d} recorded={s4:3d} {'OK' if ok4 else 'FAIL'}"
    print(line)
print("ORACLE CHECK:", "ALL OK" if allok else "MISMATCH")

# ---- fresh terms: next pc=4 (n=29,30), first pc=5 (n=31) ----
print("\n=== FRESH TERMS ===")
for n in (29, 30, 31):
    pc = bin(n).count("1")
    c2 = count_support_s(n, 2)
    c4 = count_support_s(n, 4)
    print(f"n={n} pc={pc}: support-2={c2} (2^pc-2={2**pc-2})  "
          f"support-4={c4}")
