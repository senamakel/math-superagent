# Claims established by the reference library — Hilbert 16th, limit cycles

Each fenced `claim` block below is read into `derived/CLAIMS.md`. Status labels:
`sourced` = asserted-by-source (held full text or verified abstract); nothing
here is proved in this run. Evidence class, the exact source, and a falsifier
are given for each.

```claim
id: h16-dulac-finiteness-theorem
status: sourced
statement: A planar polynomial vector field has only finitely many limit
  cycles; the same holds for an analytic vector field on the 2-sphere. Proved
  independently by Ilyashenko (1991) and Écalle (1992), after Ilyashenko found
  ~1981 the gap in Dulac's 1923 proof.
hypotheses: individual field fixed (no uniformity in coefficients).
evidence-class: sourced (Ilyashenko, "Centennial History of Hilbert's 16th
  Problem", Bull. AMS 39 (2002) 301-354, held in full in
  research/sources/ilyashenko-centennial-history-h16.full.md)
falsifier: a published, refereed disproof — see below, the 2024 preprints
  claim exactly this for Ilyashenko's *approach*.
holds-here: yes as the classical received statement; see the separate claim on
  the 2024 gap claims, which put the *proof*, not the theorem, under question.
```

```claim
id: h16-gap-claims-2024
status: sourced
statement: The gap claim in Ilyashenko's approach to Dulac's finite-limits
  theorem is now made in PEER-REVIEWED form: Yeung, "Dulac's Theorem
  Revisited", Qual. Theory Dyn. Syst. 24 (2025) Art. 57,
  doi:10.1007/s12346-025-01220-2 (held full text), asserts the approach of
  Ilyashenko (1991 monograph) has a gap — the argument that its asymptotics
  are not themselves oscillatory is insufficient — gives an explicit
  counterexample, and draws confines to which Ilyashenko's result may be
  restricted to keep validity. Preprint precursors: Yeung arXiv:2402.12506
  (held full HTML), Palma-Márquez–Yeung arXiv:2410.07532 (maximum-modulus
  dichotomy, partial repair); Yeung arXiv:2409.13630 proves a specific
  hyperbolic-polycycle case in Ilyashenko's style. The classical *theorem*
  (finitely many limit cycles) is not claimed false; the *published proof's
  completeness* is under active contention, and hyperbolic polycycles remain
  the fully-understood corner stone.
hypotheses: These are the current (2024-2025) claims in the field. The 2025
  paper is peer-reviewed; the 2024 arXiv precursors are not. No Ilyashenko-side
  rebuttal located yet.
evidence-class: sourced (held full text of Qual. Theory 2025 in
  research/sources/yeung-dulac-theorem-revisited.full.md and of
  arXiv:2402.12506 HTML).
falsifier: a published refutation of the counterexample, or an independent
  verified completion of Ilyashenko's step; either side's community acceptance.
holds-here: this is live contention to report. It puts "finite limit cycles
  for a fixed field" at "settled modulo a contended proof" — directly relevant
  to GOAL.md's question of whether a complete proof of H(2)<∞ (or even of the
  individual finiteness statements it rests on) stands.
```

```claim
id: h16-bamon-quadratic-finiteness
status: sourced
statement: Bamón (1986), "Quadratic vector fields in the plane have a finite
  number of limit cycles", Publ. Math. IHÉS 64, 111-142,
  doi:10.1007/BF02699193 (held): each individual quadratic planar field has
  finitely many limit cycles. This is finiteness for a fixed quadratic field,
  NOT the uniform H(2) bound. Bamón used Ilyashenko's 1984/85 result on
  non-accumulation of limit cycles around hyperbolic singular cycles.
hypotheses: n=2, individual field.
evidence-class: sourced (bibliographic record + title/abstract held; relies on
  the Chile survey's account).
falsifier: a single quadratic field with infinitely many limit cycles.
holds-here: yes as individual-finiteness for n=2; it does NOT settle H(2).
```


