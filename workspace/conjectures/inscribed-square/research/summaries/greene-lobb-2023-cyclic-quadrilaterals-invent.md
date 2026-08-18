# Greene–Lobb 2023 — Cyclic quadrilaterals and smooth Jordan curves

**Source:** Joshua Evan Greene, Andrew Lobb, "Cyclic quadrilaterals and smooth Jordan curves," Inventiones mathematicae 234 (2023). DOI: 10.1007/s00222-023-01212-6. Full text on disk is the arXiv preprint arXiv:2011.05216 at [[research/sources/greene-lobb-2023-cyclic-quadrilaterals-invent.full.md]].

## What it establishes

**Theorem.** Every cyclic quadrilateral inscribes in every smooth Jordan curve in the Euclidean plane — for every smooth Jordan curve γ and cyclic quadrilateral Q, there is an orientation-preserving similarity taking the vertices of Q to γ.

- **Best possible:** the smoothness hypothesis is necessary — the only cyclic quadrilaterals that inscribe in all triangles are the isosceles trapezoids (a sharp shrinkout obstruction, consistent with gl2024-cyclic-quadrilateral-sharpness). And no quadrilateral beyond cyclic ones can inscribe in every smooth curve (the circle is a smooth curve).
- **Method:** symplectic. A cyclic quadrilateral with parameters (s,t,φ) corresponds to Lagrangian tori T₁, T₂ ⊂ C² intersecting cleanly along γ×{0}; a smoothing (Lemma 2) gives a Lagrangian torus T. The proof relies on **Polterovich–Viterbo's theorem**: an embedded Lagrangian torus in C² has minimum Maslov number 2. The proposition: the minimum Maslov number of T is 4 — a contradiction — which forces the inscribed quadrilateral.
- **Context:** this solves the Circular Quad Peg Problem (Matschke survey Conjecture 9) for smooth curves, generalizing the Greene–Lobb rectangle result (a rectangle is a cyclic quadrilateral).

## Why it matters here

- This is the third published symplectic result from the Greene–Lobb school (rectangles 2021, cyclic quadrilaterals 2023, Floer homology 2024). The Maslov-number-4 proposition is the exact mechanism that replaces the Mobius-band boundary winding number in the symplectic setting.
- The triangle sharpness (only isosceles trapezoids inscribe in all triangles) is the concrete published obstruction to smooth→continuous extension — the run's own extension must produce something strictly stronger, or a formalization of this.

## Claims

```claim
id: gl2023-cyclic-quadrilateral-theorem
statement: Every cyclic quadrilateral inscribes in every smooth Jordan curve (orientation-preserving similarity taking its vertices to the curve).
status: asserted-by-source
evidence: Greene–Lobb, Invent. Math. 234 (2023) (arXiv:2011.05216), main theorem
holds-here: yes — solves the Circular Quad Peg Problem for smooth curves; strictly generalizes greene-lobb-2021-rectangular-peg
falsifies: a smooth Jordan curve and a cyclic quadrilateral with no similar inscribed copy
```

```claim
id: gl2023-triangle-sharpness
statement: The only cyclic quadrilaterals that inscribe in all triangles are the isosceles trapezoids; hence some regularity hypothesis on the curve is necessary for the cyclic-quadrilateral theorem.
status: asserted-by-source
evidence: Greene–Lobb, Invent. Math. 234 (2023), theorem discussion (citing [6, §3.6])
holds-here: yes — a published, exact obstruction showing shrinkout prevents smooth→continuous extension
falsifies: a cyclic non-isosceles-trapezoid quadrilateral inscribing in every triangle
```
