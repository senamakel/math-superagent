# Wikipedia: Conway's 99-graph problem (encyclopedic statement)

<!-- source: https://en.wikipedia.org/wiki/Conway%27s_99-graph_problem -->
<!-- full text: research/sources/wikipedia-conway-99-graph.full.md -->

## What it establishes (encyclopedic, secondary but traceable)

The standard statement of the problem. A Conway 99-graph is a strongly regular
graph srg(99,14,1,2): every two adjacent vertices have exactly one common
neighbour (λ=1, each edge in a unique triangle) and every two non-adjacent
vertices have exactly two common neighbours (μ=2, each non-edge in a unique
4-cycle). Central structural fact recorded: **the neighbourhood of every vertex
induces 7 disjoint edges (a perfect matching 7K₂)** — "locally 7K₂".

Status recorded: the existence question is **open**; the two known members of
the same λ=1,μ=2 family are the rook's graph (9,4,1,2) and the
Berlekamp–van Lint–Seidel graph (243,22,1,2).

## Consistency checks against the library
- Lambda=1 → N(v) is a perfect matching on 14 vertices: consistent with claim c5
  (checked) and with the windmill/7K2 structure shared by srg(57,14,1,4).
- Open status: consistent with Brouwer's table `?` and the whole library.
- v=|V|=99, k=14, edges=99·14/2=693, triangles=231 (=7 per vertex).

## Implication / status
Secondary source; confirms the restatement, the local structure, and open
status. Use the primary sources (problem.md derivation, Brouwer table, the
construction papers) for anything load-bearing rather than quoting Wikipedia.

```claim
id: wikipedia-conway99-statement
statement: srg(99,14,1,2) is open; every vertex's neighbourhood induces a
  perfect matching (locally 7K2); the two existing members of the family are
  the rook's graph (9,4,1,2) and the Berlekamp-van Lint-Seidel graph (243,22,1,2).
hypotheses: none (encyclopedic statement).
holds-here: yes.
status: asserted-by-source (Wikipedia, secondary; the 7K2 fact is elementary
  from lambda=1 and independently checked, the two controls verified by oracle).
bearing: the standard encyclopedic statement; cross-confirms c4, c5,
  existence-status-open.
anchor: research/sources/wikipedia-conway-99-graph.full.md
```

[[wikipedia-conway-99-graph.full]]
