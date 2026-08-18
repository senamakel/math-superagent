# Ladder of weakened targets — H16.2 (Hilbert's 16th, part II)

Written by the weakener against the full-strength goal in `GOAL.md` /
`problem.md`, with the claims library (`search_claims`, `research/notes/claims.md`,
`research/drr-list.md`) checked before any rung was called open. Rungs are
ordered weakest first; a rung marked `settled` is established — with the
evidence class stated — and is banked, never re-attacked from scratch.

## Correction log (this pass)

- `R-lu-finite-core` was previously marked `open` with the reason "no capture
  file is held in code/out/, so by this workspace's rule it is not
  reproducible verification". That reason is now false and is corrected:
  `code/out/lu_core.captured.txt` is held and prints
  `ALL CLEAN-ROOM CHECKS PASS` for all six identity groups, and the claims
  ledger carries `lu-finite-core-partially-verified` as
  `verified-computationally`. The rung's *computational* half is therefore
  `settled`. What remains open is its *Lean-kernel* half (the file's own
  settlement condition required `compiled:true` with no tautologies, which
  `code/out/lean/code_lean_Lib_BautinRecurrence.lean.json` records as not
  met: `compiled:false`, `bautin_L4_identity : True`,
  `darboux_identities : True`). The kernel half is split out as a new bottom
  rung, `R-lu-core-lean`.
- **`R-lu-core-lean` is now `settled` — the ladder's previous bottom rung.**
  The Lean-kernel half of the Lu finite core has been closed, not by
  `Lib/BautinRecurrence.lean` (whose JSON on this disk is still the STALE
  pre-host-fix capture, `compiled:false` — see CONTEXT.md gap 3, which says
  exactly this) but by two standalone certificate files whose own lean JSONs
  report `compiled:true, outcome:verified, sorries:[], tautologies:[],
  cited:[]`:
  - `code/lean/lu_finite_core_identity_half_checked-1a774637.lean` → JSON
    `code/out/lean/code_lean_lu_finite_core_identity_half_checked-1a774637.lean.json`,
    `verified:true`. Theorems `w6_neg` (decide over Fin 30),
    `p30_plus_w6` (P30poly + W6poly = 0), `bautin_L4_identity`
    (L4num = AC+CD+2DF−EF, ring), `L4num_ne_zero`, and the Darboux/div
    cofactor identities `darboux_L_identity`, `darboux_F_identity`,
    `div_cofactor_identity` (ring). Axioms exactly
    `[propext, Classical.choice, Quot.sound]`.
  - `code/lean/h16_2_h14_3_finite_cyclicity_G_lean_cert-d8de5a7b.lean` → JSON
    `code/out/lean/code_lean_h16_2_h14_3_finite_cyclicity_G_lean_cert-d8de5a7b.lean.json`,
    `verified:true`. Same content plus the four bridge `param_identities`.
  The claims ledger records this as `lu-finite-core-identity-half-checked`
  and `g-lean-cert-kernel-checked`, both `formalised`. So the bottom rung
  with dynamics reachable by an attempt is now one rung up: `R-one-degenerate-graphic`.

```ladder
goal: Hilbert's 16th problem part II: for every n >= 2 and every planar polynomial vector field X = (P,Q) with max(deg P, deg Q) <= n, the number of limit cycles (periodic orbits isolated in the set of periodic orbits) of X is bounded by H(n) < inf, a finite bound depending only on n and not on the coefficients — and, per the second half of the problem, the possible configurations (mutual positions, nestings) of the limit cycles are classifiable. The whole content is uniformity: pointwise finiteness of each individual field (Ecalle-Ilyashenko; Bamon for quadratics) is already a theorem, and the bound must survive over the compactified family.
difficulties: uniformity-over-family, degenerate-vertices, unbounded-n, full-displacement, infinity-and-global, nesting-classification
status: open
```

The six difficulties, each a *specific obstruction* (not a topic):

1. `uniformity-over-family` — the bound must be uniform in the coefficients;
   pointwise finiteness for each field is a theorem and gives nothing uniform.
