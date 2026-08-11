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
