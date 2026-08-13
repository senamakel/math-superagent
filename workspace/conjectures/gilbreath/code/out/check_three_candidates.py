#!/usr/bin/env python3
"""Verify the mechanisms of three proposed approaches against the real prime rows.

Candidate 1 (window-range-bound): A_k(i) <= range(g_i..g_{i+k-1}) for k>=2,
  where g_m = A_1(m) is the even gap. Check zero violations.
Candidate 2 (alternating-sum-telescope-invariant): exact identity
  sigma(b) = a_0 - (-1)^W a_W - 2*sum_i (-1)^i min(a_i,a_{i+1})
  where b_i = |a_i - a_{i+1}|, sigma(b) = sum_i (-1)^i b_i.
Candidate 3 (max-plus-tropical-spectral-dynamics): probe whether any
  max-plus affine functional Phi(a) = max_i(a_i + c_i) with fixed c is
  non-increasing (Phi(Ta)<=Phi(a)) on the actual rows, and whether a
  two-point form max_{i<j}(a_i - a_j + d(j-i)) can be non-increasing.
"""
from lib.gilbreath import primes_up_to, rows_generator

primes = primes_up_to(200000)          # ~17984 primes
depth = 160                            # stay in live regime (block has intruder)
rows = list(rows_generator(primes, depth))

# ---- Candidate 1: cell-wise range bound ----
# g_m = A_1(m).  A_k(i) depends on gaps g_i..g_{i+k-1} (k gaps).
A1 = rows[1]
viol1 = 0
checked1 = 0
worst_slack = 0
for k in range(2, depth + 1):
    row = rows[k]
    for i in range(1, len(row)):       # i>=1 (A_k(i) with i the block-position index)
        lo = i - 1
        hi = i - 1 + (k - 1)           # indices into A1: gaps g_{lo}..g_{hi}
        if hi >= len(A1):
            break
        window = A1[lo:hi + 1]
        R = max(window) - min(window)
        checked1 += 1
        if row[i] > R:
            viol1 += 1
            if viol1 <= 3:
                print(f"C1 VIOL k={k} i={i} A={row[i]} R={R}")
    # also check intruder specifically on live rows (index b_k+1 -> A1 window)
print(f"C1: checked {checked1} cells, violations {viol1}")

# ---- Candidate 2: alternating-sum telescope identity ----
def sigma(v):
    return sum((-1) ** i * v[i] for i in range(len(v)))

viol2 = 0
for k in range(1, depth):              # check rows k (a) -> k+1 (b)
    a = rows[k]
    b = rows[k + 1]                    # b_i = |a_i - a_{i+1}|, i=0..len(a)-2
    W = len(a) - 1
    lhs = sigma(b)
    # b has W entries (indices 0..W-1); sigma over those
    minterm = sum((-1) ** i * min(a[i], a[i + 1]) for i in range(0, W))
    rhs = a[0] - ((-1) ** W) * a[W] - 2 * minterm
    if lhs != rhs:
        viol2 += 1
        if viol2 <= 3:
            print(f"C2 VIOL k={k} lhs={lhs} rhs={rhs}")
print(f"C2: checked rows k=1..{depth-1}, identity violations {viol2}")

# ---- Candidate 3: max-plus affine functional non-increase probe ----
# Form A: Phi(a) = max_i (a_i - c*i) for c in a range. Non-increasing?
from itertools import product
def phi_affine(a, c):
    return max(a[i] - c * i for i in range(len(a)))

# test on halved rows (values/2) restricted to live block+intruder region
canded3a = []
for c in [0.0, 0.5, 1.0, 2.0]:
    bad = 0
    tot = 0
    for k in range(1, depth):
        a = rows[k]
        b = rows[k + 1]
        tot += 1
        if phi_affine([x / 2 for x in b], c) > phi_affine([x / 2 for x in a], c) + 1e-9:
            bad += 1
    canded3a.append((c, bad))
print("C3 (affine Phi=max(a_i-c*i), halved): #non-increase violations per c:", canded3a)

# Form: two-point Phi(a)=max_{i<j}(a_i - a_j + d*(j-i)), d>0 means penalize for a_i large far-left
def phi_2pt(a, d):
    best = -1e18
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            v = a[i] - a[j] + d * (j - i)
            if v > best:
                best = v
    return best

canded3b = []
for d in [0.0, 0.5, 1.0, 2.0, -0.5, -1.0]:
    bad = 0
    tot = 0
    for k in range(1, depth):
        a = rows[k]
        b = rows[k + 1]
        tot += 1
        if phi_2pt([x / 2 for x in b], d) > phi_2pt([x / 2 for x in a], d) + 1e-9:
            bad += 1
    canded3b.append((d, bad))
print("C3 (two-point Phi), #non-increase violations per d:", canded3b)
