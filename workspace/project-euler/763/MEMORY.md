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
