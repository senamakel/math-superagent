#!/usr/bin/env python3
"""Machine checks for three candidate approaches (grounding cycle).

1. gantmacher-krein: is M[k][j] = (-1)^(k-j) * C(k,j) sign-regular?
   Sign-regular means: for each minor order r, ALL r x r minors have a
   single (weak) sign (all >= 0 or all <= 0), OR all <= 0 / all >= 0.
   Find two minors of the same order with opposite nonzero signs.

2. zero-sum-flow: the recharge identity is already proved; nothing to check
   beyond reproducing b_k from the identity on the delete-5 sequence.

3. fenchel-duality: universal claim "A_k(1) in {0,2} for ALL even-gap
   2-then-odds inputs" -- check the Colonna delete-5 sequence
   (2,3,7,11,13,17,19,23,...), which has all gaps after the first even.
   Compute A_1(1) and A_2(0).
"""
from math import comb
from itertools import combinations
import json

def alternating_pascal_minors(N=6):
    """M[k][j] = (-1)^(k-j) binom(k,j) for 0<=j<=k<=N. Report 2x2 minors by sign."""
    M = [[0]*(N+1) for _ in range(N+1)]
    for k in range(N+1):
        for j in range(k+1):
            M[k][j] = (-1)**(k-j) * comb(k, j)
    pos, neg = [], []
    rows = list(range(N+1)); cols = list(range(N+1))
    for (i1, i2) in combinations(rows, 2):
        for (j1, j2) in combinations(cols, 2):
            d = M[i1][j1]*M[i2][j2] - M[i1][j2]*M[i2][j1]
            if d > 0: pos.append(((i1,i2),(j1,j2),d))
            elif d < 0: neg.append(((i1,i2),(j1,j2),d))
    return M, pos, neg

def gilbreath_rows(seq, depth):
    rows = [seq]
    for _ in range(depth):
        rows.append([abs(rows[-1][i] - rows[-1][i+1]) for i in range(len(rows[-1])-1)])
    return rows

def delete5_primes(n=12):
    # primes with 5 removed: 2,3,7,11,13,17,19,23,29,31,37,41
    P = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71]
    return [p for p in P if p != 5][:n]

print("="*70)
print("CHECK 1: alternating Pascal matrix sign-regularity")
M, pos, neg = alternating_pascal_minors(6)
n_pos, n_neg = len(pos), len(neg)
print(f"2x2 minors: {n_pos} strictly positive, {n_neg} strictly negative")
if pos and neg:
    print(f"  positive example: rows {pos[0][0]} cols {pos[0][1]} det={pos[0][2]}")
    print(f"  negative example: rows {neg[0][0]} cols {neg[0][1]} det={neg[0][2]}")
    print("  => NOT sign-regular (same order has both signs) => Gantmacher-Krein")
    print("     variation-diminishing theorem does NOT apply to this matrix.")
else:
    print("  (no mixed-sign pair found at this size)")

print("="*70)
print("CHECK 2: signed forward differences of the primes oscillate")
# first 12 primes; signed k-th forward difference D_k(i) = sum_j (-1)^(k-j) C(k,j) A0(i+j)
A0 = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
D = {0: A0[:]}
for k in range(1, 5):
    D[k] = [sum(((-1)**(k-j))*comb(k,j)*A0[i+j] for j in range(k+1))
            for i in range(len(A0)-k)]
for k in range(1, 5):
    signs = [1 if v > 0 else (-1 if v < 0 else 0) for v in D[k]]
    sc = sum(1 for a,b in zip(signs, signs[1:]) if a*b < 0)
    print(f"  D_{k} signs: {signs}  sign changes: {sc}")

print("="*70)
print("CHECK 3: universal even-gap class claim (candidate 3)")
seq = delete5_primes()
rows = gilbreath_rows(seq, 3)
print(f"  A_0 = {seq}")
print(f"  A_1 = {rows[1][:8]}")
print(f"  A_1(1) = {rows[1][1]}")
print(f"  A_2 = {rows[2][:8]}")
print(f"  A_2(0) = {rows[2][0]}")
gaps = [seq[i+1]-seq[i] for i in range(len(seq)-1)]
print(f"  gaps = {gaps}  (all even after the first: {all(g%2==0 for g in gaps[1:])})")
if rows[1][1] not in (0,2):
    print("  => A_1(1) = 4: a 2-then-odds sequence with all subsequent gaps even")
    print("     violates the universal claim 'A_k(1) in {0,2} for ALL even-gap inputs'.")
    print("     (This is the Colonna delete-5 example already in the library.)")
print("="*70)
