# Schwartz 2020 — A trichotomy for rectangles inscribed in Jordan loops

**Source:** Richard Evan Schwartz, "A trichotomy for rectangles inscribed in Jordan loops," Geometriae Dedicata (2020). DOI: 10.1007/s10711-020-00516-8. Full text on disk is the arXiv preprint arXiv:1804.00740 at [[research/sources/schwartz-2020-trichotomy-rectangles.full.md]].

## What it establishes

A structural theorem about the space I(γ) of rectangles inscribed in an arbitrary Jordan loop γ.

**Theorem 1.1 (Trichotomy).** For any Jordan loop γ, I(γ) contains a connected set S satisfying one of three alternatives (the "trichotomy" — the three cases organize how the inscribed rectangles sit in γ).

**Corollary 1.2.** All but at most 4 points of any Jordan loop are vertices of rectangles gracefully inscribed in γ.

**Corollary 1.3.** If γ has 3 points which are not vertices of gracefully inscribed rectangles, then γ has gracefully inscribed rectangles of every aspect ratio.

**Corollary 1.4.** For any non-atomic probability measure µ on γ, there is a gracefully inscribed rectangle R such that each pair of opposite sides of R cuts off total µ-measure 1/2.

**Theorems 1.5–1.7 (genericity).** There is an open dense set P of polygons for which I(γ) is a piecewise smooth 1-manifold, the aspect-ratio function ρ is locally injective at smooth points, and G(γ) contains a global component. For γ ∈ P, the number of squares is odd (Corollary 3.5) — the parity statement in this framework.

**Key lemmas (Section 3).** Each arc component of I(γ) has order 4 (Lemma 3.1); labeled hyperbolic components contain an odd number of inscribed squares, any other labeled arc component an even number (Lemma 3.2); elliptic components contain 4k squares (k odd); loop components 2k (k even) (Lemmas 3.3–3.4).

## Why it matters here

- The trichotomy is a *global structural statement about all Jordan loops* — the rectangle side of the problem is essentially completely understood (all but ≤ 4 points are rectangle vertices; the aspect-ratio map is almost surjective). This brackets the square problem: squares are the special case ρ = 1 of the rectangle picture, and the odd-parity structure (Lemma 3.2, Cor 3.5) is the same Mobius-band parity that powers the square proofs.
- The parity lemmas (hyperbolic components odd, others even) are the cleanest modern statement of the odd-count mechanism — a candidate for Lean formalization.
- The "all but at most 4 points" result is sharp: the non-circular ellipse is the example (only its 4 symmetric points... the 4 points where the rectangle family degenerates).

## Claims

```claim
id: schwartz2020-all-but-4-points
statement: All but at most 4 points of any Jordan loop are vertices of gracefully inscribed rectangles.
status: asserted-by-source
evidence: Schwartz, "A trichotomy for rectangles inscribed in Jordan loops," Geom. Dedicata 2020 (arXiv:1804.00740), Corollary 1.2
holds-here: yes — the strongest continuous-curve rectangle result; brackets the square problem
falsifies: a Jordan loop with 5 points that are not vertices of any gracefully inscribed rectangle
```

```claim
id: schwartz2020-three-points-all-aspect-ratios
statement: If a Jordan loop has 3 points that are not vertices of gracefully inscribed rectangles, then it has gracefully inscribed rectangles of every aspect ratio.
status: asserted-by-source
evidence: Schwartz, Geom. Dedicata 2020 (arXiv:1804.00740), Corollary 1.3
holds-here: yes — a sharp condition for full aspect-ratio coverage; relevant to the θ-rectangle family of Asano–Ike
falsifies: a Jordan loop with 3 non-vertex points and a missing aspect ratio
```

```claim
id: schwartz2020-odd-squares-generic
statement: For γ in an open dense set P of polygons, the space G(γ) of gracefully inscribed squares contains an odd number of squares.
status: asserted-by-source
evidence: Schwartz, Geom. Dedicata 2020 (arXiv:1804.00740), Corollary 3.5
holds-here: yes — the parity mechanism in its cleanest form; consistent with cdm2022-genericity-odd-squares
falsifies: a polygon in P with an even number of gracefully inscribed squares
```
