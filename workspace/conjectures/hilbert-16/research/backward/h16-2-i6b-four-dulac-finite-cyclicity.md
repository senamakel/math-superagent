# Backward skeleton — finite cyclicity of the full I^1_6b graphic via the four-second-type-Dulac ECT route

Decomposition of the run's **adopted** four-Dulac/ECT line
(`research/approaches/compensator-pfaffian-mourtada-moussu-synthesis.md`,
`research/approaches/reduced-bautin-depth-chen-coefficient-engine.md`) into the
propositions that, together, give finite cyclicity of the *full* quadratic DRR
graphic **Λ₀ = I^1_6b** — the one open target for which the run already holds a
conditional Lean theorem (`code/lean/Lib/SlowDivergenceECTPartial.lean`) and a
kernel-checked ECT consequence (`code/lean/Lib/ECTSlowDivergence.lean`).

This is the concrete instance of the frame skeleton `h16-2-finite-cyclicity`'s
G-transition/G-zeros/G-uniform for a specific graphic, and is deliberately
**distinct** from `h16-2-h14-3-finite-cyclicity` (the Lu five-parameter
hemicycle route). The claims ledger says RR 2015 leaves **three** graphics with
only boundary-set cyclicity — I^1_6b, H^3_13, DI_2b — and the non-boundary
I^1_6b center strata carry four second-type Dulac maps whose composition is a
two-equation problem; that is the exact object decomposed here.

```skeleton
goal: cycl(Λ₀ = I^1_6b, full graphic) < ∞ — finite cyclicity of every
      non-boundary blown-up limit periodic set of the quadratic DRR graphic
      I^1_6b (RR parameter 1/2 < B < 1), uniformly over the family. The
      non-boundary center strata carry four second-type Dulac maps T₁,…,T₄ at
      the semi-hyperbolic endpoints, and their displacement is a coupled
      two-equation problem in (r₁,ρ₁,r₂,ρ₂) with rᵢρᵢ = νᵢ.
implies: The displacement is D = T₄ ∘ R₃ ∘ T₃ ∘ R₂ ∘ T₂ ∘ R₁ ∘ T₁ (four
      second-type Dulac maps composed with the regular transitions Rⱼ). The
      chain of four gaps below produces an `ECTReduction K δ` and then the
      uniform zero bound:
      G-endpoint-germs supplies all four Tᵢ in the RSZ Thm 2.3 shape with a
        common parameter-uniform property-J remainder over the stratum — this
        is exactly the pair `endpoint_maps ∧ analytic_uniform_remainder` that
        `SlowDivergenceECTPartial.full_graphic_zero_bound` takes as
        hypotheses, and it is where analyticity genuinely enters (Test 1: a
        C^∞ passage has no such uniform remainder; Mourtada–Moussu: not
        analytically normalisable ⇒ not 1-Pfaffian).
      G-reduce-finite-rank produces, on a common section, the representation
        of D (or of the coupled two-equation displacement) as a nontrivial
        linear combination of a finite-dimensional family of generalized
        monomials — powers × Ecalle–Roussarie compensators × iterated logs —
        with parameter-coefficients, covering the identically-zero
        slow-divergence strata by a zero-count-preserving
        contact/derivation-division (Rolle) reduction. This is the
        `representation ∧ nonzero` half of `ECTReduction`; the toy
        obstruction (i6b-ect-four-passage-closure-refuted) forces it to be
        proved for the family as a whole, never inferred per passage.
      G-ect-certificates verifies that family is an ECT-system on the section
        uniformly over the compact closure of the stratum — the
        `ect_property` half of `ECTReduction` — through Wronskian/CT,
        domain and transversality certificates. The ECT ⇒ ≤ dim−1 zeros
        consequence is already kernel-checked
        (`ECTSlowDivergence.displacement_zero_bound`, axioms = the kernel's
        three).
      G-specialise-uniform-bound completes the `sorry` in
        `SlowDivergenceECTPartial.full_graphic_zero_bound` (rewrite δ via
        `reduction.representation`, apply `reduction.ect_property`, take
        N = reduction.dimension − 1, uniform in p), yielding
        ∃ N, ∀ p ∈ K, δ's zero set on the section is finite with ncard ≤ N.
      Chain: (G-endpoint ∧ G-reduce ∧ G-ect-cert) ⇒ an `ECTReduction K δ`;
      G-specialise ⇒ the uniform bound over K; hence cycl(Λ₀) ≤ N < ∞ on the
      stratum — the DRR row the literature leaves open
      (i6b-four-second-type-full-graphic-not-covered). Uniformity is not a
      separate lemma: `ECTReduction.ect_property` is uniform in p ∈ K by
      construction, and K is the compact closure [½+δ, 1−δ] of the stratum —
      the compactness binder must be stated, not assumed.
rests-on: i6b-four-second-type-full-graphic-not-covered,
      i6b-four-second-type-dulac-hypotheses-not-established,
      i6b-slow-divergence-ect-not-applicable-as-held,
      i6b-ect-four-passage-closure-refuted,
      gmv-ect-does-not-cover-i6b-four-dulac, scholar-open-center-graphics,
      drr-1994-citation-anchor (DRR frame);
      files: code/lean/Lib/ECTSlowDivergence.lean (kernel-checked,
      displacement_zero_bound), code/lean/Lib/SlowDivergenceECTPartial.lean
      (conditional, sorry), code/lean/Lib/SecondTypeDulacRemainder.lean
killed-by: (1) The composition diagnostic of
      compensator-pfaffian-mourtada-moussu-synthesis showing a new
      parameter-dependent exponent per passage — then no common chart exists,
      G-endpoint/G-reduce fail, and the line narrows to Kaloshin's elementary
      restriction (the open graphic is not elementary, so the four-Dulac route
      dies for the full I^1_6b). (2) A G-reduce that never uses the
      analytic/transseries structure of the endpoint germs — a purely
      topological/C^∞ reduction bounds a smooth falsity (Dulac's 1923 error
      shape); the derivation-division must act on analytic/quasianalytic germs
      with the remainder controlled uniformly. (3) The DRR-definition match:
      RR 2015 already settles the boundary limit-periodic sets
      (drr-rr-boundary-only-for-3-graphics); if the ECT/zero-bound statement
      here covers only strata RR already closed, a correct proof would not
      close the DRR row — the statement must be the *full* graphic. (4) Any
      certificate that infers the summed family's ECT from per-passage ECT is
      refuted before it starts (i6b-ect-four-passage-closure-refuted: exact
      toy A=(1,x), B=(−1,−x), each Wronskian 1, sum zero; (a,ax) loses rank at
      a=0).
status: sketched
```

