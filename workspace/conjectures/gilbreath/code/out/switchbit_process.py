#!/usr/bin/env python3
"""Characterise the mod-4 switch bit process b_i = [p_{i+1} != p_i mod 4]
(the atomic supply-side quantity for Granville Route B).

For a long prime list, extract the bit string and test specifically whether it
is compatible with a low-order shift-register / LFSR / Bernoulli-with-memory
model. We look for the strongest simple description that is EXACT on the bits:
1) run-length distribution of 0s and 1s (empirical density + mean run length)
2) lag-k autocorrelation for k=1..5 (empirical, exact fractions)
3) whether the bits satisfy ANY short constant-coefficient linear recurrence
   over GF(2) (LFSR order m): Gaussian elimination tries m=1..12; a nonzero
   recurrence means the bits are low-complexity.
4) pair (bigram) and 4-gram frequency vs Bernoulli product (deviation).
We report the numbers exactly over the primes actually produced; this is
evidence about the process, not a proof of any model.
"""
import time
from lib.gilbreath import primes_up_to

t0 = time.time()
P = primes_up_to(2_000_000)
t1 = time.time()
print(f"primes: {len(P)}  sieve {t1-t0:.2f}s")

# bit = gap//2 mod 2  (=1 iff gap == 2 mod 4). This is the run's hbits.
bits = [((P[i+1]-P[i])//2) % 2 for i in range(len(P)-1)]
N = len(bits)
print(f"bits: {N}")

ones = sum(bits)
print(f"density of 1: {ones}/{N} = {ones/N:.6f}")

# run lengths
runs0, runs1 = [], []
run = 0
prev = bits[0]
for b in bits:
    if b == prev:
        run += 1
    else:
        (runs0 if prev == 0 else runs1).append(run)
        run = 1
        prev = b
(runs0 if prev == 0 else runs1).append(run)
import statistics as st
print(f"run-length 0: count={len(runs0)} mean={st.mean(runs0):.3f} max={max(runs0)}")
print(f"run-length 1: count={len(runs1)} mean={st.mean(runs1):.3f} max={max(runs1)}")

# autocorrelation
def acf(k):
    return sum(1 for i in range(N-k) if bits[i] == bits[i+k]) / (N-k)
print("lag-k equality rate (0.5 = uncorrelated):")
for k in range(1, 6):
    print(f"  k={k}: {acf(k):.6f}")

# bigram / 4-gram counts vs Bernoulli(p)
from collections import Counter
big = Counter(zip(bits[:-1], bits[1:]))
print("bigram rates (expected product for Bernoulli):")
p = ones/N
for (a,b),c in sorted(big.items()):
    exp = (p if a else 1-p)*(p if b else 1-p)
    print(f"  ({a},{b}): {c/N:.5f}  expected {exp:.5f}")

quad = Counter(zip(bits[:-3], bits[1:-2], bits[2:-1], bits[3:]))
print(f"4-gram types seen: {len(quad)}/16")

# GF(2) linear recurrence (LFSR) search: does bits satisfy sum_{j} c_j b_{i+j}=0?
def lfsr_order(m):
    # find c with b_{i+m} = sum_{j<m} c_j b_{i+j} over GF(2), exact on all i
    # Gaussian elimination on (N-m) equations, m unknowns
    rows = []
    for i in range(N - m):
        rows.append([bits[i+j] for j in range(m)] + [bits[i+m]])
    # gaussian elim
    rows = [r[:] for r in rows]
    pivots = []
    col = 0
    cur = 0
    rank = 0
    while col < m and cur < len(rows):
        # find pivot
        piv = None
        for r in range(cur, len(rows)):
            if rows[r][col] == 1:
                piv = r; break
        if piv is None:
            col += 1
            continue
        rows[cur], rows[piv] = rows[piv], rows[cur]
        for r in range(len(rows)):
            if r != cur and rows[r][col] == 1:
                for c in range(col, m+1):
                    rows[r][c] ^= rows[cur][c]
        cur += 1
        col += 1
    # check consistency: no row with lhs 0 rhs 1
    for r in range(len(rows)):
        if all(rows[r][c]==0 for c in range(m)) and rows[r][m]==1:
            return None  # inconsistent -> no recurrence works
    return rows  # consistent

for m in (1,2,3,4,5,6,8):
    res = lfsr_order(m)
    if res is None:
        print(f"LFSR order {m}: NOT consistent (no such recurrence)")
    else:
        print(f"LFSR order {m}: consistent -> recurrence exists over GF(2)")
