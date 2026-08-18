# Aslam–Chen–Frick–Saloff-Coste–Setiabrata–Thomas 2020 — Splitting loops and necklaces: variants of the square peg problem

**Source:** Jai Aslam, Shu-Jian Chen, Florian Frick, Sam Saloff-Coste, Linus Setiabrata, Hugh Thomas, "Splitting loops and necklaces: variants of the square peg problem," Forum of Mathematics, Sigma 8 (2020), e5. DOI: 10.1017/fms.2019.51. arXiv:1806.02484. Full text: `research/sources/aslam-2020-splitting-loops-necklaces.full.md`.

**Status: verified against full text on disk (published, Forum Math. Sigma).**

## What it establishes

A common framework (fair division / necklace splitting / colored Tverberg) for variants of the square peg problem, proved for **all continuous curves**:

1. **Hadwiger's conjecture (1971) holds:** any simple loop in R³ inscribes a parallelogram; moreover the set of parallelogram vertex positions is **dense** in the loop. (Parallelograms may be degenerate: four pairwise-distinct collinear points that are limits of parallelograms, as Hadwiger allowed.)
2. **Dense rectangles in planar loops:** any simple planar loop inscribes sufficiently many rectangles that the vertex set is **dense** in the loop. (Independently due to Schwartz.)
3. **Rectifiable loop balancing:** a rectifiable simple planar loop inscribes a rectangle cutting the loop into four arcs γ¹,γ²,γ³,γ⁴ in cyclic order with total length of γ¹∪γ³ equal to total length of γ²∪γ⁴. (Also independently Schwartz, who calls it "tantalizingly close to the square peg problem".)
4. **Higher-dimensional fair division:** a rectifiable loop in R^d can be cut into (r−1)(d+1)+1 pieces that can be rearranged by translations to form r loops of equal length.

**Method:** topological Tverberg-type theorems, Hobby–Rice theorem in L¹ approximation, fair division of necklaces (Alon). This is a **common framework** for all-continuous-curve inscribed-polygon results — a genuinely different attack surface from the Möbius-band parity argument.

## Relation to the square peg problem

The dense-rectangle result (2) is the sharpest all-continuous-curves rectangle statement before Greene–Lobb 2026 (positive-measure angle set, θ-rectangles). It does **not** give squares: the rectangle's aspect ratio is uncontrolled (like Vaughan's original rectangle theorem). The balancing result (3) is described by Schwartz as "tantalizingly close" to the square peg problem — it pins an inscribed rectangle whose *length partition* is balanced, not one whose diagonals are equal.

## Claim blocks

```claim
id: aslam2020-hadwiger-parallelogram-dense
statement: Any simple loop in R³ inscribes a parallelogram; in fact the set of parallelogram vertex positions is dense in the loop (Hadwiger's 1971 conjecture).
hypotheses: simple closed curve (loop) in R³; degeneracies allowed as limits.
holds-here: R³ parallelogram result — adjacent to the planar square problem; demonstrates the all-continuous-curves methods extend to R³.
evidence: full text verified (arXiv:1806.02484; Forum Math. Sigma 8, e5, 2020).
status: theorem (published)
falsifies: a simple loop in R³ with no inscribed parallelogram, or a non-dense vertex set.
```

```claim
id: aslam2020-dense-rectangles-planar
statement: Any simple planar loop inscribes sufficiently many rectangles that the set of their vertices is dense in the loop.
hypotheses: simple closed curve in the plane (continuous; no regularity).
holds-here: all-continuous-curves rectangle density — stronger than Vaughan's single-rectangle theorem; does NOT give the square.
evidence: full text verified; independently due to Schwartz.
status: theorem (published)
falsifies: a planar Jordan curve whose inscribed-rectangle vertices are not dense.
```

```claim
id: aslam2020-rectifiable-balancing-rectangle
statement: A rectifiable simple planar loop inscribes a rectangle cutting the loop into four arcs γ¹,γ²,γ³,γ⁴ (cyclic order) with total length of γ¹∪γ³ equal to total length of γ²∪γ⁴.
hypotheses: rectifiable (finite-length) simple planar loop.
holds-here: rectifiable curves — a balancing-rectangle result "tantalizingly close" (Schwartz) to the square peg problem, but not a square.
evidence: full text verified; independently Schwartz.
status: theorem (published)
falsifies: a rectifiable planar loop with no such balanced inscribed rectangle.
```

## Why this source entered the library

The fair-division/necklace-splitting framework is the one **all-continuous-curves** attack surface the library lacked a primary for. It supplies the dense-rectangle and R³-parallelogram results with a common method, and its balancing result is the closest published rectangle statement to the square peg problem's needed scale control. Cited 4× in the library's own sources.
