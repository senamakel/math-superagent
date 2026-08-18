# Polygons inscribed in Jordan curves with prescribed edge ratios (Xu–Zhou 2024)

**Source:** Yaping Xu, Ze Zhou, Topology and its Applications (2024), DOI 10.1016/j.topol.2024.108971; arXiv:2211.05515.

**Full text:** `research/sources/xu-zhou-2024-polygons-prescribed-edge-ratios.full.md`

## What it establishes

**Main theorem (Theorem 1.2):** Let J be a simple closed curve in Rᵏ (k ≥ 2) that is differentiable with non-zero derivative at a point A₀ ∈ J. For a tuple of positive reals a₁, …, aₙ (n ≥ 3), each of which is less than the sum of the others (the triangle-type inequality), there exists a polygon Qₙ inscribed in J with sides of lengths proportional to (a₁, …, aₙ).

**Corollary 1.3:** For any target triangle T, there exist points A₁, A₂ on J such that A₀A₁A₂ forms a triangle similar to T.

**Theorem 1.4:** The constructed polygon Qₙ is convex if J is strictly convex in R².

**Theorem 1.5:** For any A₀ ∈ J and almost every vector (a₁, …, aₙ) in a suitable set W, there are at most finitely many inscribed polygons starting at A₀ with side lengths proportional to (a₁, …, aₙ).

**Hypothesis:** The differentiability is only needed at the single point A₀ (nonzero derivative there). The rest of the curve can be arbitrary.

## Why it matters here

- The n = 4 case with a₁ = a₂ = a₃ = a₄ gives an inscribed quadrilateral with four equal sides — a rhombus. Combined with equal diagonals... but the theorem only prescribes side lengths, not angles, so the n=4 equal-sides case gives rhombi, not squares. (Fung 2021 gives uncountably many rhombi with no hypothesis at all.)
- The square peg problem is the special case a₁=a₂=a₃=a₄ plus equal diagonals. Xu–Zhou give the side-length prescription for differentiable-at-a-point curves; the angle/diagonal condition is not addressed.
- The hypothesis (differentiable at one point) is nearly the weakest possible for an inscribed-polygon statement with prescribed edge ratios, and the result is in the same family as the polygonal pegs problem.

## Claims

```claim
id: xu-zhou-2024-prescribed-edge-ratios
statement: A simple closed curve in Rᵏ differentiable with nonzero derivative at a point A₀ inscribes, for any positive a₁,…,aₙ each less than the sum of the others, a polygon with side lengths proportional to (a₁,…,aₙ).
status: asserted-by-source
evidence: Xu–Zhou 2024, Topology and its Applications, arXiv:2211.05515, Theorem 1.2
holds-here: yes — the n=4 equal-sides case gives a rhombus (matching Fung 2021 but with a different hypothesis); the diagonal-equality condition for squares is not addressed
falsifies: a curve differentiable at a point failing to inscribe a polygon with prescribed side lengths; or a correction/retraction
```
