#!/usr/bin/env python3
"""Extract candidate integer sequences from the Project Euler 185 L=16 data.

The guess matrix is 22 guesses x 16 positions. We derive several integer
sequences and print them for `analyze_sequence` / `find_linear_recurrence`:

  counts   : the per-guess required counts c_i (length 22)
  col_p    : for each position p, the sequence of digits g_i[p] across guesses
             (length 22 each) -- tests whether any column has exploitable
             structure.
  per_rowsum: sum of digits in each guess (length 22)
  per_colsum: sum of digits in each column (length 16)

These are structural facts about the constraint data, reported so the exact
sequence tools can decide whether any regularity actually holds.
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

L = len(GUESSES[0])
G = len(GUESSES)
assert all(len(g) == L for g in GUESSES)

counts = COUNTS[:]
cols = [[int(g[p]) for g in GUESSES] for p in range(L)]
rowsums = [sum(int(ch) for ch in g) for g in GUESSES]
colsums = [sum(cols[p]) for p in range(L)]

print("counts (length %d):" % len(counts))
print(counts)
for p in range(L):
    print("col_%02d (length %d):" % (p, len(cols[p])))
    print(cols[p])
print("rowsums (length %d):" % len(rowsums))
print(rowsums)
print("colsums (length %d):" % len(colsums))
print(colsums)
