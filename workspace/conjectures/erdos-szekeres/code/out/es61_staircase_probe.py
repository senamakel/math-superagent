"""Probe: ES61 staircase placement of cup/cap blocks, verified by exact oracle.

Per research/summaries/erdos-szekeres-1961-construction-concrete.md, the full
2^(n-2)-point set S = union_{k=1}^{n-1} S_k is built with:
  * within each S_k all slopes are positive,
  * the slopes of lines joining S_k to S_{k+1} are negative and steep
    (in ~(-1/(n-k), -1/(n-k-1))),
so that a convex-position subset Y = union_i P_i (P_i subset S_{k_i},
k_1<...<k_r) has |P_1| as a concave/cap (<=k_1 pts), |P_r| a convex/cup
(<= n-k_r+1 pts... matching bounds), interior singletons, hence |Y| <= n-1.

Here I place blocks left-to-right in x, each internally flat and positive
slope, lift each successive block so every cross slope (i < j) is negative
and steep.  Then check the FULL set with the exact largest_convex_subset
oracle at n=4,5,6.
"""
from fractions import Fraction
from lib.es_geom import largest_convex_subset, in_general_position, longest_cup, longest_cap
from lib.es_lower import g as block_g, _flatten, _bbox


def es61_staircase(n, internal=Fraction(1, 20), cross=Fraction(-1, 3)):
    """Blocks T_i = g(i+2, n-i), flat with tiny internal slopes. Place
    left-to-right; lift block j so every cross slope i->j (i<j) is steep
    negative, far beyond internal slopes."""
    blocks = []
    for i in range(n - 1):
        T = block_g(i + 2, n - i)     # |T| = C(n-2,i), no (i+2)-cup no (n-i)-cap
        if i == 0 or i == n - 2:
            T = [(Fraction(0), Fraction(0))]
        else:
            T = _flatten(T, internal)
        blocks.append(T)
    # place incrementally
    placed = []      # (block, x0)
    cur_x = Fraction(0)
    for T in blocks:
        if len(T) == 1:
            placed.append((T, cur_x))
            cur_x += Fraction(10)
            continue
        placed.append((T, cur_x))
        cur_x += max(x for x, y in T) + Fraction(10)
    # now assign y-position to put block j above block i with steep negative cross slope.
    # We process in order: keep running position. Each block gets a y-offset so
    # slope from an earlier block's top to this block = cross (negative steep).
    out = []
    ycur = Fraction(0)
    prev_x_max = None
    prev_y_max = None
    for idx, (T, x0) in enumerate(placed):
        if len(T) == 1:
            out.append((x0, ycur))
            prev_x_max = x0
            prev_y_max = ycur
            continue
        xs_max = max(x for x, y in T)
        cur_y0 = None
        if prev_x_max is not None:
            # want cross slope = (ycur - prev_y_max) / (x0 - prev_x_max) = cross (neg)
            # but every previous point up to prev top: use steepest guarantee.
            ycur = prev_y_max + cross * (x0 - prev_x_max)
        for (px, py) in T:
            out.append((x0 + px, ycur + py))
        prev_x_max = x0 + xs_max
        prev_y_max = max(y for x, y in T) + ycur
    return out


for n in (4, 5, 6):
    S = es61_staircase(n)
    gp = in_general_position(S)
    k, why = largest_convex_subset(S)
    good = len(S) == 2 ** (n - 2) and gp and k == n - 1
    print(f"n={n}: |S|={len(S)} exp={2**(n-2)} gp={gp} maxConvex={k} expect {n-1} -> {'PASS' if good else 'FAIL'}")
    if k != n - 1 and n <= 5:
        print("   witness blocks:", [round(float(x) / 10) for x, y in why])
