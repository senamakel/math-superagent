#!/usr/bin/env python3
"""Independent oracle check of cycle_parity.py: enumerate all permutations for
small n, compute prod over cycles of (-1)^C(size,2), count even.  Also compare
to the pure-race p(n,inf) values, and (for context) to the pure-race MC parity
recomputed here at a fresh seed to confirm the limit_mc.py numbers are stable.
"""
import itertools
import random
from fractions import Fraction
from math import comb, sqrt

def cycle_parity_of_perm(p):
    # p: list, permutation on 0..n-1. Product of (-1)^C(cycle_size,2) -> is it +1?
    n = len(p)
    seen = [False]*n
    prod = 1
    for i in range(n):
        if not seen[i]:
            cyc = []
            j = i
            while not seen[j]:
                seen[j] = True
                cyc.append(j)
                j = p[j]
            c = len(cyc)
            if (c*(c-1)//2) % 2 == 1:
                prod *= -1
    return 1 if prod == 1 else 0

def brute(n):
    even = 0
    total = 0
    for p in itertools.permutations(range(n)):
        total += 1
        even += cycle_parity_of_perm(p)
    return Fraction(even, total)

# import the pure-bump MC engine 
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extend_limit_mc import pure_bump_edges, forest_chain_parity

def pure_mc(n, N=400000, seed=7):
    rng = random.Random(seed)
    even = 0
    for _ in range(N):
        v = [rng.expovariate(1.0) for _ in range(n)]
        even += (1 - forest_chain_parity(n, pure_bump_edges(n, v)))
    p = even/N
    se = sqrt(p*(1-p)/N)
    return p, se

print("=== brute cycle-even prob vs EGF values ===")
for n in [2,3,4,5,6,7,8]:
    print(f"n={n} brute={float(brute(n)):.6f}")

print()
print("=== pure-race (no-finish) MC p(n,inf) with fresh seed ===")
for n in [2,3,4,5,6]:
    p,se = pure_mc(n, 400000, seed=11+n)
    print(f"n={n} p={p:.6f} +/- {se:.6f}")

print()
print("=== compare cycle-even prob vs pure-race MC p(n,inf) ===")
import cycle_parity as cp
N=13
A = cp.egf_A_coeffs(N)
for n in [2,3,4,5,6]:
    cy = float(Fraction(1,2)*(1+A[n]))
    p,se = pure_mc(n, 400000, seed=21+n)
    print(f"n={n} cycle_even={cy:.6f}  purerace_mc={p:.6f}  diff={cy-p:+.6f}")
