# Backward skeleton — finite cyclicity of the open degenerate DRR graphics

The DRR frame (claim `drr-1994-citation-anchor`) folds H(2)<∞ to finite cyclicity
of 121 graphics. The ledger's open rows are ~15: the full graphics (I¹₆b),
(H³₁₃), (DI₂b) (RR 2015 closed only boundary limit periodic sets), (H³₁₄) (Lu
2026 preprint claims it — skeleton `h16-2-h14-3-finite-cyclicity`), and the 11
degenerate graphics with a line of singular points. This file decomposes the
degenerate class — the one open family with **no backward skeleton**, and the
one whose closure template (DR 2009: normal forms + family blow-up + slow
divergence integral; Huzak 2018: the P\* closure for DF₂a) is held in full
text.

```skeleton
goal: cycl(Λ) < ∞ for every degenerate DRR graphic Λ in the open set {DF1b, DF2b, DH1, DH2, DI1a, DI1b, DI2a, DI2b, DH3, DH4, DH5} — the 11 degenerate rows the literature leaves open (only DF1a, DF2a closed), uniformly over the quadratic family.
implies: Each Λ is one row of the 121-graphic conjunction that is H(2)<∞ (frame skeleton h16-2-finite-cyclicity; DRR 1994 via drr-1994-citation-anchor). The class collapses onto DR 2009's three normal-form families (Props 2.1/2.2/2.3, held full text): Prop 2.1 finite-plane line (2.2): DF1b, DF2b, DH1, DH2; Prop 2.2 line at infinity (2.8): DI1a, DI1b, DI2a, DI2b, DH3, DH4; Prop 2.3 two lines (2.14, 7 parameters): DH5. For each family F: G-degenerate-normal-forms fixes the unfolding and the invariant line/equator plus contact point on which the displacement is measured; G-degenerate-slow-divergence bounds the displacement's zeros on the desingularized generic strata — the derivative is C∞ contact-equivalent to a development whose leading term is the slow divergence integral, so the SDI's zeros bound the cycles (DR 2009 Thm 3.1 shape: ≤3 DF1a generic, ≤5 DF2a center, ≤1 under sign conditions); G-degenerate-pstar-and-center closes the residual strata — identically-zero-SDI center strata via parameter blow-up near the center conditions plus the Darboux-integrability next-order term, and the non-desingularizable P* point by the closure technique Huzak 2018 used for DF2a. The three strata partition the compact parameter box of F, so the max of the three bounds is cycl(Λ) ≤ B for each Λ in F; the max over the 11 graphics is the class bound. DI2a is the concrete first instantiation: partial treatment held (ADL 2009, strip of hyperbolas, GSPT + Bautin ideal + Darboux integrability), normal form (2.8), and DR 2009 records ADL hit the same desingularization obstruction there.
killed-by: (1) The DI2a P*-analog proving non-desingularizable in a way Huzak's DF2a technique does not port — then G-degenerate-pstar-and-center fails and the row stays open; DR 2009's expectation that its method 'can be used for the other degenerate graphics... especially for (DH5)' is an expectation, not a theorem. (2) A G-degenerate-slow-divergence that never computes the actual SDI of (2.8): a generic 'slow divergence machinery applies' statement with no explicit integral and no vanishing-strata audit bounds nothing. (3) Claiming the class closed from DF1a/DF2a alone: the normal forms are shared but the SDI, center strata and P* point are per-family computations; DH5 additionally needs the 7-parameter normal form (2.14) before any gap can start.
rests-on: drr-1994-citation-anchor (DRR frame); drr-DI2a-partial-only (11-open enumeration, ADL-partial-only); drr-huzak-df2a-hypotheses-limited (P* closure precedent); DR 2009 full text research/sources/dumortier-rousseau-2009-degenerate-graphics-cpaa.full.md (Props 2.1-2.3, family blow-up (4.1), Thm 3.1, P* obstruction); demaesschalck-dumortier-detectable-canard-2011 (SDI-derivative machinery at singular slow dynamics)
status: sketched
```

```gap
id: G-degenerate-normal-forms
lemma: For the three DR 2009 normal-form families, the quadratic family near
       the degenerate graphic reduces, by an affine change of coordinates and
       time scaling depending analytically on the parameters, to the 5-
       parameter unfoldings (2.2) [finite-plane line: ẋ = y+bxy−y²+µ1+µ2x+µ3x²,
       ẏ = xy+µ4, b∈(−2,2)], (2.8) [line at infinity: ẋ = cx−y+1+(1+µ2)x²
       +µ1xy+µ0y², ẏ = xy−µ3x², c∈(−2,2)], (2.14) [two lines, 7 parameters:
       ẋ = xy(1+µ4)+µ0+µ1x+µ2x²+µ3y², ẏ = −y+y²−µ6x²+(µ2−µ5)xy], fixing the
       invariant line/equator, the contact point, and the compact parameter
       box on which the displacement is studied. Proved in DR 2009 Props
       2.1–2.3 (held full text). FILED as claim g-degenerate-normal-forms
       (conditional; formalisation:
       code/lean/h16_2_degenerate_graphics_finite_cyclicity_G_degenerate_normal_forms-71af02d5.lean,
       lean_check outcome: conditional, no sorries; 8 transcription theorems
       kernel-verified — µ=0 restriction to (2.1)/(2.7)/(2.13), singular/
       invariant axis, focus/center at (0,1)).
status: open
next: tool_builder + scholar: (1) verify the DI2a reduction to (2.8)
       symbolically over Q with sympy on the ADL strip-of-hyperbolas stratum
       (the affine reduction map (2.10) + the scalings), capture to
       code/out/di2a_normal_form.captured.txt; (2) advance the sibling gap
       G-degenerate-slow-divergence, which consumes this node's fixing data.
```

