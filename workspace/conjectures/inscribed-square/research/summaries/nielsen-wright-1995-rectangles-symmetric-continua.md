# Nielsen–Wright 1995 — Rectangles inscribed in symmetric continua

**Source:** Mark J. Nielsen, Stephen E. Wright, "Rectangles inscribed in symmetric continua," Geometriae Dedicata 56 (1995), 285–297. DOI: 10.1007/BF01263570. Full text at [[research/sources/nielsen-wright-1995-rectangles-symmetric-continua.full.md]].

## What it establishes

**Theorem.** Let Q be any rectangle and K ⊂ Rᵈ (d ≥ 2) a continuum which is either (a) symmetric across a hyperplane, or (b) symmetric through a point z ∉ K. Then K contains the vertices of a rectangle similar to Q which exhibits the same symmetry as K.

- This is the **symmetry result** the Matschke survey attributes to "Nielsen–Wright: curves symmetric across a line or about a point." It works for continua (compact connected sets), not just curves, and in all dimensions d ≥ 2.
- The inscribed rectangle shares the symmetry: in the line-symmetric case, the rectangle is itself symmetric across the same line (so its sides are parallel/perpendicular to it); in the point-symmetric case, the rectangle is centrally symmetric about the same point (so it is a parallelogram with that center — in fact a rectangle centered at z).
- **Square special case:** if Q is a square, this gives an inscribed square for symmetric curves/continua — the symmetry result GOAL.md names as a published extension.

## Why it matters here

- GOAL.md explicitly lists "curves with a line or point symmetry" as a published extension class. This is the primary source for it (via the survey's attribution).
- The continuum formulation (not requiring a curve, just a compact connected set) is broader than the Jordan-curve setting — a structural fact worth noting for the run's own extension attempts.
- The "same symmetry" conclusion is strong: it pins the rectangle's orientation, which can matter for the exact-arithmetic oracle (a symmetric polygon's inscribed square has a predictable position).

## Claims

```claim
id: nielsen-wright-1995-symmetric-rectangles
statement: If K ⊂ Rᵈ (d ≥ 2) is a continuum symmetric across a hyperplane or through a point z ∉ K, then K contains the vertices of a rectangle similar to any given rectangle Q, with the same symmetry as K. In particular, symmetric Jordan curves inscribe squares.
status: asserted-by-source
evidence: Nielsen–Wright, Geom. Dedicata 56 (1995), 285–297 (DOI 10.1007/BF01263570)
holds-here: yes — the symmetry extension class GOAL.md names; square case gives inscribed squares on line- or point-symmetric curves
falsifies: a symmetric continuum with no rectangle similar to some Q, exhibiting the symmetry
```
