# David Ellis, "Almost Isoperimetric Subsets of the Discrete Cube" (CPC 2011)

Source URL:
https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/abs/almost-isoperimetric-subsets-of-the-discrete-cube/3E878F4F45A483ADE934A011884FC716

Full source note: [[ellis-almost-isoperimetric-cube-2011]]

## What this source establishes

Edge-isoperimetric problem on the cube, plus quantitative stability.

- **Extremal families:** for A ⊆ {0,1}^n of fixed size, the edge boundary
  ∂A (edges crossing A → complement) is minimised by **subcubes** (and, in some
  parameter ranges, by Hamming balls / completed layers). Subcubes = sets fixing
  some coordinates.
- **Stability (main theorem):** if A has edge boundary |∂A| ≤ ε|A| for small
  ε, then A can be turned into a subcube by at most
  (2ε / log2(1/ε)) · |A| additions and deletions (ε below an absolute constant).
- **Sharp converse:** if |A| = 2^t and A cannot be made into a subcube by fewer
  than δ|A| additions/deletions, then |∂A| ≥ c(δ)·|A| for an absolute c(δ) > 0;
  sharp when δ = 1/2^j, j ∈ {1,...,t}.

Method: stability of shadows / edge-isoperimetric inequalities (Samorodnitsky
2009), Roberts' vertex-isoperimetric stability.

## Why it is here and what it establishes for this run

This is a boundary-stability source. It **fixes the extremal structure** of sets
near the edge-isoperimetric minimum: they cluster around subcubes. That is the
same subcube/parity-layer shape that Barber's maximum-independent-set
classification and the sqrt-construction extremal family share, so Ellis is a
second independent source for the "subcubes are edge-extremal" fact already in
Barber–Erde.

It does **not** bound the maximum internal degree D(S). It bounds an outer
(average-style) boundary quantity. So for the stated goal (f(n) = min D(S) over
|S| = 2^{n-1}+1) it is part of the four "stuck" isoperimetric techniques — it
confirms the obstruction, it does not attack D(S).

It bears on the threshold-shadow skeleton's G2 lemma (whether
A ↦ |O_{≤d}(A)| over A ⊆ E, |A|=a is maximised by a Hamming ball): the
near-maximal (small d) regime is governed by edge boundary, and Ellis's stability
quantifies how close the competing A can be to subcubes.

## Claim block

```claim
id: ellis-edge-isoperimetric-stability
statement: If A ⊆ {0,1}^n has edge boundary |∂A| <= ε|A| (ε small), then A can
  be made into a subcube by at most (2ε/log2(1/ε))|A| additions and deletions;
  and if |A| = 2^t and A is far from every subcube (>= δ|A| modifications), then
  |∂A| >= c(δ)|A| with c(δ) an absolute function, sharp for δ = 1/2^j.
hypotheses: A ⊆ {0,1}^n; ε below an absolute constant; |A| a power of two for
  the second part.
holds-here: yes as a statement about edge-boundary stability; it constrains the
  A-side extremal structure of the threshold-shadow lemma but does not itself
  bound D(S).
status: asserted-by-source (Ellis 2011); not re-derived here.
bearing: second source that subcubes are edge-isoperimetric-extremal; quantifies
  near-isoperimetric structure; relevant to the G2 extremal-family guess, not to
  an upper or lower bound on D(S) directly.
falsifies: an explicit A with |∂A| <= ε|A| but needing more than
  (2ε/log2(1/ε))|A| modifications to reach a subcube; or a size-2^t set far from
  subcubes with |∂A| < c(δ)|A|.
anchor: Ellis, CPC 2011
```
