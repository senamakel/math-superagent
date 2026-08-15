"""Locate the bug in the earlier pattern_dw_structure.bernoulli_even_modp that
made it report 911 irregular (index 60) and 2903 irregular (index 2386), by
comparing against my validated recurrence at those exact primes.

Uses the OLD recurrence code verbatim (copied) and my validated one.
"""
from math import comb
import sympy as sp


def OLD_bernoulli_even_modp(p):
    B = [0] * (p + 1)
    B[0] = 1
    b_even = []
    for n in range(1, p - 2 + 1):
        s = 0
        c = 1
        for k in range(0, n):
            c = c * (n + 1 - k) * pow(k + 1, p - 2, p) % p
            s = (s + (B[k] * c if k > 0 else B[k])) % p
        B[n] = (-s * pow(n + 1, p - 2, p)) % p
    out = []
    for k in range(1, (p - 3) // 2 + 1):
        out.append(B[2 * k])
    return out


def NEW_recurrence(p):
    B = [0] * (p - 1)
    B[0] = 1
    for n in range(1, p - 2):
        s = 0
        for j in range(n):
            s = (s + (comb(n + 1, j) % p) * B[j]) % p
        B[n] = (-s * pow(n + 1, -1, p)) % p
    return [2 * k for k in range(1, (p - 1) // 2) if B[2 * k] == 0]


def exact(p):
    return [2 * k for k in range(1, (p - 1) // 2) if sp.bernoulli(2 * k).p % p == 0]


for p in [911, 2903]:
    old = OLD_bernoulli_even_modp(p)
    old_idx = [2 * (k + 1) for k, b in enumerate(old) if b == 0]
    print(f"p={p}: OLD indices={old_idx}")
    print(f"p={p}: exact indices={exact(p)}")
    # what did old compute at the contested index?
    if old_idx:
        m = old_idx[0]
        print(f"   OLD claims B_{m}==0 mod p; exact num(B_{m})%p={sp.bernoulli(m).p % p}")
