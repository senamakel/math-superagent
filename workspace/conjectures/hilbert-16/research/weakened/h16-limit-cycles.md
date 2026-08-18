# Ladder of weakened targets — H16.2 (Hilbert's 16th, part II)

```ladder
goal: Hilbert's 16th problem part II: for every n >= 2 and every planar polynomial vector field X = (P,Q) with max(deg P, deg Q) <= n, the number of isolated periodic orbits (limit cycles) is bounded by a finite H(n) depending only on n and not on the coefficients; additionally, classify the possible mutual positions and nestings of the cycles.
difficulties: uniformity-over-family, degenerate-vertices, unbounded-n, full-displacement, infinity-and-global, nesting-classification
status: open
```

The named difficulties are specific obstructions: pointwise finiteness does not
supply coefficient-uniformity; nilpotent, semihyperbolic and other degenerate
vertices lack the elementary Dulac-transition expansion; the degree is
unbounded; Abelian/Melnikov theory controls only the linearised displacement;
compactification introduces limit-periodic sets at infinity and global
composition of transitions; and the configuration/classification half is a
separate, largely unresolved target.

```rung
id: R-linear-center-one-family
statement: For the named quadratic genus-one Hamiltonian center families (r11) and (r18), under sufficiently small quadratic perturbations within the stated family, the first-order displacement is an Abelian integral whose derivative forms a three-dimensional Chebyshev space on the period annulus, hence it has at most two isolated zeros counted with multiplicity; the bound two is attained in the cited cases.
off: uniformity-over-family, degenerate-vertices, unbounded-n, full-displacement, infinity-and-global, nesting-classification
claim: h16-ggi-quadratic-centers-genus-one-2009 — Gautier–Gavrilov–Iliev, DCDS 25 (2009) 511–535, Thms 3–4 (asserted-by-source, holds-here yes)
stance: settled
merge: Turn full-displacement back on first by proving that higher-order displacement terms preserve the certified zero count in this named perturbative family; the obstruction to expect is that first-order Melnikov control need not control the nonlinear return map.
```

```rung
id: R-local-focus-bautin
statement: For a quadratic planar vector field with a focus or center at a specified singular point, at most three small-amplitude limit cycles bifurcate from that point in the quadratic family, and three can occur: M(2) = 3.
off: degenerate-vertices, unbounded-n, infinity-and-global, nesting-classification
claim: h16-lower-bounds — Bautin 1952/1954, M(2) = 3 (asserted-by-source, holds-here yes)
stance: settled
merge: Turn global-scale back on while retaining n = 2 and local nondegeneracy: replace the local Bautin germ by a complete period-annulus or polycycle displacement function, where local focal quantities no longer bound all cycles.
```

```rung
id: R-tangential-abelian
statement: For deg H <= n+1 and deg omega <= n, the Abelian integral I(h) = integral over a nonsingular real oval of H=h of omega has a finite number of isolated zeros uniformly over the polynomial data, with the explicit doubly-exponential Binyamini–Novikov–Yakovenko bound (and the sharper Binyamini–Dor dependence on deg omega).
off: full-displacement, degenerate-vertices, infinity-and-global, nesting-classification
claim: h16-abelian-integral-bounds — Binyamini–Novikov–Yakovenko 2010; Binyamini–Dor 2012 (asserted-by-source, holds-here yes)
stance: settled
merge: Turn full-displacement back on: pass from the first-order Abelian integral to the complete return-map displacement for a non-Hamiltonian perturbation; analyticity and a uniform preparation theorem, not the Abelian zero count alone, are required.
```

```rung
id: R-elementary-polycycle
statement: For a fixed elementary polycycle whose vertices are hyperbolic saddles, cyclicity in a generic finite-parameter analytic family is finite and uniformly bounded over the parameter family; Kaloshin supplies an explicit bound of the form 2^(25 k^2) for k parameters.
off: degenerate-vertices, unbounded-n, nesting-classification
claim: h16-kaloshin-uniform-bound — Ilyashenko–Yakovenko finiteness; Kaloshin explicit bound 2^(25 k^2) (asserted-by-source, holds-here yes)
stance: settled
merge: Turn degenerate-vertices back on while keeping a fixed finite-degree family: resolve one nilpotent or semihyperbolic vertex by analytic normal form and blow-up, then prove that the composed full displacement has finitely many zeros. The smooth test must identify the analytic/quasianalytic step.
```

```rung
id: R-fake-saddle-transition
statement: For the generic fake-saddle normal-form unfolding with nonzero quadratic jet and d(mu) > 0, the Dulac transition has a parameter-uniform asymptotic expansion with a flat remainder, and in the cited reversible application the resulting return map has zero cyclicity at the specified center.
off: unbounded-n, infinity-and-global, nesting-classification
claim: fake-saddle-uniform-transition-map-marin2026 — Marín, EJQTDE 2026 no. 5 (asserted-by-source, holds-here yes)
stance: settled
merge: Turn the exceptional degenerate cases back on: handle d = 0, higher-jet and semihyperbolic cases, and compose several transitions into one complete graphic. The first missing ingredient is a division/zero theorem for the composite displacement, not another leading-term calculation.
```

```rung
id: R-one-degenerate-graphic
statement: For n = 2, one specifically named DRR graphic currently open as a full graphic — for example (I^1_6b), (H^3_13), or (DI_2b), whose boundary limit periodic sets alone are reported closed — has finite cyclicity under perturbation in the quadratic coefficient family: a fixed collar contains at most a finite coefficient-uniform number of bifurcating limit cycles.
off: unbounded-n, nesting-classification
stance: open
merge: After one graphic is settled, turn on the remaining quadratic catalogue: prove finite cyclicity for every still-open DRR graphic and make the compactification/parameter-uniform assembly explicit. The first move is to choose one graphic, state its complete return-map displacement and all vertex hypotheses in Lean, and attack the exceptional vertex rather than relying on the settled generic fake-saddle expansion.
```

```rung
id: R-h2-uniform
statement: H(2) is finite: there exists a finite coefficient-independent bound on the number of limit cycles of every planar quadratic vector field; the nesting-classification half remains excluded.
off: unbounded-n, nesting-classification
stance: open
merge: Turn unbounded-n back on. The quadratic proof cannot simply scale: it relies on the finite DRR catalogue of 121 graphics, while no corresponding finite catalogue is available for arbitrary degree. A new uniform family-level mechanism must replace that finite case list.
```

```rung
id: R-full
statement: For every n >= 2, H(n) is finite uniformly over all planar polynomial vector fields of degree at most n, and the possible mutual positions and nestings of their limit cycles are classified.
off: 
stance: open
merge: This is the full target. It is reached only after the quadratic and all-degree uniformity problems are solved, then the separate configuration-classification problem is also addressed; none of the weaker rungs implies it without those additional results.
```
