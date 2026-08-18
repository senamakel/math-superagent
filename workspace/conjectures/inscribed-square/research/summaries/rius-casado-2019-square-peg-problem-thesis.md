# Rius Casado 2019 — The Square peg problem (Bachelor thesis, Universitat de Barcelona)

**Source:** Raquel Rius Casado, "The Square peg problem," Treball final de grau, Facultat de Matemàtiques, Universitat de Barcelona, 15 June 2019. Advisor: Juan Carlos Naranjo del Val. hdl.handle.net/2445/151918. Direct PDF: `https://diposit.ub.edu/bitstreams/faaf3e1f-d770-4fab-b829-c543947edef7/download`. Full text: `research/sources/rius-casado-2019-square-peg-problem-thesis.full.md`.

**Status: full PDF now on disk and verified. This CLOSES the acquisition gap recorded in CONTEXT.md** — the previous on-disk "full text" was only the repository landing page; the claims `rius2019-stromquist-lemma-3.24` and `rius2019-locally-monotone-definition` were dropped as unbacked. They are now backed by a genuine full text.

## What the thesis contains

A full exposition of **Stromquist's 1989 proof** (Section 3.4, pp. 23–38) with the complete structure:

1. **The simplex Q** = {(x₁,x₂,x₃,x₄) ∈ ℝ⁴ : 0 ≤ x₁ ≤ x₂ ≤ x₃ ≤ x₄ ≤ 1} — a 4-simplex representing inscribed quadrilaterals (vertices w(xᵢ), in the same cyclic order as on the curve). Vertices v₀=(1,1,1,1), v₁=(0,1,1,1), v₂=(0,0,1,1), v₃=(0,0,0,1), v₄=(0,0,0,0); faces Fᵢ opposite vᵢ.
2. **Side-length functions** sᵢ(x) = ‖w(x_{i+1}) − w(xᵢ)‖, and the closed sets Qᵢ = closure of {x ∈ Q⁰ : sᵢ(x) = maxⱼ sⱼ(x)}. R = ⋂ᵢ Qᵢ = the set of **rhombi** (equal sides, nonzero). Thin/fat rhombi by diagonal comparison d₁₃ vs d₂₄; a **square-like quadrilateral** (equal sides and equal diagonals) is both thin and fat.
3. **The mod-2 degree argument** (Lemmas 3.25–3.27): a cover of closed vertex neighborhoods {Aᵢ} with vᵢ ∈ Aᵢ, Fᵢ ∩ Aᵢ = ∅, ⋃Aᵢ = A has deg(⋂Aᵢ) = 1 in ℤ₂. Applying to the cover {F₀ ∩ Qᵢ}: deg(F₀∩R) = deg(F₀∩R_THIN) + deg(F₀∩R_FAT) = 1. The face map h: F₀→F₄ (re-indexing vertices) swaps thin and fat, and continuity of the degree across slices of Q forces deg(F₀∩R_THIN) = deg(F₄∩R_THIN) = deg(F₀∩R_FAT), contradicting (3.1) unless R_THIN ∩ R_FAT ≠ ∅ — i.e., a square-like quadrilateral exists.
4. **Three smoothness conditions**, in increasing generality:
   - **Smooth (C¹)** — Lemma 3.24: each one-point quadrilateral lies in exactly one Qᵢ; Theorem 3.28: square exists.
   - **Condition A** — Lemma 3.30: no two chords in a neighborhood U(y) are perpendicular. Satisfied by smooth curves and polygons with only obtuse angles. **This is sufficient but NOT equivalent to local monotonicity** — it fails for polygons with acute angles, which are still locally monotone. (See discrepancy note below.)
   - **Locally monotone** (Def 3.34/3.35) — for every y there is an interval (y−µ, y+µ) and a direction u(y) such that w|_(y−µ,y+µ) is monotone in direction u(y) (i.e., w(x)·u(y) strictly increasing). Equivalent: no chord of the curve in U(y) is parallel to the normal n(y) ⊥ u(y). Satisfied by smooth curves, convex curves, polygons, piecewise-C¹ curves without cusps. **Theorem 3.36: a locally monotone curve in ℝ² admits an inscribed square.**

