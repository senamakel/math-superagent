# Ladder of weakened targets — H16.2 (Hilbert's 16th, part II)

Revised 2026-08-22: added rung `R-single-second-type-leading-term` below `R-center-ideal-zero-division` to give the open part of the ladder a bottom — a single-passage leading-term computation an attempt can settle today, which produces the monomials the zero-division rung assumes. Recorded on `R-center-ideal-zero-division` that its algebraic shell is kernel-checked (claim r-center-ideal-zero-division-conditional) but the analytic zero-division theorem remains an open binder hypothesis, so the rung stays open.
Revised 2026-08-21: added failed rung `R-four-passage-ect-shortcut` (the run's
refuted composition-closure shortcut, now recorded so it is not proposed again)
and rung `R-one-degenerate-noncenter` (one of the 11 open degenerate non-center
graphics, filling the gap between the second-type center graphics and full H(2)).
All settled rungs now cite the claim ids that established them.

```ladder
goal: For every n >= 2 and every planar polynomial vector field X = (P,Q) with max(deg P, deg Q) <= n, the number of isolated periodic orbits (limit cycles) is bounded by a finite H(n) depending only on n; additionally, classify the possible mutual positions and nestings.
difficulties: unbounded-n, nesting-classification, full-nonlinear-displacement, global-uniform, infinity-boundary, degenerate-vertices, second-type-dulac, non-generic-degenerate, line-of-singular-points
status: open
```

## Named difficulties

Every entry names a *specific obstruction*, not a topic. A rung switching off
something not named here means the ladder and rung disagree about what makes
the problem hard.

1. **unbounded-n** — The degree `n` is not fixed to 2. The DRR reduction
   (finite catalogue of 121 graphics) is specific to `n = 2`; a structural
   mechanism, not a case list, must replace it for arbitrary degree.

2. **nesting-classification** — The second half of Hilbert's problem:
   classifying possible mutual positions and nestings of limit cycles, almost
   untouched for `n >= 3`.

3. **full-nonlinear-displacement** — The complete nonlinear return map, not
   merely the first-order Abelian/Melnikov linearisation. The step from
   linearised to nonlinear is where the Bautin ideal and division-in-the-
   center-ideal enter.

4. **global-uniform** — Compactification of parameter and phase space, plus
   the upgrade from pointwise finiteness (Écalle–Ilyashenko: each fixed field
   has finitely many cycles) to a uniform bound over the coefficient family.
   Compactness of the parameter space plus the DRR/Roussarie reduction is the
   standard frame; the step itself is not automatic from pointwise finiteness.

5. **infinity-boundary** — Limit periodic sets passing through infinity, and
   boundary strata of the blown-up compactified family. Center-type graphics
   through the triple nilpotent point at infinity are the locus where this
   bites.

6. **degenerate-vertices** — Nilpotent, degenerate, and semi-hyperbolic
   vertices, beyond elementary/hyperbolic saddles. An elementary saddle has a
   classical power-times-log Dulac transition; a semi-hyperbolic or nilpotent
   vertex has a transition in a strictly larger transseries class.

7. **second-type-dulac** — At semi-hyperbolic endpoints of center-type
   quadratic graphics, the Dulac transition maps are of *second type* (one
   chart → blow-up divisor → another chart, RR 2015 §2.6): their asymptotic
   expansions are transseries with iterated logarithms/exponentials and
   parameter-dependent exponents, not short power-times-log sums. The
   passage-wise ECT shortcut is refuted (toy Wronskian W3=0, captured).

8. **non-generic-degenerate** — Exceptional subcases beyond generic
   unfoldings: `d = 0` in the fake-saddle parameter, higher jets vanishing,
   non-generic unfoldings of nilpotent points.

9. **line-of-singular-points** — The 13 DRR degenerate graphics have a line
   (or circle) of singular points with a unique contact point. Desingularizing
   the family at the contact point requires a weighted blow-up whose monomial
   content depends on the chosen normal form, and no analytic 5-parameter
   normal form desingularizes all degenerate graphics uniformly (DR 2009 CPAA
   8:1133–1157). The slow-divergence integral is the leading term of the
   derivative of the displacement; when it vanishes identically at center
   conditions, the existing theoretical results need extension. DH5 needs a
   7-parameter normal form and is the hardest.

