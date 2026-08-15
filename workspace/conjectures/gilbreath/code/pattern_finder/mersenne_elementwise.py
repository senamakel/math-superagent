#!/usr/bin/env python3
"""Confirm the elementwise structure of the Mersenne per-residue half-constant
arrays R_k (c_r/2) to high k, to decide whether the sum identity sum c_r =
3^k - 3 is PROVABLE BY INDUCTION via a discovered exact recursion.

Newly-observed structural facts to test (conjectures):
  (A) R_k has EXACTLY k ones, located at r=0 and r = P_k - (2^j - 1) for
      j = 1..k-1   (i.e. r = 2^k - 2^j for j=0..k-1... check)
  (B) R_k[1] = 2^(k-1) - 1  (the only non-power-of-2 value; the Mersenne)
  (C) all other R_k[r] are powers of 2
  (D) sum_r R_k[r] = (3^k - 3)/2   (=> sum c_r = 3^k - 3)
"""
import sys
sys.path.insert(0, '/workspace/code')
from lib.rightdiag import incremental_diagonals, cycle_and_nu2


def build_seq(word, n_terms):
    q = [2, 3]
    per = len(word)
    while len(q) < n_terms:
        bit = word[(len(q) - 2) % per]
        q.append(q[-1] + (2 if bit else 4))
    return q[:n_terms]


def nu2_seq(word, nmax):
    q = build_seq(word, nmax + 1)
    out = {}
    for k, dd in enumerate(incremental_diagonals(q)):
        if k >= 2:
            out[k] = cycle_and_nu2(dd)[1]
    return out


def per_residue_affine(vals, P, nmin, nmax):
    cs = []
    ok = True
    for r in range(P):
        diffs = {vals[n + P] - vals[n] for n in range(nmin, nmax - P + 1)
                 if n % P == r}
        if len(diffs) != 1:
            ok = False
            cs.append(None)
        else:
            cs.append(diffs.pop())
    return ok, cs


def get_R(k, N=14000):
    P = 2 ** k - 1
    word = [0] * (P - 1) + [1]
    nmin = max(int(N * 0.22), P * 3)
    vals = nu2_seq(word, N)
    ok, cs = per_residue_affine(vals, P, nmin, N)
    assert ok, f"not affine k={k}"
    return [x // 2 for x in cs]


def is_pow2(x):
    return x >= 1 and (x & (x - 1)) == 0


all_okA = all_okB = all_okC = all_okD = True
for k in range(2, 10):
    R = get_R(k)
    P = 2 ** k - 1
    # (A) ones positions
    ones = [r for r in range(P) if R[r] == 1]
    predicted = [0] + [P - (2 ** j - 1) for j in range(1, k)]
    # note: predicted should equal ones
    okA = (sorted(ones) == sorted(predicted))
    # (B) special at r=1
    okB = (R[1] == 2 ** (k - 1) - 1)
    # (C) all other values powers of 2
    okC = all(is_pow2(R[r]) or r == 1 for r in range(P))
    # (D) sum
    okD = (sum(R) == (3 ** k - 3) // 2)
    all_okA &= okA; all_okB &= okB; all_okC &= okC; all_okD &= okD
    print(f"k={k:2d} P={P:4d} ones@={sorted(ones)}  ones_ok={okA} "
          f"R[1]={R[1]}==2^{k-1}-1?{okB} pow2else={okC} sum_ok={okD}  R={R}")

print()
print(f"ALL k=2..9: A(ones-positions)={all_okA}  B(special R[1])={all_okB} "
      f"C(pow2-elsewhere)={all_okC}  D(sum=3^k-3)={all_okD}")
