#!/usr/bin/env python3
"""Probe whether the excess-coordinate stabilization of the maximal safe set
holds beyond M=3 (the small box of the first-step). For each M in {3,4,5,6}
and K=2..KMAX report:
  - |S_K| in raw and in excess-projected coordinates,
  - the set of attainable excess values at each coordinate position,
  - whether the projected set equals a full product box {t_1=0} x {t_2 subset} x free,
  - the Pareto frontier (a compact invariant signature).

Falsifier for the invariant candidate: if the family of attainable-excess sets
changes with M (t_2 restricted differently, or later coordinates constrained),
then the M=3 stabilization is a small-box artifact, not a parametric invariant.
"""
from itertools import product

KMAX = 7


def H(w):
    return tuple(abs(w[i] - w[i + 1]) for i in range(len(w) - 1))


def backward_S(M, KMAX):
    S = {0: {()}}
    for k in range(1, KMAX + 1):
        prev = S[k - 1]
        S[k] = {w for w in product(range(M + 1), repeat=k)
                if w[0] <= 1 and H(w) in prev}
    return S


def excess(w):
    return tuple(max(0, x - 1) for x in w)


def frontier(eset, k):
    par = []
    for p in eset:
        dominated = any(q != p and all(q[i] >= p[i] for i in range(k)) for q in eset)
        if not dominated:
            par.append(p)
    return sorted(par)


def analyze(M, KMAX):
    S = backward_S(M, KMAX)
    print(f"\n########## M = {M} ##########")
    for k in range(2, KMAX + 1):
        eset = {excess(w) for w in S[k]}
        # per-position attainable excess values
        vals = [sorted({t[i] for t in eset}) for i in range(k)]
        front = frontier(eset, k)
        # product-box test: projected set == {t_1=0} x {t_2 subset} x (all combos >= pos 3)
        # full box over the per-position value sets:
        box = set(product(*[tuple(v) for v in vals]))
        is_product = (box == eset)
        nnz = [v for v in vals]  # value sets
        print(f"  K={k:2d} |S|raw={len(S[k]):7d} |excess|={len(eset):7d} "
              f"attainable-excess-vecs={vals}")
        print(f"          isFullProductBox(over attainable sets)={is_product}  frontier={front}")
    return S


def main():
    for M in (3, 4, 5, 6):
        analyze(M, KMAX)
    print("\nDONE")


if __name__ == "__main__":
    main()
