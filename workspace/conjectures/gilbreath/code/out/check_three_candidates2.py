#!/usr/bin/env python3
"""Adversarial check of candidate-3 max-plus/affine functionals:
is ANY max-plus affine Phi(a)=max_i(a_i + c_i) (no position penalty) or
any two-point form non-increasing along the operator on the {0,2}-block
interior? Concentrate on the halved {0,1} interior (Rule-90 regime) where
the map is T(x)_i = |x_i - x_{i+1}| = x_i XOR x_{i+1} for bits.
Also test candidate-1's range bound on RANDOM 2-then-odds arrays
(universality of the cell-wise bound).
"""
from itertools import product

# ---- Candidate 3, restricted: is there a max-plus affine c_i with Phi non-increasing
# on ALL 2-bit and 3-bit {0,1} strings?  Phi(x)=max_i(x_i + c_i). T on bits = XOR.
def T_bits(x):
    return [x[i] ^ x[i + 1] for i in range(len(x) - 1)]

def phi_c(x, c):
    return max(x[i] + c[i] for i in range(len(x)))

# try small coefficient vectors c_i in a grid
violations_found = False
best_viol = None
for n in [2, 3, 4]:
    coeffs = [list(p) for p in product(range(-2, 3), repeat=n)]
    for c in coeffs:
        for x in product([0, 1], repeat=n):
            y = T_bits(x)
            # y shorter; phi(y) uses first len(y) coeffs
            if phi_c(y, c[:len(y)]) > phi_c(x, c):
                violations_found = True
                best_viol = (n, c, x, y)
                break
        if violations_found:
            break
    if violations_found:
        break

print("C3 restricted: any max-plus affine c non-increasing on {0,1} interior?",
      "NO - first violation" if violations_found else "YES candidate found")
if best_viol:
    print("  violation:", best_viol)

# ---- Candidate 1 universality: cell-wise range bound on random 2-then-odds ----
import random
def range_bound_holds(seq):
    # seq = A_0 = (2, odd, odd, ...); build A_1 gaps then trend triangle
    A = [list(seq)]
    while len(A[-1]) > 2:
        A.append([abs(A[-1][i] - A[-1][i + 1]) for i in range(len(A[-1]) - 1)])
    A1 = A[1]
    ok = True
    for k in range(2, len(A)):
        row = A[k]
        for i in range(1, len(row)):
            lo = i - 1
            hi = lo + k - 1
            if hi >= len(A1):
                break
            w = A1[lo:hi + 1]
            if row[i] > max(w) - min(w):
                ok = False
    return ok

random.seed(1)
fails = 0
for _ in range(2000):
    n = random.randint(6, 12)
    seq = [2] + [random.choice([3,5,7,9,11,13,15,17]) for _ in range(n - 1)]
    if not range_bound_holds(seq):
        fails += 1
print("C1 universality on 2000 random 2-then-odds arrays: failures =", fails)
