#!/usr/bin/env python3
"""Tool_builder target — two precise structural claims to verify.

CLAIM A (deterministic reverse cap-collapse).
Every reachable 3D config S (N>=1) has:
  A1. exactly 3 cells on its max level M (histograms all show a_M == 3);
  A2. those 3 top cells are the complete forward-child triangle {p+1,0,0),
      p+(0,1,0), p+(0,0,1)} of a single EMPTY parent p at level M-1;
  A3. cap-merging (replace those 3 by p) gives a reachable (N-1) config, and
      repeating reaches {origin} deterministically.
Consequence: configs are in bijection with their reverse-collapse sequence =
with full ternary collapse trees = with voidance sets (Eriksson Prop 20/Thm 9).

CLAIM B (forward recurrence).
Let conf(N) = set of reachable N-configs and f(C) = #{p in C : none of
p+e1,p+e2,p+e3 is in C} (dividable cells).  Then
        D(N+1) = sum_{C in conf(N)} f(C).
Equivalently D(N) counts (config, dividable-cell) pairs at level N-1, and by
CLAIM A this map (C,p) -> S is injective (S collapses to a unique (C,p)).

Verify BOTH on the run's own BFS reachable configs (small N) and on the
histogram dumps (N=2..12).  If either fails, the reverse structure is NOT as
claimed and the collapse-tree bijection is wrong.
"""
from itertools import product
from lib.amoeba import forward_level

E = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]


def children(p):
    return tuple(tuple(p[i] + e[i] for i in range(3)) for e in E)


def level(p):
    return sum(p)


def top_caps(S):
    maxlvl = max(level(pt) for pt in S)
    Sset = set(S)
    top_cells = [pt for pt in S if level(pt) == maxlvl]
    caps = []
    for p in product(range(maxlvl), repeat=3):
        if level(p) != maxlvl - 1:
            continue
        if p in Sset:
            continue
        if set(children(p)) == set(top_cells):
            caps.append(p)
    return caps


def deterministic_collapse(S):
    """Returns (ok, count) : ok if S's reverse cap-merge reduces to origin,
    count = number of cap-merges (should equal N = #divisions)."""
    Sset = set(S)
    cnt = 0
    while Sset != {(0, 0, 0)}:
        caps = top_caps(Sset)
        if len(caps) != 1:
            return (False, cnt)
        p = caps[0]
        Sset = (Sset - set(children(p))) | {p}
        cnt += 1
    return (True, cnt)


def f_of(C):
    Sset = set(C)
    cnt = 0
    for p in Sset:
        if all(c not in Sset for c in children(p)):
            cnt += 1
    return cnt


def main():
    level = {frozenset([(0, 0, 0)])}
    Nmax = 7
    D = []
    for N in range(Nmax + 1):
        # CLAIM A on this level
        a1_bad = a2_bad = a3_bad = 0
        for S in level:
            M = max(level(pt) for pt in S)
            if len([pt for pt in S if level(pt) == M]) != 3:
                a1_bad += 1
            caps = top_caps(S)
            if len(caps) != 1:
                a2_bad += 1
            else:
                ok, cnt = deterministic_collapse(S)
                if not ok:
                    a3_bad += 1
        D.append(len(level))
        print(f"N={N}: D={len(level)}  claimA1(top==3)bad={a1_bad} "
              f"A2(unique_cap)bad={a2_bad} A3(det_collapse)bad={a3_bad}")
        if N < Nmax:
            # CLAIM B: sum of f over this level's configs == D(N+1)
            s = sum(f_of(S) for S in level)
            print(f"    claimB: sum f(C) over conf(N)={s}  (D(N+1)="
                  f"{len(forward_level(level, 3))})  match={s==len(forward_level(level, 3))}")
        level = forward_level(level, 3)
    print("\nD(N):", D)


if __name__ == "__main__":
    main()