## Rungs — weakest first

```rung
id: R-linear-center-one-family
statement: For the named quadratic genus-one Hamiltonian center families (r11) and (r18), under sufficiently small quadratic perturbations, the first-order displacement is an Abelian integral whose derivative forms a three-dimensional Chebyshev space on the period annulus, hence it has at most two isolated zeros counted with multiplicity; the bound two is attained. Established by claim h16-sharp-abelian-named-family-G-sharpness (formalised, unchecked) with the ECT criterion of h16-ftv2013-chebyshev-abelian-ca (proved) and the model h16-sharp-abelian-named-family-G-model.
off: unbounded-n, nesting-classification, full-nonlinear-displacement, global-uniform, infinity-boundary, degenerate-vertices, second-type-dulac, non-generic-degenerate, line-of-singular-points
stance: settled
merge: Turn full-nonlinear-displacement back on by proving that higher-order displacement terms preserve the certified zero count in this specific Hamiltonian perturbative family. First-order Melnikov control does not bound the nonlinear return map; the merge needs a Bautin-ideal argument or a specific nonlinear Dulac function for this family.
```

```rung
id: R-local-focus-bautin
statement: For a quadratic planar vector field with a focus or center at a specified singular point, at most three small-amplitude limit cycles bifurcate from that point in the quadratic family, and three can occur: M(2) = 3. The Bautin ideal I = ⟨L₁, L₂, …⟩ has three independent generators (L₄, L₆, L₈) and the local nonlinear displacement division-in-I gives the bound. Established by claim h16-lower-bounds (Bautin 1952/1954) and h16-bamon-romanovskii-quadratic-pointwise (formalised).
off: degenerate-vertices, unbounded-n, infinity-boundary, nesting-classification, second-type-dulac, non-generic-degenerate, line-of-singular-points
stance: settled
merge: Turn global scale back on while retaining n = 2: replace the local Bautin germ by a complete period-annulus or polycycle displacement, where local focal quantities no longer bound all cycles. The first move is to state the displacement function for one specific non-local limit periodic set.
```

```rung
id: R-tangential-abelian
statement: For deg H <= n+1 and deg omega <= n, the Abelian integral I(h) = integral over a nonsingular real oval of H=h of omega has a finite number of isolated zeros uniformly over the polynomial data, with the explicit doubly-exponential Binyamini–Novikov–Yakovenko bound. The tangential (infinitesimal) H16 is settled for all n. Established by claims h16-bny-abelian-bound and h16-bd-abelian-linear-in-m (Binyamini–Novikov–Yakovenko 2010; Binyamini–Dor 2012); for n=2 the unified treatment is clt-2024-book-weak-h16-n2-chapter (catalogued).
off: full-nonlinear-displacement, degenerate-vertices, infinity-boundary, second-type-dulac, non-generic-degenerate, line-of-singular-points, nesting-classification
stance: settled
merge: Turn full-nonlinear-displacement back on: pass from the first-order Abelian integral to the complete return-map displacement for a non-Hamiltonian perturbation. For n=2 this is the CLT 2024 weak-H16 chapter (asserted, catalogued); for general n the BNY bound applies only to the linearised problem.
```

```rung
id: R-elementary-polycycle
statement: For a fixed elementary polycycle whose vertices are hyperbolic saddles, cyclicity in a generic finite-parameter analytic family is finite and uniformly bounded. Ilyashenko–Yakovenko proved finiteness; Kaloshin supplied an explicit bound ~2^{25 k²} for k parameters. Established by the Hilbert–Arnold theorem (Ilyashenko–Yakovenko; Kaloshin), the analytic scaffolding in iy-lectures-analytic-de-held-draft, and the elementary-graphics work drr-demr-1996-elementary-graphics-abstract.
off: degenerate-vertices, second-type-dulac, non-generic-degenerate, line-of-singular-points, nesting-classification
stance: settled
merge: Turn degenerate-vertices back on: resolve one semi-hyperbolic or nilpotent vertex by analytic normal form and blow-up, then prove the composed full displacement has finitely many zeros. The smooth test: a purely C^∞ argument re-proves Dulac's 1923 error. The analytic/quasianalytic step must be named explicitly.
```

