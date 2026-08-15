#!/usr/bin/env python3
"""Explore constructive witnesses for the n=8 d<=3 decision.

Q_8 is bipartite: 128 even-weight vertices E and 128 odd-weight vertices O,
every edge crosses.  We need S = E' U O' with |E'|+|O'| = 129 and every
selected vertex having <= 3 neighbours inside S.

We try several CLOSED-FORM / heuristic families (not searches) and measure
each exactly.  The target of the decision is to find ANY set meeting |S|=129
and D(S)<=3.
"""
import sys, itertools, random
from collections import Counter

POP = [bin(x).count('1') for x in range(256)]
E = [x for x in range(256) if POP[x] % 2 == 0]
O = [x for x in range(256) if POP[x] % 2 == 1]
NB = {v: [v ^ (1 << k) for k in range(8)] for v in range(256)}


def measure(S):
    S = set(S)
    mx = 0
    for v in S:
        d = sum(1 for u in NB[v] if u in S)
        mx = max(mx, d)
    return len(S), mx


# --- Family 1: even vertices chosen by low degree to a chosen odd side,
#     iterated (a greedy alternating refinement).
def greedy_bipartite(target_e, target_o):
    Erem = set(E); Orem = set(O)
    # pick odd set first: all odds except drop the degree-heavy ones iteratively
    Esel = set(); Osel = set()
    # iterate: maintain Osel of size target_o, Esel of size target_e
    # greedy: start from Esel = target_e evens with fewest connections,
    # then Osel = target_o odds with fewest connections to Esel
    def ecc(Esel):  # even connection counts to Esel? no
        pass
    # simpler: co-greedy
    Esel = set(random.sample(E, target_e))
    for _ in range(2000):
        badE = [v for v in Esel if sum(1 for u in NB[v] if u in Osel) > 3]
        if badE:
            # swap a bad even out for a good even not in Esel
            good = [v for v in E if v not in Esel
                    and sum(1 for u in NB[v] if u in Osel) <= 3]
            if not good: break
            Esel.discard(badE[0]); Esel.add(random.choice(good))
        else:
            break
    # now choose odds to fit remaining
    pass


if __name__ == "__main__":
    pass
