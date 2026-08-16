#!/usr/bin/env python3
"""Refuter: machine-verify the adopted approach `derivative-ladder-delta-commutation`
identity (L1):  T_{Δ^k h}(n,d) = T(n+k, d+k)  for every k >= 0.

Definitions (problem.md facts 1-2, lib.submasks.fold_xor):
  T(n,d) = XOR_{o submask of d} h[n-1-d+o]   (reads a length-(d+1) window, indices n-1-d .. n-1)
  Δh[j]  = h[j] XOR h[j+1]  (F2 difference);  Δ^k h is the k-th iterate.

The adopted approach claims this exact identity for ALL k, hence the whole
invariance/equivalence theorem (SUPPLY(h) <=> SUPPLY(Δ^k h)) rests on it.
It is flagged in the approach file as 'derived by hand, not yet machine-verified'.

This is precisely the class of finite F2 identity that the previous refuter found
FALSE for the abel-boundary and substitution relations. So test it against a
literal oracle, especially at d ∧ k != 0 (overlapping binary supports), where
the submask decomposition is NOT unique.
"""
import itertools, random
from lib.submasks import and_subsets

def T(n, d, h):
    """Literal fold cell: XOR over bitwise submasks o of d of h[n-1-d+o]."""
    acc = 0
    for o in and_subsets(d):
        acc ^= h[n - 1 - d + o]
    return acc

def delta_pow(h, k):
    """Δ^k h where Δh[j] = h[j]^h[j+1].  Δ^k h[j] = XOR_{i submask of k} h[j+i]
    (Frobenius: (1+σ)^k = sum of σ^i over submasks i of k, mod 2)."""
    out = []
    for j in range(len(h) - k):
        acc = 0
        for i in and_subsets(k):
            acc ^= h[j + i]
        out.append(acc)
    return out

def check(nmax, kmax, ntrial):
    bad = 0
    total = 0
    examples = []
    for n in range(4, nmax + 1):
        for k in range(1, kmax + 1):
            # h must be long enough that both sides are defined: need length n+k
            for _ in range(ntrial):
                h = [random.randint(0, 1) for _ in range(n + k + 2)]
                for d in range(2, n):       # d in [2, n-1]
                    total += 1
                    lhs = T(n, d, delta_pow(h, k))
                    rhs = T(n + k, d + k, h)
                    if lhs != rhs:
                        bad += 1
                        if len(examples) < 8:
                            examples.append((n, k, d, lhs, rhs, h[:n+k]))
    print(f"checked {total} cells (n<= {nmax}, k<= {kmax}, {ntrial} random h each)")
    print(f"mismatches: {bad}")
    for ex in examples:
        print("  MISMATCH n,k,d, LHS,RHS, h=", ex)

check(nmax=10, kmax=4, ntrial=5)
