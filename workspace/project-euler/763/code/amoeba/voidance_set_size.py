import sys
sys.path.insert(0, '/workspace/code')
from lib.amoeba import next_level_fs, triangle_parent


def voidance(S):
    all_occ = set(S)
    S = set(S)
    while S != {(0, 0, 0)}:
        M = max(a + b + c for (a, b, c) in S)
        top = {(a, b, c) for (a, b, c) in S if a + b + c == M}
        assert len(top) == 3
        p = triangle_parent(top)
        assert p is not None and p not in S
        for k in top:
            S.remove(k)
        S.add(p)
        all_occ.update(S)
    return all_occ - {(0, 0, 0)}


def main():
    level = {frozenset({(0, 0, 0)})}
    LV = {0: level}
    for n in range(1, 7):
        level = next_level_fs(level)
        LV[n] = level
    print("N | D(N) | voidance-set size -> #configs")
    for n in range(0, 7):
        sizes = {}
        for S in LV[n]:
            vs = len(voidance(S))
            sizes[vs] = sizes.get(vs, 0) + 1
        print(f"N={n} D={len(LV[n])}: {dict(sorted(sizes.items()))}")


if __name__ == "__main__":
    main()