```claim
id: h16-drr-121-graphics
status: sourced
statement: H(2) < ∞ is equivalent (via the compactness/DRR program of
  Dumortier, Roussarie and Rousseau 1994, J. Diff. Eq. 110, 86-133) to proving
  finite cyclicity of 121 graphics in S²×K, where K is the compactified
  parameter space of quadratic anti-saddle-type systems and S² the Poincaré
  sphere. Proving the (I¹₁₂), (I¹₁₃) graphics (Rousseau–Shan–Zhu 2015) brought
  the count of graphics with proved finite cyclicity to 88 of 121. Verified
  post-2015 closures include: degenerate graphics DF2a (Huzak 2018,
  CPA 17(3):1305-1316, family blow-up + slow divergence integral; DF1a was
  Dumortier–Rousseau 2009, CPA 8), and the center-surrounding triple-nilpotent
  graphics (I¹₁₄), (I¹₆b), (H³₁₃), (DI²b) with (H³₁₄) left open (Roussarie–
  Rousseau 2015, Moscow Math. J.). Free full-text account:
  Huzak 2018 "Cyclicity of degenerate graphic DF2a" starts from
  Dumortier–Rousseau 2009 "Study of the cyclicity of some degenerate graphics
  inside quadratic systems", CPA 8 (2009) 1133-1157.
hypotheses: n=2; graphics surround a nondegenerate singular point of
  anti-saddle type; parameter family compact.
evidence-class: sourced (Rousseau–Shan–Zhu arXiv:1502.00689 held full HTML;
  Huzak 2018 held full bibliographic + abstract; Roussarie–Rousseau 2015
  held abstract/text).
falsifier: a graphic of the 121 proved to have INFINITE cyclicity, or a
  complete proof of finite cyclicity for all 121 (none published); or a named
  open graphic like (H³₁₄) being closed or shown open in a later paper.
holds-here: yes. NOTE 121-vs-125 discrepancy (Shan 2013 thesis counts 125) —
  to be settled from the DRR 1994 paper itself.
```


```claim
id: h16-drr-closed-rows-2015
status: sourced
statement: As of the 2015 literature, at least 88 of the 121 DRR graphics have
  finite cyclicity proved inside the quadratic family (Rousseau–Shan–Zhu 2015
  state verbatim that proving (I₁₂¹),(I₁₃¹) "will bring the number of graphics
  of the program for which finite cyclicity is proved to 88"). Specific rows
  closed with their papers: (I₁₂¹),(I₁₃¹) — Rousseau–Shan–Zhu 2015,
  arXiv:1502.00689 (held full text: I₁₃¹ via Thm 4.3; I₉b² in the codim-3
  case via the same computation as I₁₂¹); (I₁₄¹) — Roussarie–Rousseau 2015,
  Trans. Moscow Math. Soc. Thm 1.2 (held full text). For (I₆b¹), (H₁₃³),
  (DI₂b) only the BOUNDARY limit periodic set from the blow-up is closed
  (RR 2015 Thm 1.1); the full graphics are left open ("intend to address the
  problem in the next future"), and (H₁₄³) is the one graphic through a triple
  point at infinity with no partial result (RR 2015 intro). Earlier (pre-2015,
  inside the 88): HR/nilpotent families Ji2, Ji3, Jb, fib (Zhu–Rousseau/Shan
  2013); nilpotent pp-type H₇¹, F₇a¹, H₁₁³, I₆a¹ (Roussarie–Rousseau 2008,
  cyclicity 2); DF1a, DF2a (Dumortier–Rousseau 2009; DF2a re-examined by Huzak
  2018).
hypotheses: n=2; graphics surround a nondegenerate anti-saddle point; finite
  cyclicity inside the quadratic coefficient family S²×K.
evidence-class: sourced (RSZ 2015 held full HTML; RR 2015 abstract/theorem
  text verified; pre-2015 rows confirmed via thesis/survey summaries only →
  those rows are `reported` in drr-list.md, not full-text-held).
falsifier: a held primary source giving a different closed-count, or a graphic
  here marked closed later shown still open (e.g. if DF2a was closed only in
  2018 rather than 2009, or if the RR-2015 "one open boundary set" is a
  specific named graphic that this block would then mis-label).
holds-here: yes at the level of "at least 88 by 2015" (author-stated) and the
  specifically named rows; NOT as a complete 121-row enumeration (that needs
  the DRR 1994 paper, which is not held).
```

