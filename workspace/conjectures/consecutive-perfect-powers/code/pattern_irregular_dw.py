"""Index of irregularity: p is irregular iff p | num(B_{2k}) for even 2k, 2<=2k<=p-3.

For 2k <= p-3, B_{2k} is p-integral (p is not in the von Staudt-Clausen
denominator since p-1 does not divide 2k), so  p | num(B_{2k})  <=>  B_{2k} == 0 (mod p).

We compute B_n mod p by the standard Bernoulli recurrence in pure modular
arithmetic (every denominator j+1 <= p-2 is invertible mod p):
    B_0 = 1;  sum_{j=0}^{n} binom(n+1,j) B_j = 0  ==>  B_n = -(sum_{j<n} binom(n+1,j)B_j) * inv(n+1).

Validation: compare against the reliable exact route num(B_{2k}) % p == 0
(sympy Rational .p numerator) for every odd prime <= 300.
"""
import sympy as sp
from math import comb


def bernoulli_mod_p_recurrence(p):
    """Return B_n mod p for n = 0..p-3 via modular recurrence."""
    B = [0] * (p - 1)
    B[0] = 1 % p
    for n in range(1, p - 2):          # up to n = p-3
        s = 0
        for j in range(n):
            s = (s + comb(n + 1, j) * B[j]) % p
        B[n] = (-s * pow(n + 1, -1, p)) % p
    return B


def irregular_indices_recurrence(p):
    B = bernoulli_mod_p_recurrence(p)
    return [2 * k for k in range(1, (p - 1) // 2) if B[2 * k] == 0]


def irregular_indices_exact(p):
    out = []
    for k in range(1, (p - 1) // 2):
        m = 2 * k
        num = sp.bernoulli(m).p
        if num % p == 0:
            out.append(m)
    return out


# ---------- Validation over odd primes <= 300 ----------
small = [p for p in range(3, 301) if sp.isprime(p) and p % 2 == 1]
bad = 0
for p in small:
    e = irregular_indices_exact(p)
    r = irregular_indices_recurrence(p)
    if e != r:
        bad += 1
        print(f"MISMATCH p={p}: exact={e} recurrence={r}")
print(f"Validation: {len(small)} odd primes <= 300, mismatches = {bad}")
print("Known irregular <=300 from recurrence:",
      [(p, irregular_indices_recurrence(p)) for p in small if irregular_indices_recurrence(p)])
