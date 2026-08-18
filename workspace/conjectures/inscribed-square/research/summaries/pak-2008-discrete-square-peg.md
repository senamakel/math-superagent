# Pak 2008 — The Discrete Square Peg Problem

**Source:** Igor Pak, "The discrete square peg problem," arXiv:0804.0657 [math.MG], 4 Apr 2008. Full text: `research/sources/pak-2008-discrete-square-peg.full.md`. (Not a journal-published paper as far as this library knows; arXiv preprint.)

## What it establishes

Two new **elementary, direct proofs** that every simple polygon inscribes a square — the first direct proofs of the piecewise-linear case (previously obtained only as a corollary of more technical smooth/analytic results). Both proofs are combinatorial/geometric, not degree-theoretic.

**Main Theorem.** Every simple polygon on a plane has an inscribed square.

**Theorem 2.1.** Every generic simple polygon has an **odd number** of inscribed squares. (Genericity here: the polygon has no orthogonal edges and its angles lie between π/2 and 3π/2 — the proofs are done for this case, and the general polygon case follows by a deformation argument.)

## The mechanism (why it matters for this run)

**Proof 1 (via inscribed triangles).** Fix orientation on the generic polygon X. For an ordered pair (y,z) ∈ X×X, let u, v be the other two vertices of the square [zyuv]. U = {(y,z) : u ∈ X}, V = {(y,z) : v ∈ X}. For generic X, U_y = {z : (y,z) ∈ U} is finite: such z lie in X ∩ X′ where X′ is X rotated π/2 about y, so with no orthogonal edges the intersection is finite. The goal is U ∩ V ≠ ∅. The parity/intersection argument (with Lemma 2.2 as the local engine) gives the odd count.

**Lemma 2.2.** Four lines ℓ₁,…,ℓ₄ in R² in general position determine a unique square A = [a₁a₂a₃a₄] with aᵢ ∈ ℓᵢ, oriented clockwise; the map (ℓ₁,…,ℓ₄) ↦ (a₁,…,a₄) is continuously differentiable where defined.

**Why it is an oracle/Lean anchor:** "every generic simple polygon has an odd number of inscribed squares" is a **finite, exact, checkable statement** — the polygon is a finite list of rational/algebraic vertices, and the square condition is exact algebra. This is a far better machine-verification target than a smooth curve: the odd-count theorem is the discrete analogue of the smooth "generic odd number of squares" (CDM 2022) and is elementary to state in Lean. Any polygon-based oracle work in this run should verify Theorem 2.1's count on small generic polygons (exact arithmetic, no floating point) and report it as a check of Pak's theorem — not as new mathematics.

## Claim blocks

```claim
id: pak2008-every-simple-polygon-square
statement: Every simple polygon in the plane inscribes a square (there exist four points on the polygon that are the vertices of a square).
hypotheses: γ is a simple (non-self-intersecting) polygon in R²; no regularity beyond piecewise-linearity.
holds-here: yes — polygons are the exact-arithmetic instance of Stromquist's locally-monotone class; this is a direct elementary proof of the PL case.
evidence: full text verified (arXiv:0804.0657); two direct proofs; the polygon case previously only known via smooth/analytic arguments.
status: theorem (arXiv preprint; the statement itself is classical — polygonal case of Stromquist 1989 / Emch 1916)
falsifies: a simple polygon with no inscribed square; or a published counterexample to the PL case.
```

```claim
id: pak2008-generic-polygon-odd-squares
statement: Every generic simple polygon (angles in (π/2, 3π/2), no orthogonal edges) has an odd number of inscribed squares.
hypotheses: simple polygon, generic in the above sense.
holds-here: yes — this is the discrete analogue of the smooth generic-odd-count theorem (CDM 2022) and a direct oracle/Lean verification target with exact arithmetic.
evidence: full text verified (arXiv:0804.0657, Theorem 2.1); proof via U ⊂ X×X, V ⊂ X×X intersection parity.
status: theorem (arXiv preprint)
falsifies: a generic simple polygon with an even number of inscribed squares (this is exactly what a polygon oracle should check on small cases).
```

```claim
id: pak2008-four-lines-unique-square
statement: Four lines in general position determine a unique clockwise-oriented square with one vertex on each line, and the map from the lines to the vertices is C¹ where defined.
hypotheses: four lines in R² in general position (no parallel coincidences degenerating the configuration).
holds-here: yes — a local engine for the polygon proof; a clean exact statement for Lean.
evidence: full text verified (arXiv:0804.0657, Lemma 2.2).
status: theorem (arXiv preprint)
falsifies: four general-position lines admitting two distinct clockwise squares with vertices one per line.
```
