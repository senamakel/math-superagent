"""2D analogue of the Project Euler 763 amoeba process.

Rule (2D): an amoeba at (x,y) divides into two amoebas at (x+1,y) and
(x,y+1), provided both of those cells are empty; the dividing amoeba
disappears.  Start from one amoeba at (0,0).  Each division nets +1 amoeba,
so after N divisions a config holds N+1 cells (2N+1 in 3D; here it is N+1).

D_2D(N) = number of DISTINCT sets of occupied cells reachable after exactly N
divisions.

This is a BFS over frozensets of (x,y) cells (the small, fine case; the 2D
state space is far smaller than 3D), matching the structure of code/brute.py.
Correctness can be sanity-checked for N=0 (the single config {(0,0)}) and by
hand for N=1 (one division -> {(1,0),(0,1)} so D_2D(1)=1).
"""


def reachable_sets(N):
    """All distinct occupied-cell frozensets reachable after exactly N divisions."""
    start = frozenset({(0, 0)})
    level = {start}
    for _ in range(N):
        nxt = set()
        for S in level:
            Sset = set(S)
            for (x, y) in S:
                a = (x + 1, y)
                b = (x, y + 1)
                if a not in Sset and b not in Sset:
                    ns = Sset - {(x, y)} | {a, b}
                    nxt.add(frozenset(ns))
        level = nxt
        if not level:
            break
    return level


def D_2D(N):
    return len(reachable_sets(N))


if __name__ == "__main__":
    for n in range(0, 15):
        print(f"D_2D({n}) = {D_2D(n)}")
