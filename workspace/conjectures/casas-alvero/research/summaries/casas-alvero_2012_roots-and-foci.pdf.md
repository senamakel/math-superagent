# Casas-Alvero, *Roots of complex polynomials and foci of real algebraic curves* (L'Enseignement Math. 58 (2012) 223–248) — full text held

Source: https://ems.press/content/serial-article-files/44231 (DOI 10.4171/LEM/58-3-1), converted from PDF. Full text: `research/sources/casas-alvero_2012_roots-and-foci.pdf.full.md` (1232 lines, 53 KB).

## What it establishes

A rigorous, modernized proof of **Siebeck's theorem for polynomials of arbitrary degree**, following Linfield's approach, with the technical points Linfield left unaddressed (zero-dimensional components, uniqueness of the Siebeck curve).

- **Theorem 5.1 (Linfield)**: if an augmented curve D has focal group the roots of f (deg d > 1), then the polar relative to the improper line of the envelope of D envelops a non-parabolic augmented curve C of class d−1 whose focal group is the roots of df/dz. **Corollary 5.2** specializes to G = the root group of f. **Remark 5.3**: iterating, the r-th polar has focal group the roots of d^r f/dz^r (1 ≤ r ≤ d−1).
- **Theorem 6.1** (the direct generalization of Siebeck, non-aligned roots): let f have distinct roots z_1,…,z_m, multiplicities µ_1,…,µ_m, no three aligned. For each pair j,s let p_{j,s} divide the segment z_j z_s in ratio µ_s/µ_j. Then: (1) there is a unique augmented curve S of class m−1 tangent to each line z_j z_s at p_{j,s}; (2) S is non-parabolic and its foci, with multiplicities, are the roots of df/dz other than the z_j, i.e. **Z(df/dz) = Φ(S) + Σ_j (µ_j − 1) z_j**.
- Supporting theory developed from scratch: Plücker's focal-group definition for real algebraic curves (foci = intersections of conjugate tangents from the cyclic points I, J), **Prop 3.1** (envelope equation F = λH + (u²+v²)P characterizes the focal group — the key algebraic lemma, proved via Bézout), **Laguerre's theorem** on angles between tangent lines and focal lines, and the polar-curve calculus (Lemmas 4.1–4.6, including the polar of a group of points with weights).

## Why it matters for this run

This is the originator's own modern treatment of the geometry that refines Gauss–Lucas: derivative roots of f are the foci of a specific curve built from f's roots. The run's adopted `root-difference-coloring` approach and the Polstra/Laterveer–Ounaïes convex-hull arguments rest on the same Gauss–Lucas geometry; this source gives the sharpest available statement (roots of df/dz lie on/inside the Siebeck curve, a proper subset of the convex hull in the non-aligned case). It is a **primary source by the conjecture's author**, complementing the 2001 origin paper (still unobtainable) and the 2012 Siebeck-curves paper (abstract-level record only; full text fetch failed).

## Status

- **Verified by reading the held full text**: Theorem 5.1, Corollary 5.2, Remark 5.3, Prop 3.1, Theorem 3.2 (Laguerre), Theorem 6.1 with its proof sketch.
- Evidence class: primary published source (Enseign. Math., refereed journal), statement-level verified by direct reading.
- Not a CA result by itself: it concerns roots of derivatives, not shared roots with all derivatives simultaneously. Its role is geometric context for counterexample-constraint arguments.

## Cross-links

- Same author's `research/sources/casas-alvero_2012_siebeck-curves.full.md` (2012, Math. Scand. 111, 12–41) — abstract/landing page held; the two refinements of Gauss–Lucas proved there are the announced sequel to this paper ("will appear in [2]").
- Related held geometry sources: `polstra2012_convex-hulls-casas-alvero.full.md`, `laterveer_ounaies_constraints_2012.full.md`, `grafvonbothmer2007_infinitely_many.full.md`.