```claim
id: h16-drr-open-rows
status: sourced
statement: The DRR program is NOT complete: at least 33 of the 121 graphics
  were still open as of RSZ 2015 (88 closed), and the open rows lie
  overwhelmingly in the nilpotent and degenerate families. Named open /
  partially-open rows: (i) (H₁₄³) — the one graphic through a triple point at
  infinity with no partial result in Roussarie–Rousseau 2015 (the primary text
  states "We have a partial result for every graphic, but one (namely (H₁₄³)),
  through a triple point at infinity");
  (ii) (I₆b¹), (H₁₃³), (DI₂b) — only their boundary limit periodic sets are
  closed (RR 2015 Thm 1.1); the full graphics are explicitly left open
  ("intend to address the problem in the next future");
  (iii) the 11 degenerate graphics other than DF1a, DF2a (Shan 2013 thesis).
  The exact full list of open graphic ids and the precise post-2015 open count
  are NOT established by any held source. The open count here is a lower bound
  on openness, not the exact number: at least 32 of 121 are not fully closed
  (after RR 2015's full closure of I₁₄¹ on top of RSZ's 88), plus 3 partially
  closed rows, and the one open sub-problem μ₁=0 in RSZ Thm 3.2.
hypotheses: n=2; finite cyclicity in the quadratic family.
evidence-class: sourced for "88 by 2015", "(H₁₄³) the one with no partial
  result", "boundary sets of I₆b¹,H₁₃³,DI₂b only" (RR 2015 primary text held);
  reported for the 11 degenerate open (Shan 2013 thesis).
falsifier: a held post-2015 primary source that closes one of the 11 degenerate
  graphics, or (I₆b¹)/(H₁₃³)/(DI₂b) fully, or (H₁₄³); or a complete proof of
  all 121 (none exists).
holds-here: yes as reported level; the exact open count remains the live gap
  for request dumortier-roussarie-rousseau-9c4f.
```

```claim
id: h16-drr-121-vs-125-discrepancy
status: reported
statement: The DRR catalog of quadratic graphics is usually stated as 121
  (DRR 1994; RSZ 2015; Ilyashenko 2002; RR 2015), but the Shan 2013 thesis
  summary counts 125 graphics "in the standard family around the origin" with
  40 challenging cases. The same program is being described with two totals.
  Whether this is a different grouping/vertex-counting convention or a
  genuinely different list is not resolved — the DRR 1994 paper itself (the
  canonical catalogue) is not held.
evidence-class: reported (secondary/thesis summaries; DRR 1994 full text not
  held).
falsifier: the DRR 1994 paper's own count, or a primary source that reconciles
  the two totals.
holds-here: recorded as an open discrepancy to resolve before any downstream
  attack trusts a single total.
```

```claim
id: h16-abelian-integral-bounds
status: sourced
statement: Tangential/infinitesimal H16: the number of isolated zeros of
  Abelian integrals (and so limit cycles born in a first-order perturbation of
  a Hamiltonian polynomial field) is uniformly bounded. Varchenko, Khovanskii
  non-constructive; Binyamini–Novikov–Yakovenko (2010, Invent. Math. 181)
  explicit double-exponential bound; Binyamini–Dor (2012) explicit bound
  linear in deg ω: N(n,m) ≤ exp⁺(n²)·m + exp⁺(n²).
hypotheses: deg H ≤ n+1, deg ω ≤ n; nonsingular ovals.
evidence-class: sourced (BNY arXiv:0808.2952, BD arXiv:1108.1846 held).
falsifier: an Abelian integral with more zeros than the bound for explicit
  small n,m.
holds-here: yes; this is the linearised problem, NOT H16.2 itself.
```

```claim
id: h16-kaloshin-uniform-bound
status: sourced
statement: Hilbert–Arnold problem for elementary polycycles: for a generic
  k-parameter family of smooth planar fields with only elementary singular
  points, cyclicity is finite with explicit bound E(k) ≤ 2^{25 k²} (Kaloshin);
  Ilyashenko–Yakovenko proved finiteness with a primitive-recursive bound.
hypotheses: elementary singularities only; generic finite-parameter family.
evidence-class: sourced (Kaloshin arXiv:math/0111053; Ilyashenko Centennial).
falsifier: a k-parameter family with elementary singularities producing more
  than the bound.
holds-here: yes; elementary is the weight-bearing hypothesis — nilpotent and
  degenerate points are outside it.
```

