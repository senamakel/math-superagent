"""Descending-staircase ES61 lower-bound construction, exact-oracle verified.

ES61 (see primary source lines 180-215): blocks S_k (k=1..n-1), |S_k|=C(n-2,k-1),
placed so that (i) within each block all slopes are POSITIVE, (ii) the slope of
any line joining S_k to S_l (k<l) is NEGATIVE and steep.  Then a convex-position
subset P = union P_i (P_i subset S_{k_i}) has P_1 a cap (<= k_1 pts), P_r a cup
(<= n-k_r pts... matching bounds) and every interior P_i a singleton, so
|P| <= n-1, i.e. NO convex n-gon.

Block T_i = g(n-i, i+2) has no (n-i)-cup and no (i+2)-cap (size C(n-2,i)),
internally all slopes positive (built up-right by lib.es_lower.g).

Placement: blocks go to the right (x = i*W) and DOWN (y = -i*H) so every
cross slope is negative steep; within-block slopes are tiny positive.
"""
from fractions import Fraction
from lib.es_geom import largest_convex_subset, in_general_position, longest_cup, longest_cap
from lib.es_lower import g as block_g, _flatten, _bbox


def _block(n, i):
    T = block_g(n - i, i + 2)
    T = _flatten(T, Fraction(1, 20))
    return T


def staircase(n, W=Fraction(20), H=Fraction(40)):
    """Blocks at x=i*W, y=-i*H, each scaled tiny. Cross slope scale ~= -H/W."""
    scl = Fraction(1, 10 ** 3)
    out = []
    for i in range(n - 1):
        T = _block(n, i)
        cx, cy = Fraction(i) * W, -Fraction(i) * H
        for (px, py) in T:
            out.append((cx + scl * px, cy + scl * py))
    return out


for n in (4, 5, 6):
    S = staircase(n)
    gp = in_general_position(S)
    k, why = largest_convex_subset(S)
    good = len(S) == 2 ** (n - 2) and gp and k == n - 1
    print(f"n={n}: |S|={len(S)} exp={2**(n-2)} gp={gp} maxConvex={k} expect {n-1} -> {'PASS' if good else 'FAIL'}")
