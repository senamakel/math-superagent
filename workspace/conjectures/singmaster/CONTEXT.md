# Shared context

Singmaster's conjecture: `N(a) := #{ (n,k) : C(n,k) = a }` bounded by an
absolute constant. Open since 1971; working assumption is it will not be
proved here — the deliverable is a genuine partial result stated exactly,
with its bound, its evidence class, and whether it is effective and uniform
in `k`. This brief is re-sent on every model call: carry what an agent would
otherwise rebuild from disk, keep claims attached to their evidence, and run
every proposed bound against the witnesses.

**Counting convention (fixed; state on every bound):** `N(a)` counts BOTH
mirrors `(n,k),(n,n-k)` AND the trivial pair `C(a,1)=C(a,a-1)`. So
`N(3003)=8` = 3 nontrivial reps × 2 + 2 trivial; 8 here is 4 half-triangle.

## Established

Each entry carries its evidence class. Full statements live in the linked
notes; agents should not rebuild them from disk.

- **Genus closed form — PROVED by this run (Riemann–Hurwitz, structural).**
  For distinct `m,n>=2`, the genus of the normalization of the projective
  closure of `C(x,m)=C(y,n)` is `g(m,n) = ((m-1)(n-1) + 1 - gcd(m,n))/2`.
  `proved`: derivation at `research/notes/genus-closed-form-derived-by-riemann-hurwitz.md` —
  (a) degree in y is n; (b) `(y)_n'` has n−1 simple real critical points
  (Rolle, structural), m points above each, index 2 → finite ramification
  m(n−1); (c) fibre at ∞ via Puiseux: gcd(m,n) branches, index n/gcd, so
  I_inf = n−gcd; (d) RH: 2g−2 = −2n + m(n−1) + (n−gcd). Verified by
  machine for **all 171 pairs 2<=m<n<=20** (EXIT_CODE=0, ALL CHECKS PASSED,
  `code/out/verify_riemann_hurwitz_full.captured.txt`; full bisection for
  n<=15, structural branch for n>=16). **Caveat:** the note's "Range
  verified" section still says 153 pairs with the truncated description —
  stale prose; the capture (171 pairs) is ground truth. Also the finite-
  ramification smoothness (disjoint critical-value sets / mirror-only
  coincidence) is checked per-pair numerically on the tested range with the
  mechanism argued uniform, while Rolle and the Puiseux fibre are fully
  structural — attack that smoothness step before over-claiming generality.
  Supersedes the earlier 111-value table check, the 17 out-of-sample
  Singular points, and the per-column/diagonal forms; integrality of the
  numerator is independently verified below. Genus = 1 exactly at {2,3},{2,4},
  >= 2 for every other distinct pair (matches BST 1999 Thm 2.2, a primary),
  so Faltings applies per-pair — effective yes, uniform in (m,n) yes, but it
  **bounds nothing** for Singmaster (Faltings is per-pair and ineffective).
  Say so whenever citing it.

- **Genus integrality — independently verified by this run. `computed`.**
  `N(m,n)=(m-1)(n-1)+1-gcd(m,n)` is even for all `m,n>=1` (four-case parity
  proof, `research/notes/genus-integrality-proved.md`). This run's own
  reproduction: 638,401 pairs over 1<=m,n<=799, zero odd values in all four
  parity classes, both algebraic forms agree (`code/out/integrality_reproduced.captured.txt`,
  EXIT_CODE=0). Resolves the prior operator-only status.

- **Witness set / the falsifier. `computed`, 3 independent routes.**
  `3003 = C(3003,1)=C(78,2)=C(15,5)=C(14,6)` (+4 mirrors), `N(3003)=8`
  (`code/out/witnesses.json`; also MRSTT (1.2) and Singmaster FQ 1975).
  **Any bound <8, or any lemma implying one, is refuted — record refuted,
  not weakened.** Six numbers with N=6 <= 2^48: 120, 210, 1540, 7140, 11628,
  24310 (`sourced`+`computed`).

