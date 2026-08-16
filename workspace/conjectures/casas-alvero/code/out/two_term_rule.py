"""Test the exact two-term rule for F2 Hasse-CA counterexamples.

Conjecture: x^a (x+1)^{n-a} (monic, degree n, over F2, 0<a<n) is a Hasse-CA
counterexample (satisfies Hasse-CA, not a pure power)  iff  a is a proper
nonempty subset-sum of the set bits of n, i.e. popcount-limited:
   bin(a) is a submask of bin(n)   (all set bits of a occur among set bits of n)
and 1 <= a <= n-1.

Verify over all pairs (n,a) feasible by direct F2 gcd on (x^a)(x+1)^(n-a).
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

# build x^a (x+1)^{n-a} as bit-polynomial over F2
from math import comb
def two_term_bits(a, n):
    # (x+1)^{n-a} has coeff C(n-a,j) mod 2 at x^j
    # times x^a shifts by a. final f = sum_j C(n-a,j) x^{a+j} mod 2
    fb = 0
    for j in range(n - a + 1):
        if comb(n - a, j) % 2 == 1:
            fb |= 1 << (a + j)
    return fb

setbits = lambda n: [1 << k for k in range(n.bit_length()) if (n >> k) & 1]
def submask_of_n(a, n):
    # a uses only set bits of n (and is a submask)
    return (a & ~n) == 0

bad = []
count_rule_true = 0
for n in range(3, 41):
    for a in range(1, n):
        fb = two_term_bits(a, n)
        is_ca = is_ca_f2(fb)
        is_pp = is_pure_f2(fb, n)
        ce = is_ca and not is_pp
        predict = (1 <= a <= n-1) and submask_of_n(a, n)
        if ce != predict:
            bad.append((n, a, ce, predict))
print(f"tested two-term all (n,a) n=3..40; mismatches: {len(bad)}")
for row in bad[:30]:
    print("  MISMATCH", row)
print("OK" if not bad else "FAIL")

# count two-term counterexamples per n and compare to 2^pc - 2
print("\nn  pc  two-term-ce  2^pc-2  (submask-count)")
for n in range(3, 41):
    pc = bin(n).count("1")
    cnt = sum(1 for a in range(1, n) if submask_of_n(a, n))
    pred = 2**pc - 2
    tag = "OK" if cnt == pred else "X"
    if cnt != pred:
        print(f"{n:2d}  {pc}  {cnt:6d}     {pred:6d}   {tag}")
print("(rows printed only when != 2^pc - 2)")
