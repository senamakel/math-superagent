# Working memory

## Problem

3D amoeba. Amoeba at (x,y,z) can divide into three amoebas at the forward
neighbors (x+1,y,z), (x,y+1,z), (x,y,z+1), provided those three cubes are all
empty. Start: one amoeba at (0,0,0). After N divisions there are 2N+1 amoebas.
D(N) = number of distinct reachable sets of occupied cubes after exactly N
divisions, counted once even if reachable multiple ways.

## Established results (verified by two independent BFS routes)

D(N) for N = 0..14:
D(0)=1, D(1)=1, D(2)=3, D(3)=9, D(4)=30, D(5)=99, D(6)=336, D(7)=1134,
D(8)=3855, D(9)=13086, D(10)=44499, D(11)=151263, D(12)=514419, D(13)=1749267,
**D(14)=5949063**.

Checks confirmed: D(2)=3 ✓, D(10)=44499 ✓.

D(14)=5949063 confirmed by TWO independent implementations:
- `lib/amoeba.next_level_bits` (fixed-width int bitmask encoding) via
  `code/amoeba_extend.py` (26.0s for level 14).
- `code/amoeba_verify.py` (structurally different oracle: rebuilds the
  occupied set per config, tests forward-neighbour emptiness directly;
  37.84s for level 14). It also reproduces D(0..13).

So D(14) is verified by a second independent route (completion criterion).
Seen again by a third route: `code/amoeba/bfs_more.py`'s compact per-level
encoding (width W=level+1) reproduces D(0..14) exactly.

## Per-config structural data dumps

`/workspace/data/level_N.txt` for N=2..12, one line per distinct config:
`level_histogram a_k | M | dx dy dz` (a_k = #cubes at level k=x+y+z, M = max
level, dx,dy,dz = bounding-box extents). Line counts equal D(N). See
data/INDEX.md.

## Frontier growth / feasibility

Frontier grows ~x3.4 per division:
N=12: 514,419; N=13: 1,749,267; N=14: 5,949,063; N=15 ~20M (projected);
N=16 ~68M (projected).

Naive frozenset BFS OOM-killed at the N=13->14 step (5.9M frozensets / ~30GB
RAM). The bitmask (int) encoding handles it (~26s for level 14). Under the
5,000,000 cap, N=15 and N=16 are NOT reachable — the run stops cleanly at N=14.

The effective hard ceiling is the container's cgroup memory limit: 2 GiB
(/sys/fs/cgroup/memory.max = 2147483648), independent of the host's 30 GB
free RAM. The compact encoding holds ~5.9M states at N=14 (~most of that 2 GiB),
so D(15) (~20M states, ~12+ GiB) is unreachable by any exact BFS in this
container. N=14 is the last computable exact D(N) here.

## N=3 / N=4 configurations

Actual reachable configs for N=3 (9) and N=4 (30) are dumped, sorted, one per
line in `code/out/configs_n3_n4.txt` (produced by code/amoeba/configs_n3_n4.py).
Useful for studying structure (e.g. the chains/(0,0,0)->... paths and the
cross-product shapes).

## 2D analogue (new)

2D rule: an amoeba at (x,y) divides into (x+1,y) and (x,y+1) if both are
empty; parent disappears; start at (0,0); after N divisions a config holds N+1
cells. D_2D(N) = number of distinct reachable occupied-cell sets.

D_2D(N) for N=0..14:
1, 1, 2, 4, 9, 20, 46, 105, 243, 561, 1301, 3014, 6995, 16227, 37668

Verified by two independent routes:
- `code/amoeba2d/d2d.py` (frozenset BFS, mirrors code/brute.py) — matched.
- inline int-encoded bitmask BFS (independent encoding) — identical full list.

(For reference, 3D D(N) for N=0..14: 1,1,3,9,30,99,336,1134,3855,13086,44499,
151263,514419,1749267,5949063.)

## Library

`code/lib/amoeba.py` is the single shelved definition of the BFS step
(`next_level_bits`), encode/decode, and config feature extraction
(`config_features`, `feature_record`). Both `amoeba_bits.py` and data dumps
import from it (no duplicated definition).

## M-histograms (N=13, N=14)

Counting distinct configs grouped by max level M = max(x+y+z) at N=13 and
N=14 (driven with the same lib/amoeba.next_level_bits BFS as amoeba_extend.py;
program code/amoeba/mhist_13_14.py, output code/out/mhist_13_14.txt):

N=13: M=7:612 M=8:9342 M=9:51678 M=10:172044 M=11:393660 M=12:590490 M=13:531441
N=14: M=7:267 M=8:7122 M=9:54756 M=10:237897 M=11:688905 M=12:1417176 M=13:1948617 M=14:1594323

Totals sum to D(13)=1749267 and D(14)=5949063 (verified). Notable structure:
the maximal-level bin M=N equals 3^(N-1) (3^12=531441 for N=13, 3^13=1594323
for N=14) — consistent with a single chain of length N (each of the N-1
non-root steps can move along any of 3 axes). M>=7 at these N (a config after
N divisions always has its MAXIMUM level at least 7 for N=13,14; the M=N bin
is the chain(s)).

