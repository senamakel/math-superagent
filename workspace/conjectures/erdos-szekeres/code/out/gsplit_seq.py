#!/usr/bin/env python3
"""Sequence: number of valid gsplit halves (both of size 2^{n-3}, (n-1)-avoiding)
on the verified es_construct, for n=4..7 using the validated rotating-line
enumerator. n=4 included (not in gsplit_phase2 with provenance)."""
from lib.es_construct import es_set_blocks
from lib.es_geom import orient, in_general_position, has_convex_k_subset


def ordered_pair_sides(points):
    N = len(points)
    res = set()
    for a in range(N):
        for b in range(N):
            if a == b:
                continue
            strict = frozenset(x for x in range(N)
                               if orient(points[a], points[b], points[x]) > 0)
            for extra in (frozenset(), frozenset([a]), frozenset([b]),
                          frozenset([a, b])):
                side = strict | extra
                if 0 < len(side) < N:
                    res.add(side)
    return res


seq = []
for n in (4, 5, 6, 7):
    allp, blocks = es_set_blocks(n)
    N = len(allp)
    op = ordered_pair_sides(allp)
    match = (len(op) == N * (N - 1))
    target = 2 ** (n - 3)
    valid = 0
    for side in op:
        if len(side) != target:
            continue
        comp = frozenset(range(N)) - side
        if len(comp) != target:
            continue
        L_av = not has_convex_k_subset([allp[i] for i in side], n - 1)[0]
        R_av = not has_convex_k_subset([allp[i] for i in comp], n - 1)[0]
        if L_av and R_av:
            valid += 1
    seq.append(valid)
    print(f"n={n}: N={N} sides={len(op)} (N(N-1)={N*(N-1)} match={match}) "
          f"VALID splits={valid}")
print("SEQ valid splits n=4..7:", seq)
