#!/usr/bin/env python3
"""Attack the Mersenne c_r/2 elementwise recursion: compute the arrays A_k
fresh from the run's own per-residue affine extraction (k=2..10), then test
the elementwise recursion A_{k+1} = g(A_k) EXACTLY, and use it (if it holds)
to derive sum(A_k) = (3^k-3)/2 by induction.

The recursion (verbatim reading of the observed pattern):
  A_{k+1} = [1] + b1 + b2   (length 2P+1, P = 2^k - 1)
  b1 = [2*A_k[1]+1] + [2*A_k[i] for i=2..P-1] + [2]
  b2 = A_k with A_k[1] incremented by 1
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
        ds = {vals[n + P] - vals[n] for n in range(nmin, nmax - P + 1)
              if n % P == r}
        if len(ds) != 1:
            ok = False
            cs.append(None)
        else:
            cs.append(ds.pop())
    return ok, cs


def recursion(Ak, P):
    b1 = [2 * Ak[1] + 1] + [2 * a for a in Ak[2:]] + [2]
    b2 = list(Ak)
    b2[1] = b2[1] + 1
    assert len(b1) == P and len(b2) == P
    return [1] + b1 + b2


def main():
    A = {}
    N = 6000
    nmin = 800
    arrays_ok = True
    for k in range(2, 11):
        P = 2 ** k - 1
        word = [0] * (P - 1) + [1]
        vals = nu2_seq(word, N)
        ok, cs = per_residue_affine(vals, P, nmin, N)
        if not ok:
            arrays_ok = False
            print(f"k={k} P={P} affine FAILED")
            continue
        c2 = [c // 2 for c in cs]
        A[k] = c2
        s = sum(cs)
        print(f"k={k:2d} P={P:5d} affine={ok} sum_c={s} target_3k-3={3**k-3} match={s==3**k-3}")

    print("\n--- elementwise recursion test ---")
    all_ok = True
    for k in list(A)[:-1]:
        if k + 1 not in A:
            continue
        Ak = A[k]; P = len(Ak)
        rec = recursion(Ak, P)
        if rec != A[k + 1]:
            all_ok = False
            print(f"k={k} -> k+1: MATCH FAILED")
            for i, (r, a) in enumerate(zip(rec, A[k + 1])):
                if r != a:
                    print(f"   first mismatch idx {i}: rec={r} actual={a}")
                    break
        else:
            print(f"k={k} -> {k+1}: elementwise MATCH (len {P} -> {len(A[k+1])})")
    print("ALL k match:", all_ok)

    # induction: sum(A_k) = (3^k-3)/2 from recursion
    if all_ok:
        print("\n--- induction check ---")
        for k in A:
            Sa = sum(A[k])
            print(f"k={k}: sum(A_k)={Sa}  (3^k-3)/2={(3**k-3)/2 if (3**k-3)%2==0 else 'odd'} "
                  f"exact={Sa==(3**k-3)//2}")


if __name__ == "__main__":
    main()
