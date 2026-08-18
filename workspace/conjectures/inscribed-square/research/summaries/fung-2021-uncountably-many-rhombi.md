# Fung 2021 — Every Jordan curve inscribes uncountably many rhombi

**Source:** Antony T.H. Fung, "Every Jordan curve inscribes uncountably many rhombi," arXiv:2010.05101 [math.MG], 10 Oct 2020; published **Geom. Dedicata 215(1) (2021), 10.1007/s10711-021-00659-2**. Full text: `research/sources/fung-2021-uncountably-many-rhombi.full.md`.

**Status: full text now verified on disk. This REPLACES the earlier acquisition-error record** (the old file with this name was an unrelated astrophysics preprint; the correct arXiv ID is **2010.05101**, not 2010.04166).

## What it establishes

**Theorem 1.1.** Let γ : S¹ → ℝ² be a Jordan curve. Then there exists an open interval of angles such that there exist inscribed rhombi of all those angles. Furthermore, if γ does not contain a **special corner**, then there exist inscribed rhombi of all angles.

**Corollary.** Every Jordan curve in ℝ² inscribes uncountably many rhombi.

**No regularity condition is assumed on the Jordan curve.**

### Key definitions (exact, for Lean)

- **Line of angle θ:** line x sin θ − y cos θ = const (angle θ with x-axis, anticlockwise).
- **Special corner of angle θ:** a point p ∈ im γ such that both the line of angle θ through p and the line of angle θ+π/2 through p intersect im γ only at p. Equivalently (translating p to the origin and rotating): the entire curve lies within a single quadrant.
- **Special corner:** a point that is a special corner of angle θ for at least one θ.
- **Rhombus of angle θ:** a rhombus whose two diagonals are lines of angles θ and θ+π/2. (Note: "rhombus of angle θ" = "rhombus of angle θ+π/2".)

### Structure of proof

- Proposition 1.6: no special corner of angle θ ⇒ inscribed rhombus of angle θ.
- Proposition 1.7: exactly one special corner ⇒ ∃ θ₀, ε such that no special corner of angle θ for θ ∈ (θ₀−ε, θ₀+ε).
- Proposition 1.8: ≥ 2 special corners p, q with line pq of angle θ₀ ⇒ inscribed rhombus of angle θ for θ ∈ (θ₀−ε, θ₀+ε).
- Method: Emch's median construction; when medians are not paths (non-analytic curve), a new object called a **pseudopath** (Def 2.1) replaces the path. M_τ ∩ M_σ corresponds to quadrilaterals with perpendicularly bisecting diagonals = rhombi.

## Claim blocks

```claim
id: fung2021-uncountably-many-rhombi
statement: Every Jordan curve in ℝ² (no regularity assumed) inscribes uncountably many rhombi; more precisely, an open interval of angles each admitting an inscribed rhombus of that angle, and all angles if the curve has no special corner.
hypotheses: γ : S¹ → ℝ² Jordan curve (continuous injective).
holds-here: continuous curves — a rhombus result, NOT a square result. The rhombus→square gap is exactly the equality-of-diagonals condition.
evidence: full text verified (arXiv:2010.05101; Geom. Dedicata 215, 2021).
status: theorem (published; journal version Geom. Dedicata 2021)
falsifies: a Jordan curve whose inscribed rhombi are only finitely many, or an angle interval statement failing.
```

## Relation to existing library

- **Fixes the acquisition error** recorded in CONTEXT.md Gaps ("rhombi theorem not in library"). The claim `fung2021-uncountably-many-rhombi` is now backed by a real full text.
- The rhombus result narrows the obstruction to the square: perpendicular diagonals (rhombi) are free for all continuous curves; **equal diagonals** (the square condition) are the hard part — exactly as recorded in the existing CONTEXT.md claim `fung2021-rhombi-not-squares`.
- Wright 2025 (Amer. Math. Monthly 10.1080/00029890.2025.2556357) gives a short proof that a given line direction admits a rhombus with two sides parallel to it; and Wright 2026 (Aequationes Math.) extends to diagonals collinear with a point. Both are related, complementary (monthly-short) treatments; neither is on disk yet.
