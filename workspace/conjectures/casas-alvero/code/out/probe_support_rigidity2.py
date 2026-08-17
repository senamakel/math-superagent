"""Push the small-support rigidity conjecture (C) across more popcount classes.

Recorded (this run): support-2 = 2^pc-2 (theorem); support-4 = 5 at pc=3,
106 at pc=4 (n=15,23,27,29,30), 1465 at pc=5 (n=31).  Conjecture: support-4 is
a function of popcount only.  Test at dtmore pc=5 degrees (n=47,55,59) and
the first pc=6 degree (n=63), plus more pc=3 degrees.  Each support-s count is
C(n,s-1) candidates — cheap at these n.
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
    top = 1 << n
    cnt = 0
    for T in combinations(range(0, n), s - 1):
        fb = top
        for e in T: fb |= 1 << e
        if is_ca_f2(fb) and not is_pure_f2(fb, n):
            cnt += 1
    return cnt

# n ranges: pc=3 degrees 35,37,38; pc=5: 47,55,59,61; pc=6: 63
import sys
nlist = [int(x) for x in sys.argv[1].split(",")]
for n in nlist:
    pc = bin(n).count("1")
    c2 = count_support_s(n, 2)
    c4 = count_support_s(n, 4)
    print(f"n={n} pc={pc}: support-2={c2} (2^pc-2={2**pc-2})  support-4={c4}", flush=True)
