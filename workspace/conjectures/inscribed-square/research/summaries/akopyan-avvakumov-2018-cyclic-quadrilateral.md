# Any cyclic quadrilateral can be inscribed in any closed convex smooth curve (Akopyan–Avvakumov 2018)

**Source:** Arseniy Akopyan, Sergey Avvakumov, Forum of Mathematics, Sigma 6 (2018), e7. DOI: 10.1017/fms.2018.7. arXiv:1712.10205.

**Full text:** `research/sources/akopyan-avvakumov-2018-cyclic-quadrilateral.full.md`

## What it establishes

**Theorem 1:** Any cyclic quadrilateral can be inscribed in any closed convex C¹ curve. A cyclic quadrilateral is one whose vertices lie on a circle — equivalently, opposite angles sum to π.

**Theorem 2:** Any rectangle can be inscribed in any closed convex curve (no smoothness assumption needed).

**Sharpness:** The C¹-smoothness requirement is necessary in Theorem 1. The kite with angles π/2 and 2π/3 cannot be inscribed in the thin triangle with angles π/10, π/10, 4π/5. So for non-rectangle quadrilaterals, the C¹ hypothesis is essential.

## Why it matters here

- A square is a cyclic quadrilateral, so Theorem 1 covers squares in convex C¹ curves — but this is already covered by Emch (convex) and Stromquist (locally monotone). The new content is the *generality over all cyclic quadrilaterals*, not the square case.
- The sharpness example (kite vs thin triangle) is a concrete instance of the obstruction that smoothness hypotheses are needed for non-rectangle cyclic quadrilaterals: it shows a cyclic quadrilateral failing to inscribe in a non-smooth (cornered) convex curve. The same mechanism (thin triangles, corner degeneracies) is behind why the square problem resists approximation arguments — but for squares specifically, the kite example does not apply (a square is not a kite with those angles).

**Key connection:** This paper's Theorem 2 (rectangles in any convex curve) is the convex-case rectangle result. The sharpness construction shows a cyclic quadrilateral that inscribes in every smooth curve but not in every continuous curve — the same failure mode (shrinkout) as the square problem in the general case.

## Claims

```claim
id: akopyan-avvakumov-2018-cyclic-quadrilateral-theorem
statement: Any cyclic quadrilateral (vertices on a circle) can be inscribed in any closed convex C¹ curve. Any rectangle can be inscribed in any closed convex curve.
status: asserted-by-source
evidence: Akopyan–Avvakumov 2018, Forum Math. Sigma 6, e7; arXiv:1712.10205, Theorems 1 and 2
holds-here: yes — squares are cyclic quadrilaterals and rectangles, so convex curves inscribe squares (re-confirms Emch); the C¹ hypothesis is essential for non-rectangle cyclic quadrilaterals
falsifies: a cyclic quadrilateral failing to inscribe in a closed convex C¹ curve; a rectangle failing to inscribe in a closed convex curve
```

```claim
id: akopyan-avvakumov-2018-sharpness-kite
statement: The kite with angles π/2 and 2π/3 cannot be inscribed in the thin triangle with angles π/10, π/10, 4π/5; hence the C¹ hypothesis in the cyclic-quadrilateral theorem is necessary.
status: asserted-by-source
evidence: Akopyan–Avvakumov 2018, sharpness discussion (Figure 1)
holds-here: yes — a concrete example of a cyclic quadrilateral that inscribes in smooth curves but fails on a continuous (non-smooth) curve; the same shrinkout phenomenon as the square problem
falsifies: a published construction inscribing the π/2–2π/3 kite in the thin triangle
```
