#!/usr/bin/env python3
"""Lean claim check A1/A2 for the large N=13..14 frontiers.

The full definitive_check.py runs the expensive A3 (iterate cap-collapse) per
config, which over the ~5.9M-config N=14 frontier exceeds the 600 s tool
budget.  This probe checks only the *cheap* top-cap claims on those levels:

  A1      : every reachable N-config has exactly 3 cells on its max level M.
  A2_tri  : those 3 cells are {p+e1,p+e2,p+e3} for a single parent p at M-1.
  A2_empty: (stronger) that parent p is NOT in the config.

A3 and B on N<=12 are already established by definitive_check.py /
check_recurrence.py; B on N=13..14 equals sum f(C) vs D(N+1) which we also
report (f computation is cheap).

Exact bitmask BFS (lib.amoeba.next_level_bits), transient decode per config.
Frontier bounded to the 2GiB cap (5.9M at N=14).
"""
import sys
import time

from lib.amoeba import next_level_bits, decode_bits, children, f_of, lvl


def top_parent_present(cells, top):
    a, b, c = sorted(top)
    s = (a[0] + b[0] + c[0] - 1, a[1] + b[1] + c[1] - 1, a[2] + b[2] + c[2] - 1)
    if s[0] % 3 or s[1] % 3 or s[2] % 3:
        return None, False
    p = (s[0] // 3, s[1] // 3, s[2] // 3)
    if set(children(p, 3)) == set(top):
        return p, p in cells
    return None, False


def main(Nmax=14):
    W = Nmax + 1
    level = {1}
    t0 = time.time()
    for n in range(1, Nmax + 1):
        gen_s = time.time()
        level = next_level_bits(level, W)
        gen_e = time.time()
        a1 = a2tri = a2emp = 0
        s_f = 0
        chk_s = time.time()
        for S in level:
            cells = decode_bits(S, W)
            Sset = set(cells)
            M = max(lvl(p) for p in Sset)
            top = [p for p in Sset if lvl(p) == M]
            if len(top) != 3:
                a1 += 1
            par, pres = top_parent_present(Sset, top)
            if par is None:
                a2tri += 1
                a2emp += 1
            elif pres:
                a2emp += 1
            s_f += f_of(cells)
        chk_e = time.time()
        Dp1 = len(next_level_bits(level, W)) if n < Nmax else None
        Byes = (s_f == Dp1) if Dp1 is not None else None
        print(f"N={n} D={len(level)} A1bad={a1} A2tri_bad={a2tri} "
              f"A2empty_bad={a2emp} sum_f={s_f} D(N+1)={Dp1} Bmatch={Byes} "
              f"gen={gen_e-gen_s:.1f}s check={chk_e-chk_s:.1f}s",
              flush=True)
    print(f"elapsed {time.time()-t0:.1f}s")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 14)
