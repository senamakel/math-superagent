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

- **Genus grid — the complete two-parameter Faltings threshold. `computed`, two
  independent CAS engines agree on the original 8x11 grid and the k2=3,4,5
  extended rows (Singular `normal.lib::genus` and Sage `Curve.genus` output
  identical). The 23 rows added since (k2=6 n=13..18, k2=7..10 n=13..19) rest
  on Singular alone — the Sage check errored (`NameError: name 'PolynomialRing'
  is not defined`) and never ran. Do not describe the new rows as independently
  verified.** `genus(k1,k2)` of `C(x,k1)=C(y,k2)`
  computed for 2<=k1,k2<=12, extended to k1=24 for k2=3,4,5; outputs identical.
  This **supersedes** the operator's three-diagonal salvage
  (`code/out/genus_closed_forms.md`, now corroboration only).
  **Faltings threshold: genus = 1 exactly for {2,3} and {2,4}; genus >= 2 for
  every other distinct pair.** So Faltings applies to essentially every distinct
  pair — the complete answer to the GOAL.md deliverable.
  This delivers the Faltings threshold but NOT a uniform bound — per-pair
  finiteness is ineffective. Full grid in `code/out/genus_table.captured.txt`;
  approach in `research/approaches/genus-computation.md`.
  **Closed forms verified against every computed entry (k1<=24).**
  `{2,n}`: `y(y-1)=2C(x,n)` hyperelliptic, `genus=floor((n-1)/2)`.
  `{3,n}`: `Y^3-Y=6C(x,n)` (Y=y-1) cyclic-trigonal, `genus=n-1` if 3∤n else `n-2`.
  Both rows now have a primary anchor: the superelliptic Riemann–Hurwitz formula
  `g=((d−2)(m−1)+m−gcd(m,d))/2` (m=2,3; Sutherland 2020 eq. (1),
  Shorey–Tijdeman) — claim `superelliptic-genus-formula`, `checked` — so the
  {2,n}/{3,n} closed forms are explained, not merely fitted.
  `{4,n}`: 2:1 cover of `w^2=1+24C(x,n)` via `w=y^2-3y+1`, `genus=3(n-1)/2`
  (n odd), `3(n-2)/2+1` (n≡2 mod 4), `3(n-2)/2` (n≡0 mod 4).
  **`{5,n}` now established:** `genus = 2n-2 except 2n-4 when 5|n` — exact on
  all 19 points n=6..24, zero mismatches, operator-checked.
  **Slope conjecture established.** Mean first-difference over WHOLE periods is
  exactly `(m-1)/2` for m=2,3,4,5, with period-m diff patterns:
  m=2: [0,1]; m=3: [1,0,2]; m=4: [1,2,0,3]; m=5: [2,2,2,0,4]. Operator-checked,
  zero mismatches. **Trap:** a truncated window (not a whole number of periods)
  gives a mean below `(m-1)/2` and looks like a refutation. State periodicity
  first, mean second.
  **Diagonal closed forms (operator salvage, supplementary corroboration).**
  `g(n)=(n−1)(n−2)/2` for `C(x,n−1)=C(y,n)`; `g(n)=⌊(n−1)(n−3)/2⌋` for
  `C(x,n−2)=C(y,n)`; `g(n)=⌊(n+1)(n−1)/2⌋` for `C(x,n+2)=C(y,n)` — all 55
  points fit with zero mismatches (claim `genus-closed-forms-three-diagonals`,
  `checked`). These are three diagonals of the full two-parameter table now
  established above; the three Singular runs used to compute them each
  terminated `halt 1` (partial outputs of errored runs), while the genus_table
  grid was computed with both Singular and Sage and completed cleanly.
  Consistent with BST Thm 2.2: the only non-diagonal genus-1 pairs are (2,3)
  and (2,4). These are the structural small-column content — the k=2/3 columns
  that carry all multiplicity.

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

- **Small-(k1,k2) curves solved effectively. `sourced`.** (2,3) Avanesov;
  (2,4) de Weger/Pintér (Gelfond–Baker); (3,4) de Weger genus-3 double cover of
  `Y^2+Y=X^3-X`; (2,5) BMSST 2008 hyperelliptic. Finiteness for each fixed pair
  via Beukers–Shorey–Tijdeman (Siegel) — **ineffective**. Kiss 1988:
  `C(x,2)=C(y,p)` finite for p prime.

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
- Genus grid (Singular == Sage): k2=2 → floor((k1-1)/2); k2=3 → 1,3,4,7,9
  (k1=2..10 even); k2=4 → 1,3,6,7,9,12,13,15; k2=5 → 2,4,6,10,12,14,16,16,20,22; etc.
- Infinite family second member ~6.1e28; digit ratio → phi^4 ≈ 6.854.
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
Pintér–Tengely 2023) and the OEIS row-count convention `oeis-a003016-row-count`.

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
- **LEDGER STATUS: 43 claims — 41 asserted, 7 checked, 2 proved.** Every asserted bound must
  be run against `code/out/witnesses.json`. Any lemma implying B<8 is refuted by
  3003 (8 occurrences). State counting convention on every claim. Every new
  claim must say whether its bound is effective and whether it is uniform in k.
  The genus formula is neither and its claim block says so; keep that discipline.
  See TASKS.md.
- **PROCESS: Five uncaptured programs (directive 7).** `test_slope_across_rows.py`,
  `test_slope_hypothesis.py`, `effectivegenus/rep_pairs.py`,
  `genus/verify_k2_5_row.py`, `pattern/print_family.py` — all have zero captured
  output. Their conclusions are already operator-checked (k2=5 closed form, slope
  conjecture) but a program never executed is not evidence. Run or tombstone them.
- **PENDING CLAIM: genus table needs a standalone claim.** `genus_table.captured.txt`
  is the definitive two-parameter Faltings threshold (two-CAS agreement, 2<=k1,k2<=12,
  k2=3,4,5 extended to k1=24). It supersedes the operator's three-diagonal salvage
  and should be its own claim marked `proved-by-two-CAS` — the GOAL.md deliverable,
  not a capture file. See TASKS.md item 1.
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
  are rationals/primes, D=ρ=1). Claim `matveev-2000-explicit-constants`.
  Binding constraints: the bound grows with heights (hence with k), so it is a
  per-pair constant, not uniform (`effective-methods-wall`); GOAL.md accepts a
  per-pair effective constant stated with its k-dependence. Apply Matveev
  Thm 2.3 to one small-(k1,k2) family (e.g. (2,3) or a fixed row) and evaluate
  the bound numerically. Same shape as HPTV's effective k2=2-column result:
  per-parameter, not uniform.
- Compute policy is in place (never build the triangle; invert per small k by
  binary search; k<=log2(a); 28 CPUs; parallelise over a or (k1,k2); `timeout
  540`; state workers+range). Follow it.
meout
  540`; state workers+range). Follow it.
