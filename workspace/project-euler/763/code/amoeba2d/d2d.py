"""2D analogue of the Project Euler 763 amoeba process.

Rule (2D): an amoeba at (x,y) divides into two amoebas at (x+1,y) and
(x,y+1), provided both of those cells are empty; the dividing amoeba
disappears.  Start from one amoeba at (0,0).  Each division nets +1 amoeba,
so after N divisions a config holds N+1 cells (2N+1 in 3D; here it is N+1).

D_2D(N) = number of DISTINCT sets of occupied cells reachable after exactly N
divisions.

This is a BFS over frozensets of (x,y) cells (the small, fine case; the 2D
state space is far smaller than 3D).  It uses the canonical 2D driver
reachable_sets/D from lib/amoeba at d=2, which matches the structure formerly
duplicated in this file (this copy genuinely applied the 2D rule, diverging
from the 3D brute.py — resolved by the d parameter, not by choosing one).
Correctness sanity: N=0 -> {(0,0)} (single config), N=1 -> {(1,0),(0,1)} so
D_2D(1)=1.
"""

from lib.amoeba import D


def D_2D(N):
    return D(N, d=2)


if __name__ == "__main__":
    for n in range(0, 15):
        print(f"D_2D({n}) = {D_2D(n)}")
