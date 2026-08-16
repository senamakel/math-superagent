# Wikipedia: Berlekamp–van Lint–Seidel graph (the 243-vertex positive control)

<!-- source: https://en.wikipedia.org/wiki/Berlekamp%E2%80%93van_Lint%E2%80%93Seidel_graph -->
<!-- full text: research/sources/wikipedia-berlekamp-vanlint-seidel-graph.full.md -->

## What it establishes

The Berlekamp–van Lint–Seidel graph is the strongly regular graph with
parameters (243,22,1,2), i.e. the **second existing member of the Conway
λ=1,μ=2 family after the rook's graph**, and the largest of the two that the
run uses as a negative control. Spectrum: 22¹, 4¹³², (−5)¹¹⁰.
It is an **edge-transitive, vertex-transitive** graph (one of the few known
with λ=1, μ=2), built as the coset graph of the perfect ternary Golay code.

## The construction (used by the oracle's bvls_graph())

1. Take the 5×11 parity-check matrix H of the ternary Golay [11,6,5] code
   (kernel = the 3⁶-word code).
2. Vertices = the 3⁵ = 243 cosets of the code in F₃¹¹ (equivalently the 243
   syndromes).
3. Two cosets are adjacent iff they differ by a weight-1 vector (± one
   coordinate), i.e. iff their syndromes differ by ± one column of H.
4. Result: srg(243,22,1,2), spectrum 4¹³², −5¹¹⁰.

## Negative-control role here
The run's oracle verifies bvls_graph() is srg(243,22,1,2) by exact integer
common-neighbour counting (code/out/oracle_verification.captured.txt: 2673
edges and PASS). It is the structurally important control because it shows a
λ=1,μ=2 srg with k=22 exists with a large automorphism group — the existence
question at 99 is therefore not about a family-impossible structure, but about
the specific k=14 case.

## Status
Secondary source; the construction recipe is independently reproduced by the
oracle (checked). The existence of srg(243,22,1,2) is primary-established by
Berlekamp–van Lint–Seidel 1973 / van Lint 1975 (five-member list claim).

```claim
id: wikipedia-bvls-construction
statement: The Berlekamp-van Lint-Seidel graph is srg(243,22,1,2), coset graph
  of the perfect ternary Golay code (5x11 parity-check H; 243 cosets; adjacent
  iff syndromes differ by a unit column), spectrum 22^1, 4^132, (-5)^110. It is
  vertex- and edge-transitive.
hypotheses: perfect ternary Golay code machinery.
holds-here: yes — the run's bvls_graph() reproduces exactly this construction
  and the oracle verifies (243,22,1,2) (checked).
status: asserted-by-source (Wikipedia); construction verified computationally
  by the run's oracle (checked) and primary-supported by Berlekamp-van
  Lint-Seidel 1973 / van Lint 1975.
bearing: the second negative control; shows a lambda=1 mu=2 srg with a large
  automorphism group exists, so 99-openness is specific to k=14, not a
  family-wide obstruction.
anchor: research/sources/wikipedia-berlekamp-vanlint-seidel-graph.full.md
```

[[wikipedia-berlekamp-vanlint-seidel-graph.full]]
