# Ladder of weakened targets — H16.2 (Hilbert's 16th, part II)

Written by the weakener against the full-strength goal in `GOAL.md` /
`problem.md`, with the claims library (`search_claims`, `research/notes/claims.md`,
`research/drr-list.md`) checked before any rung was called open. Rungs are
ordered weakest first; a rung marked `settled` is established — with the
evidence class stated — and is banked, never re-attacked from scratch.

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
3. `unbounded-n` — the degree n varies; an explicit reduction to a finite
   graphic catalogue exists only for n = 2 (DRR 1994, 121 graphics).
4. `full-displacement` — the displacement function is nonlinear; Melnikov /
   Abelian-integral (linearised) zero counts do not bound its zeros.
5. `infinity-and-global` — limit periodic sets at infinity on the Poincare
   sphere; the equatorial objects must be included and compactified.
6. `nesting-classification` — the second half: which configurations (nestings)
   of k limit cycles are realisable in degree n; almost untouched for n >= 3.

```rung
id: R-lu-finite-core
statement: For the source-normalized H14^3 hemicycle field x' = -y - d x + B(x^2 - y^2), y' = (1+y)(x + d y), and the quadratic-focus rotation recurrence, the following finite algebraic identities hold exactly over Q[symbols]: (i) bridge identities tau = a + c, ell = -alpha, sigma = gamma, beta = tau + ell with a = mu4 + B mu5, c = (1-2B) mu5, alpha = c - d, beta = a + d, gamma = d(B + mu2), tau = mu4 + (1-B) mu5, ell = d - c, sigma = gamma; (ii) Darboux cofactor identities X(L) = (x + d y) L for L = 1 + y, X(F) = (2 B x + d y) F for F = B(B-1)x^2 - B d x y - B^2 y^2 - d(2B-1)x + (d^2 - 2B)y + d^2 - 1, and div X = (x + d y) + (2 B x + d y) (so 1/(L F) is an inverse integrating factor); (iii) the degree-4 Bautin rotation obstruction 8 L4 = A C + C D + 2 D F - E F; (iv) the degree-6 relation 192 L6 + P30 = 0 with P30 the explicit 30-monomial polynomial. Settlement condition: a clean-room exact-sympy run (code/bautin/verify_lu_core.py), written from the paper's stated definitions without importing its scripts, asserting each identity on its produced data, captured to code/out/lu_core.captured.txt; and the identities closed by the Lean kernel over MvPolynomial — generated coefficient data as untrusted defs under code/lean/Lib/Generated/, hand-written checker in the theorem, decide = iff, no theorem inside Generated/.
off: uniformity-over-family, degenerate-vertices, unbounded-n, full-displacement, infinity-and-global, nesting-classification
stance: open — nothing verified-computationally exists. research/notes/lu-finite-core-verified.md is downgraded to UNVERIFIED (transcription only, no executed program, no capture); claim lu-finite-core-partially-verified is asserted-by-source (the paper's own certificates assert these) and holds-here is not yet yes. code/lyap_audit.py encodes the L4/L6/P30 identities and CONTEXT.md records a PASS, but no capture file is held in code/out/, so by this workspace's rule it is not reproducible verification. BautinRecurrence.lean still has P30 := 0, bautin_L4_identity := True, Divergence := 0 — the Lean side is a stub.
merge: Nothing is turned back on by the next rung; this rung is the certificate base for one hemicycle proof. The first rung with dynamics in it is R-local-focus-bautin: turning uniformity-over-family and full-displacement back on (n fixed at 2) means showing the displacement germ at a quadratic focus has at most 3 zeros uniformly in the coefficients — first move: run the exact Lyapunov/Bautin-ideal computation and close the M(2)=3 certificate in Lean (replacing the V1=V2=V3=0 placeholders).
```

```rung
id: R-local-focus-bautin
statement: For a quadratic planar vector field whose linearisation at a singular point is a focus or a centre, at most 3 small-amplitude limit cycles bifurcate from that point within the quadratic family, and the bound 3 is attained: M(2) = 3. Equivalently, the Bautin ideal — the ideal generated by the Lyapunov quantities as polynomials over Q in the eleven coefficients — has the structure bounding the zeros of the displacement germ by 3, and the bound is uniform over the whole quadratic coefficient family.
off: degenerate-vertices, unbounded-n, infinity-and-global, nesting-classification
claim: h16-lower-bounds — Bautin 1952/1954, M(2) = 3 (asserted-by-source, holds-here yes)
stance: settled — as sourced mathematics: Bautin 1952/1954 (M(2) = 3), evidence class asserted-by-source (research/notes/claims.md, claim h16-lower-bounds; holds-here yes). NOT verified by this run: code/lean/Lib/Bautin.lean has V1 = V2 = V3 := 0 placeholders so bautin_finitely_generated is vacuous and does not compile cleanly (CONTEXT gap 3); code/lyap_extend.py crashed in poly_terms (TypeError, after computing the degree-12 recurrence, 109s), so the L8/L10/L12 ideal-membership extension (whether the Bautin ideal is generated by the first three quantities, checked by Groebner) is NOT established — the failed attempt stays on the ladder as the reason not to re-propose the degree-8+ extension without fixing the recurrence driver.
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
merge: Turning degenerate-vertices back on is the wall: R-one-degenerate-graphic. At a nilpotent/semihyperbolic vertex the displacement expansion is not the Ramified elementary one; it needs the normal form and blow-up at the singularity, then the transition maps, then a finite-zero argument on the resulting displacement — and every such argument must pass test 1 (analyticity must enter where a C-infinity field would fail, the exact shape of Dulac's 1923 error).
```