```claim
id: h16-lower-bounds
status: sourced
statement: H(2) ≥ 4 (Shi 1982; Chen–Wang 1979) with (3,1) configuration; H(2)=4
  is the standing conjecture but OPEN; H(3) ≥ 13 (Li–Liu–Yang 2009); H(4) ≥ 28
  (Prohens–Torregrosa 2018); M(2)=3 (Bautin 1952); M(3) ≥ 11 (Żołądek);
  H(n) grows at least as fast as (n+2)^2 log(n+2)/(2 log 2) — i.e. order
  n^2 log n — so H(n) is NOT bounded above by any quadratic polynomial in n.
  [CORRECTED 2025: the earlier "(n+2)^2/ln(n+2), order n^2/ln n" wording was
  a transcription inversion; the held full text of Buzzi-Novaes (2024), quoting
  Christopher-Lloyd 1995 and Han-Li 2012, has liminf H(n)/((n+2)^2 log(n+2))
  >= 1/(2 log 2), which is n^2 log n growth.]
hypotheses: none beyond degree.
evidence-class: sourced (abstracts/records of the named papers; M(2)=3 via
  Liang–Torregrosa held, and Kuznetsova survey).
falsifier: a certified configuration beating the stated bound for its degree.
holds-here: yes, as lower bounds. NOTE: the precise asymptotic constant and
  whether it is n² ln n or n²/ln n needs a primary source download (only
  abstract-level now).
```

```claim
id: h16-lienard-ldmp-disproved
status: sourced
note: attribution nuance (scholar, 2nd pass, per held Llibre-Zhang postprint
  pp. 2-3): DPR 2007's own contribution was n >= 7 (one extra cycle beyond the
  conjecture). The degree-6 system with 4 limit cycles is a base case in the
  survey's own proof (following De Maesschalck-Huzak 2015): I1(x)=0.4x^3
  -1.248x^5+1.17429x^7-0.3x^9 has exactly 3 positive zeros -> 4 cycles. The
  core claim (conjecture FALSE for n>=6) is unaffected; only the specific
  "degree-6 example from DPR 2007" attribution is loose.
statement: The Lins–de Melo–Pugh conjecture — classical Liénard ẋ=y−F(x),
  ẏ=−x with deg F = n has at most ⌊(n−1)/2⌋ limit cycles — is FALSE for
  n ≥ 6. A degree-6 f with 4 limit cycles exists (survey's own construction
  following De Maesschalck–Huzak 2015; DPR 2007's own paper established n ≥ 7
  with one extra cycle); later work gives ≥ n−2 cycles for n ≥ 6. n=5 was
  open as of Llibre–Zhang 2017 survey. The classic bound is achieved (not
  exceeded) by simple FSTS-canard families (De Maesschalck–Dumortier 2010).
hypotheses: classical Liénard form.
evidence-class: sourced (abstracts of DPR 2007, Dumortier–Llibre counterexamples,
  Llibre–Zhang survey). Full text of DPR 2007 NOT held (only AMS landing pages
  downloaded — see librarian report).
falsifier: a degree-n≥6 Liénard system with fewer than the claimed constructible
  count (does not exist) — this is instead a WARNING for the slow–fast test.
holds-here: yes as the received disproof.
```

```claim
id: h16-lienard-n5-open
status: sourced
statement: For the classical Liénard system the exact maximum number of limit
  cycles for degree n=5 was open as of the 2017 Llibre–Zhang survey: whether a
  degree-5 system can have more than ⌊(5−1)/2⌋=2 limit cycles was unknown.
evidence-class: sourced (Llibre–Zhang 2017 FULL postprint held in
  research/sources/llibre-zhang-lienard-survey-postprint-2017.full.md; the
  survey's open problem is verbatim "What is the maximum number of limit
  cycles for the Liénard differential systems (1) when n ≥ 5?" and Theorem 2
  leaves only n=5 undecided).
falsifier: a published determination of the degree-5 Liénard maximum after the
  survey.
holds-here: reported as open per the held source; needs a post-2017 check.
```

