"""Shape comparison of F2 Hasse-CA counterexamples at n=15 and n=23 (both pc=4).

m differs: 457 (n=15) vs 466 (n=23).  Question: what counterexample shape
accounts for the 9 extra at n=23?  Count counterexamples by monomial-support
size, and by the a-values of two-term x^a(x+1)^{n-a} forms (if any).
Also count ce = 2(m-1): n=15 -> 912, n=23 -> 930; i.e. 18 more ce at n=23
(466-457 = 9 more m <-> 18 more ce).  Report the two-term a-value multiset.
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

def Cparity(n, k):
    return (k & n) == k

def is_pure_f2(fbits, n):
    if fbits == (1 << n): return True
    bits = 0
    for j in range(n + 1):
        if Cparity(n, j): bits |= 1 << j
    return fbits == bits

def support(fbits):
    return [j for j in range(fbits.bit_length()) if (fbits >> j) & 1]

def analyze(n):
    ces = []
    for v in range(1 << n):
        fb = (1 << n) | v
        if is_ca_f2(fb) and not is_pure_f2(fb, n):
            ces.append(fb)
    sz = Counter(len(support(fb)) for fb in ces)
    twoterm = [fb for fb in ces if len(support(fb)) == 2]
    avals = sorted(min(j for j in range(n) if (fb >> j) & 1) for fb in twoterm)
    print(f"n={n} pc={bin(n).count('1')} ce={len(ces)} "
          f"m={(len(ces)//2)+1}")
    print(f"   ce by support-size: {dict(sorted(sz.items()))}")
    print(f"   two-term a-values ({len(twoterm)}): {avals}")
    setbits = [1 << k for k in range(n.bit_length()) if (n >> k) & 1]
    print(f"   setbits of n: {setbits}")

if __name__ == "__main__":
    for n in (15, 23):
        analyze(n)
