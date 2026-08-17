#!/usr/bin/env python3
"""Structural hypothesis for the Bautin focal-value monomial counts.

The 6-term sequence a_d = (4, 30, 97, 236, 485, 890) = number of monomials of
the d-th focal value L_d in the 5 parameters (A,C,D,E,F), d=4,6,8,10,12,14.

Hypothesis: L_d is invariant under the rotational symmetry of the normal form
(the rotation part rot = -v du + u dv), so it is spanned ONLY by monomials of
zero rotational weight.  If the 5 parameters carry weights such that the
degree-4 obstruction's monomials (AC, CD, DF, EF) are all weight 0, then the
predicted count at degree h = d-2 is the number of degree-h monomials in 5 vars
with total weight zero.

Route A (phenomenological): solve weights from L4 = (AC+CD+2DF-EF)/8 requiring
each of its monomials weight 0, giving per-parameter weights.
Route B (first-principles): build the actual 5x5 representation of the rotation
generator on the quadratic part (Q1,Q2) and read the true weights off the
diagonalized operator; then weight-0 selection count.

Route A weights come out to: w(A)=+1, w(C)=-1, w(D)=+1, w(E)=+1, w(F)=-1 (up
to sign & scale).  We compute the weight-0 monomial count for each h and
compare with a_d.  This is a test over the terms supplied; it does NOT prove
the symmetry explanation unless weights from Route B agree AND counts match.
"""
from itertools import product
from math import comb


def weight0_count(h, weights):
    """# degree-h monomials in 5 vars with total weight 0, weights dict keyed A,C,D,E,F."""
    names = "ACDEF"
    cnt = 0
    total = 0
    for exps in product(range(h + 1), repeat=5):
        if sum(exps) != h:
            continue
        total += 1
        wsum = sum(weights[n] * e for n, e in zip(names, exps))
        if wsum == 0:
            cnt += 1
    return cnt, total


# Route A: weights derived from L4 monomials AC, CD, DF, EF all weight 0.
weightsA = {"A": 1, "C": -1, "D": 1, "E": 1, "F": -1}

actual = {4: 4, 6: 30, 8: 97, 10: 236, 12: 485, 14: 890}
print("actual a_d:", actual)
print()
print("hypothesis A (weights A:+1 C:-1 D:+1 E:+1 F:-1): weight-0 monomial count")
for d, h in zip((4, 6, 8, 10, 12, 14), (2, 4, 6, 8, 10, 12)):
    cnt, total = weight0_count(h, weightsA)
    print(f"  d={d:2d} h={h:2d} weight0={cnt:4d} / dim={total:4d}   actual={actual[d]:4d}  match={cnt==actual[d]}")

# also try the other sign
weightsA_neg = {k: -v for k, v in weightsA.items()}
print("\nhypothesis A' (all weights negated — should be identical count):")
for d, h in zip((4, 6, 8, 10, 12, 14), (2, 4, 6, 8, 10, 12)):
    cnt, _ = weight0_count(h, weightsA_neg)
    print(f"  d={d:2d} weight0={cnt:4d}")
