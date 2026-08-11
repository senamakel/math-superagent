"""Naive oracle for Project Euler 763.

An amoeba at p=(x,y,z) divides into three amoebas at (x+1,y,z), (x,y+1,z),
(x,y,z+1), provided those three cubes are all empty. The dividing amoeba
itself disappears, so each division nets +2 amoebas: starting from one at
(0,0,0), after N divisions there are 2N+1 amoebas.

D(N) = number of DISTINCT sets of occupied cubes reachable after exactly N
divisions (same arrangement reachable many ways counts once).

This is the naive oracle: BFS over sets of occupied cubes, level = number of
divisions. Exponential state space; only for tiny N as a definition check.
"""

from functools import lru_cache


def reachable_sets(N):
    """Return the set of frozensets of cubes reachable after exactly N divisions."""
    E1, E2, E3 = (1, 0, 0), (0, 1, 0), (0, 0, 1)
    start = frozenset({(0, 0, 0)})
    level = {start}
    for _ in range(N):
        nxt = set()
        for S in level:
            Sset = set(S)
            for p in S:
                a = (p[0] + E1[0], p[1] + E1[1], p[2] + E1[2])
                b = (p[0] + E2[0], p[1] + E2[1], p[2] + E2[2])
                c = (p[0] + E3[0], p[1] + E3[1], p[2] + E3[2])
                if a not in Sset and b not in Sset and c not in Sset:
                    ns = Sset - {p} | {a, b, c}
                    nxt.add(frozenset(ns))
        level = nxt
        if not level:
            break
    return level


def D(N):
    return len(reachable_sets(N))


if __name__ == "__main__":
    for n in [2, 10]:
        d = D(n)
        print(f"D({n}) = {d}")
