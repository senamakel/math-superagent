# Scholar findings — second pass (verified, source-backed)

**Memory server status**: Cognee is down this cycle; `remember_memory` refused
(health check timeout). Per workspace rule these durable findings are persisted
here and in the claims ledger; retry `remember_memory` when the server recovers.
Each entry is verified against the held full text cited.

## 1. H(2) ≥ 4 is certified, not merely asserted (Galias–Tucker 2022)

Source: Z. Galias, W. Tucker, "The Songling system has exactly four limit
cycles", Appl. Math. Comput. 415 (2022) 126691 — open access,
http://www.zet.agh.edu.pl/~galias/ps/amc2022.pdf. Full text held:
`research/sources/galias-tucker-songling-four-cycles.full.md`.

Verified statement (Theorem 1 + Lemmas 2–10, read in full):
the Songling quadratic system
```
ẋ = λx − y − 10x² + (5+δ)xy + y²
ẏ = x + x² + (−25 + 8ε − 9δ)xy
δ = −10⁻¹³, ε = −10⁻⁵², λ = −10⁻²⁰⁰
```
has EXACTLY four limit cycles, with the four at wildly separated scales
(y ≈ 0.0427, 6.7·10⁻⁸, 2.2·10⁻²¹, 7.1·10⁻⁷⁵). Proof: adaptive-precision
(up to 2048-bit) interval arithmetic on the return map P over the transversal
segment {0}×I, interval-Newton for existence+uniqueness (Lemmas 2,3), and
no-fixed-point chunks by iteration-based (Lemma 4), derivative-based (Lemma 6)
and Lyapunov-function (Lemmas 7,10) methods; the [0.004,0.04] gap cleared with
the normal-form result of Filimonov [12]. P′ enclosures show the 4 cycles are
alternately stable/unstable (P′<1 / P′>1, with P′ extremely close to 1 for the
three inner cycles).

Implication for this run: **H(2) ≥ 4 no longer rests on the asserted 1980 Shi
bound — it is a fully certified computation**, stronger than the historical
lower bound (exactly four, with explicit positional bounds). It is the model
oracle for GOAL.md's certified limit-cycle counter: trapping/return-map argument
with interval-arithmetic verdict, adaptive precision essential because
fixed-precision numerics cannot separate the scales.

Hypotheses: quadratic; does not prove H(2)=4; the extreme separation of scales
is essential to the difficulty (the paper's own methods fail to clear
[2·10⁻²⁰², 10⁻³] computationally — 40h+ for [10⁻³,2.7·10⁻²] alone).

Claim id: `h16-four-cycles-songling-galias-tucker`.

## 2. H(n) strictly increasing in degree when finite (Gasull–Santana 2025)

Source: A. Gasull, P. Santana, "A note on Hilbert 16th problem", Proc. AMS
153(2):669–677 (2025), arXiv:2407.13465 — peer-reviewed. Full postprint held:
`research/sources/gasull-santana-note-h16-pams-2025.full.md`.

Verified statements (read in full):
- Theorem 1: H(n+1) ≥ H(n)+1 for all n∈N. Hence if H(n₀)=∞ then H(n)=∞ for
  all n≥n₀.
- Theorem 2: H(n) is realized by structurally stable fields with all limit
  cycles hyperbolic (Σⁿ_h): (a) H(n)<∞ ⟹ ∃X∈Σⁿ_h, π(X)=H(n); (b) H(n)=∞ ⟹
  ∀k∃X_k∈Σⁿ_h with π(X_k)≥k.
- Proposition 3: a planar analytic field has an enumerable (≤ℵ₀) number of
  limit cycles; so H(n)≤ℵ₀ for every n.
- Recalls Christopher–Lloyd recurrence H(2n+1) ≥ 4H(n).

