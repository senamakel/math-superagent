# Thread: the c7 μ=2 common-neighbour-independence lead

```thread
id: thread-c7-4vertex-lead
question: Does c7 — the two mu=2 common neighbours of a nonadjacent pair are
  nonadjacent — give any 99-specific constraint, or is it a family-uniform
  restatement of mu=2 that constrains 99 no more than 9 and 243?
status: open
rests-on: c7-4vertex-mu2-common-neighbour-nonadjacent, c5
blocked-by:
next: name the configuration C that c7 + 7K2 would forbid at 99, and check
  bvls(243) against it.
```

## Status of the lead

c7 SURVIVED the 9/243 test (`code/out/c7_4vertex.captured.txt`: both controls
have independent mu=2 common-neighbour sets, 0 violations). That is the
expected outcome, not a result: c7 is sourced as a theorem for all lambda<=1
SRGs (Sims' criterion, Brouwer-Ihringer-Kantor Prop 2.1), so it holds
identically at 9, 99, and 243. A family-uniform theorem constrains 99 no more
than it constrains the existing graphs, and c7 is in fact just the mu=2
condition stated on common neighbours.

## What refutes it at 99

The lead is **dead** if: every configuration C that c7 (combined with the k=14
local structure — 7K2, 231 triangles, replication 7) would forbid in a 99-graph
is also absent from bvls(243) under c7 + the k=22 local structure (11K2). Then
c7 adds no separating power: it forbids at 99 exactly what it already forbids
at 243, so it cannot distinguish 99 from the existing 243 graph.

The lead is **alive** only if: there is a configuration C present in bvls(243)
that c7 + 7K2 (with k=14 counting) forces to be impossible at 99. Name that C
and check it — that is the next step, and until it is done c7 is a constraint
to combine, not a result.
