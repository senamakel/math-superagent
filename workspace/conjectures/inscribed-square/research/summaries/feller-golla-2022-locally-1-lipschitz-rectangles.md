# Non-orientable slice surfaces and inscribed rectangles (Feller–Golla 2022)

**Source:** Peter Feller, Marco Golla, Annali della Scuola Normale Superiore di Pisa, Classe di Scienze (2022), pp. 1463–1485. DOI: 10.2422/2036-2145.202105_099. arXiv:2003.01590.

**Full text:** `research/sources/feller-golla-2022-locally-1-lipschitz-rectangles.full.md`

## What it establishes

**Theorem 1.1:** Let Γ be a **locally 1-Lipschitz Jordan curve** (each point p ∈ Γ has a neighborhood U such that Γ ∩ U is the graph of a 1-Lipschitz function). Then for all integers n ≥ 2, there exists an integer 1 ≤ k ≤ n−1 such that Γ has an inscribed rectangle with aspect ratio tan(kπ/2n).

**Consequences for the square peg problem:** Aspect ratio 1 (a square) is tan(π/4) = tan(kπ/2n) when k = n/2 for even n, so the theorem gives **inscribed squares** for all locally 1-Lipschitz Jordan curves. Also gives rectangles with aspect ratio √3 (n = 3, k = 1: tan(π/6) = 1/√3, reciprocal-invariant).

**Method:** The proof connects the inscribed-rectangle problem to non-orientable surface theory in 4-manifolds. A rectangle inscribed in Γ corresponds to a Möbius band bounded by a torus knot in a branched double cover. Main 4-dimensional theorem: certain families of torus knots are not the boundary of an embedded Möbius band in the 4-ball (locally-flat category), showing the smooth/locally-flat non-orientable 4-genus can differ.

## Relation to other classes

- **Locally 1-Lipschitz ⊂ locally monotone:** 1-Lipschitz means slope bounded by 1 (quantitative); local monotonicity is qualitative (some linear functional makes the curve strictly monotone, no slope bound).
- **Nesting with rectifiable is UNPROVEN (do not assert):** the earlier digest claimed "locally monotone curves have finite length... locally monotone ⊂ rectifiable." That claim is not established by any source in the library, and is likely FALSE: local monotonicity is in a *point-dependent* linear functional, so the curve can wind in different directions in different neighborhoods, accumulating unbounded total length while each piece is monotone in its own functional. Asano–Ike (Corollary 5.12) prove locally monotone curves satisfy the Legendrian-lift condition directly (Proposition 5.11) — they do not route through rectifiability. So locally monotone and rectifiable are two *separate* classes, both contained in the Legendrian-lift class; neither nesting is established.
- The Feller–Golla result is a special case of Stromquist's locally monotone theorem for squares, but the proof method (4-manifold topology) is different and gives a quantitative aspect-ratio family.

## Why it matters here

The Feller–Golla method is a **4-dimensional attack surface**: inscribed rectangles correspond to Möbius bands bounded by torus knots in branched double covers. This is a route distinct from the Mobius-band parity argument, Tao's integrals, Matschke's special-trapezoid criterion, and Asano–Ike's sheaf quantization. The class it covers (locally 1-Lipschitz) is narrower than Stromquist's, so it does not extend the positive classes, but its method is a genuinely different way to count inscribed squares.

## Claims

```claim
id: feller-golla-2022-locally-1-lipschitz-squares
statement: Every locally 1-Lipschitz Jordan curve (each point has a neighborhood on which the curve is the graph of a 1-Lipschitz function) inscribes a square, and in fact inscribes rectangles of aspect ratios tan(kπ/2n) for all n ≥ 2 and some 1 ≤ k ≤ n−1.
status: asserted-by-source
evidence: Feller–Golla 2022, Annali SNS Pisa, DOI 10.2422/2036-2145.202105_099, arXiv:2003.01590, Theorem 1.1
holds-here: yes — a restricted class (subset of locally monotone) solved by a different (4-manifold) method; the method is the new value, not the class
falsifies: a locally 1-Lipschitz Jordan curve with no inscribed square; or a correction/retraction
```

```claim
id: feller-golla-2022-4d-mobius-band-route
statement: The inscribed-rectangle problem for a Jordan curve Γ is connected to whether certain torus knots bound Möbius bands in branched double covers of the 4-ball; Batson's smooth non-orientable 4-genus bound does not hold in the locally-flat category.
status: asserted-by-source
evidence: Feller–Golla 2022, main theorems (4-dimensional part)
holds-here: yes — an independent route to counting inscribed quadrilaterals; the smooth/locally-flat distinction is the technical obstruction
falsifies: a published proof that the smooth and locally-flat non-orientable 4-genera coincide for all torus knots
```