```rung
id: R-generic-fake-saddle
statement: For the generic fake-saddle normal-form unfolding with nonzero quadratic jet and d(μ) > 0, the Dulac transition has a parameter-uniform asymptotic expansion with a flat remainder; the cited reversible application has zero cyclicity at center. This covers the generic degenerate-vertex case. Established by claim fake-saddle-uniform-transition-map-marin2026 (conditional, kernel-checked wrapper on the Marín 2026 axiom); the lower-bound context is drrt-2015-fake-saddle-cyclicity-lower-bound, which also notes (drrt-2015-fake-saddle-no-drr-contribution) that fake saddles contribute no DRR row.
off: second-type-dulac, non-generic-degenerate, unbounded-n, line-of-singular-points, nesting-classification
stance: settled
merge: Turn non-generic-degenerate back on: handle d = 0, higher-jet vanishing, and non-generic unfoldings at degenerate vertices. The first missing ingredient is a normal-form classification of the exceptional strata, not another leading-term computation.
```

```rung
id: R-boundary-graphic-second-type
statement: For the three center-type quadratic graphics I^1_6b, H^3_13, and DI_2b, the **boundary** limit periodic sets (where one or more transition maps degenerate to the boundary stratum) have finite cyclicity under perturbation in the quadratic family. RR 2015 Theorems 1.1 and 3.3. The full graphics with their interior second-type Dulac compositions remain open. Established by claim drr-rr-boundary-only-for-3-graphics (asserted); the boundary-vs-full distinction is i6b-four-second-type-full-graphic-not-covered.
off: non-generic-degenerate, unbounded-n, line-of-singular-points, nesting-classification
stance: settled
merge: Turn the interior limit periodic sets back on: the full graphics involve four second-type Dulac maps that RR 2015 §2.6 explicitly says cannot be reduced to one equation. The merge step is deriving the coupled two-equation displacement for the interior strata and proving a zero-count theorem for it.
```

```rung
id: R-four-passage-ect-shortcut
statement: REFUTED, KEPT AS A WARNING. The proposed shortcut read: assume each of the four interior Dulac passage contributions at the second-type vertices of a center-type quadratic graphic (I^1_6b, H^3_13, DI_2b) is individually representable in an ECT family, then conclude the sum is ECT and finite cyclicity follows. Why it failed: refuted by exact symbolic counterexample, not defeated by difficulty — ECT is not closed under addition or parameter specialization. Over Q[x], the pairs (1,x) and (−1,−x) each have Wronskian 1 yet their sum is zero, and the family (a, ax) loses rank at a=0 (code/refute/i6b_ect_obstruction_exact.py, capture code/out/i6b_ect_obstruction_exact.captured.txt, exact arithmetic, no floats). A second toy with four iterated-log passages gives W3 = 0 identically at the boundary specialization L=0 (code/out/i6b_second_type_toy.captured.txt). The board recorded this dead-end three times on 2026-08-18. Scope: the refutation kills the shortcut inference, not the actual I^1_6b dynamics — finiteness of those graphics remains open.
off: non-generic-degenerate, unbounded-n, line-of-singular-points, nesting-classification
stance: failed
merge: What went wrong: refuted by exact symbolic counterexample, not defeated by difficulty — ECT is not closed under addition or parameter specialization. Over Q[x], the pairs (1,x) and (−1,−x) each have Wronskian 1 yet their sum is zero, and the family (a, ax) loses rank at a=0 (code/refute/i6b_ect_obstruction_exact.py, capture code/out/i6b_ect_obstruction_exact.captured.txt, exact arithmetic, no floats). A second toy with four iterated-log passages gives W3 = 0 identically at the boundary specialization L=0 (code/out/i6b_second_type_toy.captured.txt). The board recorded this dead-end three times on 2026-08-18. Scope of the refutation: it kills the shortcut INFERENCE, not the actual I^1_6b dynamics — finiteness of those graphics remains open, but any route through them must prove fixed-rank noncancellation for the specific four-Dulac displacement, control the parameter-dependent exponent strata and the identically-vanishing slow-divergence strata, and bound zeros by a derivation-division argument that never uses additivity of the ECT property. That positive form is exactly what R-center-ideal-zero-division isolates; the failure is structural and is not patchable by repairing the Wronskian.
```