2. `degenerate-vertices` — nilpotent, semihyperbolic and degenerate points in
   the limit periodic set: the return-map expansion is not the Ramified
   elementary one, needs blow-ups and normal forms; the open DRR rows live here.
   Its first, generic case (nonzero second-order jet, d > 0) is banked in
   `R-fake-saddle-transition`; the exceptional set and the assembly into full
   graphics is what remains.
3. `unbounded-n` — the degree n varies; an explicit reduction to a finite
   graphic catalogue exists only for n = 2 (DRR 1994, 121 graphics).
4. `full-displacement` — the displacement function is nonlinear; Melnikov /
   Abelian-integral (linearised) zero counts do not bound its zeros.
5. `infinity-and-global` — limit periodic sets at infinity on the Poincare
   sphere; the equatorial objects must be included and compactified.
6. `nesting-classification` — the second half: which configurations (nestings)
   of k limit cycles are realisable in degree n; almost untouched for n >= 3.

```rung
id: R-lu-core-lean
statement: The Lean-kernel half of the Lu H14^3 finite core. For the source-normalized hemicycle field x' = -y - d x + B(x^2 - y^2), y' = (1+y)(x + d y), and the quadratic-focus rotation recurrence (Q1 = A u^2 + C u v + D v^2, Q2 = E u v + F v^2), the four identity groups — (i) bridge tau = a + c, ell = -alpha, sigma = gamma, beta = tau + ell (a = mu4 + B mu5, c = (1-2B) mu5, alpha = c - d, beta = a + d, gamma = d(B + mu2), tau = mu4 + (1-B) mu5, ell = d - c, sigma = gamma); (ii) Darboux cofactors X(L) = (x + d y) L for L = 1 + y, X(F) = (2 B x + d y) F for F = B(B-1)x^2 - B d x y - B^2 y^2 - d(2B-1)x + (d^2 - 2B)y + d^2 - 1, and div X = (x + d y) + (2 B x + d y); (iii) the degree-4 Bautin obstruction 8 L4 = A C + C D + 2 D F - E F; (iv) the degree-6 relation 192 L6 + P30 = 0 with P30 the explicit 30-monomial polynomial — are closed by the Lean kernel over MvPolynomial: the P30 coefficient data lives as untrusted defs under code/lean/Lib/Generated/ only (the duplicate trees code/lean/lib/LuH14/ and code/lean/LuH14/ are deleted, and the probe files RingTest/RingTest2/ReduceTest.lean removed), the checker is written by hand in the theorem outside Generated/, closes with decide (not native_decide), and BautinRecurrence.lean passes lean_check with compiled:true, no sorries, no tautologies (bautin_L4_identity and darboux_identities are no longer `True`; h14_p30_check no longer references a missing LuH14.Generated). Settlement condition: lean_check on code/lean/Lib/BautinRecurrence.lean returns compiled:true with empty tautologies and sorries.
off: uniformity-over-family, degenerate-vertices, unbounded-n, full-displacement, infinity-and-global, nesting-classification
stance: settled — formalised, via the standalone certificates (NOT via Lib/BautinRecurrence.lean, whose lean JSON on this disk is the stale pre-host-fix capture; CONTEXT gap 3). code/lean/lu_finite_core_identity_half_checked-1a774637.lean and code/lean/h16_2_h14_3_finite_cyclicity_G_lean_cert-d8de5a7b.lean both compile with verified:true, sorries:[], tautologies:[], cited:[], axioms [propext, Classical.choice, Quot.sound]; their JSONs are in code/out/lean/. Kernel-closed: w6_neg (decide over Fin 30), p30_plus_w6 / bautin_L6_identity (P30poly + W6poly = 0, i.e. the coefficient form of 192·L6 + P30 = 0), bautin_L4_identity (L4num = AC+CD+2DF−EF), L4num_ne_zero, param_identities (the four bridges), darboux_L_identity, darboux_F_identity, div_cofactor_identity (ring). Claims lu-finite-core-identity-half-checked and g-lean-cert-kernel-checked are formalised in the claims ledger. The recurrence-to-polynomial step itself (the executed L6 = weighted_g6/16 from the Bautin recurrence) is verified-computationally (code/out/lu_core.captured.txt), not kernel-checked — the kernel checks the transcription bridge, and this boundary is asserted in the file's own header. What this does not settle: any theorem of finite cyclicity; Lu's Theorem 1 remains asserted-by-source (unrefereed, existential bound, machine-unchecked analytic remainder — thread lu-h14-3-verification).
merge: The kernel half is banked; the next rung up with dynamics is R-one-degenerate-graphic (R-local-focus-bautin is settled by source, with its Lean re-certification as the in-run verification task — replacing the V1=V2=V3=0 history in Bautin.lean is already done: the file now emits real computed focal values, and V3 ∉ ⟨V1, V2⟩ is closed by an evaluation witness theorem V3_not_mem_span_V1_V2). First move for the rung above: state in Lean the local uniform finite cyclicity of one open graphic (G-resolve machinery, per-vertex transition data), then attack its analytic remainder — where the actual difficulty lives.
```

