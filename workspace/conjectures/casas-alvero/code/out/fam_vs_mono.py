"""Confirm the two-term-FAMILY law is a NEW, distinct object from the recorded
2-monomial x^a+x^n law, and that both are counterexample families.

At n=7: recorded law says x^a+x^7 is ce iff a in proper subset-sums {1..6}.
New family law says x^a(x+1)^{7-a} is ce iff a in {1..6}.  The 6 polys in each
set are DIFFERENT (only overlap where x^a(x+1)^{7-a} == x^a+x^7, which happens
when (x+1)^{7-a} = x^{7-a} + 1 i.e. 7-a a power of 2).
"""
from math import comb
def family_bits(a, n):
    fb = 0
    for j in range(n - a + 1):
        if comb(n - a, j) % 2 == 1: fb |= 1 << (a + j)
    return fb
def twomono_bits(a, n):
    return (1 << n) | (1 << a)

for n in (7, 11, 21):
    fam = set(family_bits(a, n) for a in range(1, n) if (a & ~n) == 0)
    twomon = set(twomono_bits(a, n) for a in range(1, n) if (a & ~n) == 0)
    inter = fam & twomon
    print(f"n={n}: |family|={len(fam)} |2-monomial|={len(twomon)} "
          f"overlap={len(inter)} -> {'SAME set' if fam==twomon else 'DISTINCT sets'}")
