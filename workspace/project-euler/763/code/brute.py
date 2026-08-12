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

from lib.amoeba import D


if __name__ == "__main__":
    for n in [2, 10]:
        d = D(n, d=3)
        print(f"D({n}) = {d}")
