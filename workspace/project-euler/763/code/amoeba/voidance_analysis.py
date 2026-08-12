import sys
from lib.amoeba import next_level_fs, triangle_parent


def c(S):
    S = set(S)
    rem, steps = 0, 0
    while S != {(0, 0, 0)}:
        M = max(a + b + c for (a, b, c) in S)
        top = {(a, b, c) for (a, b, c) in S if a + b + c == M}
        assert len(top) == 3
        p = triangle_parent(top)
        assert p is not None and p not in S
        for k in top:
            S.remove(k)
        S.add(p)
        rem += 3
        steps += 1
    return rem, steps


level = {frozenset({(0, 0, 0)})}
LV = {0: level}
for n in range(1, 7):
    level = next_level_fs(level)
    LV[n] = level

print("N | D(N) | void-set-size -> #configs | steps set")
for n in range(0, 7):
    sizes, stepset = {}, set()
    for S in LV[n]:
        vs, st = c(S)
        sizes[vs] = sizes.get(vs, 0) + 1
        stepset.add(st)
    print(f"N={n} D={len(LV[n])}: sizes={dict(sorted(sizes.items()))} steps={stepset}")