```claim
id: h16-drr-h14-3-lu-2026-claim
status: asserted-by-source
statement: H. Lu, "Local Uniform Finite Cyclicity of the H₁₄³ Semihyperbolic
  Hemicycle", arXiv:2607.13785 (Jul 2026, 80 pp., unrefereed preprint),
  claims finite cyclicity for exactly the (H³₁₄) graphic that Roussarie–
  Rousseau 2015 left open. The claim: for the full five-parameter quotient
  unfolding (1.3) (= RR 2015 Theorem 3.1's family (3.2) with B=0 the H₁₄³
  case), there is a fixed annual collar U of Γ_{H₁₄³}, a neighborhood Λ⊂ℝ⁵ of
  0, and a finite constant B such that every λ∈Λ has ≤ B isolated limit
  cycles in U. Bound existential, not explicit. Identification is source-
  backed from both sides: RR 2015 line 63 "We have a partial result for every
  graphic, but one (namely (H³₁₄))", and Lu's §1.2 citing RR Theorem 3.1
  B=0 as precisely the H₁₄³ case.
hypotheses: n=2; graphic through triple nilpotent point at infinity
  (semihyperbolic hemicycle, noncompact source, two semihyperbolic endpoints,
  upper-equatorial degeneration); full 5-parameter quotient unfolding.
evidence-class: asserted-by-source (PREPRINT, NOT peer-reviewed; full HTML
  held in research/sources/lu-h14-3-hemicycle-html.full.md; RR 2015 full text
  held; identification verified against both texts).
falsifier: peer review finding an error in the stopped-first-hit atlas or one
  of the zero theorems; a published counterexample; or rejection of the
  preprint. Also falsifiable if the paper's "local uniform finite cyclicity in
  one collar" turns out not to match DRR's definition of finite cyclicity of
  the graphic (needs DRR 1994, not held).
holds-here: as a claim to chase, NOT established. The library's recorded open
  graphic (H³₁₄) now has a candidate closure in preprint form, and the
  candidate has ancillary reproducibility code. Priority: verify.
```

```claim
id: h16-drr-lu-2026-does-not-complete-program
status: sourced
statement: Even if Lu 2026 is correct, the DRR program is not complete. The
  closure of (H³₁₄) is one graphic. As of RR 2015 the open/partially-open
  rows also include full graphics (I₆b¹), (H₁₃³), (DI₂b) (only boundary sets
  closed) and ≥11 degenerate graphics beyond DF1a/DF2a (Shan 2013). The
  consolidated post-2015 graphic-by-graphic ledger is still NOT in the
  library.
hypotheses: n=2.
evidence-class: sourced (RR 2015 held full text; Shan 2013 thesis held).
falsifier: a complete ledger showing a different set of open graphics.
holds-here: yes.
```

```claim
id: h16-four-cycles-songling-galias-tucker
status: sourced
statement: The Songling quadratic system — ẋ = λx − y − 10x² + (5+δ)xy + y²,
  ẏ = x + x² + (−25+8ε−9δ)xy with δ≈−10⁻¹³, ε≈−10⁻⁵², λ≈−10⁻²⁰⁰ — has
  EXACTLY four limit cycles, proved rigorously by interval arithmetic
  (adaptive precision, P-map fixed points, explicit positional bounds for all
  four cycles spanning scales from 10⁻⁷⁵ to ~0.04). Verified configuration
  (Fig. 2 caption): three of the four limit cycles surround the origin, the
  fourth surrounds the equilibrium (0,1) — i.e. the (3,1) configuration
  associated with Shi's H(2)≥4 example. The four are alternately stable /
  unstable (P'<1 / P'>1, P' extremely close to 1 for the three inner cycles).
  This is a certified computational reproduction of Shi's 1980 H(2) ≥ 4 lower
  bound, and a model oracle (trapping-region/return-map with certified sign
  change) for this run's own certifier.
hypotheses: H(2) ≥ 4 with a (not necessarily (1,3)) configuration; does not
  show the 4 cycles can be arbitrary; the exponential separation of scales is
  essential to the difficulty.
evidence-class: verified-computationally (rigorous, reflexive, interval)
  — full text held in research/sources/galias-tucker-songling-four-cycles.full.md.
falsifier: a flaw in an interval-arithmetic branch; a corrected count.
holds-here: yes — H(2) ≥ 4 is confirmed by a fully certified computation,
  stronger than the historical asserted lower bound.
```

