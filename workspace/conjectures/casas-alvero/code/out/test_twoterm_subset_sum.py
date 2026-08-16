"""Test the two-term subset-sum law for F2 Hasse-CA counterexamples.

Conjecture: Let n have binary set-bits B (n = sum_{b in B} 2^b, |B| = k >= 1).
Among the F2 monic degree-n polynomials that satisfy Hasse-CA, a polynomial
x^a + x^n (exactly two monomials) is a *counterexample* (satisfies but is not
a pure power) IFF a is a proper nonempty subset-sum of B (i.e. a ranges over
the 2^k - 2 strict subset-sums of the set-bits).

This is verified by full enumeration for n <= 15 (n=3..15, all popcount
classes) in analyze_p2_shapes_small.py.  Here we test the law for much larger
n (up to 55) with a TARGETED check (no full enumeration): for each n, check
every candidate subset-sum a AND every non-candidate a in 2..n-1, verifying
x^a+x^n is / is not a counterexample respectively.  That is O(n) poly-time
Hasse-CA tests per n, feasible far past the 2^n enumeration bound.
"""
from math import comb
from itertools import combinations

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
        if hi == 0:
            continue
        if pgcd(fbits, hi) == 1:
            return False
    return True

def is_pure_f2(fbits, n):
    if fbits == (1 << n):
        return True
    bits = 0
    for j in range(n + 1):
        if comb(n, j) % 2 == 1:
            bits |= 1 << j
    return fbits == bits

def subset_sums(B):
    """Proper nonempty subset-sums of set B of powers of two."""
    B = list(B)
    sums = set()
    for k in range(1, len(B)):
        for c in combinations(B, k):
            sums.add(sum(c))
    return sums

def main(nmax):
    ok = True
    for n in range(3, nmax + 1):
        if n == 2:  # base case, skip
            continue
        B = {1 << i for i in range(n.bit_length()) if (n >> i) & 1}
        cand = subset_sums(B)
        for a in range(1, n):
            # x^a + x^n
            fbits = (1 << n) | (1 << a)
            is_ce = is_ca_f2(fbits) and not is_pure_f2(fbits, n)
            expect = (a in cand)
            if is_ce != expect:
                print(f"BREAK n={n} B={sorted(B)} a={a} "
                      f"candidate={a in cand} is_counterexample={is_ce}")
                ok = False
    print("ALL MATCH the subset-sum law" if ok else "MISMATCH FOUND")
    return ok

if __name__ == "__main__":
    import sys
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 55
    main(nmax)
