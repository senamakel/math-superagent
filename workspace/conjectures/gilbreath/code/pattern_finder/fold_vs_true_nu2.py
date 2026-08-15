#!/usr/bin/env python3
"""Check whether the TRUE nu2 (maximal {0,2} suffix of right diagonal)
equals the FOLD WEIGHT (number of fold cells c=1..n-3 with fold bit 1,
i.e. the subset-zeta sum over F2) for the Mersenne tail-1 words.

This matters: nu2 = #{d : zeta(h)[d]=1} is computed by the PROVED
subset-zeta / Rule-90 fold structure, so if the true maximal-{0,2}-suffix
nu2 equals the fold weight, the per-residue affine law (and sum c_r = 3^k-3)
may be derivable, elevating the documented conjecture to a proof.
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


def submasks(c):
    out = []
    i = c
    while True:
        out.append(i)
        if i == 0:
            break
        i = (i - 1) & c
    return out


def fold_weight(h, n):
    """fold weight over cells c=1..n-3 using last (n-2) entries of h
    (m = n-2, cells 1..m-1)."""
    mm = n - 2
    base = len(h) - mm
    w = 0
    for c in range(1, mm):
        s = 0
        for i in submasks(c):
            s ^= h[base + mm - 1 - c + i]
        w += s
    return w


def true_nu2(word, n):
    q = build_seq(word, n + 1)
    d = None
    for k, dd in enumerate(incremental_diagonals(q)):
        if k == n:
            d = dd
            break
    return cycle_and_nu2(d)[1]


def main():
    print("Compare TRUE nu2 (max {0,2} suffix) vs FOLD WEIGHT, on Mersenne tail-1 words.\n")
    for k in (2, 3, 4):
        P = 2 ** k - 1
        word = [0] * (P - 1) + [1]
        # build full h of length n+2
        h = [word[j % len(word)] for j in range(200 + 2)]
        diffs = 0
        for n in range(6, 200):
            t = true_nu2(word, n)
            f = fold_weight(h[:n], n)
            if t != f:
                diffs += 1
                if diffs <= 5:
                    print(f"  k={k} n={n}: true={t} fold={f} DIFFER")
        print(f"k={k} P={P}: fold==true over n=6..199?  {'YES (0 diffs)' if diffs==0 else str(diffs)+' diffs'}")


if __name__ == "__main__":
    main()
