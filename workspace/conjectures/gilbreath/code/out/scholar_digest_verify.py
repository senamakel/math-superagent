#!/usr/bin/env python3
"""Verify the scholar-digest claims and corrections against the run's own data.

Checks (all exact integer / closed-form / source-quote arithmetic):
1. C2 alternating-sum identity on 159 real prime row pairs plus 2000 random
   strings (the symbolic proof is by hand in the note below the run).
2. Geometric vs linear fit on the 15 genuine 6e8 giant landing blocks
   [2179,5942,23265,31499,92620,103973,141706,271629,325090,515906,733564,
   1094273,5417975,10655286,23163290] -- R^2 and per-event factor.
3. Parity count among the 15 pre-jump rows and exact one-sided p.
4. Ratio bound: max gap 64 vs the FOLLOWING giant's jump at 6e8
   (12,508,030), and the stale thread figure 64/(5,237,310+1).
5. BCZ Table 1 style check: on the run's own primes < 1e6, ray w_1 (the
   second ray parallel to the left edge, mod 4) -- |#0 - #2| / N.
"""
import math
import random

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
        A, B = rows[k], rows[k + 1]
        W = len(A) - 1
        rhs = A[0] - ((-1) ** W) * A[W] - 2 * sum(
            ((-1) ** i) * min(A[i], A[i + 1]) for i in range(W))
        if sigma(B) != rhs:
            bad += 1
    return bad

# --- 1. C2 identity ---
primes = sieve(200000)
rows = rows_from_primes(primes, 159)
print("C2 real prime rows: rows =", len(rows) - 1, "violations =", check_c2(rows))
random.seed(7)
bad_r = 0
for _ in range(2000):
    n = random.randint(3, 12)
    A = [random.randint(0, 50) for _ in range(n)]
    B = [abs(A[i] - A[i+1]) for i in range(n - 1)]
    W = len(A) - 1
    rhs = A[0] - ((-1) ** W) * A[W] - 2 * sum(
        ((-1) ** i) * min(A[i], A[i + 1]) for i in range(W))
    if sigma(B) != rhs:
        bad_r += 1
print("C2 random strings: violations =", bad_r)

# --- 2. Fit on the 15 landing blocks ---
land = [2179, 5942, 23265, 31499, 92620, 103973, 141706, 271629,
        325090, 515906, 733564, 1094273, 5417975, 10655286, 23163290]
n = len(land)
xs = list(range(n))
ly = [math.log(b) for b in land]

def lsfit(xs, ys):
    m = len(xs)
    sx, sy = sum(xs), sum(ys)
    sxx = sum(x * x for x in xs); sxy = sum(x * y for x, y in zip(xs, ys))
    a = (sy * sxx - sx * sxy) / (m * sxx - sx * sx)
    b = (m * sxy - sx * sy) / (m * sxx - sx * sx)
    yhat = [a + b * x for x in xs]
    ss_res = sum((y - yh) ** 2 for y, yh in zip(ys, yhat))
    ss_tot = sum((y - sy / m) ** 2 for y in ys)
    return a, b, 1 - ss_res / ss_tot

_, mgeo, r2geo = lsfit(xs, ly)
_, mlin, r2lin = lsfit(xs, [float(b) for b in land])
print("geometric: slope = %.6f R^2 = %.6f factor/event = %.6f" % (mgeo, r2geo, math.exp(mgeo)))
print("linear:    slope = %.1f R^2 = %.6f" % (mlin, r2lin))

# --- 3. Parity ---
pre = [34, 56, 64, 68, 94, 96, 110, 112, 126, 130, 134, 146, 161, 174, 238]
even = sum(1 for r in pre if r % 2 == 0)
p = (sum(math.comb(len(pre), k) for k in range(even, len(pre) + 1))) / (2 ** len(pre))
print("pre-jump even = %d/%d  one-sided p = %.6g" % (even, len(pre), p))

# --- 4. Ratio bound ---
gap = 64
j_6e8 = 12508030
j_stale = 5237310
print("ratio 64/(%d+1) = %.6g ; stale 64/(%d+1) = %.6g"
      % (j_6e8, gap / (j_6e8 + 1), j_stale, gap / (j_stale + 1)))

# --- 5. BCZ Table-1-style ray check on the run's own primes < 1e6 ---
pr = sieve(1000000)
# build w_1: the second ray parallel to the left edge = column 1 of the triangle,
# i.e. A_k[1] for k = 0.. (the run's second-entry column), mod 4.
row = list(pr)
ray = []
while len(row) > 2:
    row = [abs(row[i] - row[i+1]) for i in range(len(row) - 1)]
    ray.append(row[1])
cnt0 = sum(1 for v in ray if v % 4 == 0)
cnt2 = sum(1 for v in ray if v % 4 == 2)
N = len(ray)
print("ray w1 mod4 (primes<1e6): N=%d #0=%d #2=%d |diff|=%d frac=%.6f"
      % (N, cnt0, cnt2, abs(cnt0 - cnt2), abs(cnt0 - cnt2) / N))
