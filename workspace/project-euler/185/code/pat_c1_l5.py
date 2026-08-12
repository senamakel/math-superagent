#!/usr/bin/env python3
"""Check the c=1 regularity against the L=5 oracle 39542 (the run's only
other fully-computed instance).  The observation on L=16 (from
pat_minmult_c1.py) was: the six c=1 guesses match at six distinct positions
{0,2,4,6,8,15} - all even except the final odd 15.  Does L=5 repeat it?
"""
from lib.pe185 import CONSTRAINTS5

SECRET = "39542"
L = len(SECRET)
matchpos = []
for g, c in CONSTRAINTS5:
    pos = [p for p in range(L) if g[p] == SECRET[p]]
    assert len(pos) == c
    matchpos.append(pos)
print("L=5 secret", SECRET, "all counts verified: True")
c1pos = sorted(pos[0] for (g, c), pos in zip(CONSTRAINTS5, matchpos) if c == 1)
print("L=5 c=1 match positions:", c1pos)
print("L=5 c=1 all distinct:", len(set(c1pos)) == len(c1pos),
      "| all even:", all(p % 2 == 0 for p in c1pos))
print("L=5 per-guess (guess, c, pos):",
      [(g, c, pos) for (g, c), pos in zip(CONSTRAINTS5, matchpos) if c == 1])