Proof mechanism: rotated vector fields (Duff's Theorem 3) — non-hyperbolic
cycles split or disappear; analytic displacement map makes the bifurcating
cycles hyperbolic (their Proposition 1, via Perko's formula ∂D/∂α = C∫(e^{∫div})
(P²+Q²)dt ≠ 0). Monotonicity: embed X∈Xⁿ in X^{n+1} by multiplying both P,Q by
a linear factor ax+by with a line of singularities ℓ avoiding all cycles, then
perturb to a monodromic origin with nonzero first Lyapunov constant and
bifurcate one more cycle. Deliberately does NOT rely on the contested
Ilyashenko–Écalle finiteness: π(X) is allowed to be ∞ throughout.

Implication: structural facts about H(n) independent of its finiteness; the
H(2n+1)≥4H(n) recurrence is the concrete mechanism behind the n² log n growth.

Claim id: `h16-strong-monotone-gasull-santana`.

## 3. PROVENANCE CORRECTION — "Christopher–Lloyd weakened-16th" is Li–Li–Llibre–Zhang 2001

The held full text `christopher-lloyd-weakened-16th-extracta-2001.full.md` is
by **Chengzhi Li, Weigu Li, Jaume Llibre, Zhifen Zhang** ("Polynomial systems:
a lower bound for the weakened 16th Hilbert problem", Extracta Math. 16(3):
441–447, 2001), NOT by Christopher & Lloyd. Christopher & Lloyd 1995
("Polynomial systems: a lower bound for the Hilbert numbers", Proc. R. Soc.
Lond. A 450:219–224) is a different, paywalled paper giving the H(n) ≳ n² log n
growth. The librarian conflated the two (both are "Polynomial systems: a lower
bound ... 16th Hilbert problem"). Corrected in claim `h16-christopher-lloyd-
weakened-16th` (a `note:` field records the correction; the statement now names
Li-Li-Llibre-Zhang). The mathematical content is unaffected and verified from
the full text.

Verified statement (Li–Li–Llibre–Zhang 2001): for m,n odd, the maximum number
b_{m,n} of isolated zeros (with multiplicity) of the Abelian integral
I(h)=∮_{H=h} ȳQ(x,y)dx, H=y²/2+x^{m+1}/(m+1), deg Q ≤ n−1, is at least
((n+1)(n+3)/8 − 1) if n ≤ m and ((m+1)(2n−m+3)/8 − 1) if n ≥ m. Proof via
Green's theorem: I(h) becomes a double integral over {H≤h}, collapsing to a
sum Σ C_{ij}h^{α_{ij}} with α_{ij}=2i/(m+1)+1/(m+1)+j+1/2; the count of distinct
exponents is exactly the bound's numerator/8. Then b_{m,n} ≤ N(m,n) ≤
H(max{m,n}), giving order-n² growth of the weakened H16 at one singular point.
Also states Ilyashenko's older H_m ≥ (m²+m−2)/2 and Basarab–Horwath–Lloyd
H_m ≥ (m−1)(m+2)/4 (cycles in several nests, not around one point).

Claim id: `h16-christopher-lloyd-weakened-16th`.

## 4. Liénard LdMP survey — full postprint now held; attribution nuances

Source: J. Llibre, X. Zhang, "Limit cycles of the classical Liénard
differential systems: a survey on the Lins Neto, de Melo and Pugh's
conjecture", Expo. Math. 35(3):286–299 (2017), DOI 10.1016/j.exmath.2016.12.001.
Full postprint PDF now downloaded and held:
`research/sources/llibre-zhang-lienard-survey-postprint-2017.full.md`
(summary replaced at `research/summaries/llibre-zhang-lienard-survey-postprint-2017.md`).
The earlier held file `llibre-zhang-lienard-survey-expmath-2017.uab.full.md`
is only the UAB record page (abstract + metadata), not the paper body.

Verified statements (read in full, including the proofs):
- Theorem 1: degree-n Liénard systems (1) exist with ⌊(n−1)/2⌋ limit cycles
  (sharp lower bound), proved here by first-order averaging f(r)=
  Σ_{j=0}^{⌊(n−1)/2⌋} a_{2j+1}b_{2j+1}r^{2j+1} with chosen coefficients giving
  simple roots.
- Theorem 2: (a) n=1,2 no limit cycles; (b) n=3,4 at most one (n=3: two new
  proofs — divergence/Greens integral showing every cycle hyperbolic unstable,
  and a first-integral V comparison; n=4: Li–Llibre 2012, 20pp, not repeated);
  (c) n≥6 at least n−2 limit cycles.
- **n = 5: OPEN** — the survey's own open problem is the maximum number of
  limit cycles for n≥5.
- History: DPR 2007 proved n≥7 (one extra cycle beyond the conjecture);
  De Maesschalck–Dumortier 2011 proved n≥6 (+2); De Maesschalck–Huzak 2015
  proved n−2 cycles for n≥6. The degree-6 four-cycle example in the survey's
  own proof (Step 1: I₁(x)=0.4x³−1.248x⁵+1.17429x⁷−0.3x⁹ with exactly 3
  positive zeros → 4 cycles) follows De Maesschalck–Huzak via the slow
  divergence integral I(x)=∫_x^{L(x)} f(s)²/s ds (Theorem 7: k simple zeros of
  I ⟹ k+1 hyperbolic limit cycles for ε>0 small).

Correction applied: claims `h16-lienard-ldmp-disproved` and
`h16-lienard-ldmp-n6` had attributed the degree-6 four-cycle example to DPR
2007; per the held survey the degree-6 case is the De Maesschalck–Huzak route
presented in the survey, while DPR 2007's own paper established n≥7. The core
claim (conjecture FALSE for n≥6) is unaffected.

Claim ids: `h16-lienard-ldmp-survey-2017`, `h16-lienard-ldmp-disproved`,
`h16-lienard-ldmp-n6`, `h16-lienard-n5-open`.

## 5. BIRS 2007 report — independent confirmation + one new concrete open problem

Source: BIRS workshop 07w5021 report, "Mathematical developments around
Hilbert's 16th problem" (2007), https://www.birs.ca/workshops/2007/07w5021/report07w5021.pdf.
Full text held: `research/sources/birs-workshop-h16-2007-report.full.md`.

Verified statements (read in full):
- Confirms the DRR 121-graphics reduction verbatim (line 54: "the proof that
  H(2)<∞ ... [reduces] to the proof that 121 graphics have finite cyclicity",
  following Roussarie's compactification idea; limit cycles can only accumulate
  on limit periodic sets in phase×parameter).
- Confirms the Christopher–Lloyd lower bound "of the order H(n) ≥ C n² ln n"
  (the report's [3] = Christopher–Lloyd 1995).
- Roussarie's own lecture: slow-fast systems as a key to uniform upper bounds;
  the DPR 2007 Liénard counterexample is "negative answer to Smale's system" —
  a classical Liénard system with 5 limit cycles where only 4 were expected
  (this is the n≥7 case, one extra).
- Mourtada: finite cyclicity of hyperbolic polycycles in compact families on
  S², quasi-analytic algebras + fewnomials; extends Varchenko–Khovanskii to
  neighbourhoods of hyperbolic polycycles (Morse H, generic at infinity, gives
  N(d) bound on limit cycles of any dH-perturbation with nonvanishing Abelian
  integrals).
- Novikov: generalization of Varchenko–Khovanskii to Darboux-integrable
  systems (first integral ΠP_i^{α_i}) — uniform bound exists, non-explicit,
  generic; Picard–Fuchs no longer holds.
- Dumortier–Caubergh: uniform explicit bound for classical Liénard in any
  compact subset of parameter space away from the singular limit; finiteness
  for this subfamily reduced to finite cyclicity of the singular-perturbed
  graphics.
- **New concrete open problem (Roussarie, §4.1)**: bound the number and type
  of fixed points of a composition of maps R_i(x) = α_i + x^{r_i} (x>0, α_i∈R,
  r_i>0); very little known globally (Mourtada handled α_i~0, x→0); any bound
  from below or above welcome. This is a self-contained one-dimensional
  displacement/composition problem within this run's reach.

Claim ids: co-anchors `h16-121-vs-125-rrousseau-survey` (121 frame),
`h16-lienard-ldmp-disproved` (DPR counterexample context).

## 6. Entailment edges repaired

The derived ENTAILMENT.md previously listed several "follows from nothing"
dangling edges (`drr-121-graphics-reduction`, `h16-kaloshin-elementary-bound`).
All `follows-from:` lines now name existing claim ids:
- 4 summaries → `h16-drr-121-graphics` (the DRR reduction claim; the id
  `drr-121-graphics-reduction` never existed as a claim block — the reduction
  is carried by `h16-drr-121-graphics`).
- Kaloshin summary → `h16-kaloshin-uniform-bound` (was `h16-kaloshin-elementary-bound`).
- binyamini-dor → `h16-bny-abelian-bound`; buzzi-novaes → `h16-lower-bounds`;
  llibre-abel survey → `h16-dulac-proof-contested`, `h16-bamon-quadratic-finiteness`;
  lu → `drr-rr-boundary-only-for-3-graphics`; palma-marquez-yeung,
  yeung-natural-levels → `h16-dulac-proof-contested`.

## 7. Candidate target surfaced (not endorsed): Roussarie's composition problem

From the BIRS 2007 report §4.1 (Roussarie's own stated open problem): bound the
number and type of fixed points of a composition of maps
R_i(x) = α_i + x^{r_i}  (x > 0, α_i ∈ R, r_i > 0).
Little is known globally (Mourtada handled the local case α_i ~ 0, x → 0);
any bound from below or from above of such a composition's fixed points is
welcome, and the problem arises naturally in singular-perturbation / return-map
theory. This is a one-dimensional displacement/composition question that this
run's zero-counting machinery could in principle address without the full weight
of H16, and its fixed points are the model for limit-cycle accumulation. Recorded
for the inventor/director; NOT endorsed as this pass's target.