```claim
id: h16-strong-monotone-gasull-santana
status: sourced
statement: H(n) is a strictly increasing function of the degree when finite:
  H(n+1) ≥ H(n) + 1 for all n ∈ N (Gasull–Santana, PAMS 153 (2025),
  669–677, arXiv:2407.13465). Also H(n) is realizable by structurally stable
  fields with only hyperbolic limit cycles (if finite), and H(n) ≤ ℵ₀.
hypotheses: none beyond plane polynomial fields of degree n.
evidence-class: sourced (postprint held full)
  — research/sources/gasull-santana-note-h16-pams-2025.full.md; peer-reviewed
  Proc. AMS 2025.
falsifier: a published error in the sup/inf argument; a family with
  H(n+1) = H(n).
holds-here: yes.
```

```claim
id: h16-christopher-lloyd-weakened-16th
status: sourced
note: PROVENANCE CORRECTED (scholar, 2nd pass) — the held full text is by
  Chengzhi Li, Weigu Li, Jaume Llibre, Zhifen Zhang (2001), not Christopher &
  Lloyd. Christopher & Lloyd 1995 ("Polynomial systems: a lower bound for the
  Hilbert numbers", Proc. R. Soc. Lond. A 450:219-224) is a DIFFERENT,
  paywalled paper giving the H(n) ≳ n² log n growth. The two were conflated
  by the librarian; the mathematical content of this claim (the b_{m,n}
  tangential bound at one singular point) is correct and belongs to the
  2001 Li-Li-Llibre-Zhang paper.
statement: Li-Li-Llibre-Zhang (2001), "Polynomial systems: a lower bound for
  the weakened 16th Hilbert problem", Extracta Math. 16(3), 441–447: for m, n
  odd, the maximum number b_{m,n} of isolated zeros (with multiplicity) of the
  Abelian integral I(h)=∮_{H=h} ȳQ dx with H = y²/2 + x^{m+1}/(m+1), deg Q ≤
  n−1 is at least ((n+1)(n+3)/8 − 1) if n ≤ m, and ((m+1)(2n−m+3)/8 − 1) if
  n ≥ m; hence b_{m,n} ≤ N(m,n) ≤ H(max{m,n}). Growth of order n². This is
  the primary (open-access) treatment of the tangential/weakened H16 lower
  bound at a single singular point.
hypotheses: m,n odd; Hamiltonian H as given; perturbation of the centre.
evidence-class: sourced (full text held)
  — research/sources/christopher-lloyd-weakened-16th-extracta-2001.full.md.
falsifier: an error in the zero-counting / Abelian-integral multiplicity
  argument.
holds-here: yes — confirms the weakened-H16 growth rate O(n²) directly from
  the primary source.
```

```claim
id: h16-121-vs-125-rrousseau-survey
status: sourced
statement: Chris Rousseau's own survey "Hilbert's 16th problem for quadratic
  vector fields and cyclicity of graphics" (Nonlin. Anal. 30(1), 1997) describes
  the DRR program as proving finite cyclicity of the 121 graphics and
  summarizes methods (§1). Note: the survey predates the RSZ/RR closures; the
  121-vs-125 discrepancy (RSZ/RR/Ilyashenko say 121, Shan 2013 thesis says
  125) is NOT resolved by this survey — it states 121. The BIRS 2007 workshop
  report independently confirms the DRR reduction (compactify phase×param →
  limit periodic sets finite cyclicity) and that H(2)<∞ reduces to 121
  graphics.
hypotheses: n=2.
evidence-class: sourced (BIRS report full held;
  research/sources/birs-workshop-h16-2007-report.full.md; Rousseau 1997
  abstract via search).
falsifier: a source stating a different DRR graphic count.
holds-here: yes for the 121 frame; the 125 discrepancy remains open.
```

