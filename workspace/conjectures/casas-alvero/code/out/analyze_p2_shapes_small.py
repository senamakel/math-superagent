"""Shape analysis of F2 Hasse-CA counterexamples restricted to small n where
single-threaded enumeration is fast (n <= 14 for popcount classes; n=15 allowed).

Question: for popcount-2 n the counterexamples are exactly x^a(x+1)^{n-a}
with a a set-bit power.  Count two-term (x^a+x^n) counterexamples per n and
report the a-values to see the set-bit pattern.
"""
from math import comb

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

def two_term(fbits, n):
    return sum(1 for j in range(n + 1) if (fbits >> j) & 1) == 2

def analyze(n):
    ces = []
    for v in range(1 << n):
        fb = (1 << n) | v
        if is_ca_f2(fb) and not is_pure_f2(fb, n):
            ces.append(fb)
    twoterm = [fb for fb in ces if two_term(fb, n)]
    avals = sorted(min(j for j in range(n) if (fb >> j) & 1) for fb in twoterm)
    setbits = [1 << k for k in range(n.bit_length()) if (n >> k) & 1]
    print(f"n={n:2d} pc={bin(n).count('1')} ce={len(ces)} two-term={len(twoterm)} "
          f"a={avals} setbits={setbits}")

if __name__ == "__main__":
    # only small n: enumeration <= 2^15
    for n in range(3, 16):
        if bin(n).count("1") <= 4:
            analyze(n)
