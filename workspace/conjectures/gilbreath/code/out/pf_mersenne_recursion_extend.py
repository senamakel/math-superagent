#!/usr/bin/env python3
"""Push the Mersenne elementwise recursion attack to k=11,12 (beyond the
run's tested k=2..10).  What a larger run would settle: whether the
elementwise recursion A_{k+1}=g(A_k) and the derived induction
sum(c_r)=3^k-3 survive past the data that suggested them.  The first k
that breaks the recursion (or the sum identity) is the first falsifying term.
"""
import sys
sys.path.insert(0, '/workspace/code')
from lib.rightdiag import incremental_diagonals, cycle_and_nu2


def build_seq(word, n_terms):
    q = [2, 3]; per = len(word)
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
    cs = []; ok = True
    for r in range(P):
        ds = {vals[n + P] - vals[n] for n in range(nmin, nmax - P + 1) if n % P == r}
        if len(ds) != 1:
            ok = False; cs.append(None)
        else:
            cs.append(ds.pop())
    return ok, cs


def recursion(Ak, P):
    b1 = [2 * Ak[1] + 1] + [2 * a for a in Ak[2:]] + [2]
    b2 = list(Ak); b2[1] = b2[1] + 1
    assert len(b1) == P and len(b2) == P
    return [1] + b1 + b2


A = {}
for k in range(2, 13):
    P = 2 ** k - 1
    N = P * 6 + 1000
    nmin = P * 2 + 100
    vals = nu2_seq([0] * (P - 1) + [1], N)
    ok, cs = per_residue_affine(vals, P, nmin, N)
    print(f"k={k:2d} P={P:5d} affine={ok} sum_c={sum(cs) if ok else 'NA'} "
          f"target={3**k-3} match={ok and sum(cs)==3**k-3} nmin={nmin} N={N}")
    if ok:
        A[k] = [c // 2 for c in cs]

print("\n--- elementwise recursion test (extended) ---")
all_ok = True
for k in sorted(A)[:-1]:
    if k + 1 not in A: continue
    rec = recursion(A[k], len(A[k]))
    if rec != A[k + 1]:
        all_ok = False
        print(f"k={k}->{k+1}: FAILED")
        for i, (r, a) in enumerate(zip(rec, A[k + 1])):
            if r != a:
                print(f"   idx {i} rec={r} actual={a}"); break
    else:
        print(f"k={k}->{k+1}: elementwise MATCH len {len(A[k])}->{len(A[k+1])}")
print("ALL:", all_ok)
