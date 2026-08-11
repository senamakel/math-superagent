# Confirm/refute checklist for the inventor's collapse-tree proposal

Tool_builder target. All checks are against the run's OWN verified data
(D(0..14)=1,1,3,9,30,99,336,1134,3855,13086,44499,151263,514419,1749267,5949063
and the data/level_N.txt dumps), so a pass/fail is unambiguous.

## Characterization being proposed

Every 3D reachable config S at N>=1 divisions has:
  A1. EXACTLY 3 cells on its max level M  [hand-confirmed: every histogram in
      level_2..7.txt I read ends in "3": "0 2 3","0 2 2 3","0 1 5 3",
      "0 2 2 2 2 2 2 3", ...; pattern consistent through level_12]
  A2. those 3 top cells = {p+e1,p+e2,p+e3} = full child-triangle of a single
      EMPTY parent p at level M-1  [Eriksson Prop 24: n>=3 no double-play]
  A3. iterated cap-merge (replace the 3 top children by p) is deterministic
      and reaches {origin} in exactly N steps.
Bijection: reachable N-configs <-> deterministic reverse-merge sequences
<-> full ternary collapse trees <-> voidance sets of size N-1 (Eriksson
Prop 20 / Thm 9; 2D analogue A007902, chessboard pebbling CGMO).

## Exact recurrence (CLAIM B), verifiable without any new theory

Let conf(N) = all reachable N-configs, and
   f(C) = #(cells p in C : none of p+e1,p+e2,p+e3 lies in C)   (dividable).

CLAIM B:  D(N+1) = sum_{C in conf(N)} f(C)      for all N >= 0.

Hand-verified:
  N=0: conf(0)={{origin}}, f=1                       -> D(1)=1  correct
  N=1: conf(1)={{(1,0,0),(0,1,0),(0,0,1)}}, f=3      -> D(2)=3  correct
  N=2: 3 configs ("0 2 3", 5 cells each); sum of f = D(3)=9  (see script)

Why it is true: the map (C, dividable-cell p) -> config-with-p-divided is
injective, because the resulting (N+1)-config collapses to a unique (C,p) via
the deterministic cap-merge (CLAIM A3).  So dividing exactly the dividable
cells of every change N-config produces every (N+1)-config exactly once.

## Script to run

    python3 code/inventor/check_recurrence.py

It forward-BFSs distinct 3D configs N=0..7 and reports violation counts for
A1 (top==3), A2 (unique cap), A3 (deterministic collapse to origin) and the
per-N match `sum f(C) == D(N+1)` for CLAIM B.

Expected (prediction): all violation counts 0; CLAIM B match for every N.
If any claim fails, the reverse structure is NOT canonical and the whole
collapse-tree route is wrong — that is a real, cheap falsification.

## The open seam (NOT yet claimed true)

CLAIM B sums over conf(N), i.e. it still enumerates state space.  The true
reduction (to reach N=10000) must be a transfer DP that counts the
collapse-tree / voidance-set / folded-polyominoid objects directly, the 3D
analogue of the 2D two-index DP  G(k,m)  that computes A007902 without
enumerating.  Eriksson Fig.3 col n=3 (folded-polyominoid counts
1,3,12,57,300,1680,9900,...) is NOT D(N); D(N) is the refinement with the
reachable-position/level constraints.  That DP is the announced open seam.

Falsifiers that any candidate DP must satisfy (from MEMMORY/GOAL):
  compute D(14)=5949063 exactly,
  then D(20)=9204559704,
  then last nine digits of D(100)=780166455,
  then D(10000) mod 10^9.
A candidate that fails D(14) or D(20) is dead.
