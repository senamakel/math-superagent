#!/usr/bin/env python3
"""Adversarial check of the adopted derivative-ladder-delta-commutation
approach (research/approaches/derivative-ladder-delta-commutation.md).

The approach's foundational identities (L1)-(L5) are stated as "derived by
hand, NOT yet machine-verified". Refused to let an adopted, load-bearing route
stay unverified; I attack each identity against the literal fold oracle.

Definitions (literal, no reliance on any library reduction):
  T(n,d) = XOR_{o submask of d} h[n-1-d+o],   d in [2,n-1]
  (Delta h)[j] = h[j] ^ h[j+1]
  Phi_n h weight = #{d in [2,n-1] : T(n,d)=1} = nu2(n)  (problem.md fact 1)

Claimed identities:
  (L1) T_{Delta^k h}(n,d) = T(n+k, d+k)           for all k>=0
  (L2) nu2(n+1) = wt(Phi_n Delta h) + [T(n+1,2)=1]
  (L3) nu2(n+k) = wt(Phi_n Delta^k h) + #{d in [2,k+1] : T(n+k,d)=1}   fixed k
  (L4) T(n+1,d) = T(n,d) ^ T(n+1,d+1)             (anti-Pascal)
  (L5) Delta h[j] = [q_j != q_{j+2} mod 4]        (over real prime residues)

I also independently verify the ladder for GENERAL binary strings h, not just
the prime string, because (L1),(L4) are claimed as F2 identities holding for
any {0,1} string h (an approach-level structural claim).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from lib.supply_fold import t_direct
from lib.primes import mod4_string

def submasks(d):
    s = d
    while True:
        yield s
        if s == 0:
            break
        s = (s - 1) & d

def T(n, d, h):
    """Literal fold cell. h indexed 0..n-1."""
    x = 0
    for o in submasks(d):
        x ^= h[n - 1 - d + o]
    return x

def Delta(h):
    return [h[j] ^ h[j + 1] for j in range(len(h) - 1)]

def Delta_k(h, k):
    for _ in range(k):
        h = Delta(h)
    return h

def wt(n, h):
    return sum(T(n, d, h) for d in range(2, n))

# ---------- (L1) on general binary strings ----------
import random
random.seed(11)
print("=== (L1) T_{Delta^k h}(n,d) = T(n+k,d+k), over general h ===")
bad = total = 0
for trial in range(400):
    L = 40
    h = [random.randint(0,1) for _ in range(L)]
    for k in (0,1,2,4):
        dh = Delta_k(h, k)
        # dh has length L-k. Need T(n,d) with dh of length >= n
        for n in range(3, L-k+1):
            for d in range(2, n):
                lhs = T(n, d, dh)          # uses dh[0..n-1]
                rhs = T(n+k, d+k, h)       # uses h[0..n+k-1]
                total += 1
                if lhs != rhs:
                    bad += 1
                    if bad <= 3:
                        print(f"  FAIL n={n} d={d} k={k}: lhs={lhs} rhs={rhs} h={h}")
print(f"  (L1): {bad}/{total} mismatches over random h")

# ---------- (L1) on the real prime string ----------
print("\n=== (L1) on real prime-residue h ===")
big = mod4_string(60)
r = big[:60]
h = [1 if r[j+1] != r[j] else 0 for j in range(len(r)-1)]   # length 59
bad = total = 0
for k in (0,1,2,4):
    dh = Delta_k(h, k)
    for n in range(3, len(dh)+1):
        for d in range(2, n):
            if T(n, d, dh) != T(n+k, d+k, h):
                bad += 1
            total += 1
print(f"  (L1/prime): {bad}/{total} mismatches")

# ---------- (L2),(L3): ladder on the prime string ----------
print("\n=== (L2) nu2(n+1) = wt(Phi_n Delta h) + [T(n+1,2)=1] ; (L3) ladder ===")
bad2 = total2 = 0
for n in range(3, 40):
    # Hn = length-(n+1) prefix of h
    Hn = h[:n+1]
    nu2_np1 = wt(n+1, Hn)                     # wt over d in [2,n]
    dh = Delta(h[:n+1])                        # length n
    w = wt(n, dh)                              # over d in [2,n-1]
    term = T(n+1, 2, Hn)
    if nu2_np1 != w + term:
        bad2 += 1
        print(f"  L2 FAIL n={n}: nu2(n+1)={nu2_np1} wt={w} T(n+1,2)={term}")
    total2 += 1
    # (L3) k=1: should give nu2(n+1) = wt(Phi_n Del h) + #{d in [2,2]:T(n+1,d)=1}
    if nu2_np1 != w + sum(T(n+1, d, Hn) for d in range(2, 3)):
        print(f"  L3/k1 FAIL n={n}")
print(f"  (L2): {bad2}/{total2} mismatches")

# ---------- (L4) anti-Pascal T(n+1,d)=T(n,d)^T(n+1,d+1), general h ----------
print("\n=== (L4) anti-Pascal T(n+1,d)=T(n,d)^T(n+1,d+1), general h ===")
bad4 = total4 = 0
for trial in range(400):
    L = 32
    h = [random.randint(0,1) for _ in range(L)]
    for n in range(3, L-1):
        Hn = h[:n+2]     # length n+2 so T(n+1,*) well defined via index n
        for d in range(2, n):
            lhs = T(n+1, d, Hn)
            rhs = T(n, d, h[:n]) ^ T(n+1, d+1, Hn)
            total4 += 1
            if lhs != rhs:
                bad4 += 1
                if bad4 <= 3:
                    print(f"  FAIL n={n} d={d}: lhs={lhs} rhs={rhs}")
print(f"  (L4): {bad4}/{total4} mismatches over random h")

# ---------- (L5) Delta h[j] = [q_j != q_{j+2} mod 4], real primes ----------
print("\n=== (L5) Delta h[j] = [q_j != q_{j+2} mod 4], real primes ===")
bad5 = total5 = 0
for j in range(len(h)-1):
    lhs = h[j] ^ h[j+1]
    rhs = 1 if r[j] != r[j+2] else 0
    total5 += 1
    if lhs != rhs:
        bad5 += 1
print(f"  (L5): {bad5}/{total5} mismatches")

print("\n=== SUMMARY ===")
for nm, b, t in [("L1(random)",bad,total),("L1(prime)",bad,total),
                 ("L2",bad2,total2),("L4",bad4,total4),("L5",bad5,total5)]:
    print(f"  {nm:14s}: {b}/{t} mismatches {'-> HOLDS' if b==0 else '-> REFUTED'}")
