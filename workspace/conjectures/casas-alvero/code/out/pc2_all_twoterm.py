"""For popcount-2 n over F2: verify that EVERY Hasse-CA counterexample is of the
two-term form x^a (x+1)^{n-a} with a a single set bit of n.

i.e. for n = 2^b + 2^c (pc=2), the p(n-1)=... counterexamples are exactly the
two polys x^{2^b}(x+1)^{2^c} and x^{2^c}(x+1)^{2^b} (after binomial id).
Count ce per n and the two-term ce are both 2 = 2^2 - 2.
"""
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
    from math import comb
    bits = 0
    for j in range(n + 1):
        if comb(n, j) % 2 == 1: bits |= 1 << j
    return fbits == bits

def twoterm_bits(a, n):
    from math import comb
    fb = 0
    for j in range(n - a + 1):
        if comb(n - a, j) % 2 == 1: fb |= 1 << (a + j)
    return fb

def support(fb):
    return [j for j in range(fb.bit_length()) if (fb >> j) & 1]

for n in range(3, 61):
    if bin(n).count("1") != 2:
        continue
    ces = 0; twoterm = 0; non_two_term_shapes = set()
    for v in range(1 << n):
        fr = (1 << n) | v
        if is_ca_f2(fr) and not is_pure_f2(fr, n):
            ces += 1
            s = len(support(fr))
            if s == 2:
                twoterm += 1
            else:
                non_two_term_shapes.add(s)
    # two-term counterexamples predicted = exactly the a = single set bits
    setbits = [1 << k for k in range(n.bit_length()) if (n >> k) & 1]
    pred_two = len(setbits)  # each set bit as 'a'
    # verify each single set bit gives a ce
    gb = 0
    for sbit in setbits:
        fb = twoterm_bits(sbit, n)
        ca = is_ca_f2(fb); pp = is_pure_f2(fb, n)
        if ca and not pp: gb += 1
    ok = (ces == 2) and (twoterm == 2) and (non_two_term_shapes == set()) and (gb == pred_two)
    print(f"n={n:3d} setbits={setbits} ce={ces} two-term={twoterm} "
          f"non-two-term-support-sizes={sorted(non_two_term_shapes)} single-bit-ok={gb==pred_two} -> {'OK' if ok else 'FAIL'}")