```rung
id: R-single-second-type-leading-term
statement: For one named second-type Dulac transition map at a single semi-hyperbolic endpoint of one center-type quadratic graphic (H^3_14 or I^1_6b), compute the leading asymptotic term from the blow-up and normal form of the triple nilpotent point at infinity, and classify the transseries class — iterated logarithms and exponentials with parameter-dependent exponents — to which the leading term and the finite-rank module of that single passage's displacement contribution belong. This is the computational precursor to the zero-division theorem: it produces the generalized monomials m_i that R-center-ideal-zero-division assumes given. RR 2015 §2.6 gives the shape but explicitly does not establish the endpoint germs (claim i6b-four-second-type-full-graphic-not-covered); the run's task i6b-four-passage-analytic-gap records the endpoint maps as the remaining gap. The smooth test: the leading term must come from the analytic normal form, not a C^∞ estimate.
off: full-nonlinear-displacement, global-uniform, non-generic-degenerate, unbounded-n, line-of-singular-points, nesting-classification
stance: open
merge: Turn full-nonlinear-displacement back on: compose the single passage's leading term with the opposite-endpoint passage and the regular transition to form the full scalar (H^3_14) or two-equation (I^1_6b) displacement, then feed the resulting generalized-monomial family into the zero-division theorem of R-center-ideal-zero-division. The first move is to verify the single-map leading term against the Mourtada–Moussu 1-pfaffien criterion (claim mourtada-moussu-1997-dulac-pfaffian-iff-normalisable, full text held) as a consistency check on the transseries class.
```

```rung
id: R-center-ideal-zero-division
statement: For one named center-type quadratic graphic (H^3_14, the Lu 2026 target whose Bautin-ideal core — the identities L₄, L₆, L₈ in the five-parameter unfolding — is discharged by this run's exact Gröbner computations and kernel-checked Lean certificate), **assume** the displacement function on a fixed collar has been expanded in the Bautin-trick form Δ(z;λ) = Σ_{i=1}^k a_i(λ) m_i(z) (1 + h_i(z;λ)) where the generalized monomials m_i are determined by the vertex asymptotic classes, the coefficients a_i lie in the center ideal ⟨L₄, L₆, L₈⟩ (finitely generated, three generators, proved by this run), and h_i = o(1) uniformly in λ on a fixed complex collar. Then prove that Δ(·;λ) has at most k−1 isolated zeros counted with multiplicity, uniformly over the compact five-parameter neighbourhood Λ. This isolates the derivation-division (Rolle/Hadamard/Roussarie) zero-counting step from the Dulac-map expansion problem. STATE UPDATE 2026-08-21: the algebraic shell of this rung is kernel-checked as claim r-center-ideal-zero-division-conditional (conditional, axioms = kernel's three, no sorry) — the implication "Admissible data + zero_division theorem ⇒ uniform finite ncard bound" is verified. The rung remains OPEN because the analytic zero_division theorem on the iterated-log transseries class is an explicit binder hypothesis, not a Cited axiom (no source covers it), and is the run's open G-remainder gap.
off: second-type-dulac, non-generic-degenerate, unbounded-n, line-of-singular-points, nesting-classification
stance: open
merge: Turn second-type-dulac back on: derive the actual m_i and h_i from the two second-type Dulac transition maps at the semi-hyperbolic endpoints. The run's refuted short-Dulac approach forces the expansion class to be transseries with iterated logs/exponentials. The merge must produce the m_i in that class. The first concrete move is the rung directly below this one, R-single-second-type-leading-term: compute the leading asymptotic term of one second-type map from the blow-up/normal-form of the triple nilpotent point at infinity.
```

