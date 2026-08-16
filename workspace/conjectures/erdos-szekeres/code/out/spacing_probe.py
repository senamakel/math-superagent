"""Probe how block separation on the convex arc affects the max convex subset.
Goal: find an exact-rational placement of T_i = g(n-i,i+2) (no (n-i)-cup,
no (i+2)-cap) at distinct arc points where interior blocks contribute <=1 to
any convex subset, giving largest convex subset == n-1.
"""
from fractions import Fraction
from lib.es_geom import largest_convex_subset, in_general_position
from lib.es_lower import g as block_g, _flatten


def place(n, sep_num, sep_den, scale_num, scale_den):
    blocks = []
    for i in range(n - 1):
        T = block_g(n - i, i + 2)
        T = _flatten(T, Fraction(1, 20))
        blocks.append(T)
    out = []
    sep = Fraction(sep_num, sep_den)
    scl = Fraction(scale_num, scale_den)
    for i, T in enumerate(blocks):
        cx, cy = Fraction(i) * sep, (Fraction(i) * sep) ** 2
        for (px, py) in T:
            out.append((cx + scl * px, cy + scl * py))
    return out


for n in (5, 6):
    print(f"=== n={n} ===")
    for sep in [(10, 1), (100, 1), (10 ** 4, 1)]:
        for scl in [(1, 10 ** 2), (1, 10 ** 4), (1, 10 ** 6)]:
            S = place(n, sep[0], sep[1], scl[0], scl[1])
            gp = in_general_position(S)
            if not gp:
                res = "gp=False"
            else:
                k, why = largest_convex_subset(S)
                res = f"maxConvex={k} expect {n-1} -> {'PASS' if k==n-1 else 'FAIL'}"
            print(f"  sep={sep} scale={scl} : {res}")
