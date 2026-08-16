# kill-n3-ge1-case: resolved at the local-closure level

Task asked: can a disjoint triangle pair joined by exactly 2 edges (the n3
configuration: T1={a,b,c}, T2={d,e,f}, cross edges a-d and b-e, the other
seven cross pairs non-joined) extend AT ALL in a lambda=1, mu=2, locally-7K2
graph, as a FINITE SAT/CP-SAT-style question over the bounded local ball?

## Result (executed, exact)

1. **The shared arc-consistency engine has a soundness bug.** When a pair is
   saturated (its required common neighbours are already fixed), the engine
   forces every candidate out on BOTH sides (`a-v=0 AND b-v=0`). The sound
   conclusion is only the 2-SAT clause `NOT(a-v AND b-v)` — at least one edge
   off, not both. For the n3 seed the pair (a,b) (lambda witness c) then
   forces candidate vertex `6` off both sides, flipping the already-fixed
   `a-6=1` lambda-witness of edge (a,d) → spurious `CONTRADICTION` `return
   False` with a clean log. Confirmed by direct trace
   (`code/out/n3_seed_consistency_ub.py` + standalone trace).

2. **The n3 seed IS locally consistent.** A sound upper-bound oracle
   (adjacent pair ≤ 1 common neighbour, non-adjacent ≤ 2, deficits satisfiable
   by the ~91 outside vertices, complete enumeration of the 9 free interior
   edges of the 8-vertex forced closure = 512 assignments) finds 2 satisfying
   assignments. So no local obstruction exists at this radius.

3. The stale capture `code/out/n3_local_propagation.captured.txt` (produced by
   the pre-refactor engine) claiming CONTRADICTION for this seed must not be
   read as a theorem. Re-running the current program still returns False but
   ONLY because of the saturation over-forcing bug; the propagation log itself
   is clean (just two witness additions).

## What this settles, and what it does not

- Settles: the local-closure question of `kill-n3-ge1-case`. The 2-edge-joined
  disjoint triangle pair extends locally; there is no local contradiction from
  (lambda=1, mu=2, 7K2) at this radius.
- Does NOT settle: global existence/nonexistence of srg(99,14,1,2). An
  8-vertex patch is not the graph; local consistency neither proves nor
  disproves it. A real attack must propagate to a larger forced patch, or the
  engine's saturation branch must be replaced by a proper `NOT-both`
  (2-SAT / at-least-one-off) propagator that does not manufacture flips.

## Controls

rook(3)=srg(9,4,1,2), bvls=srg(243,22,1,2), doily=srg(15,6,1,3), GQ(2,4)=
srg(27,10,1,5) all pass is_srg and the lambda/mu/7K2 checks in the probe,
so the rule set itself is not contradictory — the contradiction was an engine
bug, not a property of (lambda=1, mu=2, 7K2).

## Directive 14 write-up — the false positive, recorded properly

This result is recorded as the canonical claim `n3-seed-locally-consistent-radius1`
(note `research/notes/n3-seed-locally-consistent-radius1.md`, anchor
`code/out/n3_seed_consistency_ub.captured.txt`). In one sentence: the
2-edge-joined disjoint triangle pair is LOCALLY CONSISTENT — under the only
criterion arc-consistency may soundly conclude (adjacent pair ≤1 common
neighbour, non-adjacent ≤2, deficits satisfiable by the ~91 outside vertices),
complete enumeration of the 9 free interior edges of the 8-vertex forced
closure (512 assignments, exact) finds 2 satisfying assignments, so the seed
extends locally; the earlier CONTRADICTION was the localprop.py over-forcing
bug, not an obstruction. Next question (directive 14): at what radius, if any,
does the seed stop extending?

## Audit of localprop.py consumers

`grep` for `localprop` across the workspace: the ONLY consumer of
`code/lib/localprop.py` is `code/out/n3_local_propagation.py` (imports
`PartialGraph`, `neighbourhood_is_7k2`). Its capture
`code/out/n3_local_propagation.captured.txt` is now annotated SUPERSEDED at the
top. No other code/out script imports the engine, so no other capture can be
contaminated by the over-forcing saturation bug.

## Tooling: enumeration vs sat_solver

The 8-vertex closure has 9 free interior edges = 512 assignments; complete
enumeration is exhaustive, needs no encoder validation, and is more
trustworthy — keep it (directive 14 confirms). Reach for sat_solver only when
the radius grows so the free-bit count outgrows exhaustive enumeration
(≈ 2^20 assignments); the radius at which that happens is to be reported when
the ball is grown.
