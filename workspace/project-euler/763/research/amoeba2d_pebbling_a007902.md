# 2D amoeba = pebble spreading = OEIS A007902

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
match.

URL: https://oeis.org/A007902

## Exact recurrence (Alois P. Heinz, from the OEIS entry)

The OEIS gives an exact three-term-triggered recurrence via an auxiliary
G(k,m) (the number of reachable configurations with k pebbles whose top/special
structure sits in level m):

```
G(k, m):
  k < 1          -> 0
  m = 0          -> 2*G(k-1,0) + G(k,1) + (1 if k=2 else 0)
  m = 1          -> G(k-3,0) + 2*G(k-2,1) + G(k-1,2) + G(k-4,1)
  m >= 2         -> G(k-m-2, m-1) + 2*G(k-m-1, m) + G(k-m, m+1)
a(n) = 1 if n=1 else G(n,0)
```

This is an exact, structural recurrence (not enumeration) and is the standard
way the 2D counts are generated. Limit: a(n) ~ c*d^n with
d = 2.3216421994942297... , c = 0.12268707342148599... (Knessl 2006/2008,
Kotesovec 2014).

## Structure: configurations are polyominoids determined by voidance sets

From Chung–Graham–Morrison–Odlyzko / the EJC "Pebblings" survey
(https://www.combinatorics.org/ojs/index.php/eljc/article/download/v2i1r7/pdf/):

- The cells played in a 2D pebbling game form a **polyominoid**: all points on
  or between two lattice paths with common start and end points.
- A reachable configuration is completely characterised by its **voidance set**
  (the left/lower boundary points of those paths). Reachability of a
  configuration is equivalent to the emptiness conditions of the process.
- If a configuration is reachable with stacking allowed it is also reachable
  without stacking (so the "empty-cell" constraint is exactly the reachability
  condition).

Purpose for this run: the 3D Project-Euler-763 amoeba is the **3-dimensional
generalisation** of this same pebbling process (a cell splits into its three
forward neighbours). The 2D sequence is catalogued (A007902) and has an exact
recurrence + bijective structure; the 3D sequence is not catalogued (see
research/amoeba_seq_oeis.md). The 2D toolkit (polyominoid/voidance bijections,
the G(k,m) recurrence) is the natural structural model to try to lift to 3D.

## Sources

- OEIS A007902: https://oeis.org/A007902
- Chung, Graham, Morrison, Odlyzko, "Pebbling a chessboard", Amer. Math.
  Monthly 102 (1995) 113–123.
- Zhen & Knessl, exact asymptotics, arXiv:1009.5731 (pdf).
- EJC "Pebblings" survey: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v2i1r7/pdf/

Deliberately NOT consulted: any Project Euler 763 solver/forum thread
(per run instruction).
