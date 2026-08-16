#!/usr/bin/env python3
"""Verify the derivative-ladder two-point identity (L5) and the anti-Pascal
relation (L4) on the REAL prime-residue string, and the (L2) ladder corridor,
using the canonical library oracle (not a re-derivation).

  h[j] = [q_{j+1} != q_j mod 4];   Delta h[j] = h[j]^h[j+1]
  (L5): Delta h[j] = [q_j != q_{j+2} mod 4]
  (L4): T(n+1,d) = T(n,d) ^ T(n+1,d+1), literal fold cell
  (L2): nu2(n+1) = wt(Phi_n Delta h) + [T(n+1,2)=1]

All against the literal submask-XOR oracle lib.supply_fold.t_direct /
lib.nu2.fold_nu2 (the authoritative, guard-pinned fold), so this is an
independent-per-route check of the hand-derived ladder identities on the real
prime string.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from lib.primes import mod4_string
from lib.supply_fold import t_direct
from lib.nu2 import fold_nu2

BIG = mod4_string(200)          # r[j] = q_{j+1} mod 4
R = BIG[:200]
H = [1 if R[j+1] != R[j] else 0 for j in range(len(R)-1)]   # length 199

def submasks(d):
    s = d
    while True:
        yield s
        if s == 0:
            break
        s = (s - 1) & d

def T(n, d, h):
    x = 0
    for o in submasks(d):
        x ^= h[n - 1 - d + o]
    return x

# ---- (L5): Delta h[j] = [q_j != q_{j+2} mod 4] on the real prime string ----
bad5 = tot5 = 0
for j in range(len(H)-1):
    lhs = H[j] ^ H[j+1]
    rhs = 1 if R[j] != R[j+2] else 0
    tot5 += 1
    if lhs != rhs:
        bad5 += 1
print(f"(L5) two-point: {bad5}/{tot5} mismatches on real prime h")

# ---- (L4): anti-Pascal T(n+1,d) = T(n,d) ^ T(n+1,d+1), real prime string ----
bad4 = tot4 = 0
for n in range(3, 40):
    hn = H[:n+2]              # length n+2 so T(n+1,*) is well-defined
    for d in range(2, n):
        lhs = T(n+1, d, hn)
        rhs = T(n, d, H[:n]) ^ T(n+1, d+1, hn)
        tot4 += 1
        if lhs != rhs:
            bad4 += 1
print(f"(L4) anti-Pascal: {bad4}/{tot4} mismatches on real prime h")

# ---- (L2): nu2(n+1) = wt(Phi_n Delta h) + [T(n+1,2)=1], real prime h ----
bad2 = tot2 = 0
for n in range(3, 60):
    hn = H[:n+1]               # length n+1
    nu2_np1 = fold_nu2(n+1, hn)   # canonical oracle, d in [2, n]
    dh = [hn[j] ^ hn[j+1] for j in range(len(hn)-1)]   # length n
    w = fold_nu2(n, dh)          # d in [2, n-1]
    term = T(n+1, 2, hn)
    tot2 += 1
    if nu2_np1 != w + term:
        bad2 += 1
        print(f"  L2 FAIL n={n}: nu2(n+1)={nu2_np1} wt={w} T(n+1,2)={term}")
print(f"(L2) corridor: {bad2}/{tot2} mismatches on real prime h")

print()
print("SUMMARY (real prime string):")
print(f"  (L5): {'HOLDS' if bad5==0 else 'REFUTED'}  ({bad5}/{tot5})")
print(f"  (L4): {'HOLDS' if bad4==0 else 'REFUTED'}  ({bad4}/{tot4})")
print(f"  (L2): {'HOLDS' if bad2==0 else 'REFUTED'}  ({bad2}/{tot2})")