```gap
id: G-endpoint-germs
lemma: For each semi-hyperbolic endpoint of the non-boundary I^1_6b center
       strata (RR 1/2 < B < 1), the second-type Dulac map Tᵢ admits the RSZ
       Thm 2.3 expansion
         Tᵢ(s) = ηᵢ(ν) s^{σ̄ᵢ} ω(s, αᵢ) + s^{σ̄ᵢ}(Y₀ + φᵢ(s; λ))
       with property-J remainder φᵢ flat uniformly in the stratum
       parameters, and the four expansions share one chart: the composed
       displacement D = T₄∘R₃∘T₃∘R₂∘T₂∘R₁∘T₁ has a single asymptotic
       expansion on a common section with format fixed over the stratum.
       Not established anywhere in the library: RSZ §2.6 says only first-type
       maps are needed for its Theorem 2.3
       (i6b-four-second-type-dulac-hypotheses-not-established).
status: open
next: tool_builder + symbolic_math, today: from the held Shan thesis §4.2
       eq 4.2.1 (research/sources/shan-phd-thesis-2013.full.md lines
       ~2060–2100) and RSZ Thm 2.3, write the four endpoint germs for the
       stratum as explicit formulas over Q(ν, α, σ̄); then run the
       composition diagnostic of
       compensator-pfaffian-mourtada-moussu-synthesis — compose Tᵢ with the
       regular transitions Rⱼ symbolically and record whether the leading
       exponent format stays fixed (common chart exists: line live) or a new
       parameter-dependent exponent appears per passage (format unbounded:
       line narrows to Kaloshin's elementary restriction). Capture to
       code/out/compensator_pfaffian_composition.captured.txt.
```

```gap
id: G-reduce-finite-rank
lemma: The complete I^1_6b displacement — the coupled two-equation problem in
       (r₁,ρ₁,r₂,ρ₂) with rᵢρᵢ = νᵢ — admits a zero-count-preserving
       contact/derivation-division (Rolle) reduction to a finite-dimensional
       family of generalized monomials (powers × Ecalle–Roussarie compensators
       ω = (x^{−α}−1)/α × iterated logs) with parameter-coefficients, on a
       common section; the identically-zero slow-divergence strata are covered
       by treating the first nonvanishing higher-order term (a vanishing
       leading coefficient must not silently remove first-order control). The
       reduction must be proved for the family as a whole:
       i6b-ect-four-passage-closure-refuted shows per-passage ECT does not
       survive summation.
status: open
next: tool_builder, today: execute code/pfaffian/verify_compensator_chain.py
       (df₀ = −f₀², df₁ = −αf₁f₀, df₂ = σ̄f₂f₀, df₃ = (1/l)f₃f₀,
       df₅ = f₀) and capture to code/out/compensator_pfaffian_chain.captured.
       txt — the leading part is Pfaffian of fixed format iff the chain's
       format is bounded over the stratum; then extend the exact toy
       (A = (1,x), B = (−1,−x)) to the vanishing-slow-divergence stratum and
       record, exactly over Q in sympy, the first higher-order term that
       restores displacement control.
```

