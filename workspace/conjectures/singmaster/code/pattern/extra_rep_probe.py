"""Probe for EXTRA reps (beyond the two family mirrors + trivial) in the
Singmaster N>=6 family, cheaply.

Family: n_i = F_{2i+2}F_{2i+3}-1, k_i = F_{2i}F_{2i+3}-1, a_i = C(n_i+1,k_i+1).
Known reps: (n_i+1,k_i+1), (n_i,k_i+2) [two family mirrors] + trivial (a_i,1),(a_i,a_i-1).
i=1 (3003) has ONE extra canonical rep (78,2) -> N=8.  All i>=2 computed so far
have exactly these 6 -> N=6.

This program cheaply chases the most likely *small-column* extra reps that could
grow the boundary count for large i.  It is NOT a full scan (that is done by
code/pattern/extend_exact_N_family.py up to i=5); it targets:
  (a) does 8*a_i+1 square (a k=2 rep C(x,2)=a_i in column 2) ever appear for i>=2?
  (b) columns k=3..8 : for each, does C(N,k)=a_i have an integral solution N?
        (binary search in N, exact integer arithmetic)
  (c) first falsifying i for any of these.

Convention: N(a) counts both mirrors + trivial (matches witnesses.json).
Only the family construction's two interior pairs are the "guaranteed" reps;
anything extra found here is a genuine additional occurrence.
"""
import math
import gmpy2

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def family_a(i):
    n = fib(2*i+2) * fib(2*i+3) - 1
    k = fib(2*i) * fib(2*i+3) - 1
    return math.comb(n+1, k+1), n, k

import sys
sys.set_int_max_str_digits(0)
print("=== (a) column-2 rep test: C(x,2)=a_i  <=>  8*a_i+1 is a perfect square ===")
print("%3s %10s %6s" % ("i", "a bits", "sq+odd"))
for i in range(1, 13):
    a, n, k = family_a(i)
    cand = 8*a + 1
    r = gmpy2.isqrt(cand)
    sq = r*r == cand
    # a k=2 rep exists iff 8a+1 is a square AND sqrt is odd (x odd)
    odd = (r % 2 == 1)
    print("%3d %10d %6s" % (i, a.bit_length(), sq and odd))

print()
print("=== (b) columns k=3..8: does any C(N,k)=a_i have integral N? ===")
print("     (a 'FOUND' row is an extra rep; none expected from the full scans i<=5)")
def rep_in_column(a, k):
    # solve C(N,k)=a for integer N>=2k ; binary search
    kfact = math.factorial(k)
    hi = k - 1 + gmpy2.iroot(kfact * a, k)[0] + 2
    while math.comb(hi, k) < a:
        hi <<= 1
    lo = 0
    while lo + 1 < hi:
        mid = (lo + hi) >> 1
        if math.comb(mid, k) <= a:
            lo = mid
        else:
            hi = mid
    if math.comb(lo, k) == a:
        return lo
    return None

for i in range(2, 9):
    a, n, k = family_a(i)
    hits = [(kk, rep_in_column(a, kk)) for kk in range(3, 9)]
    found = [(kk, N) for (kk, N) in hits if N is not None]
    status = ("EXTRA REP col=%r"%found) if found else "none"
    print("i=%d a_bits=%d n=%d k=%d  small columns k=3..8: %s" % (i, a.bit_length(), n, k, status))
print()
print("NOTE: full-scan exact counts (code/out/extend_exact_N_family_i*.captured.txt) already gave")
print("N(a_i)=6 for i=2..5 (no extra rep in ANY column).  This probe only cheaply checks the")
print("most likely extra-rep columns for i=2..8 (incl. the k=2 archetype) and the whole family i=1..12 for k=2.")
