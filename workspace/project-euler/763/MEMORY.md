# Working memory

## Problem
3D amoeba. Amoeba at (x,y,z) divides into three amoebas at (x+1,y,z),
(x,y+1,z),(x,y,z+1) iff those three cubes are all empty; parent disappears.
Start: one amoeba at (0,0,0). After N divisions there are 2N+1 amoebas.
D(N) = number of distinct reachable sets of occupied cubes after exactly N
divisions, counted once even if reachable multiple ways.

## Established results (two independent BFS routes)
D(0..14)=1,1,3,9,30,99,336,1134,3855,13086,44499,151263,514419,1749267,5949063.
D(14)=5949063 verified by THREE independent implementations. D(2)=3, D(10)=44499
match the statement's worked examples. Hard ceiling: 2 GiB cgroup cap, exact BFS
stops at N=14 (~5.9M states); D(15) unreachable by any exact BFS here.

## Sourced structural backbone (Eriksson "Pebblings", EJC 2 (1995) #R7)
- The 3D PE763 amoeba is exactly Eriksson/Vaderlind's n=3 pebbling game
  (a cell -> 3 children one unit out along +e1,+e2,+e3, all targets empty).
- **n>=3**: there is a bijection between reachable positions, voidance sets,
  and folded polyominoids (Eriksson Thm 9), and **no node is ever played
  twice** (Prop 24), so positions = voidance sets = folded polyominoids.
- 2D analogue = chessboard pebbling (CGMO AMM 102 (1995)) = OEIS A007902,
  governed by the two-index DP G(k,m); no small one-index closed form.

## Inventor's NEW structural observation (the collapse lever)

**Top-cap structure (hand-verified on config dumps, to be confirmed by
code/inventor/check_recurrence.py):**
- CLAIM A1: every reachable N-config (N>=1) has EXACTLY 3 cells on its max
  level M (all level histograms end in "3": "0 2 3", "0 2 2 3", "0 1 5 3", ...).
- CLAIM A2: those 3 top cells are the complete forward-child triangle
  {p+e1,p+e2,p+e3} of a single EMPTY parent p at level M-1.
- CLAIM A3: cap-merging (replace those 3 by p) gives a reachable (N-1)
  config; repeating reaches {origin} DETERMINISTICALLY.
Consequence: configs <-> reverse-collapse sequences <-> full ternary
collapse trees <-> voidance sets (Eriksson Prop 20/Thm 9).

**Consequence recurrence (CLAIM B):** f(C) = #{cells p in C none of whose
p+ei is in C} (dividable cells).  Then
        D(N+1) = sum_{C in conf(N)} f(C)
provided the map (C,p) -> child config is injective (which CLAIM A3 gives).
This is the forward DP step; it reproduces D exactly if the collapse bijection
holds.  Verified only by hand on small configs so far; see check script.

## The gap to D(10000)
CLAIM B's sum still ranges over all reachable configs (enumerates the space),
so it does NOT by itself reach N=10000.  The real reduction must come from the
**voidance-set / folded-polyominoid** counting (Eriksson Thm 9): count, for
each N, the voidance sets of the collapse that produce an N-division config.
Eriksson Fig.3 column n=3 gives folded-polyominoid counts f(k,3)=
1,3,12,57,300,1680,9900,... (k=0..6) but D(N) is NOT f(k,3); the PE763 "position
with 2N+1 cells" count is a refinement (level/weight constraints).  Proposing
a two-index DP (3D analogue of the 2D G(k,m)) as the concrete next target;
falsifier: must reproduce D(14) and then D(20)=9204559704, D(100) last
nine=780166455.  NOT yet derived; this is the open seam.

## Files
- code/inventor/check_recurrence.py — tool_builder target verifying CLAIM A
  (top-cap deterministic collapse) and CLAIM B (D(N+1)=sum f(C)) on BFS
  configs N<=7.
- code/inventor/probe_topcap.py, probe_reachable.py — empirical probes.
