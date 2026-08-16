"""Match family-law counterexamples against the full Hasse-CA ce set per n.

Family F(a,n) = x^a (x+1)^{n-a} over F2 is a ce iff a submask of n (verified
elsewhere n=3..40).  Count |{F(a,n): a submask, 1<=a<=n-1}| = 2^pc - 2 per n,
and compare to total |ce| and the number captured by the family (they are all
distinct?).
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

def family_bits(a, n):
    fb = 0
    for j in range(n - a + 1):
        if comb(n - a, j) % 2 == 1: fb |= 1 << (a + j)
    return fb

for n in range(3, 25):
    pc = bin(n).count("1")
    ce_set = set()
    for v in range(1 << n):
        fr = (1 << n) | v
        if is_ca_f2(fr) and not is_pure_f2(fr, n):
            ce_set.add(fr)
    # family set from submasks
    fam = set()
    for a in range(1, n):
        if (a & ~n) == 0:
            fam.add(family_bits(a, n))
    in_fam = sum(1 for fb in ce_set if fb in fam)
    fam_values = 2**pc - 2
    print(f"n={n:2d} pc={pc} |ce|={len(ce_set):4d} family-values={fam_values:4d} "
          f"ce-captured-by-family={in_fam:4d} "
          f"family-exhaustive={'YES' if len(ce_set)==in_fam else 'no'}")