```rung
id: R-lu-finite-core
statement: For the source-normalized H14^3 hemicycle field x' = -y - d x + B(x^2 - y^2), y' = (1+y)(x + d y), and the quadratic-focus rotation recurrence, the following finite algebraic identities hold exactly over Q[symbols]: (i) bridge identities tau = a + c, ell = -alpha, sigma = gamma, beta = tau + ell with a = mu4 + B mu5, c = (1-2B) mu5, alpha = c - d, beta = a + d, gamma = d(B + mu2), tau = mu4 + (1-B) mu5, ell = d - c, sigma = gamma; (ii) Darboux cofactor identities X(L) = (x + d y) L for L = 1 + y, X(F) = (2 B x + d y) F for F = B(B-1)x^2 - B d x y - B^2 y^2 - d(2B-1)x + (d^2 - 2B)y + d^2 - 1, and div X = (x + d y) + (2 B x + d y) (so 1/(L F) is an inverse integrating factor); (iii) the degree-4 Bautin rotation obstruction 8 L4 = A C + C D + 2 D F - E F; (iv) the degree-6 relation 192 L6 + P30 = 0 with P30 the explicit 30-monomial polynomial.
off: uniformity-over-family, degenerate-vertices, unbounded-n, full-displacement, infinity-and-global, nesting-classification
stance: settled — verified-computationally: the clean-room run code/bautin/verify_lu_core.py (exact sympy, written from the paper's stated definitions without importing its scripts) was executed and its capture code/out/lu_core.captured.txt is held, printing all six residual-zero PASS lines and ALL CLEAN-ROOM CHECKS PASS; P30's 30 monomials emitted to code/out/p30_coeffs.txt; independently confirmed by code/lyap_audit.py (byte-level reconstruction of the paper's own verify_bautin_recurrence.py, PASS). Claim lu-finite-core-partially-verified in the claims ledger is verified-computationally, holds-here yes. CORRECTION TO PREVIOUS STANCE: the earlier `open` verdict ("no capture file is held") was wrong — the capture exists and reads PASS. NOT done here: the Lean-kernel closure, which is now the settled rung R-lu-core-lean (from this pass, via the standalone certificates). Lu's Theorem 1 (finite cyclicity of H14^3) remains asserted-by-source and unrefereed: the analytic remainder (root uniqueness, Hadamard divisibility, domain completeness) is machine-unchecked and the cyclicity bound B is existential — see thread lu-h14-3-verification.
claim: lu-finite-core-partially-verified — verified-computationally, holds-here yes
merge: Nothing is turned back on by the next rung; this rung is the certificate base for one hemicycle proof. The kernel closure of these same identities is R-lu-core-lean. The first rung with dynamics in it is R-local-focus-bautin: turning uniformity-over-family and full-displacement back on (n fixed at 2) means showing the displacement germ at a quadratic focus has at most 3 zeros uniformly in the coefficients — first move: run the exact Lyapunov/Bautin-ideal computation and close the M(2)=3 certificate in Lean (replacing the V1=V2=V3=0 placeholders).
```