```rung
id: R-one-full-graphic-second-type
statement: For n = 2, one specifically named DRR graphic whose full (not only boundary) limit periodic sets are currently open — either H^3_14 (the semihyperbolic hemicycle through a triple nilpotent point at infinity, Lu 2026 claims closed with unverified analytic remainder), or I^1_6b (whose boundary RR 2015 settled but whose interior involves four second-type Dulac maps in a coupled two-equation displacement), or H^3_13, or DI_2b — has finite cyclicity under perturbation in the quadratic family: a fixed collar contains at most a finite coefficient-uniform number of bifurcating limit cycles. This is the full G-remainder: the second-type Dulac transseries expansion, the derivation-division zero bound, and uniformity over the compact parameter box.
off: non-generic-degenerate, unbounded-n, line-of-singular-points, nesting-classification
stance: open
merge: After one such graphic is settled, the remaining center-type second-type graphics must also be closed. Then turn line-of-singular-points back on: 11 open degenerate non-center graphics with a line/circle of singular points and a contact point whose weighted blow-up depends on the chosen normal form. The first move after settling one second-type graphic is to state the slow-divergence integral as leading term of displacement derivative for the degenerate non-center case, identify the center-condition stratum where it vanishes identically, and extend the theoretical results (blow-up of parameters) to that stratum.
```

```rung
id: R-one-degenerate-noncenter
statement: For one named degenerate non-center graphic from the DRR list — e.g., DF2b (the center version of DF2a, whose generic form DF1a/DF2a DR 2009 closed) or DI2a (the one Artés–Dumortier–Llibre 2009 already has partial results on) — prove finite cyclicity in the 5-parameter quadratic unfolding. The graphic has a line of singular points with one contact point; the derivative of the displacement is C^∞ contact-equivalent to a development with the slow-divergence integral as leading term; finite cyclicity follows when the slow-divergence integral does not vanish identically.
off: second-type-dulac, unbounded-n, nesting-classification
stance: open
merge: The first difficulty to turn back on after settling one degenerate non-center graph is either non-generic-degenerate (if the chosen graphic is generic, prove the exceptional subcases: the center-condition stratum where the slow-divergence integral vanishes identically, requiring parameter blow-up and extension of existing results) or second-type-dulac (if the graphic's limit periodic set touches a semi-hyperbolic vertex at infinity). The concrete first move is to choose one specific graphic — DI2a is the one with existing partial results in ADL 2009 — write its 5-parameter normal form from DR 2009 Table 1 (or the appropriate normal form for the chosen graphic type from DR 2009 §2), and compute the slow-divergence integral as an explicit rational/transcendental function.
```

```rung
id: R-all-degenerate-noncenter
statement: Every one of the 11 open degenerate non-center DRR graphics (DF1b, DF2b, DH1, DH2, DI1a, DI1b, DI2a, DI2b, DH3, DH4, DH5) has finite cyclicity in the quadratic family. DH5 is the hardest: it has two lines of singular points and needs a 7-parameter normal form rather than the standard 5-parameter reduction.
off: second-type-dulac, unbounded-n, nesting-classification
stance: open
merge: Turn second-type-dulac back on for the center-type graphics through infinity, and non-generic-degenerate for the exceptional center-condition strata of the degenerate graphics. At this point the only remaining open graphics are the four center-type second-type graphics (I^1_6b, H^3_13, DI_2b, H^3_14), which must be settled by the Dulac transseries expansion and derivation-division route.
```

```rung
id: R-h2-uniform
statement: H(2) is finite: there exists a finite coefficient-independent bound on the number of limit cycles of every planar quadratic vector field; the nesting-classification half remains excluded. Equivalent by the DRR reduction to finite cyclicity of all 121 graphics — the four center-type second-type graphics plus the 11 degenerate non-center graphics.
off: unbounded-n, nesting-classification
stance: open
merge: Turn unbounded-n back on. The quadratic proof relies on the finite DRR catalogue of 121 graphics; no corresponding finite catalogue exists for arbitrary degree. A structural mechanism — not a case list — must replace it.
```

```rung
id: R-full
statement: This is the full target, identical to the ladder goal. It is not a weakened rung — it is the goal itself, recorded here only so the ladder's bottom is visible. A rung that switches off no difficulty is not weaker than the goal; the goal belongs in the ladder header, not as a rung. The ladder is exhausted when every difficulty has been turned back on and the statement above is proved.
off: (none)
stance: open
merge: This is the full target, reached only after the quadratic and all-degree uniformity problems are solved, then the separate configuration-classification problem is also addressed. None of the weaker rungs implies it.
```
