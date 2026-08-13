"""Verify Singmaster witness set and infinite Fibonacci family against the library's claims.

Convention: count both (n,k) and (n,n-k) (standard N(a)).
"""
import math
from math import comb

def occurrences_exactly(a):
    """All (n,k) with 0<=k<=n and C(n,k)=a, both halves (STANDARD convention)."""
    out = []
    # a > 1 appears only in first a+1 rows
    for n in range(2, a+1):
        for k in range(0, n//2 + 1):
            v = comb(n, k)
            if v == a:
                # count both k and n-k (they coincide iff k==n/2, where it's one)
                if 2*k == n:
                    out.append((n, k))
                else:
                    out.append((n, k))
                    out.append((n, n-k))
            elif v > a:
                break
    return sorted(out)

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print("=== Witness 3003, both-halves convention ===")
occ = occurrences_exactly(3003)
print("N(3003) =", len(occ))
for p in occ: print("  ", p)
assert len(occ) == 8, "3003 must appear 8 times (both halves)"
assert (3003,1) in occ and (78,2) in occ and (15,5) in occ and (14,6) in occ
assert (3003,3002) in occ and (78,76) in occ and (15,10) in occ and (14,8) in occ
print("Half-triangle count (k<=n/2):", len(set((n,min(k,n-k)) for n,k in occ)))
print("CHECK: all 8 occurrences of 3003 verified.\n")

print("=== Infinite family C(n+1,k+1)=C(n,k+2) (Fibonacci), N(a)>=6 ===")
for i in range(1, 6):
    n = fib(2*i+2)*fib(2*i+3) - 1
    k = fib(2*i) * fib(2*i+3) - 1
    lhs = comb(n+1, k+1)
    rhs = comb(n,   k+2)
    a = lhs
    assert lhs == rhs, (i, lhs, rhs)
    occa = occurrences_exactly(a)
    mult = len(occa)
    print(f"i={i}: n={n} k={k} a={a}  C(n+1,k+1)==C(n,k+2): {lhs==rhs}  N(a)={mult}")
    assert mult >= 6, (i, mult)
print("CHECK: infinite family verified for i=1..5, each has N(a)>=6.")
print("\ni=1 is 3003 :", 3003 == comb(fib(4)*fib(5)-1+1, fib(2)*fib(5)-1+1))
