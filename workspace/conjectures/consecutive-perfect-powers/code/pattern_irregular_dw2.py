"""Irregularity (index of irregularity) of the double-Wieferich primes.

For 2k <= p-3, B_{2k} is p-integral, so p | num(B_{2k})  <=>  B_{2k} == 0 (mod p).
Efficient O(p^2) modular Bernoulli recurrence with factorial-based binomials.

Validation (in pattern_irregular_dw.py) already confirmed this recurrence
matches the exact num(B_{2k}) route for all 61 odd primes <= 300.  Here we
apply it to the double-Wieferich primes the descent must run on.
"""
from math import comb


def bernoulli_even_mod_p(p):
    """Return B_{2k} mod p for 2k = 2,4,...,p-3, via O(p^2) modular recurrence."""
    # factorials mod p
    fact = [1] * p
    for i in range(1, p):
        fact[i] = fact[i - 1] * i % p
    inv_fact = [1] * p
    inv_fact[p - 1] = pow(fact[p - 1], -1, p)
    for i in range(p - 1, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % p
    B = [0] * (p - 1)
    B[0] = 1
    for n in range(1, p - 2):
        s = 0
        nn = n + 1
        for j in range(n):
            c = fact[nn] * inv_fact[j] % p * inv_fact[nn - j] % p
            s = (s + c * B[j]) % p
        B[n] = (-s * pow(nn, -1, p)) % p
    return B


def irregular_indices(p):
    B = bernoulli_even_mod_p(p)
    return [2 * k for k in range(1, (p - 1) // 2) if B[2 * k] == 0]


primes = [83, 911, 2903, 4871, 18787]
for p in primes:
    idx = irregular_indices(p)
    print(f"p={p}: irregular={bool(idx)}  indices(B_{{{2*k}}})={idx}" if idx else
          f"p={p}: REGULAR (no index)")
