#!/usr/bin/env python3
"""Fresh re-check of PE185 structural facts from verified data.

Re-derives the c=1 pairwise-distinct-position conjecture and the answer value
from the run's own data (lib/pe185secret.py GUESSES/COUNTS/SECRET), so the
report is current, not from memory.
"""
from lib.pe185secret import GUESSES, COUNTS, SECRET

L = len(SECRET)

# 1. Confirm the secret satisfies every constraint
all_ok = True
for g, c in zip(GUESSES, COUNTS):
    m = sum(1 for p in range(L) if g[p] == SECRET[p])
    if m != c:
        all_ok = False
        print("FAIL", g, "c=", c, "got", m)
print("secret:", SECRET, " all counts OK:", all_ok)

# 2. c=1 guesses: positions where they match the secret
c1_pos = [p for i, (g, c) in enumerate(zip(GUESSES, COUNTS))
          if c == 1
          for p in range(L) if g[p] == SECRET[p]]
print("c=1 guess match positions:", c1_pos)
print("pairwise distinct:", len(c1_pos) == len(set(c1_pos)),
      "n c=1 guesses:", COUNTS.count(1))

# 3. Verify per-position hitcounts and their sum == sum(c_i)
hitcounts = [0] * L
for g in GUESSES:
    for p in range(L):
        if g[p] == SECRET[p]:
            hitcounts[p] += 1
print("hitcounts:", hitcounts)
print("sum(hitcounts)=%d sum(c_i)=%d match:%s"
      % (sum(hitcounts), sum(COUNTS), sum(hitcounts) == sum(COUNTS)))

# 4. secret digits
print("secret_digits:", [int(ch) for ch in SECRET])
