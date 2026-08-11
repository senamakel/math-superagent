# 2D amoeba = pebble spreading = OEIS A007902 — and its structural model

## Question

The 2D amoeba process: an amoeba at (x,y) splits into (x+1,y) and (x,y+1) if
those two cells are both empty; the parent disappears; start with one amoeba
at (0,0). D(N) = number of distinct sets of N+1 occupied cells reachable after
N splits. Sequenced terms (N = 0..14):
1,1,2,4,9,20,46,105,243,561,1301,3014,6995,16227,37668.

## Result: this IS OEIS A007902 — and it is the classical pebbling problem

The 2D amoeba is exactly the **"pebble spreading" / chessboard pebbling**
problem posed by Kontsevich (Kvant, 1981) and Khodulev (Kvant, 1982), with the
first complete enumeration by Chung, Graham, Morrison & Odlyzko,
"Pebbling a chessboard", Amer. Math. Monthly 102 (1995), pp. 113–123.

The rule matches verbatim (Q. Zhen & C. Knessl, arXiv:1009.5731): start with a
pebble at (0,0); remove a pebble at (i,j) and place pebbles at (i+1,j) and
(i,j+1) provided those two cells are unoccupied; after k steps there are k+1
pebbles; G(k) = number of reachable configurations with k pebbles.

**Offset mapping.** A007902 has offset 1 with a(1)=1; the run's D(N)=a(N+1):
D(0)=a(1)=1, D(1)=a(2)=1, D(2)=a(3)=2, ..., D(14)=a(15)=37668. All 15 terms
match, and the direct OEIS lookup (this run) confirmed A007902 is the only
match for the 15-term head.

URL: https://oeis.org/A007902

## Exact recurrence (Alois P. Heinz, from the OEIS entry = CGMO eqs 2.1-2.3)

The OEIS gives an exact structural recurrence via an auxiliary G(k,m) (the
number of reachable configurations with k pebbles whose top structure sits in
level m):

```
G(k, m):
  k < 1          -> 0
  m = 0          -> 2*G(k-1,0) + G(k,1) + (1 if k=2 else 0)
  m = 1          -> G(k-3,0) + 2*G(k-2,1) + G(k-1,2) + G(k-4,1)
  m >= 2         -> G(k-m-2, m-1) + 2*G(k-m-1, m) + G(k-m, m+1)
a(n) = 1 if n=1 else G(n,0)
```

This is an exact, structural recurrence (not enumeration). Verified by this
run: a(n+1) reproduces the independent 2D BFS oracle D2D(0..14).
Limit: a(n) ~ c*d^n with d = 2.3216421994942297..., c = 0.12268707342148599...
(Knessl 2006/2008, Kotesovec 2014). Exact contour formula in Zhen-Knessl,
arXiv:1009.5731 (Thm 2.1).

## Structure (this is the point of the research fetch)

Reachable 2D configurations are **polyominoids** (all points on or between two
lattice paths with common endpoints), bijectively represented by their
**voidance sets** (the left/lower boundary points of those paths; Prop 20:
positions ⇄ shot counts ⇄ voidance sets). The 2D subtlety is the **crossing**
(a cell played twice), which forces the marked-crossing GF g(x) of Eriksson
Theorem 10 with growth 4.112.

For the 3D PE763 process the generalisation is decisive: in n ≥ 3 **no cell is
ever played twice** (Eriksson Prop 24), so reachable positions, voidance sets
and **folded polyominoids** all coincide (Eriksson Theorem 9, n≥3). The PE763
amoeba is exactly Eriksson/Vaderlind's n=3 pebbling game (3 forward-neighbour
children). Full sourced account: research/pebbling_structure_3d_ladder.md
and research/L2.0/pebbling_ejc_survey.md (Eriksson "Pebblings", EJC 2 (1995)
#R7, https://doi.org/10.37236/1201).

## Sources

- OEIS A007902: https://oeis.org/A007902
- Chung, Graham, Morrison, Odlyzko, "Pebbling a chessboard", Amer. Math.
  Monthly 102 (1995) 113–123. DOI 10.2307/2975345. Opening transcribed in
  Dijkstra EWD 1200 (https://www.cs.utexas.edu/~EWD/transcriptions/EWD12xx/EWD1200.html).
- Zhen & Knessl, exact asymptotics, arXiv:1009.5731 (pdf).
- Eriksson, "Pebblings", EJC 2 (1995) #R7 — the higher-dimension/
  folded-polyominoid generalisation.
  https://www.combinatorics.org/ojs/index.php/eljc/article/view/v2i1r7/pdf

Deliberately NOT consulted: any Project Euler 763 solver/forum thread
(per run instruction).
