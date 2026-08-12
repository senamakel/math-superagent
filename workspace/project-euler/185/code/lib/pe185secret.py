#!/usr/bin/env python3
"""Derived integer sequences from the PE 185 L=16 secret produced by the run.

The secret was computed by code/solution2.py (scipy MILP) and independently
verified against all 22 (guess, c_i) constraints; see /workspace/code/out/
solution2_run.log.  This module prints, for the sequence tools:

  secret_digits : the 16 digits of the secret s, in position order
  hitcounts     : per position p, the number of guesses whose digit at p
                  equals s[p]  (sum must equal sum(c_i) = 44)
  dist          : how many times each digit 0..9 occurs in the secret
  matchpos      : for each guess i, the list of positions where it matches s
"""

GUESSES = [
    "5616185650518293",
    "3847439647293047",
    "5855462940810587",
    "9742855507068353",
    "4296849643607543",
    "3174248439465858",
    "4513559094146117",
    "7890971548908067",
    "8157356344118483",
    "2615250744386899",
    "8690095851526254",
    "6375711915077050",
    "6913859173121360",
    "6442889055042768",
    "2321386104303845",
    "2326509471271448",
    "5251583379644322",
    "1748270476758276",
    "4895722652190306",
    "3041631117224635",
    "1841236454324589",
    "2659862637316867",
]
COUNTS = [2, 1, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 1, 2, 0, 2, 2, 3, 1, 3, 3, 2]

SECRET = "4640261571849533"
L = len(SECRET)
assert all(len(g) == L for g in GUESSES)

secret_digits = [int(ch) for ch in SECRET]
hitcounts = [0] * L
matchpos = []
per_guess_ok = True
for g in GUESSES:
    pos = [p for p in range(L) if g[p] == SECRET[p]]
    for p in pos:
        hitcounts[p] += 1
    matchpos.append(pos)

print("secret_digits (length %d):" % L)
print(secret_digits)
print("hitcounts (length %d):" % L)
print(hitcounts)
print("sum(hitcounts) =", sum(hitcounts), " sum(c_i) =", sum(COUNTS))
print("dist (length 10):")
print([SECRET.count(str(d)) for d in range(10)])
print("per-guess match counts vs c_i:")
for i, (g, c) in enumerate(zip(GUESSES, COUNTS)):
    m = len(matchpos[i])
    print("  %02d  %s  matches=%d c=%d %s  pos=%s"
          % (i, g, m, c, "OK" if m == c else "FAIL", matchpos[i]))
print("all per-guess counts OK:", all(len(mp) == c for mp, c in zip(matchpos, COUNTS)))