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

## Library

`code/lib/amoeba.py` is the single shelved definition of the BFS step
(`next_level_bits`), encode/decode, and config feature extraction
(`config_features`, `feature_record`). Both `amoeba_bits.py` and data dumps
import from it (no duplicated definition).
