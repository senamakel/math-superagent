#!/usr/bin/env python3
"""Extract ALL k>=6 grids (repeats allowed) from the oracle's near-miss box
c = e^2, e <= 80, |u|,|v| <= 120, and classify by difference structure.
Reconciles the oracle note's '4 seven-square grids' with my
difference-sieve, which found no u,v,u+v in S(e) for e <= 10^7.
"""
from math import isqrt


def grid_from_params(c, u, v):
    return [
        [c + u, c - u - v, c + v],
        [c - u + v, c, c + u - v],
        [c - v, c + u + v, c - u],
    ]


def is_sq(x):
    return x > 0 and isqrt(x) ** 2 == x


def main():
    E_MAX, V_MAX = 80, 120
    sevens = []
    sixes = []
    for e in range(1, E_MAX + 1):
        c = e * e
        for u in range(-V_MAX, V_MAX + 1):
            for v in range(-V_MAX, V_MAX + 1):
                g = grid_from_params(c, u, v)
                entries = g[0] + g[1] + g[2]
                if any(x < 1 for x in entries):
                    continue
                k = sum(1 for x in entries if is_sq(x))
                if k >= 7:
                    sevens.append((e, u, v, k, entries))
                elif k == 6:
                    sixes.append((e, u, v, k, entries))
    print(f"k=7 grids: {len(sevens)}")
    for e, u, v, k, ent in sevens:
        U, V = abs(u), abs(v)
        # which of the eight off-centre entries are squares
        sq = [(x, is_sq(x)) for x in ent]
        pat = "".join("1" if s else "0" for _, s in sq)
        print(f"  e={e} u={u} v={v} U={U} V={V} U+V={U+V} U-V={U-V} "
              f"k={k} distinct={len(set(ent))} pattern={pat} entries={ent}")
    print(f"k=6 grids: {len(sixes)}  distinct-entry among them: "
          f"{sum(1 for _,_,_,_,e in sixes if len(set(e)) == 9)}")
    # distinct k=6 examples if any
    for e, u, v, k, ent in sixes:
        if len(set(ent)) == 9:
            print(f"  distinct k=6: e={e} u={u} v={v} entries={ent}")


if __name__ == "__main__":
    main()