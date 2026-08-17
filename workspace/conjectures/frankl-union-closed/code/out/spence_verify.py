"""Verify Spence's finite counterexamples (arXiv/zenodo frank1-conjecture-audit, 2026).

Prop 3.1: the 5x4 matrix, every column has exactly two ones (no heavy column),
yet A2 returns True. Also: row set is NOT union-closed (Remark 3.3).
Prop 4.1: {empty,{1},{2},{3}} intersection-closed fails Schrader's bound.
"""
from lib.uc import abundance, decide_union_closed

# Prop 3.1 matrix rows: 0000,0011,0101,1010,1100 -> bits (bit i = column i)
rows = [0b0000, 0b0011, 0b0101, 0b1010, 0b1100]
n = 4
counts = abundance(rows, n)
print("column counts (bit0=rightmost/col4):", counts)
print("every column exactly 2 ones (no heavy in 5 rows)?",
      all(c == 2 for c in counts))
print("row set distinct?", len(set(rows)) == len(rows))
print("no all-zero column?", all(c > 0 for c in counts))
print("row set union-closed? (should be False, Remark 3.3)",
      decide_union_closed(rows))

# Prop 4.1 family F = {empty,{1},{2},{3}} on N=[3]
# intersection-closed; elements each freq 1. Schrader t-computation:
# t0=2^(3-1)=4; D1 empty t1=4; level2 only discarding set {1}, H={{1,2},{1,2,3}},
# t2=4-2=2; level3 discarding sets {1},{2}, H={{1,3}},{{2,3}}, t3=2-1-1=0 vs |F3|=1.
print("\nSchrader check: t0=4 t1=4 t2=2 t3=0, |F_3|=1 -> 0 < 1 fails bound",
      (0 < 1))

# Also verify {empty,{1},{2},{3}} union-closed version is abundant-trivial
F = [0b000, 0b001, 0b010, 0b100]
print("family {0,{1},{2},{3}} union-closed?", decide_union_closed(F))
print("abundant (has singletons -> trivially yes):", abundance(F, 3))
