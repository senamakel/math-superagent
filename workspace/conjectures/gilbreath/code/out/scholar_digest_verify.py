#!/usr/bin/env python3
"""Independent verification of the new-session claims in the scholar digest.

Checks (all exact integer / closed-form arithmetic):
1. C2 alternating-sum identity, symbolic check on 159 real row pairs plus a
   random-string sanity check: sigma(A_{k+1}) = A_k(0) - (-1)^W A_k(W)
   - 2 * sum_{i<W} (-1)^i min(A_k(i), A_k(i+1)).
2. Geometric vs linear fit on the 15 genuine 6e8 giant landing blocks:
   [2179,5942,23265,31499,92620,103973,141706,271629,325090,515906,733564,
   1094273,5417975,10655286,23163290] -- R^2 and per-event factor.
3. Parity count among the 15 pre-jump rows and the exact one-sided p.
4. Ratio bound: max gap 64 against the following giant's jump (12,508,030 at
   6e8), and the stale thread figure 64/(5,237,310+1).
"""
import math
import random
import sys

def rows_from_primes(primes, depth):
    row = list(primes)
    out = []
    for _ in range(depth):
        row = [abs(row[i] - row[i+1]) for i in range(len(row) - 1)]
        out.append(row)
    return out

def sieve(n):
    bs = bytearray(b'\x01') * (n + 1)
    bs[0:2] = b'\x00\x00'
    for i in range(2, int(n ** 0.5) + 1):
        if bs[i]:
            bs[i*i::i] = b'\x00' * (((n - i*i) // i) + 1)
    return [i for i in range(n + 1) if bs[i]]

def sigma(v):
    return sum((-1) ** i * v[i] for i in range(len(v)))

def check_c2(rows):
    bad = 0
    for k in range(len(rows) - 1):
        A = rows[k]
        B = rows[k + 1]
        W = len(A) - 1
        rhs = A[0] - ((-1) ** W) * A[W] - 2 * sum(
            ((-1) ** i) * min(A[i], A[i + 1]) for i in range(W))
        if sigma(B) != rhs:
            bad += 1
    return bad

# --- 1. C2 identity on real prime rows ---
primes = sieve(200000)
rows = rows_from_primes(primes, 159)
bad = check_c2(rows)
print("C2 on real prime rows: rows checked =", len(rows) - 1, "violations =", bad)

# random sanity check (any non-negative integers)
random.seed(7)
bad_r = 0
for _ in range(2000):
    n = random.randint(3, 12)
    A = [random.randint(0, 50) for _ in range(n)]
    B = [abs(A[i] - A[i + 1]) for i in range(n - 1)]
    W = len(A) - 1
    rhs = A[0] - ((-1) ** W) * A[W] - 2 * sum(
        ((-1) ** i) * min(A[i], A[i + 1]) for i in range(W))
    if sigma(B) != rhs:
        bad_r += 1
print("C2 on 2000 random strings: violations =", bad_r)

# --- 2. Geometric vs linear fit on the 15 landing blocks ---
land = [2179, 5942, 23265, 31499, 92620, 103973, 141706, 271629,
        325090, 515906, 733564, 1094273, 5417975, 10655286, 23163290]
n = len(land)
xs = list(range(n))
ly = [math.log(b) for b in land]

def lsfit(xs, ys):
    m = len(xs)
    sx = sum(xs); sy = sum(ys)
    sxx = sum(x * x for x in xs); sxy = sum(x * y for x, y in zip(xs, ys))
    a = (sy * sxx - sx * sxy) / (m * sxx - sx * sx)
    b = (m * sxy - sx * sy) / (m * sxx - sx * sx)
    yhat = [a + b * x for x in xs]
    ss_res = sum((y - yh) ** 2 for y, yh in zip(ys, yhat))
    ss_tot = sum((y - sy / m) ** 2 for y in ys)
    return a, b, 1 - ss_res / ss_tot

ageo, mgeo, r2geo = lsfit(xs, ly)
aline, mlin, r2lin = lsfit(xs, [float(b) for b in land])
print("geometric fit: slope = %.6f  R^2 = %.6f  factor/event = %.6f"
      % (mgeo, r2geo, math.exp(mgeo)))
print("linear fit:    slope = %.1f  R^2 = %.6f" % (mlin, r2lin))

# --- 3. Parity among the 15 pre-jump rows ---
pre = [34, 56, 64, 68, 94, 96, 110, 112, 126, 130, 134, 146, 161, 174, 238]
even = sum(1 for r in pre if r % 2 == 0)
print("pre-jump rows: even =", even, "/", len(pre))
p = (sum(math.comb(len(pre), k) for k in range(even, len(pre) + 1))) / (2 ** len(pre))
print("one-sided p (>= %d of %d even, fair coin) = %.6g" % (even, len(pre), p))

# --- 4. Ratio bound ---
gap = 64
j_6e8 = 12508030   # giant 15 at 6e8 (row 238 -> 239)
j_stale = 5237310  # giant 14 (the thread's stale pairing)
print("ratio bound: 64/(%d+1) = %.6g ; thread's stale 64/(%d+1) = %.6g"
      % (j_6e8, gap / (j_6e8 + 1), j_stale, gap / (j_stale + 1)))