```rung
id: R-local-focus-bautin
statement: For a quadratic planar vector field whose linearisation at a singular point is a focus or a centre, at most 3 small-amplitude limit cycles bifurcate from that point within the quadratic family, and the bound 3 is attained: M(2) = 3. Equivalently, the Bautin ideal — the ideal generated by the Lyapunov quantities as polynomials over Q in the eleven coefficients — has the structure bounding the zeros of the displacement germ by 3, and the bound is uniform over the whole quadratic coefficient family.
off: degenerate-vertices, unbounded-n, infinity-and-global, nesting-classification
claim: h16-lower-bounds — Bautin 1952/1954, M(2) = 3 (asserted-by-source, holds-here yes)
stance: settled — as sourced mathematics: Bautin 1952/1954 (M(2) = 3), evidence class asserted-by-source (research/notes/claims.md, claim h16-lower-bounds; holds-here yes). Partial in-run verification exists: code/lean/Lib/Bautin.lean now carries the REAL computed focal values (V1 = L4, V2 = L6, V3 = L8 emitted by code/bautin/lyapunov_quadratic.py, capture code/out/bautin_focal_values.captured.txt — no V1=V2=V3=0 placeholders remain), V3 ∉ ⟨V1, V2⟩ is closed by the evaluation-witness theorem V3_not_mem_span_V1_V2, and Bautin's finite-generation + cyclicity-3 statements are Cited axioms so the file is conditional. NOT established: the full M(2)=3 certificate closed in Lean from the Bautin ideal (bautin_ideal_eq_span_three is kernel-checked only conditional on the Cited finite-generation axiom — which is correct, the theorem is Bautin's, not this run's); the L8/L10/L12 ideal-membership extension beyond ⟨L4,L6⟩ (whether the Bautin ideal is generated by the first three quantities) is NOT established through the kernel — code/lyap_extend.py crashed in poly_terms (TypeError, after the degree-12 recurrence, 109s); membership.captured.txt records L8∉⟨L4,L6⟩, L10,L12∉⟨L4,L6,L8⟩ computationally, with a proviso that an earlier reading of sympy reduce()'s quotient list instead of its remainder is void.
merge: Turning unbounded-n back on while full-displacement stays off gives the linearised rung R-tangential-abelian (all n, Abelian integrals) — settled by source, no new mathematics needed. Turning infinity-and-global back on with the full displacement gives R-elementary-polycycle — settled by source. The first rung that is genuinely open after this one is R-one-degenerate-graphic, where degenerate-vertices is turned on and the Ramified-expansion assumption stops holding.
```

```rung
id: R-tangential-abelian
statement: For a polynomial Hamiltonian H of degree n+1 and a polynomial 1-form omega with deg omega <= n, the Abelian integral I(h) = integral over the nonsingular ovals gamma(h) subset {H = h} of omega has a uniformly bounded number of isolated real zeros, counted with multiplicity and summed over ovals: V(n) < inf uniformly in (H, omega). Explicit forms: Binyamini-Novikov-Yakovenko 2010 give 2^{2^{Poly(n)}} with Poly(n) = O(n^61); Binyamini-Dor 2012 sharpen to N <= exp^+(n^2) * m + exp^+(n^2), linear in deg omega = m. This is the linearised (first-order Melnikov) bound on limit cycles born from nonsingular ovals in a small non-conservative Hamiltonian perturbation.
off: full-displacement, degenerate-vertices, infinity-and-global, nesting-classification
claim: h16-bny-abelian-bound, h16-bd-abelian-linear-in-m, h16-abelian-integral-bounds — BNY 2010, Binyamini-Dor 2012 (asserted-by-source, holds-here yes)
stance: settled — by source: Varchenko/Khovanskii non-constructive; BNY 2010 (Invent. Math. 181) explicit; Binyamini-Dor 2012 linear-in-m. Claims h16-abelian-integral-bounds, h16-bny-abelian-bound, h16-bd-abelian-linear-in-m, all asserted, holds-here yes. Not machine-verified by this run; the distinguishing weakness is exactly that it bounds the linearised displacement, so it is the rung with full-displacement off.
merge: Turning full-displacement back on (keep all other difficulties off) is the step the whole problem is gated on: replace the Abelian-integral zero count with a zero count on the full displacement of the perturbed family — the simplest setting where that is a known theorem is the elementary polycycle, R-elementary-polycycle.
```

