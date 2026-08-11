# C1 conjecture test — result

## Claim C1

A set S of cells containing the origin is reachable (via amoeba divisions)
iff S is 'origin-connected': every cell c != origin has at least one backward
neighbour in S (one of c-e1, c-e2, c-e3 with coords >= 0).

Origin-connected sets are precisely the positive directed animals rooted at
the origin: every non-root cell has a backward (lower-coordinate) neighbour,
equivalently every cell is reached from the origin by a directed lattice path
inside S.

## Method

Enumerated origin-connected sets by size (not by reachability BFS): a set is
origin-connected iff it can be grown from {origin} by appending forward
neighbours one at a time; the cells with a backward neighbour in S are
exactly the forward neighbours of S.  Finite bound: in any origin-connected
set of size m every coordinate is <= m-1 (a backward path decreases the
coordinate sum by >=1 per cell), so candidates live in the box [0,m-1]^d.
Counts reported by distinct set per size.

Compare sizes: 2D config holds N+1 cells at generation N (amoeba divides into
2), 3D holds 2N+1 (divides into 3).

## Result — C1 is FALSE in both dimensions

2D (size N+1), D_2D from existing verified oracle:

| N | D_2D(N) | C1_2D(N) | equal? |
|---|---------|----------|--------|
| 0 | 1 | 1 | True |
| 1 | 1 | 2 | False |
| 2 | 2 | 5 | False |
| 3 | 4 | 13 | False |
| 4 | 9 | 35 | False |
| 5 | 20 | 96 | False |
| 6 | 46 | 267 | False |
| 7 | 105 | 750 | False |
| 8 | 243 | 2123 | False |
| 9 | 561 | 6046 | False |
| 10 | 1301 | 17303 | False |
| 11 | 3014 | 49721 | False |
| 12 | 6995 | 143365 | False |

C1_2D list (N=0..12): 1, 2, 5, 13, 35, 96, 267, 750, 2123, 6046, 17303,
49721, 143365.

Cross-check: this is the 2D directed-animal count (OEIS A005773,
1,2,5,13,35,96,267,750,2123,...), so the enumeration is the directed-animal
count and is not the amoeba D_2D.  First disagreement at N=1.

3D (size 2N+1), D(N) = 1,1,3,9,30,99,336,1134,3855,13086,...:

| N | size | D(N) | C1_3D(N) | equal? |
|---|------|------|----------|--------|
| 0 | 1 | 1 | 1 | True |
| 1 | 3 | 3 | 12 | False |
| 2 | 5 | 30 | 237 | False |
| 3 | 7 | 1134 | 5339 | False |
| 4 | 9 | 3855 | 128247 | False |

C1_3D level-growth (distinct sets by size m): m=1:1, m=2:3, m=3:12, m=4:52,
m=5:237, m=6:1113, m=7:5339, m=8:26011, m=9:128247, m=10:638346.  The m=11
level (~6.4M sets) OOM-killed under the 2 GiB container cap before it could
count C1_3D for N=5; not needed since C1 already fails from N=1.

## Why C1 fails

Reachability is much more constrained than origin-connectivity.  In a
reachable set the total number of cells at "level" k = x+y+z is bounded
thermodynamically by the division count (dividing a level-k cell adds one
cell at level k+1 and removes one at level k, moving one unit of "mass" up a
level), so a reachable set cannot place an arbitrary directed animal.  The
simplest witness: in 2D the config {(0,0),(1,0),(0,1)} IS origin-connected
but is NOT reachable — with one amoeba at (0,0) the only division yields
{(1,0),(0,1)} (2 cells).  C1_2D(1)=2 because {(0,0),(2,0)} also counts as
origin-connected, but it is not a valid division result.  So origin-onnected
(3 cells at N=2 in 3D) also fails: e.g. {(0,0,0),(2,0,0),(0,2,0)} is
origin-connected but not reachable.