## The anti-shrinkout mechanism in Stromquist's proof (Theorem 3.36)

This is the load-bearing detail for this run: the locally-monotone case is proved by **smooth approximation with a parameter-space scale certificate**:

- Approximate w by w_ε(x) = (1/δ)∫₀^δ w(x+t)dt (a smoothing), which is C¹ and satisfies ‖w_ε − w‖ < ε.
- Each w_ε is locally monotone **with constant ½µ** (where µ is the constant of local monotonicity of w).
- Any inscribed square in a monotone segment is impossible; hence the square S_ε inscribed in w_ε (by Theorem 3.28) has **size ≥ µ in parameter space** — where |x| = min of the four segment lengths (x₄−x₁), ((1+x₃)−x₄), ((1+x₂)−x₃), ((1+x₁)−x₂).
- The sequence S_ε (ε→0) has a convergent subsequence; the limit square has size ≥ µ > 0 and is inscribed in w — **non-degenerate by construction**.

So Stromquist's own proof of the locally monotone case IS an anti-shrinkout argument with an explicit positive scale bound in parameter space. This is the strongest known positive class, and its proof contains the mechanism the general case lacks.

## Claim blocks

```claim
id: rius2019-stromquist-proof-structure
statement: Stromquist's 1989 proof (as exposited by Rius Casado): a 4-simplex Q of inscribed quadrilaterals, mod-2 degree of a vertex-neighborhood cover, thin/fat rhombus parity contradiction forcing a square-like quadrilateral (equal sides and equal diagonals); the locally monotone case is proved by smoothing with an explicit parameter-space lower bound (size ≥ µ) on the inscribed square, precluding shrinkout.
hypotheses: w simple closed curve in ℝ², locally monotone (every point has a neighborhood monotone in some direction).
holds-here: the structure the run must formalize in Lean (GOAL.md criterion 4); the size-bound mechanism is the template for a genuine extension.
evidence: full text verified (thesis PDF on disk); matches Matschke 2009's and Barber 2026 Def 1.9's locally-monotone definition.
status: sourced claim (thesis exposition of a published theorem; Stromquist 1989 Mathematika 36 paywalled but content now in library via this exposition + survey + Matschke 2009)
falsifies: an error in the thesis's exposition that changes the theorem's hypotheses or conclusion.
```

```claim
id: rius2019-condition-a-vs-locally-monotone
statement: The thesis's "Condition A" (no two chords in a neighborhood perpendicular) is strictly stronger than local monotonicity: polygons with an acute angle satisfy local monotonicity but fail Condition A.
hypotheses: plane curve.
holds-here: exact hypothesis for Lean — the formalized hypothesis must be local monotonicity (linear functional strictly monotone), not Condition A.
evidence: thesis §3.4 (Condition A definition, obtuse-polygon restriction; local monotonicity Def 3.34 covering all polygons); Matschke 2009 (linear functional definition).
status: sourced claim (discrepancy resolved: two different conditions)
falsifies: a polygon with an acute angle that fails local monotonicity; or a source showing Stromquist's Condition A is equivalent to local monotonicity.
```

## Discrepancy recorded (important)

The thesis's **Condition A** — "no two chords in U(y) are perpendicular" — is **not** the same as "locally monotone": it excludes any 90° chord-pair, whereas local monotonicity only requires the chords to have a common direction of positive projection (a linear functional strictly monotone). A polygon with an acute interior angle violates Condition A (near the corner, two chords can be perpendicular) but is still locally monotone (project onto the angle bisector direction). Matschke 2009 and Barber 2026 Def 1.9 both use the linear-functional definition for Stromquist's theorem, so **the formalizable hypothesis for Stromquist's theorem is local monotonicity, and Condition A is a strictly stronger sufficient condition** (the thesis's Lemma 3.30 covers only the obtuse-polygon case). This resolves the earlier ambiguity in CONTEXT.md Gaps, which listed "the exact 'weaker condition' (Condition A)" as unknown: the thesis supplies both conditions and their relationship.
