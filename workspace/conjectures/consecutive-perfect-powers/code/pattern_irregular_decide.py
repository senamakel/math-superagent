"""Decision: are 911 and 2903 regular (no index 2k we have p | num(B_{2k}))?

Compare my modular Bernoulli recurrence against the exact sympy numerator
route for EVERY even index 2k = 2..p-3 for these two primes.  My recurrence
already validated 0/61 mismatches over odd primes <= 300.  Here we cover the
full index range for the two previously-mis-reported primes.
"""
import sympy as sp
from math import comb


def irregular_indices_recurrence(p):
    # only need B_{2k} for 2k <= p-3
    B = [0] * (p - 1)
    B[0] = 1
    for n in range(1, p - 2):
        s = 0
        for j in range(n):
            c = comb(n + 1, j)
            s = (s + (c % p) * B[j]) % p
        B[n] = (-s * pow(n + 1, -1, p)) % p
    return [2 * k for k in range(1, (p - 1) // 2) if B[2 * k] == 0]


def irregular_indices_exact(p):
    out = []
    for k in range(1, (p - 1) // 2):
        if sp.bernoulli(2 * k).p % p == 0:
            out.append(2 * k)
    return out


for p in [911, 2903]:
    r = irregular_indices_recurrence(p)
    e = irregular_indices_exact(p)
    print(f"p={p}: recurrence_indices={r}")
    print(f"p={p}: exact_indices   ={e}")
    print(f"p={p}: AGREE? {r == e}   REGULAR? {e == []}")