```gap
id: G-degenerate-slow-divergence
lemma: On the desingularized charts of the family blow-up at the contact point
       of a normal-form family, the displacement map's derivative is C^∞
       contact-equivalent to a development whose leading term is the slow
       divergence integral; wherever that integral is not identically zero, the
       displacement has at most B zeros with B read off the SDI (the DR 2009
       Thm 3.1 shape: ≤3 cycles for DF1a generic, ≤5 for the DF2a center case,
       ≤1 under sign conditions). For DI2a this means concretely: the SDI of
       the family (2.8) on the strip-of-hyperbolas stratum is computed
       explicitly, its zeros bound the limit cycles on the generic strata, and
       the strata where it vanishes identically are identified — that list is
       exactly the input to G-degenerate-pstar-and-center. This is the gap
       where the zero count is actually obtained: a generic invocation of
       "slow divergence machinery" with no computed integral bounds nothing.
status: open
next: tool_builder + symbolic_math, today: port the DR 2009 §4 family blow-up
       (4.1) computation — charts, center manifold (4.5), the SDI — from the
       DF1a/DF2a family (3.1) to the DI2a family (2.8), exact in sympy over Q;
       validate the port by reproducing the DF1a/DF2a SDI first (live check
       against the held text, DR 2009 §4), capture to
       code/out/di2a_slow_divergence.captured.txt, and report the vanishing
       strata explicitly.
```

```gap
id: G-degenerate-pstar-and-center
lemma: The residual strata of each normal-form family are bounded. (i) Center
       strata where the SDI vanishes identically: closed by the parameter
       blow-up near the center conditions plus the Darboux-integrability
       next-order term — for DI2a, the unperturbed system (2.7) has a first
       integral whose level sets (the ADL strip of hyperbolas) organize the
       strata. (ii) The non-desingularizable point P\*, the DI2a analogue of
       (D,E0,E1,E2)=(0,0,0,1) that DR 2009 could not desingularize for
       DF1a/DF2a and Huzak 2018 closed for DF2a; DR 2009 records that ADL
       encountered the same obstruction on DI2a, so DI2a's P\* needs the same
       closure ported to (2.8). This is the genuinely new analysis of the
       skeleton, and the step where a purely smooth/phase-plane argument would
       fail: the P\* closure and the center-strata control must use the
       polynomial/analytic structure of the displacement coefficients (the
       Bautin-ideal parameter blow-up) or the Darboux first integral.
status: open
next: three concrete moves, in order. (1) Compute the Darboux first integral of
       the unperturbed DI2a system (2.7) exactly over Q with sympy and check
       its level sets against the ADL strip-of-hyperbolas account in
       research/summaries/artes-dumortier-llibre-DI2a-hyperbolas.md (ADL full
       text is not held; the check is against DR 2009's description). (2)
       Locate DI2a's P\*-analog: run the family-blow-up desingularization
       condition (the E0=D=0-type obstruction of DR 2009 §4.1) on (2.8) and
       record the parameter point where the family cannot be desingularized.
       (3) Validate the port: reproduce Huzak's DF2a P\* closure structure
       (slow-fast Hopf / SDI-with-derivative) on the DF2a family first — a
       technique that does not reproduce on DF2a is not ready for DI2a.
```

**How the gaps recombine (the `implies` spelled out).** The DRR frame gives
H(2)<∞ ⇔ (∀ 121 graphics Λ) cycl(Λ)<∞. The degenerate class is 11 of the ~15
open rows. DR 2009 proves (Props 2.1–2.3, held) that three normal forms cover
all 13 degenerate graphics, so the class-level inference is: for each normal-
form family F, (normal-forms[F] ∧ slow-divergence[F] ∧ pstar-center[F]) ⇒ every
graphic of F has finite cyclicity. The three gaps partition the parameter box:
the SDI bound covers the generic strata, the center lemma covers the
identically-zero strata, the P\* lemma covers the non-desingularizable point;
each stratum's bound is uniform over its (compact) part of the box by
construction, and the max is the family bound. DI2a is the first instantiation
because it is the one open degenerate graphic with a held partial treatment
(ADL 2009) and its normal form (2.8) is written out in the held text.

**Tests applied.** Test 1: the zero bounds come from the SDI leading-term
control and, at the residual strata, from the Bautin-ideal/Darboux structure —
a purely topological or C^∞ phase-plane argument has no such control and is
refuted; the P\* closure is where this must be checked most carefully. Test 2:
finite cyclicity is a finiteness statement, not a sharp count; H(2)≥4 and
H(n)≳n²log n do not threaten it. Test 3: slow–fast is the method itself here
(the SDI is a slow–fast object), so the canard regime is inside the analysis,
not a separate counterexample mode.
