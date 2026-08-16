# Thread: the vertex-derived design (G-reduce) line at 99

```thread
id: thread-g-reduce
question: Does the vertex-derived design reduction
  (research/backward/derived-design-at-a-vertex.md) give a 99-specific
  nonexistence route: an srg(99,14,1,2) exists iff its vertex-derived design
  exists — a partial Steiner triple system on 84 points, 140 blocks,
  replication 5, attached by 84 cross lines to a 7K2, with mu=2 on the whole
  structure?
status: open
rests-on: c4, c5
blocked-by:
next: restate part (c) correctly (see finding below), then identify the
  99-specific question inside the (84,140,5) outer design that bvls(243)
  escapes.
```

## What the control run established

`code/out/g_reduce_control.captured.txt` (exact integer counts through
`lib.srg.is_srg`, controls rook(3) and bvls_graph()):

- **(a) HOLDS on both controls.** `N(v0)` induces (k/2)K2; the distance-2
  vertices biject with the non-edges of N(v0), each with exactly 2 neighbours
  in N(v0).
- **(b) HOLDS on both controls.** Triangles partition through/cross/outer =
  k/2, k(k-2)/2, k(k-2)(k-4)/12: rook 2/4/0, bvls 11/220/660, and the k=14
  formulas give 7/84/140 (replication 5) as integers.
- **(c) as worded in task `verify-g-reduce-controls` — "the outer design's
  collinearity graph has lambda=1, mu=2" — does NOT survive the controls.** On
  bvls(243) the outer collinearity graph has lambda=1 but mu in {0,1,2}
  (distribution 0:330, 1:11880, 2:9900), so the outer design is not itself an
  srg(v,k,1,2). The rook(3) verdict is internally inconsistent (the script
  prints lambda=1,mu=2 False yet "(c) HOLDS: True" — the outer design there is
  empty), which a worker should resolve rather than cite.

The correct (c) is the converse in `research/backward/derived-design-at-a-vertex.md`:
IF a structure of this shape has an outer collinearity graph with lambda=1 AND
mu=2, THEN the whole structure is an srg. The mu=2 condition is on the whole
graph (it couples outer points through their two neighbours in N(v0)), not a
property of the outer design alone.

## What would refute this line at 99

The reduction (a,b) is parameter-uniform setup, not a contradiction. The
nonexistence conclusion (G-unsat) is refuted by exhibiting a vertex-derived
design at (99,14,1,2) whose whole-structure collinearity graph has mu=2 —
that is, by the construction of the graph. The line proves nonexistence only
if the 99-specific attachment (84/140/replication-5) is shown impossible while
the 220/660 attachment at 243 is possible.
