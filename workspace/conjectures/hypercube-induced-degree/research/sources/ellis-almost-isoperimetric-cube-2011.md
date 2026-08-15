# David Ellis, "Almost Isoperimetric Subsets of the Discrete Cube" (CPC, 2011)

Source URL:
https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/abs/almost-isoperimetric-subsets-of-the-discrete-cube/3E878F4F45A483ADE934A011884FC716
(Retrieved via `read_sources`; direct PDF download blocked by network boundary.)

## What this source establishes

- **Edge-isoperimetric problem on the cube:** for A ⊆ {0,1}^n of a given size,
  the edge boundary ∂A (edges crossing A to its complement) is minimised by
  subcubes (and, in parameter ranges, by Hamming balls/completed layers). The
  extremal families are the subcubes — sets fixing some coordinates.
- **Quantitative stability:** if A has edge boundary at most ε|A| for small ε,
  then A can be turned into a subcube by at most (2ε/log2(1/ε))·|A| additions
  and deletions (ε below an absolute constant).
- **Sharp converse:** if |A| = 2^t and A cannot be made into a subcube by fewer
  than δ|A| additions/deletions, then |∂A| >= c(δ)·|A| with c(δ) an absolute
  positive function of δ (below a fixed constant); sharp when δ = 1/2^j,
  j ∈ {1,...,t}.
- Method: connections with stability of shadows and edge-isoperimetric
  inequalities (Samorodnitsky 2009), Roberts' vertex-isoperimetric stability.

## Why it is here

The `bipartite-threshold-shadow` skeleton's G2 lemma asks whether the map
`A ↦ |O_{≤d}(A)| = |{x ∈ O : |N(x)∩A| ≤ d}|` over A ⊆ E with |A| = a is
maximised by a Hamming ball (initial segment of the simplicial/colex order).
The extreme case of this (d large, so that O_{≤d}(A) is near the whole of O) is
governed by the edge boundary: a small number of vertices x with few neighbours
in A means a large A with small edge-boundary-induced structure. Ellis's
stability theorem quantifies that near-extremal sets are close to subcubes,
bearing directly on which A could beat the Hamming ball in G2 — the seed for
the claimed extremal family. It is a boundary-stability source, so like the
rest of the library it does not by itself bound the *maximum internal degree*
D(S), but it fixes the structure of the near-extremal A side of the threshold
picture.

## Claim block

```claim
id: ellis-edge-isoperimetric-stability
statement: If A ⊆ {0,1}^n has edge boundary |∂A| <= ε|A| (ε small), then A can
  be made into a subcube by at most (2ε/log2(1/ε))|A| additions and deletions;
  and if |A| = 2^t and A is far from every subcube (>= δ|A| modifications), then
  |∂A| >= c(δ)|A| with c(δ) an absolute function, sharp for δ = 1/2^j.
hypotheses: A ⊆ {0,1}^n; ε below an absolute constant; |A| a power of two for
  the second part.
holds-here: yes as a statement about edge-boundary stability of subsets of the
  cube; it constrains the A-side extremal structure relevant to the
  threshold-shadow lemma G2, but does not itself bound D(S).
status: asserted-by-source (Ellis 2011).
bearing: quantifies how close near-isoperimetric sets are to subcubes; the
  subcube/parity-layer structure is what the maximum-independent-set
  classification (Barber 2012) and the edge-isoperimetric extremal family
  share. Relevant to the extremal-family guess in the threshold-shadow
  skeleton, and as a second independent source for the subcubes-are-extremal
  edge-isoperimetric fact already in Barber–Erde.
falsifies: an explicit A with |∂A| <= ε|A| but requiring more than
  (2ε/log2(1/ε))|A| modifications to become a subcube (against the stated
  constant), or a size-2^t set far from subcubes with |∂A| < c(δ)|A|.
anchor: CPC 2011, Ellis
```
