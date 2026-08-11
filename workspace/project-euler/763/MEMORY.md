# Working memory

## Problem

3D amoeba. Amoeba at (x,y,z) can divide into three amoebas at the forward
neighbors (x+1,y,z), (x,y+1,z), (x,y,z+1), provided those three cubes are all
empty. Start: one amoeba at (0,0,0). After N divisions there are 2N+1 amoebas.
D(N) = number of distinct reachable sets of occupied cubes after exactly N
divisions, counted once even if reachable multiple ways.

## Established results (verified by brute-force BFS in /workspace/brute.py)

D(N) for N = 0..13:
D(0)=1, D(1)=1, D(2)=3, D(3)=9, D(4)=30, D(5)=99, D(6)=336, D(7)=1134,
D(8)=3855, D(9)=13086, D(10)=44499, D(11)=151263, D(12)=514419, D(13)=1749267.

Checks confirmed by the run: D(2)=3 ✓, D(10)=44499 ✓.

BFS reached N=13; the frontier at N=13 held 1,749,267 states, so the naive
oracle was stopped before N=14 (memory/state-count cap of 600k was set,
though it ran one more depth to finish D(13)). We did not attempt N=20 by BFS —
too many states. D(13) took ~200s over a 514,419-state frontier.

## Failed approaches

- Running N=15 straight BFS was OOM-killed (exit 137) at the N=13→14 step
  when frontier grew to ~1.7M sets. Fixed by capping at a count guard.

## Open questions

Sequence 1,1,3,9,30,99,336,1134,3855,13086,44499,... — not yet identified with
a known OEIS sequence; a structural/combinatorial formula for D(N) is unknown.

D(13)=1749267 was produced by the slower (~200s) run and not independently
re-checked by a second route.
