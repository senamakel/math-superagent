#!/usr/bin/env python3
"""
PE622 reference-library oracle check.

The problem: s(n) = number of consecutive out-faro (perfect riffle) shuffles
needed to restore an even deck of size n.  By the Diaconis-Graham-Kantor lemma
and Packard Thm 2.1, s(n) = ord_{n-1}(2), the multiplicative order of 2 modulo
n-1.

This script reproduces the WORKED EXAMPLES from the statement (not the answer:
sum over n with s(n)=60 is left computed by solution.py):
  - s(52) = ord_51(2) = 8
  - s(86) = ord_85(2) = 8
  - sum of all even n with s(n) = 8 equals 412
These are the test oracle.  The oracle definition of the out-shuffle is brute
force (list-rotation until identity) and is checked against ord_{n-1}(2).
"""
from math import gcd
from functools import reduce


def ord_mod(a, m):
    """Smallest r>0 with a^r == 1 (mod m); m>1 odd, gcd(a,m)=1."""
    if gcd(a, m) != 1:
        return None
    r, val = 0, 1
    while True:
        r += 1
        val = (val * a) % m
        if val == 1:
            return r


def out_shuffle(deck):
    """One perfect out-shuffle (top and bottom fixed) of an even deck."""
    n = len(deck)
    half = n // 2
    top, bot = deck[:half], deck[half:]
    out = []
    for i in range(half):
        out.append(top[i])
        out.append(bot[i])
    return out


def s_oracle(n):
    """Brute-force number of out-shuffles to restore deck of even size n."""
    deck = list(range(n))
    d = deck[:]
    count = 0
    while True:
        d = out_shuffle(d)
        count += 1
        if d == deck:
            return count


def s_ord(n):
    return ord_mod(2, n - 1)


# Worked examples from the statement
assert s_ord(52) == 8, s_ord(52)
assert s_oracle(52) == 8
assert s_ord(86) == 8, s_ord(86)
assert s_oracle(86) == 8

# Sum of all even n with s(n)=8 must be 412 (statement's worked example)
total = 0
vals = []
for n in range(2, 500, 2):          # upper bound generous; example sums to 412
    if s_ord(n) == 8:
        total += n
        vals.append(n)
print("even n with s(n)=8:", vals)
print("sum:", total)
assert total == 412, total

# oracle (brute list-rotation) vs ord formula agree on small even decks
for n in range(2, 80, 2):
    assert s_oracle(n) == s_ord(n), (n, s_oracle(n), s_ord(n))

print("All worked examples reproduced. ord vs brute oracle agree.")
