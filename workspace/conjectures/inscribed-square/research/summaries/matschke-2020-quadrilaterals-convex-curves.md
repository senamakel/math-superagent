# Quadrilaterals inscribed in convex curves (Matschke 2020)

**Source:** Benjamin Matschke, "Quadrilaterals inscribed in convex curves," arXiv:1801.01945 (2018), published Trans. Amer. Math. Soc. 373 (2020), DOI 10.1090/tran/8359.

**Full text:** `research/sources/matschke-2020-quadrilaterals-convex-curves.full.md`

## What it establishes

Classifies the quadrilaterals inscribable in convex Jordan curves, in the continuous and smooth cases. Answers a question of Makeev for convex curves.

**Theorem 1.4 (Continuous case):** The class of (continuous) convex Jordan curves inscribes exactly the set Q of **isosceles trapezoids**. Q is the largest possible such set of quadrilaterals.

**Theorem 1.5 (Smooth case):** The class of differentiable convex Jordan curves inscribes exactly the set Q⃝ of **circular quadrilaterals**. Q⃝ is the largest possible such set.

**Theorem 1.6 (Common generalization):** Let Q be a circular quadrilateral with signed angles λ, μ. Suppose γ is a (continuous) convex Jordan curve all whose inner angles have size larger than min(|λ|, |μ|). Then γ inscribes Q.

**Theorem 5.1 (Quantitative):** In the setting of Theorem 1.6, if n is the number of crucial singular points (inner angle ≤ max(|λ|,|μ|)), then γ inscribes at least max(n,1) copies of Q.

**Method:** Standard topological arguments fail here (insufficient symmetry). Instead the proof uses an area argument of **Karasev and Tao**, simplified and elaborated. The continuous case requires analysis of the singular points.

## Why it matters here

- **A square is a circular quadrilateral and an isosceles trapezoid.** For squares, Theorem 1.5 covers smooth convex curves (Emch's case) and Theorem 1.4 covers continuous convex curves — both already known, but this paper proves them in a unified framework and shows they are the *largest possible* classes of quadrilaterals for convex curves.
- **Sharpness:** the classification is exact — the largest possible sets of quadrilaterals for convex curves are exactly the isosceles trapezoids (continuous) and circular quadrilaterals (smooth). This is the convex-case analogue of the "only isosceles trapezoids inscribe in all triangles" sharpness result.
- **The area argument is a distinct technique** (Karasev/Tao) that bypasses the symmetry deficit — one of the few methods not relying on the Mobius-band parity, worth recording as a known alternative route.
- Theorem 1.6 + 5.1 give **quantitative counts** (≥ max(n,1) copies) — useful as exact-arithmetic oracle targets for convex curves with corner points.

## Claims

```claim
id: matschke2020-convex-isosceles-trapezoids
statement: The class of continuous convex Jordan curves inscribes exactly the isosceles trapezoids, and this is the largest possible set of quadrilaterals for that class. Differentiable convex curves inscribe exactly the circular quadrilaterals.
status: asserted-by-source
evidence: Matschke 2020, Trans. AMS 373, arXiv:1801.01945, Theorems 1.4 and 1.5
holds-here: yes — squares are isosceles trapezoids and circular quadrilaterals, so convex curves inscribe squares (Emch case) in the largest-possible-quadrilateral framework
falsifies: a convex Jordan curve failing to inscribe some isosceles trapezoid; a non-isosceles-trapezoid quadrilateral inscribing in all convex curves
```

```claim
id: matschke2020-quantitative-convex-count
statement: A continuous convex Jordan curve all of whose inner angles exceed min(|λ|,|μ|) inscribes a circular quadrilateral Q with signed angles λ, μ; if n crucial singular points have inner angle ≤ max(|λ|,|μ|), it inscribes at least max(n,1) copies.
status: asserted-by-source
evidence: Matschke 2020, Theorems 1.6 and 5.1
holds-here: yes — quantitative oracle target for convex curves with corners; the count depends only on the singular-point set
falsifies: a convex curve meeting the angle hypotheses with fewer than max(n,1) inscribed copies of Q
```
