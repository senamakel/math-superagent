"""Fully independent verification of the diagonal f-distribution conjecture.

Diagonal = configs of 3D PE763 with max level M==N.
Conjecture: count(M=N, f) = 3 * C(N-2, f-3) * 2^(f-3), where f = number of
cells with all three forward children absent (dividable cells).

Uses ONLY a naive frozenset oracle (independent BFS) and an inline dividable
counter; does not import lib.f_of.  Cheap: N<=7.
"""
import math
from collections import Counter

def my_dividable(S):
    Sset = set(S)
    return sum(1 for (x, y, z) in Sset
               if (x+1, y, z) not in Sset and (x, y+1, z) not in Sset
               and (x, y, z+1) not in Sset)

def my_children(p):
    x, y, z = p
    return [(x+1, y, z), (x, y+1, z), (x, y, z+1)]

def one_step(level):
    nxt = set()
    for S in level:
        Sset = set(S)
        for p in Sset:
            if all(c not in Sset for c in my_children(p)):
                nxt.add(frozenset((Sset - {p}) | set(my_children(p))))
    return nxt

level = {frozenset([(0, 0, 0)])}
for N in range(1, 8):
    level = one_step(level)
    diag = Counter()
    for S in level:
        M = max(sum(p) for p in S)
        if M == N:
            diag[my_dividable(S)] += 1
    if not diag or N < 2:
        continue
    tot = sum(diag.values())
    ok = tot == 3**(N-1)
    ok2 = all(diag[f] == 3*math.comb(N-2, f-3)*(2**(f-3)) for f in diag)
    print(f"N={N}: tot={tot} (3^(N-1)={3**(N-1)}:{ok}) "
          f"conjecture_holds={ok2}   diag={dict(sorted(diag.items()))}")
