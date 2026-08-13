#!/usr/bin/env python
"""Aggregate the mpmath-verified table into C(c) and G(n) sequences."""
import os

rows = []
for line in open("/workspace/code/out/mpmath_table.txt"):
    c, s, p, q, g = map(int, line.split())
    rows.append((c, s, p, q, g))

C = {}
for c, s, p, q, g in rows:
    C[c] = C.get(c, 0) + g

print("   c   C(c)     G(c)   dC=C(c)-C(c-1)")
acc = 0
seqC = []
seqG = []
for c in range(16, 39):
    acc += C.get(c, 0)
    dC = C[c] - C.get(c - 1, 0)
    seqC.append(C.get(c, 0))
    seqG.append(acc)
    print("  %3d  %5d  %7d  %5d" % (c, C.get(c, 0), acc, dC))

print()
print("G(16)=%d (oracle 9)  G(20)=%d (oracle 205)"
      % (seqG[0], seqG[4]))
print("C-sequence:", seqC)
print("G-sequence:", seqG)
# also write out for the tools
with open("/workspace/code/out/seq_C.txt", "w") as f:
    f.write(" ".join(map(str, seqC)))
with open("/workspace/code/out/seq_G.txt", "w") as f:
    f.write(" ".join(map(str, seqG)))
print("saved seq_C.txt and seq_G.txt")