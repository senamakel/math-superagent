# Wright 2026 — Inscribed rhombi having diagonals collinear with specified points

**Source:** Stephen E. Wright, "Inscribed rhombi having diagonals collinear with specified points," Aequationes Mathematicae, 2026-06-03, DOI 10.1007/s00010-026-01307-4. Full text: `research/sources/wright-2026-rhombi-diagonals-collinear.full.md`.

## What it establishes

A companion to the 2025 Monthly note (rhombi with two sides parallel to a given line): here the alignment constraint is on a **diagonal** instead of a side.

**Main existence result (Theorem 4.4 area).** A simple closed curve J contains the vertices of a rhombus having one diagonal collinear with a specified point z — the diagonal line passes through z.

**Theorem 5.1 / Section 5 (uncountably many).** A simple closed curve contains the vertices of **uncountably many rhombi** — a new proof of Fung's theorem with a diagonal-alignment refinement.

**Section 6 (regional collinearity).** Under natural geometric hypotheses (Proposition 6.1, Corollaries 6.2–6.3), **all points in some region** are collinear with diagonals of inscribed rhombi — the diagonal-collinearity locus is region-shaped, not point-shaped. The geometric assumptions are stated independent of the choice of z.

**Section 7.** Additional results on the structure of the diagonal-collinearity locus.

## Why it matters for this run

1. **The rhombus → square gap.** CONTEXT.md's standing note: "perpendicular diagonals are free, equal diagonals are the hard part." Wright's rhombi come with a **prescribed diagonal line** (through a specified point, or parallel to a specified line). A rhombus with a prescribed diagonal direction is one step closer to a square: if a rhombus's diagonals are perpendicular bisectors of each other (they always are), the square condition is exactly **equality of the two diagonals**. Wright's constructions give uncountably many rhombi with controlled diagonal directions — the freedom in the family is what a square-peg argument would need to collapse to the equality case. This is the same structure Matschke's special-trapezoid criterion exploits (a square is a rhombus that is also a special trapezoid).
2. **No regularity assumed.** Like Fung 2021, the theorem holds for arbitrary simple closed curves — the same generality as the conjecture itself, for rhombi rather than squares.
3. **The scale issue:** rhombi come in all sizes (uncountably many); the square-peg obstruction (shrinkout) is about whether the *square* family can be forced to have a definite scale. These results do not touch that, but they pin down the rhombus side of the gap.

## Claim blocks

```claim
id: wright2026-rhombus-diagonal-through-point
statement: Given a simple closed curve J and a point z in the plane, J contains the vertices of a rhombus one of whose diagonals is collinear with z (the diagonal line passes through z).
hypotheses: J a simple closed (Jordan) curve; z a point; no regularity on J.
holds-here: yes — an arbitrary-curve rhombus result with a diagonal-alignment constraint, complementing Fung 2021.
evidence: full text verified (Aequationes Math. 2026, Theorem 4.4 area); published journal article.
status: theorem (peer-reviewed, journal article)
falsifies: a Jordan curve and point z with no inscribed rhombus whose diagonal line passes through z.
```

```claim
id: wright2026-uncountably-many-rhombi-diagonal-refined
statement: A simple closed curve contains the vertices of uncountably many rhombi, and under geometric hypotheses (Prop 6.1) every point of a region is collinear with diagonals of such rhombi.
hypotheses: J a simple closed curve; the geometric hypotheses of Prop 6.1 for the regional statement.
holds-here: yes — re-establishes and refines the Fung uncountably-many-rhombi theorem; the regional collinearity statement is new.
evidence: full text verified (Aequationes Math. 2026, Section 5–6).
status: theorem (peer-reviewed, journal article)
falsifies: a Jordan curve whose inscribed-rhombus diagonal-collinearity locus is empty or contains no region under the stated hypotheses.
```

```claim
id: wright2026-rhombus-square-gap-diagonal
statement: Wright's rhombi come with prescribed diagonal lines; the square condition on such a rhombus is exactly equality of the two (perpendicular, mutually bisecting) diagonals — the same equality-of-diagonals gap that separates Fung's rhombi from squares.
hypotheses: none — a structural observation about the literature.
holds-here: yes — frames the rhombus side of the square-peg gap for this run's attack.
evidence: standard Euclidean fact (rhombus diagonals are perpendicular bisectors; square iff diagonals equal), applied to the Wright/Fung constructions.
status: derived observation (elementary geometry, not a new theorem)
falsifies: an inscribed rhombus family with prescribed diagonal directions that cannot be specialized to equal diagonals.
```