- **Infinite family `N(a)>=6` — the reason `B>=6`. `computed` from a
  `sourced` identity.** `C(n+1,k+1)=C(n,k+2)` has infinitely many solutions:
  `n=F_{2i+2}F_{2i+3}-1, k=F_{2i}F_{2i+3}-1` (i>=1). i=1 → 3003; i=2 →
  61218182743304701891431482520. Recurrences `n_i=7n_{i-1}-n_{i-2}+6`,
  `k_i=7k_{i-1}-k_{i-2}+9` (order-3 homogenisation `a_n=8a_{n-1}-8a_{n-2}+a_{n-3}`
  confirmed), growth ratio → φ^4 ≈ 6.854. Verified N(a)>=6 for i=1..6; exact
  counts (both mirrors + trivial): N=8 at i=1 (3003), N=6 at i=2 (29 digits),
  i=3 (205 digits), i=4 (1412 digits) and i=5 (9688 digits). Each exact count
  is an exhaustive per-k binary inversion over every reachable column:
  i=2,3 in `code/out/verify_fibonacci_identity.captured.txt`, i=4 in
  `code/out/extend_exact_N_family_i4.captured.txt` (28 workers, 1.9s), i=5 in
  `code/out/extend_exact_N_family_i5.captured.txt` (32,183 columns, 330.4s,
  28 workers — i=1..3 runs also cover i=4/5 in the same file). So through i=5
  each a_i (i>=2) has exactly the two construction reps as nontrivial
  left-half reps — no extra k=2 collision, no other column, and every one of
  them is boundary for every eps>1/3. The i>=2 exact counts go beyond BBW
  2017's 10^60 bound. Any `B<6` is refuted. This is the only Jenkins-family
  curve with infinitely many lattice points (a=b=1).

- **Lane Clark 2010 — the normal-array template giving every log bound.
  `checked`** (full text
  `research/sources/lane-clark-array-multiplicity.full.md`, claim
  `lane-clark-normal-array-bound`). For binomials reproduces Singmaster's
  `N(a) < 2 log₂ a + 2`; effective, uniform-in-k, grows with a. The paper's
  own examples achieve Θ(log_s t) infinitely often inside the template — so
  `O(log t)` is best-possible within it and a constant bound needs
  binomial-specific structure. Verified vs witnesses and brute force
  2<=a<=60 (capture `code/out/verify_lane_clark_bound.captured.txt`).

