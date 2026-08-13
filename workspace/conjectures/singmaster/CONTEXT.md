# Shared context

Singmaster's conjecture: `N(a) := #{ (n,k) : C(n,k) = a }` is bounded by an
absolute constant. Working assumption: open since 1971, not provable here; the
deliverable is a genuine partial result stated exactly. This brief is re-sent on
every model call, so everything here must survive contact with the witnesses and
the counting convention.

**Counting convention (fix before stating any bound; used everywhere in this
run):** `N(a)` counts BOTH mirrors `(n,k),(n,n-k)` AND the trivial pair
`C(a,1)=C(a,a-1)`. So `N(3003)=8` = 3 nontrivial reps × 2 + 2 trivial. A bound
of 8 here is 4 half-triangle. `computed`, matches `code/out/witnesses.json`.

## Established

Each marked with evidence class and a link.

- **Small-column genus closed forms anchored to the literature superelliptic formula. `checked` (EXIT_CODE=0).**
  `code/genus/verify_superelliptic_formula.py` cross-checks the run's computed
  small-column genus rows for `C(x,k1)=C(y,k2)` against Sutherland's superelliptic
  genus formula `g=((d-2)(m-1)+m-gcd(m,d))/2` (Open Book Series 4 (2020) eq. (1);
  Wikipedia Superelliptic curve). `{2,n}` hyperelliptic model `(2y-1)^2=1+8C(x,n)`:
  10 values OK; `{3,n}` cyclic trigonal model `(y-1)^3-(y-1)=6C(x,n)` (z^3-z): 21
  values OK; `{4,n}` correctly reported as NOT a direct superelliptic cover (2:1
  cover of `w^2=1+24C(x,n)`, base genus shown). ALL literature-formula checks PASS.
  Capture `code/out/verify_superelliptic_formula.captured.txt`. This gives the
  `{2,n}` and `{3,n}` closed forms a citable primary anchor; it is a cross-check,
  not an independent re-derivation, and it does not touch uniformity.

- **Lane Clark 2010 (INTEGERS 10 #A14) — the normal-array template that produces every log bound. `checked`** (full text held at
  `research/sources/lane-clark-array-multiplicity.full.md`, summary +
  claim `lane-clark-normal-array-bound`). A general theorem on "normal"
  triangular arrays gives `N_a(t) < r(g⁻¹(t)+Δ)` (Theorem 2); for binomials
  (`d=n`, `f=⌊n/2⌋`, `g=2^x`, `r=2` mirrors, `Δ=1`) this exactly reproduces
  Singmaster's `N(a) < 2 log₂ a + 2`. **Effective: yes** (explicit computable
  constant). **Uniform-in-k: yes** (bound holds regardless of which columns
  produce the collisions — but it grows with a, so it is uniform-in-k without
  being O(1)). Verified against `code/out/witnesses.json` and brute force
  2<=a<=60, both pass (EXIT_CODE=0, capture at
  `code/out/verify_lane_clark_bound.captured.txt`). The paper's own Examples
  5,6 construct normal arrays achieving `Θ(t^{1/s})` and `Θ(log_s t)` infinitely
  often, so the `O(log t)` shape is **provably best-possible within the
  template** — a constant bound must come from binomial-specific structure beyond
  the normal-array axioms. This is the same message as Kane/MRSTT/effective-curves
  (uniformity needs structure), now stated as a theorem about the general
  framework. Corroborates `best-unconditional-bound`,
  `singmaster-bounds-history`, and the uniformity argument of `effective-methods-wall`.

- **Riemann–Hurwitz derivation of the genus closed form now executed over the full range. `checked` (EXIT_CODE=0), captures both held.**
  `code/genus/verify_riemann_hurwitz.py` now runs the full `2<=m<n<=20` grid
  (171 pairs; genus 1 only at `{2,3},{2,4}`, rest >=2), ALL CHECKS PASSED,
  capture `code/out/verify_riemann_hurwitz_full.captured.txt` (185 KiB; the
  smaller `verify_riemann_hurwitz.captured.txt` covers 2<=m<=9,m<n<=10 plus
  (3,25),(4,25),(6,9)). The four RH ingredients: (a) degree in y = n; (b) finite
  ramification = m(n-1) points index 2 — critical points found by bisection for
  n<=15 (Rolle structural for n>15), smoothness checked explicitly (scaled
  critical-value sets disjoint); (c) exact integer RH identity
  `2g-2 = -2n + m(n-1) + (n-gcd)`; (inf) fibre at x=infinity COMPUTED via the
  Puiseux chart u=1/x giving I_inf = n-gcd (confirmed numerically), no finite-y
  point over infinity; (d) m=2 edge `g=floor((n-1)/2)`. **What this does and does not
  establish:** (a),(c),(inf) are exact/structural in m,n, so the closed form
  `g(m,n)=((m-1)(n-1)+1-gcd(m,n))/2` is now derived by the intended mechanism, not
  just fitted to grids; but ingredient (b)'s smoothness/count is numerically
  verified per pair (bisection for n<=15), so call it `checked` over this grid, not
  a fully general proof until (b) is argued for all m,n. The `m=n` diagonal stays
  degenerate (excluded). This is the RH deliverable of TASKS.md item 1; the
  singularity delta-invariant cross-check (promote-to-proved route) is still not
  separately done.

