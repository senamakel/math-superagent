"""Minimal reproduction of why the corrected DFS drops n = 26208.

n = 26208 = 2^5 * 3^2 * 7 * 13, sigma = 91728, abundancy = 7/2, so it IS a
valid hemiperfect number that brute.py finds but solution.py misses.

The DFS that reaches it needs primes introduced in order 2,3,7,13.  We show
that at the node Q = 16/13 (after 2^5 * 3^2) the 'forced' prime is d=13, and
the branch `if p < d: continue` makes the traversal skip p=7, so it can only
add 13 first and then cannot come back to 7 (monotone index pointer) -- a dead
end.  This is the bug: smaller non-denominator primes must remain available
below the forced prime.
"""
from math import gcd

def sigma_pe(p, e):
    return (p ** (e + 1) - 1) // (p - 1)

def step(r, n, num, den, p, e):
    pe = p ** e
    n2 = n * pe
    sp = sigma_pe(p, e)
    num2 = num * pe
    den2 = den * sp
    g = gcd(num2, den2)
    return n2, num2 // g, den2 // g

# state after 2^5 * 3^2 within target r=7/2
n, num, den = 1, 7, 2
n, num, den = step(7, n, num, den, 2, 5)
n, num, den = step(7, n, num, den, 3, 2)
print("after 2^5*3^2: n=%d Q=%d/%d" % (n, num, den))
assert (n, num, den) == (288, 16, 13)

# forced prime = min prime factor of den = 13
d = min(p for p in range(2, den + 1) if den % p == 0)
print("forced d =", d)

# (A) what solution.py does: forced branch only allows p == d -> add 13 first
nA, numA, denA = step(7, n, num, den, 13, 1)
print("add 13 first: Q=%d/%d -- next forced prime = min factor of den" % (numA, denA))
dA = min(p for p in range(2, denA + 1) if denA % p == 0)
print("   forced d =", dA, "(=7, but pointer already past 7 in an increasing scan)")

# (B) the correct path: add 7 (a smaller prime) before 13
nB, numB, denB = step(7, n, num, den, 7, 1)
print("add 7 first: n=%d Q=%d/%d" % (nB, numB, denB))
nC, numC, denC = step(7, nB, numB, denB, 13, 1)
print("then 13: n=%d Q=%d/%d -> %s" % (nC, numC, denC, "FOUND 26208" if (numC == denC == 1 and nC == 26208) else "FAIL"))

assert (nC, numC, denC) == (26208, 1, 1), "root-cause path should recover 26208"
print("\nRoot cause confirmed: the `if p < d: continue` rule drops p=7. Correct path adds 7 before the forced 13.")
