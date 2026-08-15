#!/usr/bin/env python3
"""Diagnostic: where does the nu2 == subset-zeta-count identification break?

The Thue-Morse 2-then-odds triangle is built exactly.  We compare several
candidate nu2 readings of the right diagonal delta(q_n) against the subset-zeta
count  #{d<=n : zeta(h)[d]=1} = #{powers of two <= n}:

  * total body count: # of 2s in diag[2:-1] that lie in {0,2} positions
    (every {0,2} cell, not just the maximal suffix),
  * the canonical maximal-{0,2}-suffix count (lib.rightdiag.cycle_and_nu2),
  * the RAW subset-zeta fold value at the tail cells.

The note thue-morse-sublinear-supply-witness claims nu2 = #{powers of two<=n}.
We determine which reading (if any) that is, and where the equivalence with
the diagonal nu2 fails.
"""
from math import isqrt


def thue(j):
    return bin(j).count('1') & 1


def subset_zeta(h):
    N = len(h)
    z = list(h)
    b = 1
    while b < N:
        step = b << 1
        for start in range(0, N, step):
            for m in range(start + b, min(start + step, N)):
                z[m] ^= z[m - b]
        b <<= 1
    return z


def pw2count(n):
    return len([p for p in range(1, n + 1) if p & (p - 1) == 0])


def main():
    D = 100
    q = [2, 3]
    for j in range(D + 2):
        q.append(q[-1] + (2 if thue(j) else 4))

    h = [thue(j) for j in range(D + 1)]
    z = subset_zeta(h)
    zcount = sum(1 for d in range(D + 1) if z[d] == 1)
    print("subset-zeta count over d<=%d (== #powers of two) : %d" % (D, zcount))
    print()

    # incremental diagonals
    D0 = [q[0]]
    diags = [D0]
    for n in range(1, D + 1):
        nd = [0] * (n + 1)
        nd[0] = q[n]
        for k in range(1, n + 1):
            nd[k] = abs(nd[k - 1] - D0[k - 1])
        D0 = nd
        diags.append(D0)

    print("n   canon-nu2   all-02-tail-count   zeta-count   delta_tail_vals")
    for n in [1, 2, 3, 4, 5, 7, 8, 9, 10, 16, 32, 50, 64, 100]:
        dd = diags[n]
        body = dd[:-1]
        # canonical maximal {0,2} suffix floored at index 2
        i = len(body)
        while i > 2 and body[i - 1] in (0, 2):
            i -= 1
        canon = body[i:].count(2)
        # all-{0,2} count within body[2:]
        tail02 = sum(1 for x in body[2:] if x in (0, 2))
        zc = pw2count(n)
        # show the {0,2} positions explicitly for the small ones
        print("%-3d %-9d %-17d %-11d %s" % (
            n, canon, tail02, zc, dd[2:]))
    print()
    print("The subset-zeta identity is bn*TRUE* (zeta==1 iff power of two).")
    print("So the claim nu2(n)==#powers-of-two is a claim about the *fold* being")
    print("the nu2 (tail {0,2} count).  The delta values above show the tail is")
    print("NOT just the fold: actual cells include repeated 2/0 patterns that")
    print("are parity-cancelled in the fold XOR.")


if __name__ == "__main__":
    main()