```gap
id: G-ect-certificates
lemma: The reduced finite-dimensional family from G-reduce-finite-rank is an
       ECT-system on the common section uniformly over the compact closure of
       the stratum: its Wronskian/CT chain, domain and transversality
       conditions hold for every p in the closure, with the ECT property
       verified for the whole family (never inferred from per-passage ECT, per
       i6b-ect-four-passage-closure-refuted). Given this, the kernel-checked
       consequence applies: ECTFamily + IsDisplacement ⇒ ZeroSet finite with
       ncard ≤ Fintype.card ι − 1
       (ECTSlowDivergence.displacement_zero_bound, axioms = the kernel's
       three).
status: open
next: symbolic_math + lean_prover, today: from the explicit G-reduce family,
       form the Wronskian chain over Q(ν, α, σ̄), reduce "ECT on the section"
       to finitely many strict-sign / Sturm-alternation conditions, discharge
       with decide/norm_num/Sturm over ℚ, and state the concrete ECTFamily
       instance as a Lean theorem (the shape
       ECTSlowDivergence.displacement_zero_bound already consumes); report
       #print axioms — must stay the kernel's three plus Cited for the
       endpoint frame, never more.
```

```gap
id: G-specialise-uniform-bound
lemma: The conditional theorem full_graphic_zero_bound
       (SlowDivergenceECTPartial.lean) is completed: from endpoint_maps,
       analytic_uniform_remainder, and an ECTReduction K δ (supplied by the
       three gaps above), ∃ N, ∀ p ∈ K, the zero set of δ(p, ·) on the
       section is finite with ncard ≤ N. The ECT-consequence half is
       discharged by the kernel-checked
       ECTSlowDivergence.displacement_zero_bound; the remaining `sorry` is the
       routine rewrite-then-apply specialisation.
status: open
next: lean_prover, today: finish the `sorry` in
       SlowDivergenceECTPartial.full_graphic_zero_bound exactly as its inline
       gap says — rewrite {x | δ p x = 0} to
       {x | ∑ i, reduction.coefficient p i * reduction.basis i p x = 0} via
       reduction.representation, apply
       reduction.ect_property p hp (reduction.nonzero p hp), take
       N = reduction.dimension − 1 (the ECT bound is uniform in p); report
       #print axioms full_graphic_zero_bound — must remain the kernel's three.
```

**How the lemmas recombine (the `implies` spelled out).** This is a reduction
chain, not an induction, and its shape is forced by the run's own material:
`SlowDivergenceECTPartial.lean` already states the top inference — the
hypotheses `endpoint_maps`, `analytic_uniform_remainder` and the structure
`ECTReduction K δ` are exactly what the three forward gaps must supply, and the
only missing glue is the `sorry` (G-specialise). G-endpoint is the
analyticity step (Test 1): the property-J remainder uniform in the stratum
parameters is what a C^∞ passage lacks, and it is what gives the composition a
single chart. G-reduce is where the toy obstruction bites: the reduced family
is a *whole-family* object, and the derivation-division (Rolle) step that
preserves the zero count must act on the analytic/quasianalytic germs, with the
identically-zero slow-divergence strata handled by their first nonvanishing
higher-order term. G-ect-certificates is the finite algebraic core the Lean
kernel can finish — the ECT property reduced to strict-sign / Sturm
certificates, exactly the "argument Lean can finish" preference. G-specialise
closes the loop uniformly because `ECTReduction.ect_property` is uniform in
p ∈ K by construction; the compactness of K is a stated binder, not an
afterthought. Order of attack: **G-specialise first** — the `sorry` is small,
its proof sketch is already written in the file, and completing it turns the
existing conditional theorem into a closed implication (conditional on the
three analytic gaps), which is the honest partial result this run can bank
today. Then G-endpoint's composition diagnostic, which settles whether the
whole route lives or narrows.

**Tests applied.** Test 1 (smooth test): satisfied at G-endpoint (the uniform
property-J remainder; Mourtada–Moussu: non-normalisable ⇒ not 1-Pfaffian) and
carried through G-reduce/G-ect-cert (the ECT structure of the monomial
family); a reduction that never uses the endpoint germs' analytic/transseries
structure bounds a smooth falsity and is refuted. Test 2 (lower-bound test):
this is a per-graphic cyclicity bound, not a global H(n) bound, so
H(2)≥4, H(3)≥13, H(n)≳n²log n do not threaten it; a downstream claim that the
bound gives H(2)<∞ would need every other graphic and is not claimed here.
Test 3 (slow–fast test): binds G-reduce — the identically-zero slow-divergence
strata are exactly where a sharp-looking count dies; the first-nonvanishing-
higher-order-term rule is the stated guard.
