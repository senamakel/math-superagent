# Newton-polyhedral displacement

```approach
slug: newton-polyhedral-displacement
status: refuted
idea: Newton-polyhedral / toric desingularisation of the displacement germ
mechanism: Toric blow-up separates competing scales sector-by-sector into finitely many monomial charts, reads dominant behaviour off the Newton polygon's compact faces, then applies Weierstrass preparation per chart — uniformity from finitely many combinatorial Newton types in fixed-degree polynomials.
killed-by: The literature supports finite blow-up/desingularisation for analytic families, but does not establish the proposed finite-Newton-type uniform displacement theorem; Newton diagrams classify selected singularities and compute local return terms, not a general finite Weierstrass/zero-counting reduction for the open non-hyperbolic DRR graphics.
precedent: https://link.springer.com/article/10.1007/BF01244900 ; https://doi.org/10.1090/bull/2002-39-03 ; https://doi.org/10.48550/arxiv.2602.20864 ; claims: drr-saddle-node-normalforms-dir2002, g-resolve-resolution-exists
```

## Literature assessment

The established name for the general operation is **desingularisation (resolution) of analytic vector-field families by blow-up**, not a theorem called Newton-polyhedral displacement. Denkowska–Roussarie (1991) state that finite blow-ups desingularise isolated planar analytic singularities and introduce a family version for periodic limit sets, but explicitly present general applicability as a conjectural direction. Ilyashenko's Desingularization Theorem gives the analytic blow-up framework used in finiteness arguments, with hypotheses involving analytic fields and the relevant elementary/polycycle setting; it does not imply that every return germ becomes a finite collection of monomial charts with a uniform finite list of Newton types.

Newton-diagram/toric terminology does occur in recent work on special monodromic singularities (García–Giné–Mañosa, arXiv:2602.20864), where the Newton diagram has restricted form (two edges) and the authors compute linear return-map data after explicit desingularisation. That is a special classification result, not the proposed theorem for the compactified quadratic parameter family.

**Hypotheses here:** polynomiality gives analyticity, and fixed degree gives a bounded monomial support before compactification. However, the missing hypothesis is precisely a proved uniform finite stratification controlling all transition germs and their zero counts after blow-up. The open DRR graphics contain non-hyperbolic/degenerate vertices; the library's DRR results show that their finite cyclicity is still unresolved. Therefore the proposed inference is unsupported.

**Application to this problem:** no source found applying a Newton-polyhedral finite-type theorem to I₆b¹, H₁₃³, DI₂b, or H₁₄³. The established application is narrower: family blow-up is an ingredient in DRR closures such as DF₂a, not a general Newton-polyhedral solution.

**What it would buy if proved:** a finite sectorial normal-form atlas plus uniform Weierstrass preparation would reduce cyclicity to finitely many certified analytic zero counts and could potentially replace graphic-by-graphic transition analysis. That is a substantial conditional payoff, but the central finite-type and uniformity assertion is exactly the unproved step; status is therefore refuted as a proposed ready route, not a claim that toric methods are mathematically impossible.

## Three tests

1. Smooth test: blow-up alone is available for analytic and smooth settings, so it does not yet supply the required analytic/quasianalytic zero-control step.
2. Uniformity: not supplied; bounded degree does not by itself prove a uniform bound on the number of zeros of all resulting germs.
3. Counterexample boundary: the smallest relevant stress cases are the non-hyperbolic DRR graphics left open by RR 2015. No theorem located covers them.
```