# Scratchpad

## Extension run (tool-builder)

BFS over distinct configs, fixed-width int bitmask encoding, one level per
step. 28 cores / 30GB available.

Level times (s), bitmask oracle (amoeba_extend.py):
1:0.00 2:0.00 3:0.00 4:0.00 5:0.00 6:0.00 7:0.002 8:0.007 9:0.03 10:0.11
11:0.43 12:1.7 13:6.4 14:26.0

Independent route (amoeba_verify.py) level 14: 37.84s. Both give D(14)=5949063.

Frozenset oracle (brute_extended.py) OOM-killed (exit 137) at N=13->14 step
when frontier reached 5.9M frozensets — expected; D(14) obtained via bitmask.

N=15, N=16 NOT reached: projected frontiers ~20M, ~68M >> 5,000,000 cap and
> 30GB RAM. Run stopped cleanly when level-14 frontier (5,949,063) exceeded the
cap.

Earlier D(N) values: D(0..12) reproduced by both frozenset and bitmask; D(13)
by both frozenset (~200s, MEMORY) and bitmask (6.4s).

## This tool-builder task's runs

- Dumped actual configs for N=3 (9 states) and N=4 (30 states), sorted, to
  code/out/configs_n3_n4.txt and stdout (code/amoeba/configs_n3_n4.py); counts
  asserted against D(3)=9, D(4)=30.
- Compact per-level bit encoding (code/amoeba/bfs_more.py, W=level+1) reproduced
  D(0..14) and independently confirmed D(14)=5949063, writing fresh complete
  code/out/d_values_more.txt.
- D(15) is unreachable here: cgroup memory cap is 2 GiB
  (/sys/fs/cgroup/memory.max = 2147483648); the ~5.9M frontier at N=14 nearly
  saturates it, and D(15) ~20M states would need ~12 GiB. The host has 30 GB
  free but the cgroup caps the container, not the host.
- Also removed the stray root brute.py (superseded; replica at code/brute_capped.py).

## C1 conjecture test (origin-connected == reachable?)

Program code/test_c1.py.  C1 FALSE in 2D and 3D.  Origin-connected sets are
positive directed animals; counts by size match A005773 in 2D
(1,2,5,13,35,96,267,750,2123,6046,17303,49721,143365), not the amoeba D_2D.
3D counts 1,3,12,52,237,1113,5339,26011,128247,638346 — always above D(N).
m=11 in 3D (~6.4M sets) OOM-killed in this container (2 GiB cap).  Generator
verified by subset oracle (verify_c1_subsets.py).  Details in
code/out/c1_test_results.md.
