#!/usr/bin/env python3
"""Verify Malyshev's sharp bound on the number of ones in a Boolean Pascal triangle.

T_s: top row has s bits in GF(2); each lower row is the XOR (rule-90) of the
adjacent pair above. Total cells = s(s+1)/2. Malyshev 2021 asserts:
  max #ones over all 2^s top rows = ceil(s(s+1)/3),
with equality attained exactly for top rows = Fibonacci sequence mod 2.

Exhaustive for small s (rule 9 of method policy: brute force on small instances).
Exact integers; no floats.
"""
import itertools
from math import ceil
import time

def triangle_ones(top):
    """Return total # of 1s in the rule-90 triangle from a top row (list of ints 0/1)."""
    total = sum(top)
    row = top
    while len(row) > 1:
        row = [row[i] ^ row[i+1] for i in range(len(row)-1)]
        total += sum(row)
    return total

def fib_mod2(n):
    """Top row: Fibonacci sequence mod 2 of length n (F_1=1,F_2=1 convention -> 1,1,0,1,0,...)."""
    out = []
    a, b = 1, 1
    for _ in range(n):
        out.append(a % 2)
        a, b = b, a + b
    return out

results = []
for s in range(1, 15):
    best = 0
    best_tops = []
    for bits in itertools.product([0, 1], repeat=s):
        v = triangle_ones(list(bits))
        if v > best:
            best = v
            best_tops = [bits]
        elif v == best:
            best_tops.append(bits)
    expected = ceil(s * (s + 1) / 3)
    results.append((s, best, expected, best == expected))
    print(f"s={s:2d} max_ones={best:3d} ceil(s(s+1)/3)={expected:3d} match={best==expected}")

print("\nAll s in 1..14 match ceil(s(s+1)/3):", all(r[3] for r in results))

# Check the Fibonacci-mod-2 top row is among the maximisers at each s.
print("\nCheck Fibonacci-mod-2 top row is a maximiser:")
for s in range(2, 15):
    fb = [b % 2 for b in fib_mod2(s)]
    v = triangle_ones(fb)
    expected = ceil(s * (s + 1) / 3)
    status = "MAXIMISER" if v == expected else "not-max"
    print(f"  s={s:2d} fib_mod2 {''.join(map(str,fb))} ones={v} bound={expected} {status}")
