"""Classify the pc=3 Hasse-CA ce that are NOT in the two-term family.

At pc=3, |ce|=14, family captures 6 = 2^3-2, leaving 8.  The naive law m=p was
'2^(pc-1)=...' no.  What are these 8?  Count by support size and by the
high-multiplicity root-0 vs root-1 structure.
Also count ce not captured by family across all n<=24 to see family captures
exactly 2^pc - 2 of them.
"""
from math import comb
from collections import Counter

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

def multiplicity_of_root(fb, root1):
    # root 1 iff f(1)=0 i.e. sum of coeffs even; multiplicity = v of f at root
    # easier: count how many hasse derivatives vanish at the root
    n = fb.bit_length() - 1
    def evald(fb, r):
        # f(r) mod 2
        s = 0
        for j in range(fb.bit_length()):
            if (fb >> j) & 1: s ^= (r**j) & 1
        return s
    return None  # not needed

for n in range(7, 25):
    if bin(n).count("1") != 3:
        continue
    fam = set(family_bits(a, n) for a in range(1, n) if (a & ~n) == 0)
    nonfam = []
    for v in range(1 << n):
        fr = (1 << n) | v
        if is_ca_f2(fr) and not is_pure_f2(fr, n) and fr not in fam:
            nonfam.append(fr)
    sz = Counter(len(support(fb)) for fb in nonfam)
    # check both roots 0 and 1 present (x and x+1 divide f)?
    with_root0 = sum(1 for fb in nonfam if (fb & 1) == 0)   # coeff of x^0 = 0 => f(0)=0
    with_root1 = sum(1 for fb in nonfam if sum((fb>>j)&1 for j in range(fb.bit_length())) % 2 == 0)
    print(f"n={n:2d} pc=3 non-family-ce={len(nonfam)} "
          f"by-support={dict(sorted(sz.items()))} root0={with_root0} root1={with_root1}")