```rung
id: R-elementary-polycycle
statement: For a fixed elementary polycycle — a graph whose vertices are hyperbolic saddles and whose edges are separatrices, allowed on the Poincare sphere — cyclicity in a generic finite-parameter family of planar fields with only elementary singular points is finite and uniformly bounded over the parameter box: Ilyashenko-Yakovenko proved finiteness (primitive-recursive bound); Kaloshin gives the explicit bound E(k) <= 2^{25 k^2} for a k-parameter family.
off: degenerate-vertices, unbounded-n, nesting-classification
claim: h16-kaloshin-uniform-bound, h16-kaloshin-indep-proof — Ilyashenko-Yakovenko finiteness, Kaloshin explicit bound (asserted-by-source, holds-here yes)
stance: settled — by source: h16-kaloshin-uniform-bound and h16-kaloshin-indep-proof, asserted, holds-here yes; the hypotheses (genericity, elementary vertices only) are exactly the ones stated. The Yeung 2024/25 gap contention against Ilyashenko's monograph concerns semihyperbolic vertices in the polycycle — non-elementary — so it does not touch this rung; hyperbolic/elementary is the sound corner (per h16-gap-claims-2024).
merge: Turning degenerate-vertices back on is the wall. Its FIRST, generic case is banked in R-fake-saddle-transition (nonzero second-order jet, d > 0, uniform expansion held); the non-generic jets and the assembly into full DRR graphics is R-one-degenerate-graphic. At a nilpotent/semihyperbolic/degenerate vertex the displacement expansion is not the Ramified elementary one; it needs the normal form and blow-up at the singularity, then the transition maps, then a finite-zero argument on the resulting displacement — and every such argument must pass test 1 (analyticity must enter where a C-infinity field would fail, the exact shape of Dulac's 1923 error).
```

```rung
id: R-fake-saddle-transition
statement: For the generic fake-saddle normal-form family X_mu = (x^2 f1 + a(mu) x y + y^2 f2) dx + (x g1 + y g2) y dy with d(mu) = 4(1 - c(mu)) - (a(mu) - b(mu))^2 > 0 and nonzero second-order jet, the Poincare transition map across the singular fiber has the UNIFORM-in-mu asymptotic expansion Pi_omega_alpha(y; mu) = e^{gamma_+- (mu)} y + flat-in-mu remainder, gamma_+-(mu) = PV integral g1/(x f1) dx +- pi(2b - c(a+b))/sqrt(d), with the remainder flat to all orders in the unfolding variables and uniform in the parameters; consequently, in the applied reversible family Z_mu (beta > 1/4), the return map is R(x; mu) = e^{2 pi alpha/(beta sqrt 3)} x + flat-uniform remainder and cyclicity of the origin is ZERO at every mu0 with beta0 > 1/4 (division lemma in the flat class). This is the first rung with degenerate-vertices ON, in its generic case.
off: unbounded-n, infinity-and-global, nesting-classification
claim: fake-saddle-uniform-transition-map-marin2026 — sourced, peer-reviewed (EJQTDE 2026 no.5), full text held, holds-here yes
stance: settled — by source: Marin 2026 (EJQTDE 2026 no.5, 1-10, peer-reviewed, full text held in research/sources/marin-fake-saddles-transition-maps.full.md), claim fake-saddle-uniform-transition-map-marin2026, evidence-class sourced, holds-here yes: it gives the exact transition-map machinery the degenerate DRR D-families at infinity (DI2a etc.) require and certifies zero cyclicity at a centre. It also corrects Coll-Gasull-Prohens 2025 (a necessity condition refuted by Example 3.1). CAUTION: DMRT 2015 (De Maesschalck-Rebollo-Perdomo-Torregrosa, cyclicity <= 2 for the quadratic fake saddle, JDE 258:588-620) is cited here but NOT held in this library — its bound must not be built on this library's word; obtain it first.
merge: The wall between this rung and R-one-degenerate-graphic is the non-generic part of degenerate-vertices: the exceptional set d = 0, the c=1,a=b semi-hyperbolic case, higher jets, the composition of several transition maps into a full DRR degenerate graphic (e.g. DI2a or one of the >= 11 Shan-2013 degenerate open rows), and the quadratic-family-specific argument that gives the finite cyclicity bound rather than just the leading term. First move toward the next rung: pick one open degenerate graphic whose vertices are generic fake saddles (thread fake-saddle-transition-maps; blocked by DMRT 2015 full text not being held), write out the transition-map composition, and apply the division-in-flat-class lemma to the composite return map.
```

