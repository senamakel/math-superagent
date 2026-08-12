#!/usr/bin/env python3
"""Two exact checks on the verified L=16 secret 4640261571849533.

A. The min-multiplicity conjecture (s[p] is a least-frequent digit of column
   p) - the verdict from pat_extract.py output, stated formally here.

B. NEW observation from the match-position table: the six guesses with c_i=1
   match at six distinct positions.  Sorted, they are the even positions
   0,2,4,6,8 plus 15.  Verify exactly and state the '1-hit' position set.

Also prints the remaining unexplored exact sequences for the tools:
   - parity of secret digits (16 terms)
   - adjacent |diff| and sums (15 terms)
   - flattened per-guess match positions (44 terms)
All derived from the verified answer; every number printed comes from this run.
"""
from collections import Counter
from lib.pe185 import CONSTRAINTS16

SECRET = "4640261571849533"
L = len(SECRET)
G, C = zip(*[(g, c) for g, c in CONSTRAINTS16])
assert list(C) == [2, 1, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 1, 2, 0, 2, 2, 3, 1, 3, 3, 2]

# --- re-verify every count (sanity anchor) ---
matchpos = []
for g, c in CONSTRAINTS16:
    pos = [p for p in range(L) if g[p] == SECRET[p]]
    assert len(pos) == c, (g, pos, c)
    matchpos.append(pos)
print("all 22 per-guess counts verified:", True)

# --- A. min-multiplicity verdict, formal ---
rarest_ok = 0
for p in range(L):
    col = Counter(g[p] for g in G)
    m_min = min(col.values())
    if col.get(SECRET[p], 0) == m_min:
        rarest_ok += 1
print("A. min-multiplicity: s[p] is a least-frequent digit of column p in",
      rarest_ok, "of", L, "columns")

# --- B. c=1 distinctness ---
c1 = [(i, matchpos[i]) for i, c in enumerate(C) if c == 1]
assert all(len(pos) == 1 for _, pos in c1)
c1pos = sorted(pos[0] for _, pos in c1)
evens = [p for p in range(L) if p % 2 == 0]
print("B. c=1 guesses (index, matched position, digit):",
      [(i, pos[0], SECRET[pos[0]]) for i, pos in c1])
print("B. c=1 match positions sorted:", c1pos)
print("B. all distinct:", len(set(c1pos)) == len(c1pos))
print("B. == even positions 0..8 plus 15:", c1pos == evens[:5] + [15])
print("B. even positions covered by c=1 matches:",
      [p for p in c1pos if p % 2 == 0], "of all even positions", evens)
print("B. per (even) position index: 1-hit position set =",
      [None if p not in c1pos else SECRET[p] for p in range(L)])

# --- sequences for the exact tools ---
digits = [int(ch) for ch in SECRET]
print()
print("parity      :", [d % 2 for d in digits])
print("adj_absdiff :", [abs(digits[i+1] - digits[i]) for i in range(L - 1)])
print("adj_sum     :", [digits[i+1] + digits[i] for i in range(L - 1)])
flat = [p for pos in matchpos for p in pos]
print("flat_matchpos (%d terms):" % len(flat), flat)
print("flat length == sum(c_i) == 44:", len(flat) == 44)