- **Witness set / the falsifier. `computed`, 3 independent routes.**
  `3003 = C(3003,1)=C(78,2)=C(15,5)=C(14,6)` (+4 mirrors), so `N(3003)=8`.
  Verified by `code/out/witnesses.json`, the naive oracle `code/brute.py`, and a
  primary source confirming it (Singmaster FQ 1975 "Added in proof"; also listed
  in MRSTT (1.2)). **Any bound <8, or any lemma implying one, is refuted.**
  Six numbers with `N=6` <= 2^48: 120, 210, 1540, 7140, 11628, 24310 (each one
  nontrivial pair + mirrors + trivial). `sourced`+`computed`.

- **Infinite family `N(a)>=6` — the reason `B>=6`. `computed` from a `sourced`
  identity.** `C(n+1,k+1)=C(n,k+2)` has infinitely many solutions:
  `n=F_{2i+2}F_{2i+3}-1, k=F_{2i}F_{2i+3}-1` (i>=1; `F` Fibonacci). i=1 gives
  3003; i=2 gives 61218182743304701891431482520. Closed form derived in
  `code/family_seq/family_sequences.py`: `n_i=7n_{i-1}-n_{i-2}+6`,
  `k_i=7k_{i-1}-k_{i-2}+9` (Lucas-identity proof checked against direct
  Fibonacci computation). Verified N(a)>=6 for i=1..5. This is the *only* curve
  in Jenkins' family with infinitely many lattice points (a=b=1). Any `B<6`
  is refuted.

- **Genus closed-form integrality — proved (operator) AND now independently verified by this run. `checked` (was `operator-computed`).**
  The expression `N(m,n) = (m-1)(n-1) + 1 - gcd(m,n)` is even for all `m,n >= 1`
  (four-case parity argument: gcd is even exactly when both are even, which is
  exactly when `(m-1)(n-1)+1` is even; the other three cases both terms are odd).
  So `g(m,n) = ((m-1)n - (m-2) - gcd(n,m))/2` is always an integer.
  **Independent repro done this run (TASKS item 4, EXIT_CODE=0):**
  `code/genus/repro_integrality.py` — 638401 pairs over 1<=m,n<=799, ZERO odd
  N in all four parity classes, and the two algebraic forms agree on 1..399;
  capture `code/out/integrality_reproduced.captured.txt` (this replaces, and
  separately from, the operator's `genus_integrality_proved.captured.txt` 1,121,253-pair
  check over 2<=m<n<1500). The ten symmetric-form predictions remain internal
  consistency (algebraically equal expressions), NOT independent genus
  confirmation — Singular confirms the genus itself; integrality alone is settled.
  Proof at `research/notes/genus-integrality-proved.md`.
  For distinct `m,n>=2` the geometric genus of the projective closure is
  `g(m,n)=((m-1)n-(m-2)-gcd(n,m))/2` (symmetric in m,n; numerator always even).
  Reduces by substitution to the per-column forms ({2,n}→`floor((n-1)/2)`
  hyperelliptic; {3,n}→n-1/n-2; {4,n}→3(n-1)/2 etc.; {5,n}→2n-2, 2n-4 if 5|n)
  and adjacent {n-1,n}→`(n-1)(n-2)/2`; it supersedes all prior per-column and
  diagonal grids. Genus is 1 exactly for **{2,3} and {2,4}**, >=2 for every
  other distinct pair (matches BST Thm 2.2, a primary-source proof; cross-checks
  Jenkins (2,2)=3 and de Weger (3,4)=3). **So Faltings applies to every distinct
  pair — the Faltings-threshold deliverable — but per-pair finiteness is
  ineffective, and a quadratically-growing genus makes uniformity harder, not
  easier (the standing trap).** Diagonal m=n reducible (contains x=y). Identically
  `g=((m-1)(n-1)+1-gcd(n,m))/2`, so coprime pairs have `g=p_a/2` with `p_a=(m-1)(n-1)`
  the bidegree arithmetic genus; equivalently the singularities' total delta
  invariant is `((m-1)(n-1)-1+gcd(n,m))/2` — the concrete statement whose
  verification would promote the formula from checked to proved (mechanism
  candidate: the involutions z→k-1-z; claim
  `genus-symmetric-form-and-delta-prediction`). Single
  formula: `code/out/genus_single_closed_form.md`, claim
  `genus-single-closed-form-all-pairs`. **Two caveats an agent must not
  overstate:** (a) the original 8x11 grid was two-CAS (Singular+Sage agree),
  but the 23 rows added since (k2=6..10) rest on Singular alone — the Sage check
  errored (`NameError: PolynomialRing`) and never ran, so do not call them
  independently verified; (b) the slope-of-mean trap — a truncated (non-whole-
  period) window gives a mean below `(m-1)/2` and looks like a refutation;
  state periodicity first, mean second (whole-period mean is exactly (m-1)/2
  for m=2..5).
  **Out-of-sample Singular confirmation — `checked`, effective but NOT uniform.**
  `g(m,n)=((m-1)n-(m-2)-gcd(n,m))/2` was predicted FIRST from the closed form,
  then recomputed independently in Singular for 17 out-of-sample pairs (outside
  the 2..12 × 2..9 grid the formula was originally fitted to; pairs span m in
  2..16, n in 13..28): 17/17 returned, 0 mismatches, incl. {13,26} gcd 13→144,
  {14,28} gcd 14→169, {16,26} gcd 2→187. Claim
  `genus-closed-form-out-of-sample-verified` in
  `code/out/genus_out_of_sample_verified.md`; anchor
  `code/out/genus_falsify.captured.txt`. Effective: yes (finite exact CAS
  recomputation); **uniform in k: no** (17 specific pairs). This confirms the
  formula past the fitted grid but does not prove it — the Riemann–Hurwitz half
  of the uniform derivation is now executed over 2<=m<n<=20 (see the
  Riemann–Hurwitz bullet above); only the singularity delta-invariant
  cross-check remains a separate route.

