#!/usr/bin/env python3
"""Find the exact array recursion R_{k+1} = F(R_k) for the Mersenne
per-residue half-constant arrays.  Given sum R_k = (3^k-3)/2 satisfies
S_{k+1} = 3 S_k + 3, the recursion F, once found, proves the sum identity
by induction (conditional on the documented affine law).

Let R3=[1,3,2,2,1,2,1], R4=[1,7,4,4,2,4,2,2,1,4,2,2,1,2,1].
Search for a block/palindromic construction of R_{k+1} from R_k.
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
    assert ok
    return [x // 2 for x in cs]


R = {k: get_R(k) for k in range(2, 7)}
for k in range(2, 6):
    print(f"R{k} sum={sum(R[k])}  (3^{k}-3)/2={(3**k-3)//2}")

# Try palindromic/block structure: R_{k+1} built from R_k via doubling+()
# Guess: R_{k+1} = [1] + [2*R_k[i] + something]
print("\n--- align R_{k+1} to 2*R_k, find the insertion ---")
for k in range(2, 5):
    Rk = R[k]; Rn = R[k + 1]
    Pk = len(Rk); Ln = len(Rn)
    d = [Rn[r] - 2 * Rk[r] for r in range(1, Pk)]  # align Rn[r] with 2*Rk[r]?
    print(f"k={k}: Rn[1:{Pk}] - 2*Rk[1:{Pk}] misfit pattern:")
    # Instead print Rn and 2*Rk with index alignment Rn[r] vs 2*Rk[r]
    print("  Rn   :", Rn)
    print("  2*Rk :", [2*x for x in Rk])
    # how are the lengths related? Ln = 2Pk+1.  Rn has 2Pk+1 entries.
    # Maybe Rn[2r] and Rn[2r+1] each map to Rk[r]-based values.
    # Test: Rn[2r] == Rk[r] and Rn[2r+1] == Rk[r] + Rk[r+1]? Let's print
    ev = [Rn[2*r] for r in range(Pk)]
    od = [Rn[2*r+1] for r in range(Pk)]
    print("  Rn[2r]  :", ev)
    print("  Rn[2r+1]:", od)
    print("  Rk      :", Rk)
    print()
