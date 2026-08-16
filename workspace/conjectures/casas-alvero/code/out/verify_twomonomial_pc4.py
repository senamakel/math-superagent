"""Verify the exact two-monomial submask law at the pc=4 degrees n=15,23,27:
THEOREM being checked (already proved n=3..40): x^a+x^n is an F2 Hasse-CA
counterexample iff a is a proper nonempty submask of n (count 2^pc - 2).

Independent route here: exact bit-polynomial Hasse-CA, listing which a give a
counterexample and comparing to the submask set at these three pc=4 degrees."""
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

def Cparity(n, k):
    return (k & n) == k

def is_pure_f2(fbits, n):
    if fbits == (1 << n): return True
    bits = 0
    for j in range(n + 1):
        if Cparity(n, j): bits |= 1 << j
    return fbits == bits

def two_monomial(a, n):
    return (1 << n) | (1 << a)   # x^n + x^a

def submask(n, a):
    return (a & ~n) == 0

for n in (15, 23, 27):
    pc = bin(n).count("1")
    submasks = [a for a in range(1, n) if submask(n, a)]
    # actual counterexamples among x^a+x^n
    ces = [a for a in range(1, n)
           if is_ca_f2(two_monomial(a, n)) and not is_pure_f2(two_monomial(a, n), n)]
    match = sorted(submasks) == sorted(ces)
    print(f"n={n:2d} pc={pc} 2^pc-2={2**pc-2}  submask={len(submasks)}  "
          f"actual-ce={len(ces)}  match={match}")
    if not match:
        print("   submasks-not-ce:", sorted(set(submasks)-set(ces)))
        print("   ce-not-submask:", sorted(set(ces)-set(submasks)))