```claim
id: h16-lienard-ldmp-survey-2017
status: sourced
statement: Llibre & Zhang (2017), "Limit cycles of the classical Liénard
  differential systems: a survey on the Lins Neto, de Melo and Pugh's
  conjecture", Expo. Math. 35(3), 286–299: the LdMP conjecture (at most
  ⌊(n−1)/2⌋ cycles for deg F = n) holds for n ≤ 4 (no cycles for n=1,2; ≤1 for
  n=3,4); is FALSE for n ≥ 6 (at least n−2 cycles, constructions: DPR 2007
  n≥7, De Maesschalck–Dumortier n≥6, De Maesschalck–Huzak n−2 for n≥6); and
  for n=5 is OPEN/unresolved as of this survey. This replaces the contaminated
  held file (which was an unrelated power-grid paper) as the correct
  Liénard-survey anchor.
hypotheses: classical Liénard ẋ=y−F(x), ẏ=−x, F of degree n.
evidence-class: sourced (FULL postprint PDF held, with complete proofs of the
  known results)
  — research/sources/llibre-zhang-lienard-survey-postprint-2017.full.md;
  the earlier .uab record page is only metadata.
falsifier: a source closing the n=5 case (≥3 cycles for deg-5 Liénard).
holds-here: yes.
```

```claim
id: drr-ledger-no-consolidated-post2020
status: sourced
statement: No consolidated graphic-by-graphic ledger of the 121 DRR graphics
  with a running closed-count and the paper closing each row exists in the
  published literature, as of this run's searches (2023-2025). Christiane
  Rousseau has published no status survey of the DRR program since the 2015
  papers (Rousseau–Shan–Zhu arXiv:1502.00689; Roussarie–Rousseau Trans. Moscow
  Math. Soc. 76, 2015): her authored arXiv/OpenAlex/Math-Net/Dialnet records
  through 2025 and her Montréal publications page (held) show no consolidation.
  The DRR 1994 original (the only complete 121-id list) is paywalled at
  Academic Press/ScienceDirect with no open full text (UHasselt DSpace holds
  only the metadata record; confirmed again this cycle). The closest thing to a
  primary per-class ledger is Shan 2013 thesis Table 1.1 (held full text).
hypotheses: n=2 quadratic DRR program.
evidence-class: sourced for "no post-2020 Rousseau survey" (her publication
  lists held/searched through 2025) and "DRR 1994 paywalled" (UHasselt metadata
  only); the completeness of the negative claim is limited by search coverage.
falsifier: a held post-2020 authoritative ledger with per-graphic status and a
  closed-count (this would FILL the request, not falsify); a graphics-table in
  a paper this run has not seen.
holds-here: yes — this is the honest resolution of requests
  dumortier-roussarie-rousseau-9c4f / complete-current-ledger-cb3d: the gap
  cannot be closed from any single published source; the run's target
  inventory must be assembled by triangulating RSZ 2015 + RR 2015 + Shan 2013
  + the individual closure papers, which is exactly what research/drr-list.md
  does.
```

```claim
id: drr-shan-2013-table11-ledger
status: sourced
statement: Shan 2013 (PhD thesis, "Theory and applications of high codimension
  bifurcations", York Univ.) Table 1.1 is the only primary per-class ledger of
  the DRR program in this library. It counts 125 graphics in the standard
  family around the origin (not 121 — the grouping/counting discrepancy is NOT
  resolved). Per-class prose statements (robust): only (DF1a),(DF2a) degenerate
  graphics have finite cyclicity, the rest 11 degenerate graphics are OPEN;
  only (I₆a) elementary non-hyperbolic graphic remains OPEN; ≥20 nilpotent
  graphics closed by Zhu–Rousseau; the thesis itself proves 4 RH-graphic
  families through a triple nilpotent point (2 saddle-type Ji2,Ua(1), 2
  elliptic-type IJb,I1b) surrounding a focus/center. The OCR'd done/open column
  totals (85 done / 36 open / 4 my-work / total 125) do NOT sum cleanly
  (classes sum to ~123) and must not be quoted as exact — cite the class labels
  and prose, not the column arithmetic.
hypotheses: n=2 quadratic DRR program; "125 graphics in the standard family
  around the origin" (Shan's counting convention).
evidence-class: sourced (full thesis text held,
  research/sources/shan-phd-thesis-2013.full.md, lines ~527-630).
falsifier: a primary ledger giving different per-class open counts; resolution
  of the 121-vs-125 discrepancy from the DRR 1994 paper itself.
holds-here: yes as a partial, per-class inventory; NOT a complete graphic-by-
  graphic 121 list (that still requires the DRR 1994 paper).
```
