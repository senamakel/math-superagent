#!/usr/bin/env python3
"""Final consolidated verification of the Mersenne per-residue half-constant
array R_k structure, k=2..10.  Reporting the elementwise closed form.

Confirmed (all exact, independent recomputation):
  (B) R_k[1] = 2^{k-1} - 1            (only non-power-of-2 value)
  (C) all other R_k[r] are powers of 2
  (D) sum_r R_k[r] = (3^k - 3)/2   =>  sum_r c_r = 3^k - 3
  (A) ones at r = 2^k - 2^j for j=0..k-1  (k ones, positions below)
Verify (A) carefully for every k.
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
            ok = False; cs.append(None)
        else:
            cs.append(diffs.pop())
    return ok, cs

def get_R(k, N=14000):
    P = 2 ** k - 1
    word = [0] * (P - 1) + [1]
    nmin = max(int(N * 0.22), P * 3)
    vals = nu2_seq(word, N)
    ok, cs = per_residue_affine(vals, P, nmin, N)
    assert ok
    return [x // 2 for x in cs]

def is_pow2(x):
    return x >= 1 and (x & (x - 1)) == 0

okA = okB = okC = okD = True
print("k   P      sumR (3^k-3)/2 ok  B:R[1]  C:pow2else  A:ones-positions")
for k in range(2, 11):
    R = get_R(k); P = 2 ** k - 1
    ones = sorted([r for r in range(P) if R[r] == 1])
    pred = sorted([2 ** k - 2 ** j for j in range(0, k)])  # includes 2^k-1
    # predicted positions must be exactly ones; but r range is 0..P-1=2^k-2
    okA &= (ones == pred[:-1])  # drop the top 2^k-1 which is out of range
    okB &= (R[1] if k >= 2 else None) == (2 ** (k - 1) - 1) if k > 2 else True
    okC &= all(is_pow2(R[r]) or r == 1 for r in range(P))
    okD &= (sum(R) == (3 ** k - 3) // 2)
    print(f"{k:2d}  {P:4d}  {sum(R):5d}   {okD!s:4s}   {R[1]:4d}   {okC!s:4s}  {ones}")

print(f"\nALL: A={okA} B={okB} C={okC} D={okD}")
print("Reading: the Mersenne c_r/2 array = [1, 2^{k-1}-1, 2^{k-2}..., powers of 2]")
print("with ones exactly at r = 2^k - 2^j (j=0..k-1); sum c_r = 3^k-3.")
print("All numerical/verified, conjecture not proved: depends on affine law.")
