#!/usr/bin/env python3
"""Primes module: exact prime sequence and mod-4 helpers for SUPPLY."""

import sympy


def primes_upto_index(n):
    """Return the first n primes q_1..q_n (q_1=2)."""
    return list(sympy.ntheory.generate.primerange(0, sympy.prime(n) + 1))[:n]


def mod4_string(n):
    """r_j = q_j mod 4 for the first n primes, as a list indexed 0..n-1
    (r[0] = q_1 mod 4 = 2; for j>=1 odd primes: r[j] in {1,3})."""
    ps = primes_upto_index(n)
    return [p % 4 for p in ps]


def h_string(n):
    """h[j] = [r_{j+1} != r_j mod 4] for j = 0..n-2, i.e. bit of primal
    gap-parity; length n-1. Equivalently ((q_{j+2}-q_{j+1})/2) mod 2."""
    r = mod4_string(n)
    return [1 if r[j + 1] != r[j] else 0 for j in range(n - 1)]


def prime_gap_parity(n):
    """Same as h_string but from ((q_{j+1}-q_j)/2) mod 2, using q_1..q_{n+1}.
    Kept as an independent route (linearisation definition of problem.md)."""
    ps = primes_upto_index(n + 1)
    return [((ps[j + 1] - ps[j]) // 2) % 2 for j in range(n)]
