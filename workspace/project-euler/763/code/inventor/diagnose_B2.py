#!/usr/bin/env python3
"""Diagnose CLAIM B collision properly.

A preimage parent of child C' is a point p NOT in C' such that children(p)
are all in C'; the parent config is (C' - children(p)) | {p}.  count such p
for each child C' and tabulate the preimage-multiplicity distribution.

  sum_C f(C)          = total number of (C,p) forward transitions
  #distinct children  = D(N+1)
  collisions          = sum_C f(C) - D(N+1)
which equals sum over children of (mult-1).
"""
from collections import defaultdict
from lib.amoeba import forward_level, children, lvl

def f_of(C):
    Sset = set(C)
    return sum(1 for p in Sset if all(c not in Sset for c in children(p, 3)))

def preimage_parents(Cp):
    """Empty points p whose full child triangle lies inside Cp."""
    Sset = set(Cp)
    M = max(lvl(p) for p in Sset)
    found = []
    for x in range(M+1):
        for y in range(M+1):
            for z in range(M+1):
                p = (x, y, z)
                if p in Sset:
                    continue
                if lvl(p) + 1 <= M and set(children(p, 3)).issubset(Sset):
                    found.append(p)
    return found

def main():
    level = {frozenset([(0, 0, 0)])}
    for N in range(8):
        Sf = sum(f_of(C) for C in level)
        nxt = forward_level(level, 3)
        mult_dist = defaultdict(int)
        for Cp in nxt:
            mult_dist[len(preimage_parents(Cp))] += 1
        total_preimages = sum(m * c for m, c in mult_dist.items())
        collisions = Sf - len(nxt)
        print(f"N={N}: sum f(C)={Sf}  D(N+1)={len(nxt)}  coll={collisions}  "
              f"sigma mult*count={total_preimages}  "
              f"mult_dist={dict(sorted(mult_dist.items()))}")
        level = nxt

if __name__ == "__main__":
    main()
