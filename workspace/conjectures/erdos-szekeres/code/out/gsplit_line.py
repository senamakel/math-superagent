#!/usr/bin/env python3
"""Binomial even/odd split identity + line-separability of ES construction.

1. Exact identity: sum_{i even} C(m,i) = sum_{i odd} C(m,i) = 2^{m-1}, m>=1.
2. Does a straight line separate even-indexed from odd-indexed blocks of the
   (correct) es_construct ES construction?  G-split needs a separating line.
   We scan the number of misclassified points over candidate lines.
"""
from math import comb
from lib.es_construct import es_set_blocks


print("Binomial identity sum_{i even} C(m,i) = 2^{m-1} for m = n-2:")
for m in range(1, 9):
    row = [comb(m, i) for i in range(m + 1)]
    ev = sum(row[::2]); od = sum(row[1::2])
    ok = (ev == 2**(m-1) and od == 2**(m-1))
    print(f"  m={m}: even-sum={ev} odd-sum={od} both=2^{m-1}={2**(m-1)} "
          f"{'OK' if ok else 'BAD'}")
print()


def orient(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])


def separation_line(points_a, points_b):
    """Find a line (as oriented pair) with all A on one side, all B on the
    other.  Brute over lines through pairs; else return None."""
    allpts = points_a + points_b
    for i in range(len(allpts)):
        for j in range(i + 1, len(allpts)):
            a, b = allpts[i], allpts[j]
            sA = {orient(a, b, p) for p in points_a}
            sB = {orient(a, b, p) for p in points_b}
            # want A all >=0 (or all <=0) and B the opposite sign set
            if (max(sA) <= 0 and min(sB) >= 0) or (max(sB) <= 0 and min(sA) >= 0):
                # strict: no point on line
                if 0 not in sA and 0 not in sB:
                    return (a, b)
                # allow line through none? need strict separation: all nonzero,
                # one group positive, other negative
                if max(sA) < 0 and min(sB) > 0:
                    return (a, b)
                if max(sB) < 0 and min(sA) > 0:
                    return (a, b)
    return None


def try_split(n, even_side=True):
    _all, blocks = es_set_blocks(n)
    A, B = [], []
    for i, blk in enumerate(blocks):
        (A if i % 2 == 0 else B).extend(blk)
    line = separation_line(A, B)
    return len(A), len(B), line is not None


print("Line-separability of even vs odd block halves (strict line):")
for n in (5, 6, 7):
    la, lb, sep = try_split(n)
    print(f"  n={n}: |even|={la} |odd|={lb} strictly-line-separable={sep}")
