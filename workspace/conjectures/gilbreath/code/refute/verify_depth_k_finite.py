#!/usr/bin/env python3
"""Cross-check the refutation of R-depth-k-finite.

Rung claim: S_k = {(2,g_2,...,g_k) : g_i even positive, A_k(1) in {0,2}} is
FINITE for every fixed k: "each gap is bounded by an explicit function of the
others and k".

Refuting family (k=3, g_1=2, g_3=2, g_2 = 2M):
  A_3(1) = ||g_1-g_2| - |g_2-g_3|| = ||2-2M| - |2M-2|| = |X - X| = 0.

This file computes it two independent ways and checks the family is infinite.

NOTE: I cannot execute this (no shell tool in this environment), but the
arithmetic is identical to the defining formula in research/weakened/
depth-survival-ladder.md, quoted verbatim below. The identity |a-b|=|b-a|
makes A_3(1)=0 identically; no numerics are needed beyond that cancellation.
"""
def A3_defn(g1, g2, g3):
    # verbatim from depth-survival-ladder.md:
    #   A_3(1) = ||g_1 - g_2| - |g_2 - g_3||
    return abs(abs(g1 - g2) - abs(g2 - g3))

def full_triangle_A3(g1, g2, g3):
    # independent route: build A_0 = (2,3,3+g1,3+g1+g2,3+g1+g2+g3)
    # and run the actual row-by-row absolute-difference triangle, read A_3(1).
    a0 = [2, 3, 3+g1, 3+g1+g2, 3+g1+g2+g3]
    rows = [a0]
    while len(rows[-1]) > 1:
        p = rows[-1]
        rows.append([abs(p[i]-p[i+1]) for i in range(len(p)-1)])
    return rows[3][1]

# exhaustive check over a wide range: every M must give 0 in both routes
mismatch = 0
for M in range(1, 2001):
    g2 = 2*M
    v1 = A3_defn(2, g2, 2)
    v2 = full_triangle_A3(2, g2, 2)
    if v1 != 0 or v2 != 0 or v1 != v2:
        mismatch += 1
        print(f"  MISMATCH M={M}: defn={v1} full={v2}")
print(f"Checked M=1..2000 (g_2=2..4000): mismatches={mismatch}, all values 0")
print("=> (2, 2M, 2) in S_3 for ALL M. g_2 unbounded with g_1=g_3=k=3 fixed.")
print("=> S_3 is INFINITE. R-depth-k-finite's 'each gap bounded by a function")
print("   of the others and k' is FALSE.")
