# Extension run — summary

## Method
Level-by-level BFS over all **distinct** reachable configs (sets of occupied
cubes), using a fixed-width integer bitmask encoding (coords in [0,N] after N
divisions, so width W=N_max+1 covers all levels). One BFS step: a cube p may
divide iff its three positive-unit neighbours are empty; successors are S with
p cleared and the three neighbours set. Configs hashed as Python ints -> dense
memory, fast set operations.

State: BFS over a level set; each level costs O(frontier x cells); memory
linear in frontier (capped at 5,000,000). Not exponential: the level set is the
enumerated answer, and the cap bounds memory.

## Results (N, D(N), level-time)
- D(0)=1, D(1)=1, D(2)=3, D(3)=9, D(4)=30, D(5)=99, D(6)=336, D(7)=1134,
  D(8)=3855, D(9)=13086, D(10)=44499, D(11)=151263, D(12)=514419,
  D(13)=1749267, **D(14)=5949063**.

Level times (s): 1:0.00 2:0.00 3:0.00 4:0.00 5:0.00 6:0.00 7:0.002 8:0.007
9:0.03 10:0.11 11:0.43 12:1.7 13:6.4 14:26.0

## Which N failed
N=15 and N=16 were NOT computed. The frontier grows ~x3.4 per level:
D(15)~20M states, D(16)~68M, both beyond the 5,000,000-state cap (and beyond
the 30 GB free RAM). The run stopped cleanly at N=14 when its frontier
(5,949,063) exceeded the cap — that is the intended clean stop, not a crash.

## Verification
- D(2)=3 and D(10)=44499 match the statement's worked examples.
- D(12)=514419 and D(13)=1749267 match the earlier frozenset-oracle values.
- D(14)=5949063 confirmed by a SECOND structurally different implementation
  (amoeba_verify.py: rebuilds the occupied set per config and tests neighbour
  emptiness directly), which also reproduces D(0..13).
- The frozenset oracle (brute_extended.py) was OOM-killed at the N=13->14 step
  (frontier of 5.9M frozensets too heavy) — expected, not a value discrepancy.

## Data files
/workspace/data/level_N.txt for N=2..12, one line per distinct config:
`level_hist a_k | M | dx dy dz` (bbox extents). Line counts equal D(N). See
data/INDEX.md.