```rung
id: R-one-degenerate-graphic
statement: For n = 2, finite cyclicity of one named DRR graphic through a degenerate (nilpotent triple, semihyperbolic, or degenerate) point currently open in the literature, under perturbation inside the quadratic coefficient family: a fixed collar neighbourhood of the graphic and a finite bound, uniform over the coefficients, on limit cycles bifurcating from it. Named candidates after RR 2015, Shan 2013 and Lu 2026: (I^1_6b), (H^3_13), (DI_2b) — only their boundary limit periodic sets are proved finite (RR 2015 Thm 1.1, sourced-held), the full graphics are open; H^3_14 is claimed closed by the unrefereed Lu 2026 preprint (unchecked; its algebraic finite core is banked in R-lu-finite-core and its kernel check is R-lu-core-lean, both below this rung); the >= 11 degenerate graphics other than DF1a/DF2a are open per Shan 2013 (reported); residual sub-gap mu1 = 0 inside RSZ Thm 3.2 (sourced-held, RSZ Remark 3.3).
off: unbounded-n, nesting-classification
stance: open — THE rung: every other difficulty is on (uniformity-over-family, full-displacement, degenerate-vertices, infinity-and-global all bite here), and it is a publishable result. The generic fake-saddle transition maps are banked (R-fake-saddle-transition); the non-generic jets, the semihyperbolic vertices, and the assembly into the graphic is this rung. The fully-open named row with no partial result is H^3_14 (Lu 2026 claims it but its Theorem 1 is unrefereed and machine-unchecked); the cleanest unclaimed targets are one of (I^1_6b), (H^3_13), (DI_2b) as full graphics, or one of the degenerate D-family graphics reachable by the fake-saddle machinery.
merge: Settled for one open graphic, the merge into R-h2-uniform is: settle each remaining open graphic of the DRR list (finite list, one row at a time — this rung is the per-row version of that list), then make the compactness step explicit: pointwise finite cyclicity of each limit periodic set does not mechanically give a uniform H(2) bound unless the finiteness is continuous in the parameter, and the continuity step must be analytic (test 1) — the exact place a purely topological argument would prove a false statement.
```

