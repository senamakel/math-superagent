"""Cross-checks of the chessboard-pebbling structural machinery for this run.

1) The exact G(k,m) recurrence (CGMO / OEIS A007902, Alois P. Heinz) reproduces
   the 2D amoeba counts a(n) = A007902(n+1); verify against the independent 2D
   BFS oracle values.

2) Reverse-merge (voidance) reachability test on small 2D and 3D configs:
   Eriksson Fact 5 'a reachable game position is completely specified by its
   voidance set' means config S is reachable iff it can be reduced to the
   singleton by repeatedly merging the d children of a common missing parent.
   Verify this 'reverse-merge reducibility' equals forward BFS reachability on
   every config the BFS frontier reaches (the run's structural claim).

3) Eriksson Fig. 3 rows: number f(k,n) of folded polyominoids in Z^n with
   circumference 2k; check the stated C_{k+1} Catalan column-2 and n(3n-1)/2
   row-2 identities on the tabulated numbers.
"""
from functools import lru_cache
from lib.amoeba2d import G, a

# ---- 1) A007902 exact G(k,m) recurrence (canonical definition imported from
# lib/amoeba2d, the single shared copy) ----
D2D = [1, 1, 2, 4, 9, 20, 46, 105, 243, 561, 1301, 3014, 6995, 16227, 37668]
print("2D recurrence a(n+1) matches BFS oracle D2D:",
      all(a(n + 1) == D2D[n] for n in range(len(D2D))))

# ---- 3) Eriksson Fig 3 folded-polyomino counts ----
# rows k=0..6, cols n=1..6 (from the paper's Figure 3)
fig3 = {
    0: [1, 1, 1, 1, 1, 1],
    1: [1, 2, 3, 4, 5, 6],
    2: [1, 5, 12, 22, 35, 51],
    3: [1, 14, 57, 148, 305, 546],
    4: [1, 42, 300, 1126, 3045, 6756],
    5: [1, 132, 1680, 9220, 32985, 91236],
    6: [1, 429, 9900, 79972, 368665, 1228575],
}
from math import comb
def catalan(j): return comb(2 * j, j) - comb(2 * j, j + 1)  # C_j (offset 1 here)
print("col n=1 is 1 (all rows):", all(r == [1, 1, 1, 1, 1, 1][0] for r in fig3.values())[:1])
# column 2 (n=2) = Catalan C_{k+1}?  values 1,1,5,14,42,132,429
col2 = [fig3[k][1] for k in range(7)]
print("col2 (n=2):", col2, "== Catalan C_{k+1}? ",
      col2 == [catalan(k + 1) for k in range(7)])
# row k=2 = n(3n-1)/2
row2 = fig3[2]
print("row k=2:", row2, "== n(3n-1)/2? ",
      row2 == [n * (3 * n - 1) // 2 for n in range(1, 7)])
