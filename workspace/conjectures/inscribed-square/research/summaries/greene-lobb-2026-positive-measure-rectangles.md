# Jordan curves inscribe a positive measure of rectangles (Greene–Lobb 2026)

**Source:** Joshua Evan Greene, Andrew Lobb, arXiv:2604.17116 (math.GT/CO/SG), April 2026  
**URL:** https://doi.org/10.48550/arxiv.2604.17116  
**Full text:** `research/sources/greene-lobb-2026-positive-measure-rectangles.full.md`

## What it establishes

**Theorem (no regularity assumption on the curve):** Suppose γ ⊂ C is a Jordan curve of diameter 2R which encloses a region of area A. Then there exists a subset I ⊂ (0, π) of measure at least A/R² such that if θ ∈ I, then there exist four points on γ at the vertices of a rectangle whose diagonals meet at angle θ.

**Key points:**
- **This is a continuous-curve result with NO smoothness, rectifiability, local-monotonicity, or other regularity hypothesis.** The only quantities are the enclosing area A and the diameter 2R.
- A rectangle whose diagonals meet at angle θ is a θ-rectangle. The result says a positive measure of θ-values (at least A/R²) are always realized.
- The measure bound A/R² is the isodiametric ratio (times a constant). By the isodiametric inequality, A ≤ (π/4)·(2R)² = πR², so A/R² ≤ π. A square has diagonals meeting at angle π/2, so the square peg problem is the special case θ = π/2.
- **Corollary:** if A/R² > π/2 (the curve encloses more than half the area of a circle of the same radius), then θ = π/2 is in the interval, so **the curve inscribes a square**. This reproduces the GL 2024 Floer result (area > half of circle of equal diameter) but now with no regularity assumption at all.

**Method:** Jordan Floer homology with spectral invariants (Derivative Property + Triangle Inequality), extending GL 2024 (arXiv:2404.05179) from rectifiable to arbitrary continuous curves. The spectral invariants give the interval of angles I.

## Why it matters here

This is the **strongest known positive result for the general continuous case** — it makes no regularity assumption on γ at all. It does not solve the square peg problem (π/2 need not lie in the interval I unless A/R² > π/2), but it shows that *every* Jordan curve, however wild, inscribes rectangles of a positive measure of diagonal angles. The obstruction for squares specifically is whether θ = π/2 falls in the guaranteed interval; the paper's measure bound A/R² is exactly the isodiametric slack.

**This refines the minimal-counterexample structure:** a counterexample to the square peg problem must have A/R² ≤ π/2 (it encloses at most half the area of a circle of equal diameter) — otherwise GL 2026 gives a square. This is a new, sharp constraint on counterexamples.

## Claims

```claim
id: gl2026-positive-measure-rectangles
statement: For any Jordan curve γ ⊂ C of diameter 2R enclosing area A, there exists a subset I ⊂ (0,π) of measure at least A/R² such that γ inscribes a rectangle whose diagonals meet at angle θ for every θ ∈ I. No regularity hypothesis on γ.
status: asserted-by-source
evidence: Greene–Lobb 2026, arXiv:2604.17116, main theorem
holds-here: yes — the strongest continuous-curve rectangle result in the library; measure bound A/R² is the isodiametric ratio
falsifies: a Jordan curve with no rectangle of diagonal angle in a set of measure A/R²; or a correction/retraction of the preprint
```

```claim
id: gl2026-area-half-circle-square
statement: If a Jordan curve γ (no regularity hypothesis) of diameter 2R encloses area A with A/R² > π/2, then γ inscribes a square. (Square = rectangle whose diagonals meet at angle π/2.)
status: asserted-by-source
evidence: Greene–Lobb 2026, arXiv:2604.17116, corollary of the main theorem (θ=π/2 ∈ I when A/R² > π/2)
holds-here: yes — extends the GL 2024 area/diameter square result from rectifiable to all continuous curves
falsifies: a Jordan curve with A/R² > π/2 and no inscribed square
```

```claim
id: gl2026-minimal-counterexample-area-constraint
statement: A counterexample to the square peg problem, if one exists, must satisfy A/R² ≤ π/2 — it encloses at most half the area of a circle of the same radius. Otherwise Greene–Lobb 2026 forces an inscribed square.
status: derived
evidence: contrapositive of gl2026-area-half-circle-square
holds-here: yes — a new constraint on the minimal-counterexample structure in ROOT.md
falsifies: a counterexample with A/R² > π/2 and no inscribed square
```