```rung
id: R-one-degenerate-graphic
statement: For n = 2, finite cyclicity of one named DRR graphic through a degenerate (nilpotent triple, semihyperbolic, or degenerate) point currently open in the literature, under perturbation inside the quadratic coefficient family: a fixed collar neighbourhood of the graphic and a finite bound, uniform over the coefficients, on limit cycles bifurcating from it. Named candidates after RR 2015 and Lu 2026: (I^1_6b), (H^3_13), (DI_2b) — only their boundary limit periodic sets are proved finite (RR 2015 Thm 1.1), the full graphics are open; H^3_14 is claimed closed by the unrefereed Lu 2026 preprint (unchecked; its finite core is R-lu-finite-core, open); the >= 11 degenerate graphics other than DF1a/DF2a are open per Shan 2013; residual sub-gap mu1 = 0 inside RSZ Thm 3.2 (sourced-held).
off: unbounded-n, nesting-classification
stance: open — THE rung: every other difficulty is on (uniformity-over-family, full-displacement, degenerate-vertices, infinity-and-global all bite here), and it is a publishable result.
merge: Settled for one open graphic, the merge into R-h2-uniform is: settle each remaining open graphic of the DRR list (finite list, one row at a time — this rung is the per-row version of that list), then make the compactness step explicit: pointwise finite cyclicity of each limit periodic set does not mechanically give a uniform H(2) bound unless the finiteness is continuous in the parameter, and the continuity step must be analytic (test 1) — the exact place a purely topological argument would prove a false statement.
```

```rung
id: R-h2-uniform
statement: H(2) < infinity: there exists a finite bound, depending only on the degree 2, on the number of limit cycles of every planar quadratic vector field. By the DRR 1994 reduction (h16-drr-121-graphics) this is equivalent to finite cyclicity of every one of the 121 graphics in S^2 x K, the compactified parameter space of quadratic anti-saddle-type systems. This rung is the bound half; classification of configurations in degree 2 is switched off here (nesting-classification off).
off: unbounded-n, nesting-classification
stance: open — H(2) < infinity itself is open; H(2) >= 4 is source-settled (Shi 1982, Chen-Wang 1979, h16-lower-bounds) and H(2) = 4 is the standing conjecture, also open. 88 of 121 graphics closed by RSZ 2015, 89 with (I^1_14) (RR 2015); the remaining rows lie in the nilpotent and degenerate families (h16-drr-open-rows, drr-list.md) — the ladder's R-one-degenerate-graphic is the per-row attack on them.
merge: Turning unbounded-n back on gives R-full. This is NOT a mechanical lift: the DRR-style reduction to a finite graphic catalogue is explicit only for n = 2; no finite catalogue for general n is known, so the uniformity/compactness argument must run directly on the full family while the graphic-level machinery is rebuilt at every degree — and turning nesting-classification back on adds the second half of H16.2, an almost untouched theory for n >= 3.
```

```rung
id: R-full
statement: H16.2 in full: for every n >= 2, H(n) < infinity uniformly over all planar polynomial fields of degree <= n, and the possible configurations (mutual positions, nestings) of the limit cycles are classifiable. After the lower-bound test: any claimed bound of order n^2 or below is refuted (h16-hn-lower-bound-asymptotic: liminf H(n)/((n+2)^2 log(n+2)) >= 1/(2 log 2), Christopher-Lloyd 1995 / Han-Li 2012).
off:
stance: open — nothing here is settled by this run or, for any n >= 3, by the literature. The gap list also carries a live warning: the pointwise-finiteness pillar (Ecalle-Ilyashenko) is under contention at the semihyperbolic-step (Yeung 2024/25, peer-reviewed 2025), so even the individual-field base is not unanimously accepted; every argument must locate where analyticity enters.
merge: This is the rung reached only when R-h2-uniform is settled and its mechanism is shown to generalise past the quadratic catalogue — the ladder is exhausted only in that event; nothing below implies R-full, and the run must not claim it on prior.
```

## Reading the ladder

- **Settled rungs are banked, with evidence classes**: R-local-focus-bautin,
  R-tangential-abelian, R-elementary-polycycle are settled **by source**
  (asserted-by-source, holds-here yes) — not by this run's computation. The
  run's own *verification* of each (Lean type + certificate) is still open and
  is recorded inside the rung's `merge`.
- **The first open rung to attack** is the bottom: R-lu-finite-core. It is the
  only rung an attempt can settle in a single turn (pure polynomial algebra,
  exact sympy + Lean `decide`), and the run currently carries an *unverified*
  claim — `lu-finite-core-partially-verified` — in its ledger that names these
  identities as holding. Everything downstream of Lu 2026's H^3_14 claim rests
  on it.
- **The difficulty that will bite** is `degenerate-vertices`. The evidence
  converges on it: the elementary rung is settled (Ilyashenko–Yakovenko–
  Kaloshin), the tangential rung is settled (BNY/BD), and every open DRR row —
  (I^1_6b), (H^3_13), (DI_2b), H^3_14, the 11 degenerate graphics — is a graphic
  through a nilpotent/semihyperbolic/degenerate vertex, where the Ramified
  expansion of the elementary theory breaks and blow-ups + normal forms take
  over. Yeung's gap claim against the Dulac proof bites at exactly the same
  place (semihyperbolic vertices). `uniformity-over-family` is the problem's
  content but is a known, delicate compactness/analyticity step; the place the
  reduction physically stops is the degenerate vertex.