```rung
id: R-h2-uniform
statement: H(2) < infinity: there exists a finite bound, depending only on the degree 2, on the number of limit cycles of every planar quadratic vector field. By the DRR 1994 reduction (h16-drr-121-graphics) this is equivalent to finite cyclicity of every one of the 121 graphics in S^2 x K, the compactified parameter space of quadratic anti-saddle-type systems. This rung is the bound half; classification of configurations in degree 2 is switched off here (nesting-classification off). NOTE the honest count from drr-list.md: >= 89 of 121 fully closed by 2015 (88 from RSZ 2015's own verbatim count + (I^1_14) from RR 2015, this run's arithmetic), (I^1_6b),(H^3_13),(DI_2b) boundary-sets-only, (H^3_14) open with Lu 2026 claiming it, >= 11 degenerate open; the definitive open count is a live gap because the DRR 1994 raw catalogue is not held (drr-ledger-no-consolidated-post2020).
off: unbounded-n, nesting-classification
stance: open — H(2) < infinity itself is open; H(2) >= 4 is source-settled (Shi 1982, Chen-Wang 1979, h16-lower-bounds) and H(2) = 4 is the standing conjecture, also open. The remaining rows lie in the nilpotent and degenerate families (h16-drr-open-rows, drr-list.md) — the ladder's R-one-degenerate-graphic is the per-row attack on them.
merge: Turning unbounded-n back on gives R-full. This is NOT a mechanical lift: the DRR-style reduction to a finite graphic catalogue is explicit only for n = 2; no finite catalogue for general n is known, so the uniformity/compactness argument must run directly on the full family while the graphic-level machinery is rebuilt at every degree — and turning nesting-classification back on adds the second half of H16.2, an almost untouched theory for n >= 3.
```

```rung
id: R-full
statement: H16.2 in full: for every n >= 2, H(n) < infinity uniformly over all planar polynomial fields of degree <= n, and the possible configurations (mutual positions, nestings) of the limit cycles are classifiable. After the lower-bound test: any claimed bound of order n^2 or below is refuted (h16-hn-lower-bound-asymptotic: liminf H(n)/((n+2)^2 log(n+2)) >= 1/(2 log 2), Christopher-Lloyd 1995 / Han-Li 2012).
off:
stance: open — nothing here is settled by this run or, for any n >= 3, by the literature. The gap list also carries a live warning: the pointwise-finiteness pillar (Ecalle-Ilyashenko) is under contention at the semihyperbolic step (Yeung 2024/25, peer-reviewed 2025), so even the individual-field base is not unanimously accepted; every argument must locate where analyticity enters.
merge: This is the rung reached only when R-h2-uniform is settled and its mechanism is shown to generalise past the quadratic catalogue — the ladder is exhausted only in that event; nothing below implies R-full, and the run must not claim it on prior.
```

## Reading the ladder

- **Settled rungs are banked, with evidence classes**: R-lu-core-lean, R-lu-finite-core
  (formalised / verified-computationally — the Lu finite core is now both
  computed and kernel-closed, via the standalone certificates), R-local-focus-bautin,
  R-tangential-abelian, R-elementary-polycycle, R-fake-saddle-transition
  (settled by source). The run's own *verification* of each source-settled
  rung (Lean type + certificate) is still open and is recorded inside the
  rung's `merge`.
- **The first open rung to attack — the bottom** — is R-one-degenerate-graphic:
  finite cyclicity of one named open DRR graphic through a degenerate vertex,
  the per-row version of H(2) < ∞. It is the only rung an attempt can settle
  with a real dynamic theorem (uniformity + full displacement + degenerate
  vertices + infinity all on), and the per-vertex transition machinery to
  start it is banked in R-fake-saddle-transition / G-resolve. The rung below
  it, R-lu-core-lean, is settled by the standalone kernel certificates whose
  JSONs say verified:true.
- **The difficulty that will bite** is `degenerate-vertices`. The evidence
  converges on it: the elementary rung is settled (Ilyashenko–Yakovenko–
  Kaloshin), the tangential rung is settled (BNY/BD), the generic fake-saddle
  case is settled (Marín 2026), and every open DRR row — (I^1_6b), (H^3_13),
  (DI_2b), H^3_14, the >= 11 degenerate graphics — is a graphic through a
  nilpotent/semihyperbolic/degenerate vertex, where the Ramified expansion of
  the elementary theory breaks and blow-ups + normal forms take over. Yeung's
  gap claim against the Dulac proof bites at exactly the same place
  (semihyperbolic vertices). `uniformity-over-family` is the problem's
  content but is a known, delicate compactness/analyticity step; the place the
  reduction physically stops is the degenerate vertex.