- **Known bounds (all grow with a; reproducing one is NOT a result). `sourced`
  from primary where noted; Singmaster 1971 Monthly still NOT held.**
  Singmaster 1971 `O(log a)` — the real paper (AMM 78 (1971) 385–386) has NOT
  been obtained; `research/sources/singmaster-1971.full.md` is a tombstone (the
  prior file was Fermat's Library comments page, flagged and replaced). Attested
  by Singmaster's own FQ 1975 paper (PRIMARY now held at
  `research/sources/singmaster-1975-fibonacci-repeated.full.md`), AEH 1974
  (held), MRSTT (held). Do not quote a constant from the Fermat's snippets.
  Abbott–Erdős–Hanson 1974 `O(log a/log log a)` — primary held.
  Kane 2007 best `N(t)=O((log t)(log_3 t)/(log_2 t)^3)` — primary summary held.
  Conditional on Cramér, `O_eps((log a)^{2/3+eps})`. None is uniform ⇒ none
  touches the conjecture. (`research/notes/established-review.md`.)

- **BST 1999 primary now held — the fixed-pair ineffectivity anchor. `sourced`.**
  Beukers–Shorey–Tijdeman, "Irreducibility of polynomials and arithmetic
  progressions with equal products of terms", in *Number Theory in Progress
  Vol. 1* (de Gruyter 1999) 11–26 — MRSTT's [4] — readable full text at
  `research/sources/number-theory-in-progress-vol1-preview.full.md` (the
  `best1.ps` preprint is raw PostScript/unreadable). Theorem 1.1: fixed
  (m,n;d1,d2) equal-products equation has finitely many integral solutions
  except the m=2,n=4,d1=2d2 family; for gcd(m,n)=1 the proof "resort[s] to
  Siegel's theorem... which is, unfortunately, ineffective" (paper's own
  words), and "Both results are ineffective" (Siegel B, Faltings C).
  Theorem 2.2: genus of the equal-products curve is ≤1 only in four genus-0
  and eight genus-1 parameter cases; for the binomial case d1=d2=1 the only
  non-diagonal genus-1 pairs are (2,3),(2,4) — every other distinct pair has
  genus ≥2 (primary-source proof of the Faltings threshold, agreeing with the
  run's computed grid). Summary + claims:
  `research/summaries/beukers-shorey-tijdeman-1999-equal-products.md`.

- **Matveev 2000 primary now held — the effective-per-pair constants. `sourced`.**
  E.M. Matveev, "An explicit lower bound for a homogeneous rational linear
  form in logarithms of algebraic numbers", Izv. Math. 62:4 (1998) 723–772,
  full English text at `research/sources/matveev-2000-homogeneous-linear-form.full.md`
  (mathnet.ru). Theorem 2.2 ineq. (2.16): under the Kummer condition
  [K(√α1..√αn):K]=2^n, with D=DK/κ, A_j ≥ max{h(αj), |ln αj|/D, 1/(DC1)},
  Ω=∏A_j, B=max|b_j|A_j/A_n, C3=n/ρ,
  C1=(1+e^{−2n}/148)(n ln 2+2)(1+1/n)C3,
  C2=4(n+1)(6+5/(n ln 2+2))e^{2n}√n·C3, C′0=ln(C2DΩ/(C1A_n)):
  ln|Λ| > −112·2^n·C2·C′0·D²·Ω·ln(2eB). Without Kummer: extra n^n
  factor, B weaker. **One gate for any effective bound this run computes:
  verify the Kummer condition and state the height convention (Matveev's A_j
  are logarithms-heights; other authors exponentiate, which is why
  Tiebekabe–Diouf's Theorem 2.9 looks different).** These constants make
  "effective with computed constant" possible per pair, but NOT uniform in
  (k1,k2) (C1,C2,D,Ω grow with n and heights).
  Summary + claim: `research/summaries/matveev-2000-homogeneous-linear-form.md`.

- **MRSTT interior, the current record. `sourced`** (arXiv:2106.03335, QJM 2022;
  Theorem 1.3). For fixed `0<eps<1`, t large: at most 2 solutions to C(n,m)=t in
  `exp(log^{2/3+eps} n)<=m<=n/2`, at most 4 in the full interior. Inner region
  at most 1. To prove the conjecture it suffices to handle
  `2<=m<=exp(log^{2/3+eps} n)`, i.e. `m<=log t/log_2^{3/2-eps} t` — that is
  **exactly what they leave open**. Interior multiplicity is 0,1,2,4 — never 3
  (Remark 1.11).
  **Effectiveness of threshold CONFIRMED from full text.** Remark 1.7 states
  verbatim: "The implied quantitative bounds in the hypothesis 't is sufficiently
  large depending on ε' are effective; however, we have made no attempt whatsoever
  to optimize them in this paper, and will likely be too large to be of use in
  numerical verification of Singmaster's conjecture in their current form." So the
  interior theorem IS effective (a computable threshold exists) but with an
  unoptimized, likely astronomically large constant — NOT non-constructive.
  Uniform-in-k: yes over the interior; no over the boundary.
  **Exact statement with effective/yes, uniform-in-k/yes (over interior) now
  in `research/approaches/mrstt-exact-statement.md`.**

- **MRSTT leaves all known witnesses untouched — fail TWICE.** `computed`.
  All 15 nontrivial witness pairs (including the three for 3003: (14,6),(15,5),
  (78,2)) lie below the interior cut exp((log n)^{2/3+eps}) for every admissible
  eps. AND every witness has t <= 24310, failing the "t sufficiently large"
  hypothesis independently. The region comparison is about the shape of the
  boundary, NOT a claim that a large-t witness would also escape — that is
  not established. So MRSTT is consistent with B=8 without constraining it,
  and progress on B must come from the edge. Recorded at
  `code/out/mrstt_leaves_witnesses_open.md`.
  **Conclusion (directive 4): the MRSTT route yields nothing for Singmaster.**
  An effective-but-astronomical interior threshold does not move B, because the
  witnesses all sit in the edge the interior theorem does not cover, and the
  edge is provably inaccessible to the interior method (Prop 1.12 barrier, even
  under RH). MRSTT has delivered its partial result — the sharpest statement of
  the open gap `2 <= m <= (log t)/(log log t)^{3/2-eps}` — and can go no
  further. Progress on B must come from the boundary, i.e. per-pair effective
  results (Avanesov/de Weger/BMSST) and Baker/Matveev height bounds, which
  currently do not give uniformity. The effective-versus-usable distinction is
  the deliverable: MRSTT gives an *effective* but unusable constant, a
  different object from a bound one can check.

- **Small-(k1,k2) curves — which pairs are COMPLETELY solved effectively. `sourced`
  (Stroeker–de Weger 1999, Math. Comp. 68:8, primary held).** `C(n,k)=C(m,l)`
  is solved completely (all integral solutions listed) for exactly
  `(2,3),(2,4),(2,6),(2,8),(3,4),(3,6),(4,6),(4,8)` — by reducing each to an
  elliptic curve and applying David's explicit linear-form-in-elliptic-logarithms
  bound + LLL (`sdw-elliptic-logarithms-eight-pairs`, `asserted`). This is a
  sharpening of the older per-case list: (2,3) Avanesov; (2,4) de Weger/Pintér
  (Gelfond–Baker); (3,4) de Weger genus-3 double cover of `Y^2+Y=X^3-X`;
  (2,5) BMSST 2008 hyperelliptic. **Every other distinct pair has genus>1 and
  only Faltings' ineffective finiteness** (consistent with the genus formula).
  So the eight pairs are the full set the effective toolbox reaches, and the
  unified method is `elliptic logarithms + David + LLL`, not a per-case trick;
  the (3,6) solution was the first cubic=cubic. Kiss 1988:
  `C(x,2)=C(y,p)` finite for p prime.

- **Yamada 2020 boundary necessary condition — the only quantitative hold on
  the MRSTT-open edge. `sourced`** (arXiv:2002.07043 Thm 1.1; summary
  `research/summaries/binom-collisions-necessary-conditions-2020.md`, claim
  `yamada-boundary-necessary-condition`, `asserted`). If
  `C(2n+δ,n-m)=C(2n+l,n-k)` (δ∈{0,1}, 0≤m<k<n/2, m≤0.735k) then
  `l > n(1.3132 log₂(2n) − 2.00271)`, and for n large `l > (cn/log n)^{40/21}`
  (any c<0.68943). Method: largest-prime-factor of the two products is
  `≤ k₀=2(k+l)−δ−1` (Lemma 2.3) + prime-gap argument. Gives finiteness of
  solutions with `m≤ηk` and `l<(cn/log n)^{40/21}` for any η<1, c<0.68943;
  Cramér would give `exp(c₂√n)`. Edge equations like `C(2n,n)=C(y,2)` are
  stated as far beyond present techniques. Per-configuration, NOT uniform —
  but it is the one result this library holds that quantifies the boundary
  regime MRSTT leaves open, so any boundary attack should measure itself
  against it.

- **Verification bound.** `sourced` from secondary attestation + Singmaster FQ 1975
  (held): no `N(a)>=8` for `a<2^23` (originally Singmaster 1971, re-stated in FQ
  1975); extended to `2^48` (Singmaster FQ 1975); Blokhuis–Brouwer–de Weger
  2017: no unknown collisions for `n<=10^6` or value `<=10^60`. This run's own
  scan: N=6 values found for `n<=20000, value<=10^12` matching the primary list.
  Note: the 1971 primary source has NOT been obtained; the 2^23 bound is attested
  in Singmaster's own FQ 1975 paper (held) and in MRSTT, but the original
  published article is not in the library.

## Ruled out

- **Finiteness per fixed (k1,k2) — already known and NOT the conjecture.**
  Faltings (genus>1, confirmed by the grid) and Siegel (genus 1) each give
  "finitely many", but **ineffective** — no count computable in (k1,k2).
  Singmaster needs a constant uniform over all pairs at once. This is the
  central obstruction; every approach must say how it beats it, and the genus
  computation does not. The Bilu–Tichy route has the same wall: HPT 2022 Thm 2.3
  (Ramanujan J 58) applies the classification to this exact problem but is
  explicitly **ineffective**; only the shifted-power-values result (Thm 2.4) is
  effective. So `bilu-tichy-classification` is refuted as a route to a uniform
  bound, with the exceptional-pair classification as its surviving kernel.

- **Genus route yields no uniform bound.** `computed`: genus>1 for essentially
  all distinct pairs, but that only re-proves per-pair Faltings finiteness.
  Closing uniformity needs effective Siegel or effective Schmidt subspace
  theorem — out of reach. Recorded so the inventor does not re-propose it.

- **Effective curve methods cannot give uniformity — the completed
  impossibility result. `sourced` (grounded; claim `effective-methods-wall`,
  four held primaries).** The effective integral-point toolbox (David's
  elliptic logarithms at genus 1; BMSST Baker/Matveev + Mordell–Weil sieve at
  genus 2) is per-curve: it requires a rational point, an explicit Jacobian
  MW basis, and canonical-height-difference bounds that are **provably
  unavailable for genus ≥ 3** (BMSST 2008 p. 2 verbatim) — and the family
  leaves genus ≤ 2 immediately (`genus{2,n}=floor((n−1)/2)`; (3,4) is already
  genus 3). Where it applies, every constant grows with the curve's
  rank/regulator/heights (David c4 has exponent r+2; Matveev
  `−112·2ⁿ·C₂·C′₀·D²·Ω·ln(2eB)` grows in n, D, Ω=∏A_j) — i.e. with the column
  index — so no k-independent constant emerges; and a uniform B would have to
  sum per-pair bounds over ~log2(a) pairs down to the MRSTT-open boundary,
  which they cannot do. **This is GOAL.md's "approach cannot give a bound
  uniform in k, obstruction named" deliverable.** The surviving honest
  per-pair task is an explicit Matveev/David constant for one small pair,
  stated with its k-dependence. Full statement:
  `research/approaches/effective-methods-wall.md`. Do not re-propose curve
  methods as a route to uniformity.

- **Kane's lattice-point method cannot beat inverse density.** `sourced`
  (Kane 2007 §8): a randomized construction proves his method cannot give
  better than `O(log_2 t)`; one cannot exclude low-density t with his
  technique. So a different mechanism is needed for constancy.

- **Mason-Stothers / polynomial abc is vacuous for binomials. `checked` with capture.**
  `code/out/check_mason_stothers_bound.captured.txt`: degB'=0 for all 21 pairs
  with 2<=k2<k1<=8, slack >= 0 throughout. Structural reason: the two binomial
  polynomials share their common falling factorial as their entire gcd; dividing
  it out leaves one monic falling factorial (|k1-k2| distinct roots) and one
  rational constant, so N0 = maxdeg+1 identically and the inequality never binds.
  The effective function-field abc/Siegel analogues (Mason 1984, Zannier 1993,
  Wang 2004, Mueller 2000) do not transfer to number-field integral points.
  Approach `mason-stothers-abc.md` refuted with the slack table as reason.
  Range: 2<=k2<k1<=8 — a vacuity check over that box, not all pairs, but the
  collapse mechanism is uniform.

- **Three newer speculatives — proposed, NOT yet refuted and NOT yet
  established; carried so nobody re-derives them.** All three are approach
  files in `research/approaches/` with no capture and no check yet; treat each
  as an open idea with a stated first computation, not as a result.
  (a) `binary-lucas-submask.md` — Lucas mod 2: every representation of an odd
  `a` must satisfy `k ⊆ n` bitwise; odd-only Pascal triangle is sparse; claim
  "no odd value appears more than 8 times" would give N(a)≤10 for odd a. First
  step: enumerate odd coefficients `n<=2^16` and check max multiplicity against
  the witnesses. (b) `consecutive-block-merge.md` — from `C(x,k1)=C(y,k2)`
  cross-multiply to a product of consecutive blocks; use Sylvester/Erdős–
  Selfridge first-power-prime structure to force `max(k1,k2)≤6` outside the
  Pell family. First step: factor the witness 3003's block products
  (15·14·13·12·11·6 = 14·13·12·11·10·9 checks; the (2,5) block split
  78·77·60 = 15·14·13·12·11) and tabulate Sylvester primes. (c)
  `sylvester-prime-machine.md` — Sylvester's theorem (product of k consecutive
  integers > k has a prime > k to the first power) applied to `C(n,k)=a` gives
  each nontrivial representation a prime `p_i > k_i` with `v_{p_i}(a)=1`;
  the attempt to force distinctness is already refuted by the 3003 overlap
  (primes 7,11,13 serve k=2,5,6 representations together), so state explicitly
  that the block-merge/Sylvester engine has not been shown to beat the
  overlap for small k. All three: any bound they yield must be run against
  `code/out/witnesses.json` and none is yet (`asserted` at best).

- **MRSTT's non-archimedean method has a hard ceiling.** `sourced` (Prop 1.12):
  requires N,M = O(exp(log^{3/2-eps} P)); even under RH this cannot be relaxed.
  Only a randomness heuristic pushes to exp(P^c). Hence the interior method
  cannot be extended to the small-m regime by improving constants.

- **Diagonal k1=k2 curves are degenerate.** `computed`: `C(x,k)=C(y,k)` factors
  (contains x=y), genus undefined — the arithmetically interesting cases are the
  distinct pairs, and the a=b=1 family is the one Jenkins left open (golden-ratio
  quadratic, infinitely many lattice points).

- **Triangular=tetrahedral `C(x,2)=C(y,3)` is NOT an infinite N>=6 family.**
  `recall_scratch` holds a provisional hypothesis claiming it is ("positive-rank
  elliptic curve → infinite integer solutions, each giving N(a)=6"). **Contradicted
  on two grounds.** (a) The curve is genus 1; positive rank gives infinitely many
  *rational* points but Siegel's theorem gives only finitely many *integral*
  points — the scratch conflated the two. (b) The pair (2,3) is solved
  (`deweger-smallk-effective`, `sourced`): Avanesov/Skolem solved `C(n,2)=C(m,3)`
  with finitely many solutions. The 6-fold witnesses 120=C(16,2)=C(10,3),
  1540=C(56,2)=C(22,3), 7140=C(120,2)=C(36,3) are isolated triangular/tetrahedral
  collisions, not a family. **The only established infinite N>=6 family is the
  Pell/Singmaster `C(n+1,k+1)=C(n,k+2)` one (genus 0, quadratic).** Do not
  rebuild the infinite family on the triangular=tetrahedral curve; verify the
  solution count before relying on it.

## Numbers

- `N(3003)=8` (both+trivial); N=6 set {120,210,1540,7140,11628,24310}.
- Genus closed form `g(m,n)=((m-1)n-(m-2)-gcd(n,m))/2`; genus=1 exactly at
  {2,3},{2,4}, >=2 elsewhere (checked 111 values; RH grid verified over
  2<=m<n<=20, 171 pairs).
- Infinite family members (Singmaster 1975, `C(n+1,k+1)=C(n,k+2)`):
  j=1 a=3003, N=8 exact; j=2 (29 digits), N=6 exact; j=3 (205 digits), N=6
  exact — the latter two beyond the Blokhuis–Brouwer–de Weger 2017 `10^60`
  verification bound; j=4..6 identity verified, N>=6 each. Capture
  `code/out/verify_fibonacci_identity.captured.txt` (EXIT_CODE=0, fast
  inversion cross-checked against `lib.binom_multiplicity` on all 10 check
  values).
- Family recurrences `n_i=7n_{i-1}-n_{i-2}+6`, `k_i=7k_{i-1}-k_{i-2}+9` checked i=3..8.

## Recalled

Durable memory holds this run's own established facts (genus plan, counting
convention, family parametrization, Jenkins framing) — those are now redundant
here and live in the sections above. Treat all library claims as
`sourced`/`computed` per the marking above, and MRSTT/Kane/internal results as
taken on their word (`asserted`) where not re-derived here.

The durable graph (`relate_memory`) connects the central objects exactly as
the sections above do: `uniform-in-k obstruction --blocks--> singmaster's
conjecture`, `effective uniform bound --would_resolve--> singmaster's
conjecture`, `genus computation approach --targets--> singmaster's conjecture`.
No additional node changes the picture; the obstruction node is the same wall
the library marks ineffective.

One independent prior durable node bears on the problem (recalled, not this
run's finding): **multinomial generalization** (De Koninck–Doyon–Verreault 2021,
arXiv:2107.09107). For fixed k, `N_k(a)` (k-term multinomial = a) has average and
normal order `k(k-1)` and `N_k(a)=O((log a/log log a)^{k-1})`; k=2 is the
binomial case. It also corroborates the verification list (N(a)>=6 up to 10^60,
3003 at N=8 as highest known). Hypothesis checked against this problem: the
k=2 restriction is exactly Singmaster, and its conclusion — small columns, not
typical values, are where a uniform bound is hard — matches the run's scratching.
Carry it as corroboration only, not as a bound.

Two further adjacent bounds exist in the library (asserted, secondary; carry as
context, not as Singmaster results): Stirling-number analogue `M_i(a) <=
2 + 2 log_a / W((1/2) log a)` (`stirling-2023-bound-and-record`, Bazsó–Mező–
Pintér–Tengely 2023) and the OEIS row-count convention `a059233-rowcount-half-triangle-conversion`.

## Contradictions

- **SOURCE INTEGRITY: `research/sources/singmaster-1971.full.md` is NOT Singmaster's paper.**
  `computed`+`sourced`. The prior download was the Fermat's Library
  comments/annotation page; it has been replaced by a tombstone (reads "this
  file is NOT the Singmaster paper; the real paper has NOT been obtained") and
  `research/summaries/singmaster-1971.md` records the accounting. The O(log a)
  argument, the `N(3003)=8` "added in proof", and the six N=6 values below 2^23
  are all attested by primaries that ARE held (Singmaster FQ 1975, AEH 1974,
  MRSTT). Do not quote a constant or exponent from the Fermat's snippets.
- **Kane bound exponent.** Fermat's Library's annotation of Singmaster 1971
  states the best bound with exponent 2 (`log_2^2 t`); Wikipedia, MRSTT, Jenkins
  all give exponent 3 (`log_2^3 t`). Exponent 3 taken as correct; the Fermat's
  slip is recorded, not trusted.
- **Standing tension** (structural, not a source clash): `k<=log2(a)` says high
  N(a) must come from small k, and every witness (3003, the N=6 family, the
  infinite family) sits in k=2/3 columns — so small-column curves carry the
  multiplicity and a uniform bound must control them uniformly. The small-`k`
  effective results (Avanesov, de Weger, BMSST) are exactly the attackable part.
- **DISCREPANCY: `research/notes/genus-closed-form-derived-by-riemann-hurwitz.md`
  overclaims relative to its own capture.** The note says "Status: proved",
  "153 pairs", and derives the claim from all four RH ingredients (a)–(d).
  The capture `code/out/verify_riemann_hurwitz_full.captured.txt` verifies
  171 pairs over `2<=m<n<=20`, with exact integer checks for (a) degree, (c)
  RH identity and (inf) Puiseux fibre at infinity on every pair, but the
  critical-point bisection AND the explicit smoothness check (scaled
  critical-value sets disjoint — the ingredient that rules out shared critical
  values) run only for n<=15 (91 of the 171 pairs); pairs with n>=16 take a
  structural Rolle branch without the numerical smoothness check. So the
  uniform claim "no shared critical values for all m,n" is verified on
  91 pairs and asserted structurally for the rest — `checked`, not `proved`.
  Treat the note's "proved" as an overstatement; the run's claim-level status
  for the closed form remains `checked` (`genus-single-closed-form-all-pairs`),
  and the missing piece before `proved` is the general argument that the
  critical-value sets are disjoint (or the singularity delta-invariant
  computation).
- **Internal contradiction fixed (scholar, this pass):** `established-review.md`,
  `ROOT.md`, and `singmaster-literature-exact.md` each contained a residual
  "Singmaster 1971 primary held" claim left over from before the tombstone —
  contradicting the source-integrity finding (the file is Fermat's Library
  comments, NOT the paper). All three now say "primary NOT held; attested by
  secondary sources", and the `best-unconditional-bound` /
  `singmaster-bounds-history` claims were updated to match. Also added: the
  collision-catalogue note's "BST 1999 not freely downloadable" gap is RESOLVED
  (the de Gruyter vol-1 preview is held readable) — that is a contradiction
  between an old "gap" record and the actual holdings, now reconciled.

## Gaps

- **RESOLVED: MRSTT effectiveness CONFIRMED from full text** (Remark 1.7:
  thresholds effective, unoptimized, likely too large for numerical use; verbatim
  quote and analysis live in the Established MRSTT bullet; full statement in
  `research/approaches/mrstt-exact-statement.md`).
- **RESOLVED: Witness double-failure stated.** `mrstt_leaves_witnesses_open.md`
  says both: every witness has t ≤ 24310 (fails "t sufficiently large") AND lies
  below the interior cut (small m). The region comparison is presented as
  shape-of-the-boundary, not as a claim about large-t behavior.
- **RESOLVED: Genus integrality independently verified by this run.** `repro_integrality.py`
  (EXIT_CODE=0): 638401 pairs over 1..799, ZERO odd values, both algebraic forms
  agree on 1..399; capture `code/out/integrality_reproduced.captured.txt`. The claim
  `genus-closed-form-integrality` is now `proved` (operator parity proof + this run's
  machine repro). See the Established genus-integrality bullet.
- **RESOLVED: Two zero-byte captures fixed.** `genus_falsify.captured.txt` and `pattern_fam_seqs.captured.txt` now carry one-line explanations (EXIT_CODE=1, program failed silently). Per directive 13.
- **LEDGER DISCIPLINE (running):** claims marked `proved` in CLAIMS.md are now
  `genus-closed-form-integrality` (reproduced this run), `erdos-selfridge-product-not-power-1975`,
  and `kummer-lucas-class-not-logarithmic`; the rest are `checked`/`asserted` per the table.
  Refresh the count whenever a claim's status changes.
- **PROCESS (resolved): the five formerly-uncaptured programs now have captures.**
  `test_slope_across_rows.py` (EXIT_CODE=0), `test_slope_hypothesis.py` (0),
  `effectivegenus/rep_pairs.py` (0), `genus/verify_k2_5_row.py` (0) all run
  clean; `pattern/print_family.py` is captured but dies at i=5 on Python's
  4300-digit int-str limit (family members i=1..4 printed first). The k2=5
  closed form `2n-2 / 2n-4 at 5|n` and the whole-period slope/period-diff
  structure rest on executed programs now, not on operator check alone.
  Attempt-1 process lesson: sub-delegation to `goals`/`tool_builder` timed out
  contributing nothing — the three deliverables (genus closed form, MRSTT gap
  statement, effective-methods-wall) came from direct execution. Compute
  directly; do not re-spawn the agent hierarchy.
- **RESOLVED: genus Faltings-threshold is now a claim, not a pending item.**
  The single two-parameter formula `g(m,n)=((m-1)n-(m-2)-gcd(n,m))/2` is claim
  `genus-single-closed-form-all-pairs` (`checked`, 111 values) in
  `code/out/genus_single_closed_form.md` — it supersedes the per-column grids
  and the three-diagonal salvage, and states the {2,3}/{2,4} Faltings threshold
  in closed form. What it is NOT (do not overstate): it is verified, not
  derived via Riemann–Hurwitz/Plücker; and the 23 newest rows (k2=6..10) are
  Singular-only (the Sage check errored). `proved`-status claims now also include
  `genus-closed-form-integrality`. See TASKS.md item 1.
- **RESOLVED: Matveev primary obtained.** The gap "authoritative constants of
  Matveev's theorem" is closed — full English text with C1,C2,C′0 held
  (`research/sources/matveev-2000-homogeneous-linear-form.full.md`, summary +
  claim `matveev-2000-explicit-constants-primary`). The remaining live step is
  applying Thm 2.3 (K=Q case, which applies to binomial products since the
  αⱼ are rationals/primes, D=ρ=1) to a chosen small-(k1,k2) family and
  numerically evaluating the resulting explicit bound — a GOAL-eligible
  partial result.
- The **only remaining live direction** toward a partial result: an effective
  height bound with a **computed** constant for a specific (k1,k2)
  family (Baker / linear forms in logarithms) — the realistic partial-result
  target, and now a computation rather than a missing source: **Matveev 2000**
  (Izv. Math. 62:4, held) gives the explicit constants
  `ln|Λ| > −112·2ⁿC₂C′₀D²ωln(2eB)` (Thm 2.2) and the rational/integer case
  with 2ⁿ improvement (Thm 2.3, K=Q — applies to binomial products since αⱼ
  are rationals/primes, D=ρ=1). Claim `matveev-2000-explicit-constants-primary`.
  Binding constraints: the bound grows with heights (hence with k), so it is a
  per-pair constant, not uniform (`effective-methods-wall`); GOAL.md accepts a
  per-pair effective constant stated with its k-dependence. Apply Matveev
  Thm 2.3 to one small-(k1,k2) family (e.g. (2,3) or a fixed row) and evaluate
  the bound numerically. Same shape as HPTV's effective k2=2-column result:
  per-parameter, not uniform.
- Compute policy is in place (never build the triangle; invert per small k by
  binary search; k<=log2(a); 28 CPUs; parallelise over a or (k1,k2); `timeout
  540`; state workers+range). Follow it.
