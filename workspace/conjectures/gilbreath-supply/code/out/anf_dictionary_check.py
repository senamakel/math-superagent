#!/usr/bin/env python3
"""Check the ANF (algebraic normal form / Reed-Muller) dictionary for proposal P1.

Claim to check: with g_n(x) = h[n-1-x] for x in [0,n-1], g_n(x)=0 for x>=n,
the ANF coefficient a_d = XOR_{x bitwise-submask of d} g_n(x) equals T(n,d)
= XOR_{o submask of d} h[n-1-d+o] for all d in [0, n-1].

So nu2(n) = #{d in [2,n-1] : a_d = 1} = the number of nonzero ANF coefficients
of g_n among indices 2..n-1 (the n-prefix of the zeta/Mobius transform of the
reversed padded string).
"""
from lib.primes import prime_gap_parity

def t_direct(n, d, h):
    x = 0
    for o in range(d + 1):
        if (o & d) == o:
            x ^= h[n - 1 - d + o]
    return x

def anf_coeff(g, d):
    """a_d = XOR over x submask of d of g[x]. g is 0-indexed over [0, n-1]."""
    x = 0
    for i in range(d + 1):
        if (i & d) == i:
            x ^= g[i]
    return x

def check(n):
    h = prime_gap_parity(n + 1)[:n]   # length n, h[0..n-1]
    g = [0] * n
    for x in range(n):
        g[x] = h[n - 1 - x]           # reversed, no padding needed for d < n
    bad = 0
    for d in range(n):
        td = t_direct(n, d, h)
        ad = anf_coeff(g, d)
        if td != ad:
            bad += 1
            if bad <= 5:
                print(f"  MISMATCH n={n} d={d}: T={td} a_d={ad}")
    return bad

if __name__ == "__main__":
    total_bad = 0
    for n in range(3, 41):
        b = check(n)
        total_bad += b
        if b == 0:
            print(f"n={n}: T(n,d) == a_d for all d in [0,{n-1}]  (OK)")
    print(f"\nTotal mismatches over n=3..40: {total_bad}")

    # Negative control: the literal geometric suffix (nu2.py) is NOT this object.
    # Confirm all-ones h has ANF weight 1 (only d=0), matching nu2=O(1).
    h = [1] * 32
    g = h[::-1]
    weights = [anf_coeff(g, d) for d in range(32)]
    print("all-ones h ANF support size:", sum(weights), "(expect 1) ->",
          "PASS" if sum(weights) == 1 else "FAIL")
