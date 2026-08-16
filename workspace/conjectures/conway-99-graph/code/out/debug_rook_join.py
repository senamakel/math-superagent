import numpy as np
from lib.srg import rook
from itertools import combinations

A = np.asarray(rook(3))
n = A.shape[0]
print("adjacency rows:")
for i in range(n):
    print(i, list(A[i]))

# find triangles
tris = []
for i, j, l in combinations(range(n), 3):
    if A[i, j] and A[i, l] and A[j, l]:
        tris.append((i, j, l))
print("num triangles", len(tris))
for t in tris:
    print("tri", t, "cells:", [(x//3, x%3) for x in t])

# join edges for each pair
for a, b in combinations(tris, 2):
    e = 0
    for x in a:
        for y in b:
            if A[x, y]:
                e += 1
    print("pair", sorted(a), "<->", sorted(b), "joined by", e, "edges")
