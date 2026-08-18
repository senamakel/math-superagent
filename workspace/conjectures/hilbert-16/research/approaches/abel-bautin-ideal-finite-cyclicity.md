# Abel-equation Bautin-ideal reduction

```approach
idea: Change the object from the planar displacement function to a first-order Abel equation
     on the transversal cylinder, and let the cyclicity of the graphic be governed by the
     finitely generated Bautin ideal of that Abel equation (Briskin–Françoise–Yomdin theory),
     computed by exact Gröbner and pushed to a kernel-checked Lean theorem.

mechanism: A planar polynomial system in the polar chart (r,θ) with angular velocity B(θ)
     that keeps its sign on the period annulus reduces the Poincaré return map to the
     2π-periodic first-order equation  dr/dθ = A(θ,r)  — an Abel-type equation (polynomial
     in r, trigonometric in θ). The displacement function is then  r(2π;ρ) − ρ, and its
     zeroes are exactly the limit cycles near the annulus. Briskin–Françoise–Yomdin and the
     Yomdin school ("The Bautin ideal of the Abel equation", Nonlinearity 11 (1998) 431–443;
     Roytvarf, Pakovich, Briskin–Roytvarf–Yomdin) prove that for fixed degree the center
     conditions and the cyclicity of the origin of such an Abel equation are governed by a
     FINITELY GENERATED ideal in a polynomial ring in the Fourier coefficients — the Abel
     analogue of the classical Bautin ideal. That is exactly the structure this run already
     computes for the planar Lu/DRR five-coefficient chart (the L4/L6/L8 obstructions, the
     membership L10,L12∈⟨L4,L6,L8⟩, verified by Gröbner over Q). The reformulation: a graphic's
     finite cyclicity is a statement that this Abel Bautin ideal has finite codimension in the
     relevant ring, so the zero-count is bounded by the ideal's height / a Gröbner-basis
     computation — a finite algebraic question Lean can close (ideal membership, resultant,
     codimension) rather than an analytic paragraph. Test 1 (smooth test) is satisfied where it
     must be: the finiteness enters through algebraicity of the polynomial coefficients of P,Q,
     not through smoothness of the return germ.

status: refuted

killed-by: The proposed route — scalar Abel-equation Bautin ideal ⇒ finite cyclicity of a
     DRR graphic — fails at three literature-checked points. (1) The Abel-equation centre set
     is NOT finitely described by the Bautin/composition ideal: the Composition Conjecture
     (centre ⇔ polynomial-composition condition, the frame Briskin–Françoise–Yomdin built
     around the Bautin ideal of the Abel equation) is false — counterexamples by Pakovich and
     by Giné–Grau–Santallusia (ETDS 2018, doi:10.1017/etds.2018.16) for polynomial Abel
     equations, and earlier for trigonometric ones; the parametric centre problem is solved
     (Pakovich, JEMS 2017, doi:10.4171/jems/719) but that is the one-parameter
     y'=p(x)y²+εq(x)y³ case, not a cyclicity bound. (2) The number of limit cycles of an Abel
     equation is itself the open Smale–Pugh problem, NOT a bounded quantity for fixed
     coefficient degree: Lins Neto (1980) proved x'=p(cos t)x³+sin t·x² has ≥N limit cycles
     for every N as deg p grows, so the Abel equation itself has no H(n)-type bound unless
     sign/transversality hypotheses are added (Gasull–Guillamon IJBC 2006,
     doi:10.1142/s0218127406017130; Bravo–Calderón–Fernández JDE/JMAA 2020,
     doi:10.1016/j.jmaa.2020.124580; Huang–Torregrosa–Villadelprat SIAM 2020,
     doi:10.1137/20m1340083 gives only H3,2(n,m)≥2(n+m)−1 lower bounds). The 'cyclicity of
     the origin' Bautin ideal of the Abel equation bounds bifurcation from the zero solution
     (Batenkov–Binyamini arXiv:1504.02208) — a local tangential statement — not the full
     displacement near a graphic. (3) The open DRR graphics (I^1_6b, H^3_13, DI_2b full;
     H^3_14) are NOT scalar Abel equations: RR 2015 explicitly leaves the full centre-type
     (I^1_6b) graphic as a TWO-equation problem in (r₁,ρ₁,r₂,ρ₂) with four second-type Dulac
     maps (claim i6b-four-second-type-full-graphic-not-covered); the scalar trigonometric
     Abel reduction exists (Cherkas; Llibre–Zhang Proc. Roy. Soc. Edinb. 2017,
     doi:10.1017/s0308210517000221 applies dr/dθ = (λ₁r+fr²)/(1+gr) to quadratic systems and
     recovers at-most-one/at-most-three results under sign hypotheses — the correct, restricted
     way the Abel machinery buys H(2) sub-bounds) but does not carry the four-Dulac coupled
     displacement. Hence the claimed implication from a finitely generated Abel Bautin ideal to
     a uniform graphic cyclicity bound is unsupported; the surviving instrument is the
     restricted scalar-Abel Bautin/zero-count machinery for center-annulus subfamilies.

survives: (narrowed) The Abel-equation reduction is a legitimate, literature-grounded
     instrument for RESTRICTED quadratic subfamilies — exactly as Llibre–Zhang 2017 uses it:
     quadratic system → Cherkas trigonometric Abel → sign-condition/Abelian bounds on limit
     cycles around the origin. The Bautin-ideal/composition machinery of Briskin–Françoise–
     Yomdin, Roytvarf, Pakovich correctly describes the Abel CENTRE set (moments, composition
     algebra, Pakovich–Muzychuk polynomial-moment solution) and the cyclicity of the zero
     solution (Batenkov–Binyamini). It does NOT close any open DRR graphic, and its finite-
     codimension claim does not transfer to the four-second-type displacement. A future
     attempt may reuse the Llibre–Zhang reduction (doi:10.1017/s0308210517000221) as the
     concrete restricted form. The container failure (a scalar Bautin ideal not closed under
     the four-map sum) is repaired by the adopted synthesis
     `quasianalytic-displacement-module-rolin-servi`, which supplies closure under addition
     by construction.

precedent:
- https://doi.org/10.1088/0951-7715/11/3/003 (Briskin–Françoise–Yomdin, The Bautin ideal of the Abel equation, Nonlinearity 11 (1998) 431–443 — the named origin of the Abel Bautin ideal)
- https://doi.org/10.4007/annals.2010.172.437 (Briskin–Roytvarf–Yomdin, Center conditions at infinity for Abel differential equations, Ann. of Math. 172 (2010) 437–483 — center set ≈ composition condition, with finitely many exceptions)
- https://doi.org/10.4171/jems/719 (Pakovich, Solution of the parametric center problem for the Abel differential equation, JEMS 19 (2017) — parametric centre ⇔ composition condition, one-parameter case only)
- https://doi.org/10.1017/etds.2018.16 (Giné–Grau–Santallusia, A counterexample to the composition condition conjecture for polynomial Abel differential equations, ETDS 2018 — Composition Conjecture FALSE)
- https://doi.org/10.1017/etds.2014.94 (Briskin–Pakovich–Yomdin, Algebraic geometry of the center-focus problem for Abel differential equations, ETDS 2014 — center set described by composition algebra up to small correction)
- https://doi.org/10.1016/j.jmaa.2012.09.006 (Cima–Gasull–Mañosas, A simple solution of some composition conjectures for Abel equations — trigonometric CC-centers solved)
- https://doi.org/10.1137/20m1340083 (Huang–Torregrosa–Villadelprat, On the number of limit cycles in generalized Abel equations — Smale–Pugh open; H3,2(n,m)≥2(n+m)−1)
- https://doi.org/10.1016/j.jmaa.2020.124580 (Bravo–Calderón–Fernández, Upper bounds of limit cycles in Abel differential equations with invariant curves — bounds only under invariant-curve/transversality hypotheses)
- https://doi.org/10.48550/arxiv.1504.02208 (Batenkov–Binyamini, Uniform upper bounds for the cyclicity of the zero solution of the Abel differential equation — cyclicity of the ZERO solution only)
- https://doi.org/10.1017/s0308210517000221 (Llibre–Zhang, Non-existence/existence/uniqueness of limit cycles for quadratic systems — the restricted Cherkas-Abel reduction to at-most-one/at-most-three results)
- https://doi.org/10.4064/bc94-0-11 (Françoise, Integrability and limit cycles for Abel equations — survey; Bautin ideal ↔ center conditions)
- claim:i6b-four-second-type-full-graphic-not-covered
- claim:i6b-slow-divergence-ect-not-applicable-as-held
- claim:gmv2008-ect-criterion
- claim:h16-alien-limit-cycles-abelian-insufficiency

first-step: (restricted, literature-grounded) Reproduce the Llibre–Zhang 2017 Cherkas reduction
     on a concrete quadratic center-annulus family already in the run's orbit: write
     dr/dθ = (λ₁r+fr²)/(1+gr), apply the Cherkas change ρ = r/(1+gr) to obtain the
     trigonometric Abel equation dρ/dθ = q(θ)ρ³+p(θ)ρ², and verify the at-most-one/at-most-
     three sign-condition bounds on a named family (the pattern that actually buys H(2)
     sub-bounds in the literature). State the sign conditions in Lean (the BautinRecurrence
     pattern). Do NOT attempt to extend the scalar Abel Bautin ideal to the four-second-type
     displacement of I^1_6b/H^3_13/DI_2b — that step is refuted above.
```
