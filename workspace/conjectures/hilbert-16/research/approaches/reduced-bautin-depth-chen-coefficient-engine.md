# Reduced Bautin depth + Chen coefficient engine — the grounded synthesis

```approach
idea: The reduced-Bautin-depth method of García (Proc. AMS 2015/2016) — bound the
  cyclicity of a monodromic singularity by the stabilization length κ of the
  INTEGRAL CLOSURES of the ascending chain of coefficient ideals of its analytic
  return map — fed by a Chen/Fliess coefficient engine that generates those
  coefficients exactly even where the Bautin ideal is not polynomial.
mechanism: García's theorem is the finite-determinacy machine: for a monodromic
  singularity with an analytic Poincaré return map whose Bautin ideal B is
  polynomial in the parameters, the ascending chain of ideals J_k = ⟨v_1,...,v_k⟩
  (v_k the return-map coefficients) stabilizes by Noetherianity, and the index κ
  at which the INTEGRAL CLOSURES of the J_k stabilize satisfies
  Cyc(X_λ, p_0) ≤ κ−1. This works even when B is non-radical, and it is reported
  as the minimum bound in the literature; the class includes nondegenerate
  centers, generic nilpotent centers, and some degenerate centers. What research
  surfaced that neither original candidate named: the polynomial hypothesis is
  exactly the boundary. The open DRR center graphics (I¹₆b, H³₁₃, DI₂b — triple
  nilpotent points at infinity surrounding a center) have displacement maps that
  are compositions of second-type Dulac maps, whose coefficients are transseries,
  not polynomials in the parameters. The Chen/Fliess iterated-integral expansion
  (candidate 1, grounded as a coefficient engine, not a finite-determinacy
  theorem) is precisely the tool that computes those coefficients word-by-word
  beyond the polynomial case. The new attack line is therefore: run the
  reduced-Bautin-depth integral-closure stabilization on the coefficient chain,
  computed exactly by the Chen engine, and locate the FIRST generator where the
  polynomial-ring chain fails to contain a genuine Dulac coefficient. Either the
  chain stabilizes in an explicitly enlarged finite-type ring (a new finite-
  cyclicity theorem for a named non-polynomial family), or it provably fails at a
  specific generator — and that generator is the named obstruction the next
  attempt must adjoin. Analyticity enters exactly where it must: the return map's
  analytic/convergent germ structure is what makes "finitely many coefficients +
  integral-closure stabilization" decide the whole germ, and this step is false
  for C^∞ fields (Dulac's error). The finite core is Gröbner/integral-closure
  computation over ℚ plus a finite stabilization certificate — Lean-finishable.
status: adopted
first-step: (a) VALIDATE by re-implementing García's reduced-Bautin-depth
  algorithm: for the quadratic focus family already computed by this run
  (u' = −v + a1u² + a2uv + a3v², v' = u + b1u² + b2uv + b3v²), form the ascending
  chain J_1 = ⟨L4⟩, J_2 = ⟨L4,L6⟩, J_3 = ⟨L4,L6,L8⟩, compute the INTEGRAL CLOSURES
  of each over ℚ (Singular/PARI via symbolic_math, or sympy with normalization),
  and check the stabilization index κ = 4, recovering M(2) = 3 as κ−1 — matching
  Bautin 1952 and García's method. (b) Then a NILPOTENT center family (García's
  stated scope: "generic nilpotent centers"; Andreev/Bogdanov–Takens normal form
  ẋ = y + …, ẏ = x² + …), compute its return-map coefficient chain and reduced
  Bautin depth exactly over ℚ, and match any published bound. (c) State the
  theorem in Lean before computing: `Cited.reduced_bautin_depth_bound` as an axiom
  with `/-- src: García, Proc. AMS 143 (2015) 4237–4247, doi:10.1090/proc/12896
  -/` docstring, whose conclusion is `Cyc ≤ κ − 1` given the stabilization
  certificate, and discharge the certificate with `decide`/`norm_num` over ℚ.
  Capture everything to code/out/ with the system, term order and field stated.
precedent: https://doi.org/10.1090/proc/12896 ; https://doi.org/10.1090/proc/13570 ;
  https://doi.org/10.1007/978-0-8176-4727-8 (Romanovski–Shafer) ;
  https://doi.org/10.1016/j.matcom.2013.02.003 (Ferčec–Mahdi) ;
  https://doi.org/10.1155/2009/590856 (Costin, Chen/nilpotent return-map expansion) ;
  https://arxiv.org/abs/1602.08655 (Brudnyi, shuffle Hopf algebras in the center
  problem) ; claims: h16-bautin-1952-m2equals3-primary,
  bautin-chart-membership-l8-l10-l12, lu-finite-core-identity-half-checked,
  i6b-four-second-type-full-graphic-not-covered
what-it-buys: A grounded, published, minimum-bound method for monodromic
  singularities (including generic nilpotent and some degenerate centers),
  re-executed clean-room with a Lean-statable stabilization certificate. Past
  validation, the Chen engine turns the polynomial-hypothesis boundary into a
  locatable, computable obstruction for the open DRR center graphics — the first
  exact record of where reduced-Bautin-depth stops, which is itself a reportable
  result and the map the next attempt needs.
```

## Why this, and not the two parents as proposed

The flatness/discriminant candidate (parent 2) proposed **generic flatness + Rees
algebras + finite jet schemes** for the *full* four-Dulac displacement. Research
closed that: generic flatness stratifies an already-supplied finite-type
morphism; it cannot manufacture one, and no source supplies a finite-jet
coherent model of the full nonhyperbolic displacement. But research surfaced the
**established reformulation** — García's reduced Bautin depth — which *is* the
integral-closure/ascending-chain mechanism I was reaching for, with the
hypotheses made precise (analytic return map + polynomial Bautin ideal) and the
strongest known bound. The Chen candidate (parent 1) was closed as a
*finite-determinacy* theorem but survives as a *coefficient engine*. The
synthesis is: García's machine consumes coefficients, Chen's engine produces
them, and the polynomial hypothesis is the named boundary where the open
graphics sit. This is the gap between my reformulation and the literature's
actual content, and it is a real, first-step-able line.

## Three tests

1. **Smooth test.** Passes: the integral-closure stabilization decides the germ
   only because the return map is analytic (convergent); a C^∞ field has no such
   finite coefficient chain. The first-step computation must record exactly where
   analyticity of the return map is used, or the argument is Dulac's error again.
2. **Uniformity.** For the local monodromic setting, uniformity is over the
   parameter space via the polynomiality of the Bautin ideal — a finite algebraic
   statement, not pointwise finiteness. For the open graphics, uniformity is the
   open question and must NOT be asserted: the first step stays local and names
   it.
3. **Counterexample hunt.** The stress test is the *degenerate* center case where
   the first Dulac coefficient is non-polynomial: hunt for the first generator
   that leaves the polynomial chain as seriously as one hunts for stabilization.
   A provable failure at generator k is a result (the located obstruction), not
   a failed run.
