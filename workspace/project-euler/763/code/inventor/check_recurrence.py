#!/usr/bin/env python3
"""Declared-infrastructure proof of correctness for the inventor proposal.

CLAIMS (all must hold; a violation refutes the reverse structure):

  A1. every reachable 3D N-config (N>=1) has exactly 3 cells on its max level M
  A2. those 3 top cells = {p+e1,p+e2,p+e3} for a single EMPTY parent p at M-1
  A3. iterated cap-merge reaches {origin} deterministically (N steps)
  B.  D(N+1) = sum_{C in conf(N)} #dividable-cells-of-C

Exact forward BFS over distinct configs for N=0..7.
Infrastructure cost declared: exponential state set (the BFS oracle itself),
bounded to N<=7 (<=15 cells, frontier 3855 at N=8 start).  Verification only.
"""
from itertools import product

from lib.amoeba import lvl, f_of

E = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]


def children(p):
    return tuple(tuple(p[i] + e[i] for i in range(3)) for e in E)


def forward_level(level):
    nxt = set()
    for S in level:
        Sset = set(S)
        for p in Sset:
            ch = children(p)
            if all(c not in Sset for c in ch):
                nxt.add(frozenset((Sset - {p}) | set(ch)))
    return nxt


def top_caps(S):
    M = max(lvl(pt) for pt in S)
    Sset = set(S)
    top = [pt for pt in S if lvl(pt) == M]
    caps = [p for p in product(range(M), repeat=3)
            if lvl(p) == M - 1 and p not in Sset and set(children(p)) == set(top)]
    return caps


def collapse(S):
    Sset = set(S)
    n = 0
    while Sset != {(0, 0, 0)}:
        caps = top_caps(Sset)
        if len(caps) != 1:
            return False, n
        Sset = (Sset - set(children(caps[0]))) | {caps[0]}
        n += 1
    return True, n


def main():
    level = {frozenset([(0, 0, 0)])}
    D = []
    Nmax = 7
    for N in range(Nmax + 1):
        a1 = a2 = a3 = 0
        for S in level:
            M = max(lvl(pt) for pt in S)
            if N >= 1 and len([pt for pt in S if lvl(pt) == M]) != 3:
                a1 += 1
            cand = top_caps(S)
            if N >= 1 and len(cand) != 1:
                a2 += 1
            else:
                ok, n = collapse(S)
                if not ok:
                    a3 += 1
        D.append(len(level))
        b_match = None
        if N < Nmax:
            s = sum(f_of(S) for S in level)
            nxt = forward_level(level)
            b_match = (s == len(nxt))
            print(f"N={N}: D={len(level)} A1bad={a1} A2bad={a2} A3bad={a3} "
                  f"B: sum f(C)={s} vs D({N+1})={len(nxt)} match={b_match}")
            level = nxt
        else:
            print(f"N={N}: D={len(level)} A1bad={a1} A2bad={a2} A3bad={a3}")
    print("\nD(0..7):", D)


if __name__ == "__main__":
    main()
