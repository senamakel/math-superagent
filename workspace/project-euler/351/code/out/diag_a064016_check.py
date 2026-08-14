#!/usr/bin/env python3
"""Diagonal A063985(10^k) vs catalogue A064016: independent verification.

Route: fresh implementation of Chai Wah Wu's recursion (OEIS A063985,
'totient-sum-fast-recursion' claim) — the independent route used by the run —
computes A(10^k) for k=0..8 and compares against the catalogued A064016
terms (recorded in research/summaries/oeis_a064016.md). The k=8 term is
A(10^8) = A063985(10^8) = 1960364533634092, which anchors H(10^8).

This is a second, independent route to the diagonal: the catalogued b-file
versus a recursion that shares no code with the stored 200000-term prefix.
"""
from functools import lru_cache

# Catalogued A064016 terms (from research/summaries/oeis_a064016.md, source OEIS)
CAT = [0, 23, 2006, 196308, 19607514, 1960399246, 196036947608,
       19603648572758, 1960364533634092]


@lru_cache(maxsize=None)
def A063985_rec(n):
    """Chai Wah Wu recursion for A063985(n) = n(n+1)/2 - Phi(n)."""
    if n == 0:
        return 0
    c, j = 0, 2
    k1 = n // j
    while k1 > 1:
        j2 = n // k1 + 1
        c += (j2 - j) * (k1 * (k1 + 1) - 2 * A063985_rec(k1) - 1)
        j, k1 = j2, n // j2
    return (2 * n + c - j) // 2


for k in range(0, 9):
    got = A063985_rec(10 ** k)
    print(f"A(10^{k}) = {got}  catalogue = {CAT[k]}  MATCH={got == CAT[k]}")
    assert got == CAT[k], f"mismatch at k={k}"
print("OK: diagonal A(10^k), k=0..8, matches catalogue A064016 exactly.")