Also of note: the run must gc.collect() between levels or the N=14 step
OOM-kills at the 2 GiB cgroup cap (peak ~2.147e9 bytes, right at the limit).
Without GC the first attempt exited 137; with explicit collection it
completes in ~69s total (~23s for the N=14 BFS step, ~30s for the histogram).

## 2D seed: the exact structural DP for A007902 (to be lifted to 3D)

The 2D amoeba (a cell at (x,y) splits into (x+1,y),(x,y+1) if both empty) is
exactly OEIS A007902 (pebble spreading, Chung-Graham-Morrison-Odlyzko).
Offset mapping: run's D_2D(N) = a(N+1); the 15 BFS terms D_2D(0..14) =
1,1,2,4,9,20,...,37668 all match a(1..15).

Exact recurrence (Alois P. Heinz, OEIS) via auxiliary G(k,m):
  k<1        -> 0
  m=0        -> 2*G(k-1,0) + G(k,1) + (k==2 ? 1 : 0)
  m=1        -> G(k-3,0) + 2*G(k-2,1) + G(k-1,2) + G(k-4,1)
  m>=2       -> G(k-m-2,m-1) + 2*G(k-m-1,m) + G(k-m,m+1)
  a(1)=1;  a(n)=G(n,0)  (n>=2)

Indexing care that makes it work: the k<1 -> 0 guard handles all the negative
indices; the m>=2 branch dies to 0 for m > k (off the lower-triangular
region); the only explicit base constant is the [k==2] term in the m=0 line.
Program: code/amoeba2d/a007902_dp.py (prints the G(k,m) table).

Verified (see code/out): reproduces OEIS A007902 EXACTLY to a(33)=144558421877
and gives a(22)=13686805; a(1..14) re-checked against the independent 2D BFS
oracle code/amoeba2d/d2d.py (all match). This exact DP is the seed to
generalise to 3D for PE763's D(10000).

G(k,m) structure: nonzero only in a lower-triangular "band"; first nonzero k
for m=1..6 is 5,9,14,20,27,35 = (m+2)(m+3)/2 - 1. Growth d = 2.32164...,
c = 0.12268... (Knessl).

## C1 conjecture — DISPROVEN (2D and 3D)

Conjecture C1: "a set S of cells containing the origin is reachable iff S is
origin-connected (every non-origin cell has a backward neighbour)".  Tested by
enumerating origin-connected sets by size and comparing counts to D(N).

Origin-connected sets == positive directed animals rooted at origin (every
cell reached from origin by a directed lattice path).  Finite: in a set of
size m every coordinate is <= m-1, so candidates live in [0,m-1]^d; a set is
origin-connected iff growable from {origin} by appending forward neighbours,
so forward-growth level BFS enumerates them exactly.

RESULT: C1 is FALSE in both dimensions.
* 2D (size N+1): C1_2D(N) = 1,2,5,13,35,96,267,750,2123,6046,17303,49721,
  143365 for N=0..12 — the 2D directed-animal count (OEIS A005773), NOT the
  amoeba D_2D (=1,1,2,4,9,20,46,105,243,561,1301,3014,6995).  First mismatch
  at N=1: {(0,0),(2,0)} is origin-connected but not a division result.
* 3D (size 2N+1): C1_3D counts by size m=1..10:
  1,3,12,52,237,1113,5339,26011,128247,638346; always >> D(N)
  (1,1,3,9,30,...).  m=11 (~6.4M sets) OOM-killed under 2 GiB container cap.

Why: reachability is far more constrained than origin-connectivity — a
division moves one unit of "mass" up one level (k->k+1), bounding how many
cells a level can hold, so an arbitrary directed animal need not be
reachable.  In 2D {(0,0),(1,0),(0,1)} is origin-connected but unreachable
(one amoeba divides into exactly 2 cells).

Verified by a second independent route: code/out/verify_c1_subsets.py
enumerates all subsets of the box and counts literally origin-connected ones,
matching the generator (2D 1,2,5,13,35,96; 3D 1,3,12,52).  Full result table
in code/out/c1_test_results.md.

## d=2 counterpart (PE763 in two dimensions)

In d=2, one step replaces an amoeba at (x,y) by two children at (x+1,y) and
(x,y+1) provided both are empty; after N divisions there are N+1 cubes and
D2(N) distinct reachable sets.  Shelved in `code/lib/amoeba2d.py`
(`next_level_bits2_compact`, per-level compact bit encoding).  Verified by a
frozenset oracle agreeing for N=0..12 (code/amoeba/d2_check.py).  Exact BFS
reaches D2(21)=13686805 then hits the same 2 GiB cgroup memory wall
(13.7M states at N=21 saturate it; N=22 needs ~31M states).

D2(N), N=0..21:
1, 1, 2, 4, 9, 20, 46, 105, 243, 561, 1301, 3014, 6995, 16227, 37668,
87426, 202961, 471150, 1093819, 2539348, 5895408, 13686805.

Saved to `code/out/d2_values.txt`.  d=3 sequence D3(0..14) remains exactly as
in `code/out/d_values_more.txt` (unchanged, reproduces the stated values).