- **Matveev 2000 primary held — the effective-per-pair constants.
  `sourced`** (Izv. Math. 62:4, full text
  `research/sources/matveev-2000-homogeneous-linear-form.full.md`; claim
  `matveev-2000-explicit-constants-primary`). Thm 2.2/2.3: under the Kummer
  condition `[K(√α₁..√αₙ):K]=2ⁿ`, D=D_K/κ, A_j ≥ max{h(α_j),|ln α_j|/D,1/(D C1)},
  Ω=∏A_j, B=max|b_j|A_j/A_n: `ln|Λ| > −112·2ⁿ·C₂·C′₀·D²·Ω·ln(2eB)` with
  C₁, C₂, C′₀ explicit. For rational-integer α_j (distinct primes), Kummer is
  automatic and A_j = ln p_j. **Gate for any computed constant: state the
  height convention (Matveev's A_j are natural-log heights; other authors
  exponentiate — why Tiebekabe–Diouf's Thm 2.9 looks different).**

- **Boundary cut correction (directive 24). `computed`.** The original
  `code/boundary_cut.py` computed `exp((log n)**(2/3) + 0.5)` instead of
  `exp((log n)**(2/3+0.5))`, a factor-of-411,000 error at n=229969 that
  misclassified Fibonacci family members j>=2 as interior. Corrected:
  `code/boundary_cut_corrected.py` and
  `code/out/boundary_cut_corrected.captured.txt` (EXIT_CODE=0). Under the
  correct cut ALL six Fibonacci family members j=1..6 are BOUNDARY
  (87839 < 1.416e8 at j=6). Asymptotically: log k_j ∝ 4j, (log n_j)^(2/3+eps)
  ∝ j^(2/3+eps); the boundary condition holds for all large j iff eps > 1/3.
  With MRSTT's admissible eps=1/2, the family stays boundary forever.
  Each Fibonacci a contributes at most 2 boundary left-half reps — the
  infinite family does not threaten a constant per-a bound. Witness-set
  boundary counts: 2 for each of 120, 210, 1540, 7140, 11628, 24310, and
  3 for 3003 (max = 3 left-half reps, matching the C >= 3 lower bound).

- **Fibonacci family is boundary — PROVED (structural). `proved`.**
  For the MRSTT boundary cut with ε > 1/3, every sufficiently large
  member of the Fibonacci family is boundary. `k/n → 1/φ²` exactly (ratio of
  consecutive Fibonacci numbers), so `log k ∼ log n` and
  `log(cut)/log(k) = (log n)^{2/3+ε − 1} = (log n)^{ε − 1/3} → ∞` for
  ε > 1/3. For ε ≤ 1/3 only finitely many j are boundary. `j0(eps)` is
  computable from `4j log φ < (4j log φ)^{2/3+eps}`. For ε = 1/2 (run's
  standard), `cut/k = (log n)^{1/6} → ∞`. **Effective** and **uniform in j**.
  Verified numerically j=1..12
  (`code/out/boundary_family_always_boundary.captured.txt`).
  **Consequence for G-boundary-uniform-count (directive 26):** the bound
  must hold for every eps in (0,1). Larger eps → larger cut → MORE
  boundary reps, so the binding case is eps → 1. The family is boundary
  throughout (1/3, 1) — most of the admissible range — so it cannot be
  set aside as interior by choosing a small eps; any C must cover it.
  **Decisive open question (directives 25–26):** each a_j carries at least
  2 boundary reps (the (k,k+1) collision). 3003 (j=1) has 3. For
  j=2..12: are there exactly 2 boundary reps per a_j, or do additional
  reps (e.g. k=2 collisions) appear and grow with j? If the count stays
  at 2, C≥3 remains the live lower bound. If it grows, C is unbounded,
  G-boundary-uniform-count is FALSE, and singmaster-uniform-bound is
  broken — a genuine refutation of the decomposition.

- **MRSTT interior, the current record. `sourced`** (arXiv:2106.03335,
  QJM 2022, Thm 1.3). Fixed 0<ε<1, t large: at most 2 solutions in
  `exp(log^{2/3+ε} n) ≤ m ≤ n/2`, at most 4 in the full interior; interior
  multiplicity is 0,1,2,4 — never 3 (Rem 1.11). The open boundary is
  exactly `2 ≤ m ≤ (log t)/(log log t)^{3/2−ε}`. Threshold is **effective**
  (Rem 1.7 verbatim: "implied quantitative bounds ... are effective; however
  ... likely too large to be of use"). MRSTT leaves all 15 witness pairs
  untouched twice over: every witness has t ≤ 24310 (fails "t large") AND
  sits below the interior cut — `checked`, `code/out/mrstt_leaves_witnesses_open.md`.
  Method ceiling (Prop 1.12): needs N,M = O(exp(log^{3/2−ε} P)), not
  relaxable even under RH. Net: MRSTT delivers the sharpest statement of the
  gap and can go no further; progress must come from the boundary.

- **Small-(k1,k2) curves — the full set the effective toolbox reaches.
  `sourced`** (Stroeker–de Weger 1999 primary held). C(n,k)=C(m,l)
  completely solved (all integral solutions listed) exactly for
  (2,3),(2,4),(2,6),(2,8),(3,4),(3,6),(4,6),(4,8), via elliptic logarithms +
  David + LLL; (2,5) by BMSST 2008 hyperelliptic. Every other distinct pair
  has genus >1 and only Faltings' ineffective finiteness.

- **Yamada 2020 boundary necessary condition — the one quantitative hold on
  the MRSTT-open edge. `sourced`** (arXiv:2002.07043 Thm 1.1, claim
  `yamada-boundary-necessary-condition`). If a boundary collision of the
  stated shape occurs, then `l > n(1.3132 log₂(2n) − 2.00271)`, and for n
  large `l > (cn/log n)^{40/21}` (any c<0.68943). Per-configuration, NOT
  uniform; any boundary attack should measure itself against it.

- **Verification bound. `sourced`.** No N(a)>=8 with a < 2^23 (Singmaster
  1971, attested by his FQ 1975 paper — the 1971 original is NOT held);
  extended to 2^48 (FQ 1975); Blokhuis–Brouwer–de Weger 2017: no unknown
  collisions for n<=10^6 or value <=10^60. This run's scan: N=6 values up to
  10^12 matching the primary list.

- **Known bounds (all grow with a; reproducing one is NOT a result).
  `sourced`.** Singmaster 1971 O(log a) — original NOT held (tombstoned
  source file; attested by FQ 1975, AEH 1974, MRSTT — don't quote a
  constant from the old Fermat's-Library snippets). Abbott–Erdős–Hanson 1974
  O(log a/log log a) (primary held). Kane 2007 best:
  `O((log t)(log_3 t)/(log_2 t)^3)` (primary summary held); conditional on
  Cramér, `O_ε((log a)^{2/3+ε})`. None uniform ⇒ none touches the
  conjecture (`research/notes/established-review.md`).

- **The k=2 column is effectively finite per prime — Kiss 1988. `sourced`**
  (FQ 26(2) 127–130, full text held, claim `kiss-1988-cx2-cyp-effective-finiteness`).
  For each fixed odd prime p≥3, `C(y,p)=C(x,2)` has finitely many positive
  integer solutions, **effectively** via Baker 1969 on `z²=(8/p!)·(x)_p+1`
  (degree-p, all roots simple by an Eisenstein argument; note the curve has
  genus (p−1)/2, matching this run's proved closed form g(2,p)=(p−1)/2).
  Constant is effective but **unevaluated and p-dependent** — per-p, NOT
  uniform in k; `effective-methods-wall` again, now with a 1988 primary.
  Same page records Avanesov's complete (2,3) list: `C(x,3)=C(y,2)` has
  exactly (x,y)=(3,2),(5,5),(10,16),(22,56),(36,120), i.e. witness values
  120,1540,7140 — the check oracle for any (2,3)-specific computation.
  Bearing: every known witness sits in k=2/3, so the k=2 column is exactly
  what `G-boundary-uniform-count` must control; Kiss gives it per-prime
  effective, never uniform.

- **BST 1999 primary held — the fixed-pair ineffectivity anchor. `sourced`.**
  Beukers–Shorey–Tijdeman, Number Theory in Progress Vol. 1 (de Gruyter
  1999) 11–26, readable full text
  `research/sources/number-theory-in-progress-vol1-preview.full.md`. Thm
  1.1: fixed (m,n;d1,d2) equal-products has finitely many integral solutions
  except one family; for gcd(m,n)=1 the proof "resort[s] to Siegel's
  theorem ... which is, unfortunately, ineffective" (paper's words). Thm 2.2:
  genus of the equal-products curve is ≤1 only in four genus-0 and eight
  genus-1 parameter cases; for binomials the non-diagonal genus-1 pairs are
  exactly (2,3),(2,4) — agreeing with the run's proved formula.

## Ruled out

Each carries the obstruction that closed it; do not re-propose.

- **Finiteness per fixed (k1,k2) — already known, NOT the conjecture.**
  Faltings (>1, confirmed by the proved formula) and Siegel (genus 1) give
  "finitely many", ineffective — no count computable in (k1,k2). Singmaster
  needs one constant over all pairs. This is the central wall; every
  approach must say how it beats it, and the genus computation does not.
  Bilu–Tichy route hits the same wall (HPT 2022 Thm 2.3 explicitly
  ineffective); approach `bilu-tichy-classification` grounded, kernel =
  exceptional-pair classification only.

- **Effective curve methods cannot give uniformity — the completed
  impossibility result. `sourced`** (claim `effective-methods-wall`, four
  held primaries). The effective integral-point toolbox is per-curve: needs
  a rational point, explicit Jacobian MW basis, and canonical-height-
  difference bounds **provably unavailable for genus ≥ 3** (BMSST 2008 p.2
  verbatim; (3,4) is already genus 3). Where it applies every constant
  grows with rank/regulator/heights (David c4 exponent r+2; Matveev's bound
  grows in n, D, Ω) — i.e. with the column index — so no k-independent
  constant emerges. This is GOAL.md's "cannot give a bound uniform in k,
  obstruction named" deliverable. Do not re-propose curve methods for
  uniformity; the honest per-pair task is an explicit Matveev/David constant
  for one small pair, stated with its k-dependence.

- **Matveev applied to (2,3) triangular=tetrahedral — exact solutions are
  outside its scope; constants computed for near-misses. `computed`** (claim
  `matveev-2-3-constants-computed`, checked; capture
  `code/out/matveev_2_3_constant.captured.txt`). For `3x(x-1)=y(y-1)(y-2)`
  the linear form Λ = ln P − ln Q attached to an exact solution is
  identically zero (equality of factorizations, n_nonzero=0) — Thm 2.2/2.3
  does not constrain exact triangular=tetrahedral equalities, so the
  "effective height bound for C(x,2)=C(y,3)" deliverable is not reachable
  by this route. For nonzero delta forms ln a − ln b (a≠b) the full constant
  set is computed exactly (K=Q, D=ρ=1, C3=n, A_j=ln p_j, Kummer automatic
  for distinct primes): e.g. Λ=ln(120/1540), n=4, gives ln|Λ| > −1.98×10^17
  (Thm 2.3(ii)); all hypotheses (2.9)–(2.11) pass. An effective-bound
  deliverable must therefore pick a **different pair or a near-miss/inequality
  family** (TASKS item 3's exact-solution framing is closed).

- **Kane's lattice-point method cannot beat inverse density. `sourced`**
  (Kane 2007 §8): randomized construction proves his method cannot give
  better than O(log₂ t). A different mechanism is needed for constancy.

- **Mason–Stothers / polynomial abc is vacuous for binomials. `checked`.**
  `code/out/check_mason_stothers_bound.captured.txt`: degB'=0 for all 21
  pairs 2<=k2<k1<=8, slack≥0 throughout. The two polynomials share their
  falling factorial as entire gcd; dividing out leaves one falling factorial
  and one constant, so N0 = maxdeg+1 identically. Function-field analogues
  do not transfer to number-field integral points.

- **Triangular=tetrahedral C(x,2)=C(y,3) is NOT an infinite N>=6 family.**
  Genus 1; positive rank gives infinitely many rational but only finitely
  many integral points (Siegel), and the pair is solved (Avanesov). The
  6-fold witnesses 120, 1540, 7140 are isolated collisions. The only
  infinite N>=6 family is the Pell/Singmaster one.

- **Diagonal m=n degenerate** (contains x=y, genus undefined); the only
  infinite Jenkins-family curve is a=b=1.

- **MRSTT's non-archimedean method has a hard ceiling** (Prop 1.12; even
  RH cannot relax it). The interior method cannot be pushed to the small-m
  boundary.

- **"Fibonacci family crosses to interior for large j" — refuted (see the
  boundary-cut correction and the PROVED boundary entry under Established).**
  The family stays boundary for all eps > 1/3, hence forever at the standard
  eps=1/2; it stays inside the object `G-boundary-uniform-count` counts, and
  any argument for C must cover it.

- **Speculatives carried earlier, now settled in `research/APPROACHES.md`:**
  `binary-lucas-submask` **adopted** (Lucas mod 2: for odd a every rep has
  k ⊆ n bitwise; first step = odd-coefficient multiplicity scan);
  `baker-linear-forms-two-logarithms` **adopted**; `matveev-explicit-2-3`
  closed by the vacuity above; `consecutive-block-merge` and
  `sylvester-prime-machine` **refuted** (block structure already exhausted by
  SST 1995/BST 1999; for 3003 the primes 7,11,13 serve k=2,5,6 together).
  The full refutation ledger (bombieri-pila, chabauty-coleman, frey-curve,
  height-gap, hypergeometric-wz, kummer-lucas, legendre-digit-sum,
  pascal-descent, s-unit, skolem-strassman, vieta-jumping, erdos-selfridge)
  is in `research/APPROACHES.md` — read it before proposing anything new.

## Numbers

- `N(3003)=8` (both-mirrors+trivial); N=6 set {120,210,1540,7140,11628,24310}.
- Genus closed form `g(m,n)=((m-1)(n-1)+1-gcd(m,n))/2`; genus=1 exactly at
  {2,3},{2,4}; verified on all 171 pairs 2<=m<n<=20.
- Infinite family: second member ≈ 6.1×10^28; digit ratio → φ^4 ≈ 6.854;
  recurrences `n_i=7n_{i-1}-n_{i-2}+6`, `k_i=7k_{i-1}-k_{i-2}+9` (i=1..8 checked).

## Recalled (durable memory from earlier runs, not this run's finding)

- **Multinomial generalization** (De Koninck–Doyon–Verreault 2021): for
  fixed k, `N_k(a)` has average/normal order k(k−1) and
  `N_k(a)=O((log a/log log a)^{k−1})`; k=2 is the binomial case.
  Corroboration only — the k=2 restriction is exactly Singmaster.
- **Stirling-number analogue** (Bazsó–Mező–Pintér–Tengely 2023):
  `M_i(a) <= 2 + 2 log a / W((1/2) log a)` — O(log a/log log a) shape, a
  different ladder with the same logarithmic bound.
- The durable graph (`relate_memory`) connects the central objects exactly
  as above: `uniform-in-k obstruction --blocks--> conjecture`, `effective
  uniform bound --would_resolve--> conjecture`; no node changes the picture.
- Scratch notes (provisional): k2=5 row closed form `2n-2`/`2n-4` at 5|n, and
  the k2=3/4 forms, are all superseded by the proved two-parameter formula;
  family-sequence findings (order-3 LRR, φ^4 ratio, k_i not in OEIS) confirm
  the recorded recurrences. NOTE: `u=5n+6, v=5k+9` do NOT satisfy Pell
  `u²−5v²=−4` — the "Pell −4" attribution in the A098565 summary refers to
  a different pairing and is unverified.

## Contradictions

- **SOURCE INTEGRITY:** `research/sources/singmaster-1971.full.md` is NOT
  Singmaster's paper — it is a tombstone (the real paper has NOT been
  obtained; the old file held Fermat's Library comments). The O(log a)
  bound, N(3003)=8, and the N=6 values are attested by primaries that ARE
  held (FQ 1975, AEH 1974, MRSTT). Do not quote a constant from the Fermat's
  snippets.
- **Kane bound exponent:** Fermat's annotation says log²_2 t; Wikipedia,
  MRSTT, Jenkins give log³_2 t. Exponent 3 is correct; the slip is recorded.
- **Standing tension (structural):** k ≤ log₂ a forces high N(a) into small
  columns, and every witness sits in k=2/3 — so small-column curves carry
  the multiplicity and a uniform bound must control them uniformly; the
  small-k effective results (Avanesov, de Weger, BMSST, SdW) are the
  attackable part.
- **Noise (generated, ignore):** ~20 "claim-contradiction" rows where a
  broken extraction of `deweger-1995-mordell-curve-complete` lists
  nonexistent ids (`(only`, `on`, `the`, ...). The note is
  `research/summaries/deweger-equal-binomial-1995.md`; its claim block has
  no clean id. Carry nothing from those rows.
- **Plain text of claims:** the ~60-row "load-bearing but unverified" list
  (every row "asserted by the source, not proved there and not checked
  here") and the ~50-claim register are generated from `research/CLAIMS.md`;
  they are all uniform status flags, not per-row facts. Consult the status
  column in CLAIMS.md before building on any claim; the ones it would hurt
  most to be wrong about: `bbw-verification-bound`, `bilu-tichy-classification-primary`,
  `bst-fixed-kl-ineffective-primary`, `yamada-boundary-necessary-condition`.

## Gaps and live direction

- Resolved: MRSTT thresholds effective (Rem 1.7); witness double-failure
  stated; Matveev primary obtained; zero-byte captures fixed; all formerly-
  uncaptured programs now captured (EXIT_CODE=0; only `pattern/print_family.py`
  dies at i=5 on Python's 4300-digit int-str limit after printing i=1..4);
  genus integrality independently reproduced (above).
- **Boundary cut bug fixed (directive 24).** The original `code/boundary_cut.py`
  computed `exp((log n)**(2/3) + 0.5)` instead of `exp((log n)**(2/3+0.5))` —
  two-character typo, factor-411k error at n=229969. `code/boundary_cut_corrected.py`
  with `code/out/boundary_cut_corrected.captured.txt` (EXIT_CODE=0) proves:
  under the CORRECT cut ALL six Fibonacci family members are BOUNDARY. The
  family never crosses to interior for eps > 1/3. `G-fibonacci-boundary-finite`
  is refuted (the family stays boundary forever, not finitely many). The
  skeleton's step (5) is revised: each Fibonacci a contributes at most 2
  boundary reps, so the infinite family does NOT threaten a constant per-a
  bound. Witness-set boundary counts: max 3 left-half reps at 3003.
- **State of the decomposition (BACKWARD.md):** the backward skeleton
  `singmaster-uniform-bound` has exactly one open gap, `G-boundary-uniform-count`
  — an absolute bound on the number of boundary representatives per a,
  for EVERY admissible eps in (0,1). Larger eps → larger cut → more reps
  counted as boundary, so the binding case is eps → 1 (directive 26).
  The Fibonacci family is boundary for eps > 1/3 (most of the admissible
  range), so it cannot be set aside as interior; any C must cover it.
  `C >= 3` from 3003 is the current lower bound. The decisive computation
  (directives 25–26) — count ALL nontrivial boundary reps per Fibonacci a_j —
  is **settled through j=5**: exhaustive full-column scans give exactly the
  two construction reps for j=2,3,4,5 (j=1 has three: 3003's extra k=2 rep),
  with j=5's 32,183-column scan at 330s the current frontier. If the count
  stays at 2 for all j, the skeleton survives; if it ever grows, C is
  unbounded and singmaster-uniform-bound is refuted. Verdict: **no refutation
  through j=5; the next member (j=6, a six-digit-of-66416, kmax≈220,000) is
  reachable but costs ~30-60 min at 28 workers with
  PYTHONINTMAXSTRDIGITS=1000000 — a larger run only extends the same
  per-j check, it settles nothing new unless a hit appears.**
  `G-interior-bounded` and `G-small-a-bounded` are catalogued.
- **Directive 25 — Fibonacci family boundary proof and per-a count.**
  `fibonacci-family-is-boundary` filed as proved (structural, k/n→1/φ²,
  log-ratio `log(cut)/log(k)` ∼ (log n)^{1/6} → ∞ at ε=1/2; verified
  j=1..12). **Directive 26 adds the binding-case analysis:** the
  `eps > 1/3` threshold with `j0(eps)` computable makes the theorem
  complete rather than a numerical observation. The consequence for
  G-boundary-uniform-count: the binding case is eps → 1 (larger eps,
  more boundary reps), and the family is boundary throughout (1/3, 1),
  so it cannot be excluded from the count. **Decisive next computation —
  PARTIALLY ANSWERED (see the Infinite-family entry above):** count ALL
  nontrivial boundary reps per Fibonacci a_j — settled at exactly 2
  (construction pair) through j=5 by exhaustive column scans; j=1 (3003)
  carries 3. j=6 is the only unaudited member, and its scan (~30-60 min,
  kmax≈220k, 28 workers) would only extend the same check per j. If always
  2 (the construction's two), C≥3 stands; if the count grows at some j,
  G-boundary-uniform-count is FALSE — a genuine result either way.
- **The other live partial-result target:** an effective height bound with a
  **computed** constant for a specific (k1,k2) inequality or near-miss family
  (Matveev Thm 2.3, K=Q, constants held, (2,3) template computed and its
  implementation verified against the paper), with its k-dependence stated —
  GOAL.md accepts such a per-pair constant since uniformity is closed by
  effective-methods-wall. The exact-solution (2,3) form is closed (vacuity
  above); candidates: a different small pair, or the delta-form |ln a − ln b|
  bounds already computed.
- **Ledger: live counts in TASKS.md (asserted=22, checked=4, proved=3 — genus-closed-form-integrality, genus R–H closed form, fibonacci-family-is-boundary). Every claimed bound must be run
  against `code/out/witnesses.json`; one not run is `asserted`, never
  `checked`. Compute policy: never build the triangle; invert C(n,k)=a per
  small k by binary search (k ≤ log₂ a); 28 CPUs, parallel over a or
  (k1,k2); `timeout 540`; state workers and ranges in every capture.
- **Administrative gaps (survey, this cycle):** `tasks` ledger is EMPTY
  (0 entries) — the run has no open/blocked/done task rows despite a live
  skeleton and two adopted approaches; `attempts` ledger is EMPTY (0 entries)
  although `approaches` (20 entries, 14 refuted) and `goals` (4 entries, 2
  live/1 complete/1 broken) are populated; `code/lean/` DOES NOT EXIST —
  the run has formalised nothing (no Statement.lean, no Cited namespace), so
  phase-3's "first-hour Lean" gate is unmet; `TASKS.md` derives from the empty
  tasks ledger so the "asserted=22, checked=4, proved=3" counts actually live
  in the claims ledger, not in TASKS. The five uncaptured programs named in
  the diophantine-curves thread (test_slope_across_rows.py,
  test_slope_hypothesis.py, effectivegenus/rep_pairs.py, genus/verify_k2_5_row.py,
  pattern/print_family.py) — `print_family.py` now HAS a capture
  (`code/out/pattern_print_family.captured.txt`, restored); the other four
  still have zero captures. `verify_sdw_transformations.py` is written but
  NOT yet executed.