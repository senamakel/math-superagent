# Naseri Sadr 2024 — A Table Theorem for Surfaces with Odd Euler Characteristic (incl. square peg for star-shaped curves)

**Source:** Ali Naseri Sadr, arXiv:2412.01977 [math.SG?], 2 Dec 2024. Full text: `research/sources/naseri-sadr-2024-table-theorem-surfaces.full.md`.

**Status: verified against full text on disk (arXiv preprint). Advisor: John Baldwin and Josh Greene.**

## What it establishes (two distinct results)

**1. Table Theorem for surfaces (main theorem, Theorem 1.1).** Let (Σ, g) be a Riemannian surface with χ(Σ) odd and f a continuous real-valued function on it. Then for every d > 0, f admits a *table* with diameter d — i.e., the vertices of a square of diameter d (image under exp_g of a square of diameter d centered at the origin in a tangent plane) at which f takes the same value.

**Corollary 1.2.** For a metric g on S² invariant under the antipodal map and f an even function, f admits a table of every diameter d — resolving the table problem for even functions (Dyson's 1951 conjecture in this setting).

**Method:** deform all circles of diameter d in TΣ by (x,v) ↦ (x, f(exp(x,v))·v); the subspace C of centers of inscribed squares in the resulting star-shaped C² Jordan curves must intersect the zero section when χ(Σ) is odd, because a generic C² star-shaped curve inscribes an odd number of graceful squares. Uses Sard–Smale transversality; the ℤ₂-cycle argument.

**2. Square Peg for star-shaped C² curves (Appendix A, Theorem A.5).** Every star-shaped C² Jordan curve inscribes at least one **graceful** square (vertices in the same cyclic order on the curve as on the square). **Corollary A.6:** a generic star-shaped curve inscribes an *odd* number of graceful squares.

**Method (Appendix A):** parametrize the star-shaped curve by θ ↦ h(θ)·θ with positive h ∈ C²(S¹); parametrize inscribed quadrilaterals by P̃ = S¹ × Δ̊₃ (the interior of a 3-simplex — the cyclic-order configuration space); the map φ_h embeds P̃ into ℝ⁸, and graceful squares correspond to φ_h(P̃) ∩ Ã where Ã is the space of 4-tuples with equal sides and equal diagonals. A ℤ₄ cyclic action is quotiented out. The universal map Φ : C²₊(S¹) × P → V is a submersion (Lemma A.1); 𝒬 = Φ⁻¹(A) is a connected codimension-4 submanifold with Fredholm projection π of index 0 (Lemma A.2). Generic functions are regular values (Sard–Smale, Cor A.4). A cobordism from an ellipse (unique square) to the given h forces an odd number of graceful squares, contradicting "none".

## Why it matters for this run

- **Theorem A.5 is a new positive class**: star-shaped C² curves are *not* a subset of locally monotone curves (a star-shaped curve with a cusp-like behavior at the origin or unbounded winding in radial slices can fail local monotonicity), and the class is not covered by the library's existing positive classes as a *named* class. The proof is a modern transversality (Sard–Smale, Fredholm index) version of the configuration-space argument — the same family as the run's target method.
- **The graceful condition is exactly the cyclic-order condition** problem.md warns about (a genuine inscribed square's vertex order on the curve matches its order on the square; a crossed quadrilateral satisfies the algebraic square conditions without it). The star-shaped proof establishes the *graceful* (ordered) version directly — valuable for the Lean formalization, which uses the cyclic-order hypothesis.
- The table-theorem direction is the *reverse* of Friedl–İnce 2023: Friedl–İnce ask when the table theorem implies the square peg problem; Naseri Sadr uses the square peg problem (for star-shaped curves) to prove table theorems on surfaces.

## Claim blocks

```claim
id: naserisadr2024-star-shaped-square
statement: Every star-shaped C² Jordan curve inscribes at least one graceful square (vertices in the same cyclic order on the curve as on the square); a generic star-shaped C² curve inscribes an odd number of graceful squares.
hypotheses: star-shaped C² Jordan curve in the plane (boundary of a star-shaped region, C², positive radial function h ∈ C²(S¹) parametrizing θ ↦ h(θ)θ).
holds-here: a positive class NOT subsumed by locally monotone as a named class; the graceful/cyclic-order condition matches problem.md's nondegeneracy requirement.
evidence: full text verified (arXiv:2412.01977, Appendix A, Theorem A.5, Corollary A.6).
status: theorem (arXiv preprint; not yet peer-reviewed as far as this library knows)
falsifies: a star-shaped C² Jordan curve with no graceful inscribed square; or an error in the submersion/Fredholm argument (Lemma A.1/A.2).
```

```claim
id: naserisadr2024-table-theorem-odd-euler
statement: On a Riemannian surface (Σ,g) with χ(Σ) odd, every continuous real-valued function admits a table of every diameter d; for even functions on antipodally-invariant S², every diameter d.
hypotheses: (Σ,g) Riemannian surface, χ(Σ) odd; f continuous; d > 0.
holds-here: table-theorem direction (uses the square peg problem for star-shaped curves) — reverse direction of Friedl–İnce 2023.
evidence: full text verified (Theorem 1.1, Corollary 1.2).
status: theorem (arXiv preprint)
falsifies: a Riemannian surface of odd Euler characteristic with a continuous function admitting no table of some diameter d.
```

## Relation to existing library

- Complements Friedl–İnce 2023 (table theorem → square peg, and its limits) with the reverse direction (square peg → table theorem on surfaces).
- The star-shaped positive class is a candidate for the run's "named subclass strictly larger than locally monotone" extension target (GOAL.md) — or at least a distinct class whose proof is a modern transversality version of the same configuration-space argument the run is formalizing.
- The graceful-square count (odd, generically) matches the CDM/Emch/Jerrard/Stromquist parity mechanism, now for star-shaped curves with a Fredholm-transversality proof.
