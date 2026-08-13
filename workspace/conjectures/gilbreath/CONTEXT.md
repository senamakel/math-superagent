# Shared context

What this run knows, in its own words. Carries what an agent would otherwise
rebuild from disk: established results with their basis, dead approaches and
why, computed numbers, durable memory, and disagreements. Not a file catalogue
(`research/INDEX.md` is that) and not a narration of activity.

Budget 10,000 tokens (this file ~5,900 — ~4,100 under). Length is a bill the
whole run pays on every model call; link the file holding any detail compressed
away.

**Run state (Directive 25 complete): geometric ×1.68/event and sublinear
exponent 0.388 are reconciled — observed ratios b_{i+1}/b_i decline toward 1
with b, so the geometric factor is a finite-sample description, not an
asymptotic law.** Directive 24 items 1–2 DONE: k\* = 162
(`code/out/directive24_width_degradation.md`), geometric R²=0.94 vs linear
0.78 over the 12 genuine giants (`code/out/directive24_geometric_growth.md`).
Directive 25 items 3–4 DONE (claim `directive25-gap-trend-and-reconciliation`,
checked): inter-giant gaps (genuine 12) = 22,8,4,26,2,14,2,14,4,4,12 rows,
mean 10.18, median 8, max 26, no trend (Spearman ρ vs prior b = −0.141; OLS
R² ≤ 0.11 both fits) while b spans 2,179 → 1,094,273; the 11 consecutive ratios
decline 3.9 → 1.49 toward 1, tracking rho = 1+C·b^(α−1) (α=0.388, C_pool=802.6;
log-residual MSE 0.140 sublinear vs 0.154 geometric — neither decisive on 12
points, the decline is the sublinear direction). **Operative target restated:
the conjecture follows if the inter-giant gap G_k grows strictly slower than
b^0.388** (G_k < j_k ≈ C·b_k^0.388); measured G ≤ 26 vs C·b^0.388 ~ 10–10³ —
orders of slack at depth 1000; only a larger width (more giants) separates
bounded-gap from growing-gap, and this run cannot (cap). Mean-rate route
superseded; do not cite D=40 smoke. Also this cycle: sign-coherence /
forward-difference identity REFUTED at its base step (Ruled out).

## Established

- **The whole conjecture = "the second entry of every row lies in {0,2}".**
  `A_1=(1, even, even, ...)` because 2 is the only even prime; the shape
  (odd, even, even, ...) is preserved by the absolute-difference operator; and
  `A_{k+1}(0)=|1-A_k(1)|` is 1 iff `A_k(1)∈{0,2}`. **Proved** (parity
  induction), checked over full rows to depth 599. If ever `A_k(1)=4` (any
  even ≥4) the conjecture dies that row. Anchor: `research/notes/reduction.md`.
- **Oracle exists and is checked.** `witnesses.json` (33860 primes) reproduces
  problem.md's rows A_1..A_5 exactly; depth 600,
  `second_entry_always_0_or_2=true`; second-entry sequence reproduces OEIS
  A089582's 105 terms exactly. Depth 1000 (sieve 2e7, 1.27e6 primes):
  `first_bad=None`. Anchors: `code/out/witnesses.json`,
  `code/out/blocks_depth1000.json`.
- **Odlyzko's block lemma — RE-DERIVED AND PROVED by this run.** A leading
  `{0,2}` block of length `n` (positions 1..n) forces `A_{k+d}(1)∈{0,2}` for
  d=0..n−1 and `A_{k+d}(0)=1` for d=0..n: **exactly n+1 rows; the protection
  constant is 1, not the ≈n/2 in problem.md/ROOT.md** (n/2 refuted — appears
  in no source). Proved by a diagonal-subtriangle argument; verified
  exhaustively over all 2^n patterns with adversarial even completions,
  n=1..11 (122,820 pairs, zero violations); real rows to depth 600 regenerate
  far past the guarantee. GOAL.md deliverable. The subtriangle apex is the
  Sierpinski/XOR-fold of the block's bit pattern. Anchor:
  `research/notes/block_lemma.md`. **Regeneration is the sole obstruction** —
  row k+n's position 1 needs `A_k(n+1)`, outside the block, which the lemma
  does not force.
- **Rule 90 interior dynamics — PROVED.** Within any {0,2} block, halved
  entries evolve under XOR (= Wolfram Rule 90 = Pascal mod 2): |a−b|/2 =
  (a/2) XOR (b/2); after d descents the halved entry is XOR_{j=0}^{d}
  [binom(d,j) mod 2]·(A_K(p+1+j)/2). Verified exhaustively n ≤ 13; confirmed
  independently by CHT 2026 §1 and Wikipedia. At d = 2^j the kernel is all-1
  (XOR of a full window). **Split from the refuted absorption wrapper** — the
  interior identification says nothing about when the boundary regenerates;
  the timing corollary is CLOSED null (Ruled out). Anchor:
  `research/notes/block_lemma.md`,
  `research/approaches/rule90-absorbing-boundary.md`.
- **Big-jump characterisation — DONE (Directive 23): the giants are genuine.**
  Of the 13 (2,4)-events with j > 1000 at depth 1000, 12 are genuine dynamics
  (landing floors 176,186..1,268,392; heavy tail j>10^4: 9 genuine of 10) and
  only **i=161 is the width artifact** (b_162 = 1,270,444 = W−162−1; true jump
  ≥ 176,181 — quote as a lower bound, never exact). Genuine giants carry 86.1%
  of S_1000=1,270,603; all 13 carry 99.76%. Giant rows: 34,56,64,68,94,96,
  110,112,126,130,134,146,161. Rows k ≥ 162 are the width-exhaustion artifact:
  **every block/jump/event measurement at rows ≥ 162 is a LOWER BOUND** (j at
  i=161 recorded as ≥ 176,181; flooring falls 176,182 → 0 at k\* = 162 and all
  12 genuine giants sit ≥ 536,885 above the threshold — none width-limited).
  Claim `bigjump-cap-characterization-1000`; anchors
  `code/out/bigjump_characterization.captured.txt`,
  `code/out/bigjump_characterization.notes.md`.
- **Ducci literature (four primary papers) — cyclic boundary drawn.** All
  classical Ducci theorems are CYCLIC (wraparound); nilpotence-iff-power-of-2,
  cycle structure, no-uniform-bound do NOT transfer to the half-infinite
  Gilbreath operator (Eppstein's escape is the witness). What transfers: the
  mod-2/Pascal law (= this run's proved rule90-interior-xor, now in four
  peer-reviewed sources) and Chamberland's factored-max +
  rigidity-equality-case template — the shape any surviving potential must
  take, since raw run-count potentials are dead. Anchor:
  `research/notes/library-state.md` Ducci section.
- **Step law + recharge identity — PROVED as theorems of the absolute-difference
  operator for ANY array (no parity, no primes).** With intruder pair
  (x,y)=(row[b_k], row[b_k+1]), `b_{k+1} ≥ b_k ⟺ (x,y)=(2,4)`, else
  `b_{k+1} = b_k − 1` (erosion exactly 1 per row); recharge identity
  `b_k = b_1 + Σ_{events i<k}(j_i+1) − (k−1)` (j_i = jump) — the `−(k−1)` term
  IS the Odlyzko protection constant 1; (2,4)-events are the only growth
  mechanism. **Narrowed target: the conjecture holds iff (2,4)-events arrive so
  fast that Σ(j_i+1) never falls k−1 behind.** Corollaries (proved): drain law
  `y_{k+1} = y_k − 2·[x_k=2]`; intruder-4 absorbing under erosion. Verified on
  primes (depth 1000, 60 events) and 400 random nonneg arrays (3,521 rows, 610
  events, zero failures). Anchor: `research/notes/step_law_proved.md`, claim
  `step-law-theorem-proved`. Do not re-derive — only the (2,4)-event RATE is
  open.
- **Regeneration criterion — ESTABLISHED (exact, oracle-checked).** Edge
  `e_k = A_k[b_k]` (last {0,2} value — index b_k, not b_k−1; the off-by-one
  that earlier made this look refuted), intruder `c_k = A_k[b_k+1]`. Then
  `b_{k+1} ≥ b_k ⟺ (e,c)=(2,4)`, zero failures over all 998 transitions, exactly
  60 regeneration events. Intruder==4 is necessary not sufficient (36 erosion
  rows also have y=4). c_k ≥ 6 forces b_{k+1}=b_k−1 exactly (proved corollary:
  |e−c| ∈ {c−2,c} ⊄ {0,2}). Anchor: `code/out/check_regenerate_lemma.captured.txt`,
  thread `research/threads/regeneration.md`.
- **Conditional-rate experiment — DONE (Directive 19).** Post-startup (k>10)
  event rate is family-independent: pooled λ̂ = 0.585 (1098/1876), Pearson X²
  p = 0.68 over 8 families, D=400, W=200000. **λ̂ is MEASURED, not bounded
  below for all k; and it is a MEAN, the wrong summary for the heavy-tailed
  jump distribution (Directive 23) — do not build a mean-rate bound.** Claim
  `conditional-rate-experiment-family-independent`; anchors
  `code/out/conditional_rate_experiment.notes.md`.
- **Mod-4 linearization (invariant candidate, mod 4 is the ceiling).**
  For k≥1, n≥2 (entries even), `d_{k+1}(n) ≡ d_k(n)+d_k(n+1) (mod 4)`
  (Odlyzko §2 eq.201); CHT Lemma 3.10 generalises mod 2. The lift to mod 2^t
  fails at t=3 (`|2−6|=4 ≢ 0 (mod 8)` vs 2+6=8≡0) because the free congruence
  holds iff the smaller entry is divisible by 2^{t−1}; mod 4 conflates 0↔4 and
  2↔6 — exactly the failure values to exclude. The mod-4 level is the run's
  best algebraic handle; nothing higher works.
- **CHT 2026 inverse theorem (sourced).** (Chase–Hunter–Tao, arXiv:2607.08712)
  The only ways an array with small non-negative initial data can fail to decay
  to {0,1} are **long zero-blocks** and **long shallow {0,d}-blocks (d≥2)**.
  Either rule those out for the primes (needs Cramér + analytic hypotheses,
  unproved) or find an invariant bypassing the dichotomy. Random analogue
  (Thm 1.3): i.i.d. geometric Cramér model satisfies a.s. {0,1} — strongest
  heuristic support, not a proof for primes. **Hypothesis check — DONE,
  holds-here = no**: max normalized gap a_n = 89 → M=7, longest 0-run L=2,
  R_0 = 100·L·8^M ≈ 4.2e8 ≫ 1000, so the inverse theorem does not bite at any
  reachable depth. Do NOT re-run. `code/out/cht_hyp_check.captured.txt`.
- **Generalisation families sourced.** Li 2026 modulo-k (primes kn+2, leading
  entry stabilises to k; asserted-by-source); Croft's bounded-gap
  generalisation FALSE via Eppstein; Chase 2024 random analogue = Math. Ann.
  388, arXiv:2005.00530. **2-separation is the operative general-class
  hypothesis** (Ross 2026, consistent with CHT (ii), Eppstein): not "gaps
  slowly growing" but "gaps do not concentrate in a 2-separated set".
- **Probabilistic-prime-gap grounding landed (Banks–Ford–Tao 2023).** The
  canonical peer-reviewed source behind the random-analogue input (Chase 2024,
  CHT 2026, Tao-blog Cramér model) is now in the library: *Large prime gaps
  and probabilistic models*, Invent. math. 233 (2023) 1471–1518, open access,
  doi 10.1007/s00222-023-01199-0. Full text at
  `research/sources/maier-pomerance-2023-large-prime-gaps-probabilistic-models.full.md`
  (filename is a misnomer — authors are Banks, Ford & Tao; the file header
  records the correction). Summary + claim `bft2023-cramer-model-canonical` at
  `research/summaries/banks-ford-tao-2023-large-prime-gaps-probabilistic-models.md`.
  Content: Cramér's model (each n≥3 in with prob 1/log n, independent) gives
  largest gap ~ log²x a.s.; Granville's model ~ ξ log²x (ξ=2e^{-γ}=1.1229.);
  a new random-sieve model satisfies uniform Hardy–Littlewood (Thm 1.3) and an
  RH analogue (Thm 1.4), largest gap g((ξ±ε)log²x); any set obeying uniform HL
  has large gaps (Thm 1.5/1.6). **Caveat the run must keep:** the plain Cramér
  model demonstrably fails for real primes (prime-k-tuple residue bias; Maier's
  short-interval phenomenon), so a random-model → primes transfer is heuristic
  support, not proof. This does NOT settle Gilbreath; it fixes the model and
  its limits. Cramér's own 1936 paper is quoted therein; its scanned full text
  is unobtainable by this converter (repository records under
  `research/summaries/cramer-19*.md`), content grounded through this paper +
  Chase 2024 + CHT 2026.
- **Parity wave (proved, Ross 2026):** any (2, odd, odd, ...) sequence has every
  row's leading term odd — but odd is NOT 1 (witness 2,3,13 → leading 9). The
  conjecture lives strictly between "odd" and "1". **{0,d} closure double edge
  (proved, one line):** {0,d} is closed under absolute differencing for every
  d≥2, so the mechanism pinning 1 at d=2 is also the mechanism preserving large
  disturbances at d≥4 (the CHT obstruction).
- **Verification record, kept distinct:** run's own depth 600 (33860 primes)
  and depth 1000 (1.27e6 primes); literature (sourced, not reproduced):
  Killgrove–Ralston 1959 to 63,419 primes (<792,722); Odlyzko 1993 to 10^13
  (G=635); Plouffe 2025 to 10^14; Colonna 2025–26 to 1.5×10^15 (G=800). Do not
  conflate.
- **Restricted classes proved (this run, from the reduction's mechanism):**
  consecutive odds; any sequence with `A_1=(1,2,2,...,2)`; any triangle
  reaching a row `(1,c,c,c,...)`, c∈{0,2} — leading 1 persists forever from
  there. These prove the mechanism but not that regeneration is entered
  infinitely often.
- **`block_profile(k) = A000232(k) − 1`**, checked against the OEIS b-file for
  k=1..16; the shifted sequence is **uncatalogued** (nobody re-search). No
  closed form from the catalogue.
- **Gilbreath-polynomial route (alternate handle, UNVERIFIED).** MDPI
  Mathematics 2023, 11(18), 4006 claims GC follows from `p_n − 2^{n−1} ≤
  P_{n−1}(1)` for a "Gilbreath polynomial" over weighted factorials. Page
  returns HTTP 403, no arXiv mirror — asserted-by-source only. Worth the
  inventor's attention; do not re-fetch blind. Anchor:
  `research/notes/library-state.md` claim `gilbreath-polynomials-imply-gc`.

## Ruled out

- **Gatti 2020 "prime-class proof" — REFUTED (invalid Theorem 4; full text in
  library).** Gatti's *Gilbreath's Sequences...* (Preprints 202003.0145.v1)
  proves the global valid-extension formula (`k = ±s^{n−1}_1 ± … ± s^1_{n−1}
  + s_n ± 1`) and parity alternation Lemmas 1–3, but Theorem 4's `min K ≤
  p_n ≤ max K` proof assumes its own conclusion and derives only a trivial
  `min K ≤ α` via Bertrand; its Lemma 4 interval-completeness is false in
  general (Muney's length-5 hole; even `dim K_S = 2^{n−1}` fails at {2,3,5}:
  |K_S|=5 — machine-checked this run, two independent programs). **So no
  published deterministic bounded-gap or prime-class theorem exists.**
  Claims `gatti-2020-theorem4-proof-invalid`,
  `gatti-2020-lemma4-interval-completeness-refuted`,
  `gatti-2020-valid-extension-global-formula`. Anchor:
  `research/sources/gatti-2020-preprints-gilbreath-conditions.full.md`.
- **LLM-era claimed "proofs" — all not-load-bearing, do not cite.** Granville
  2026 "Piercing Gilbreath's Conjecture" (arXiv:2607.04166, cs.CR — fintech
  author, NOT the number theorist), Maréchal 2025, ZARKOUNA 2026: claim
  preprints with no checkable mechanism; no peer review. Claims
  `granville-2026-piercing-gilbreath-not-load-bearing` etc.
- **Small gaps alone do NOT suffice (Eppstein 2011, sourced, quoted in CHT).**
  For any unbounded monotone f(n)≥2 there is a 2-then-odds sequence with gaps
  ≤ f(n) whose right edge switches between 1 and other values infinitely often.
  **Kills the blanket "general class with gaps bounded by g" strategy** — a
  general-class theorem needs non-concentration (CHT's 2-separated condition)
  or restriction to the primes. Sharpener (`colonna-deletion-left-edge-failure`,
  asserted): deleting 5 (or 7) from the primes gives a 2-then-odds sequence
  with gaps ≤ 4 (≤ 6) whose second entry is 4 — a concrete row-2 failure; only
  gaps ≤ 3 is un-refuted as a plain bounded-gap class.
- **Proth's "failed proof" is a retracted myth — no error to locate.** GOAL.md's
  item rests on a claim its originator H.C. Williams retracted (email 2020,
  quoted in Chase 2024 §7): Proth's paper states the property as a theorem
  with no proof; Catalan's note calls it a postulate. GDZ with a JS-capable
  browser is the only remaining route; no further offline fetch.
- **Randomness is necessary, not optional:** Chase 2024 constructs exotic
  {0,3}-style sequences where the {0,1} result fails — evenness/2-then-odds
  alone is not enough.
- **Rule 90 uniform boundary absorption — REFUTED.** The claimed bounded
  absorption of any intruder v≥4 adjacent to a long {0,2} block fails in the
  2-then-odds class: CHT Lemma 3.7(iii) shows {0,d}-valued blocks persist in
  all descendants without decrease; Eppstein escapes arbitrarily. The interior
  identification survives; the absorption mechanism is dead. Anchor:
  `research/approaches/rule90-absorbing-boundary.md`. **Timing corollary —
  CLOSED (null):** the relative-depth form (21/27 within tol=1 of a power of
  2) gives p=0.0173 exact binomial, dead at tol=0 (p=0.113) and erased by
  conditioning on [2,9] (p=0.68) — mild, tolerance-dependent, not structural.
- **Raw run-count potential r(T) ≤ r — MACHINE-REFUTED in the actual
  regime.** Exhaustive over 6,725,600 strings (len ≤ 8, values 0..6): fails
  (first counterexample (6,6,6,6,6,6,5,5); worst (0,0,1,1,0,0,1,1)); fails
  even in the halved {0,1} interior — minimal counterexample (0,0,1,1) →
  (0,1,0), the halved form of (0,0,2,2) inside the leading {0,2} regime.
  (a,a,c,c) is exactly Chamberland's rigid Ducci equality case where the
  factored-max potential stalls. `runcount-lemma-refuted`. Only a corrected
  weighted/max-factored potential (Chamberland's template) survives, untested.
- **Block-apex pattern-class forcing — REFUTED.** Mixed blocks do not force
  intruder reduction: CHT Lemma 3.7(iii) proves a {0,d}-valued block persists
  in ALL descendants regardless of pattern, and depth-1000 data shows
  regeneration fires on (edge, intruder)=(2,4) and nothing else (60/60 regens
  at y=4, 0/65 at y≥6). Do not re-propose. Anchor:
  `research/approaches/block-apex-parity-forcing.md`.
- **Prime-gap mod-6 structure — REFUTED as a constraint machine.** The operator
  has NO reduction mod 3 (|a−b| mod 3 is not a function of the residues:
  witness (0,1)/(3,1)); "H_k(1) mod 3 ∈ {0,1}" is the conjecture restated.
  Anchor: `research/approaches/prime-gap-mod6-structure.md`.
- **Mod-4 linearization cannot be lifted — mod 4 is the ceiling** (see
  Established: |a−b| ≡ a+b (mod 2^t) holds iff smaller entry ≡ 0 (mod
  2^{t−1}); fails at t=3). Any invariant on a higher modulus is dead. Anchor:
  `research/approaches/mod4-pascal-invariant.md`.
- **Sign-coherence / forward-difference linearization — REFUTED at its base
  step (this cycle; `code/out/check_fwd_diff_identity.captured.txt`, claim
  `fwd-diff-identity-refuted`).** `A_k(i) = |Δ_k(i)|` (Δ_k = signed k-th
  forward difference) is FALSE on the primes: first violation at (k,i)=(3,2) —
  |Δ_3(2)|=4 vs A_3(2)=0, inside the leading {0,2} block; first at position 1
  is k=4 (|Δ_4(1)|=6 vs 2). Mechanism: |u−v| = ||u|−|v|| iff u·v ≥ 0; the
  signed triangle oscillates [4,−4,4,−4] where the rows are constant 0.
  Sampler: 60 random 2-then-odds, all fail within 3 rows (D_1(i)=−gap_i, so
  any local extremum of the gap sequence kills it — the primes have one at
  i=2: gaps 2,4). Any linearization must survive (k=3, i=2).
- **Backward-extension automaton and minimal-counterexample geometry —
  REFUTED (valid-extension criterion is global, not local).** Alkan et al.
  2023 (factorial-weighted K-criterion) and Muney 2026 (order-sensitive
  subset-sum analogue; interior holes at length 5) both reach over the whole
  prefix; a bounded SAT/SMT encoding is either the global criterion (as hard
  as the conjecture) or strictly weaker. Muney's valid-extension set
  re-describes the regeneration obstruction instead of resolving it. Anchors:
  `research/approaches/backward-extension-automaton.md`,
  `research/approaches/minimal-counterexample-geometry.md`.

## Numbers

- **Event-rate sweep over the 2-then-odds class — DONE.** 1154 sequences, 26
  families × seeds, D=600..4000, W=2e5..2e6, 26 workers, wall 278 s, exact
  int64. Step law + recharge identity fail **0 times** across all (46,528
  eligible rows, 20,013 events) — universal in the class. **852/1154 (73.8%)
  reach b_k=0, ALL within the first 10 rows (90% by k≤3)** — death is g_0
  startup, not asymptotic (Directive 16 resurrected Route A). Full detail:
  `code/out/event_rate_sweep.notes.md`.
- Block profile (leading {0,2} length) rows k=1..40: `2,7,13,13,24,23,22,21,24,
  58,97,96,97,96,173,175,175,175,175,290,289,288,739,873,872,871,872,871,870,
  869,868,867,866,865,2179,2178,2177,2176,2770,2769`. Growth by doubling bursts
  around k=15,20,23,35,39.
- Depth 1000 stats: min b=2 (k=1), max b=1,270,444 (k=162); 60 regeneration
  events in 999 transitions; max jump 360,698 (k=146); intruder min 4, max 14,
  59.6% exactly 4, all ≡0 or 2 mod 4. **All 60 regen rows had intruder==4,
  but intruder==4 is NOT sufficient** (36 erosion rows also have it).
- **CORRECTION: the "/838-row pure-erosion run" is a finite-width artifact.**
  At k=162 the block fills the whole remaining sieve row; k=162..999 is the
  block retracting one column per row as width runs out. Genuine longest
  pure-erosion run is **13** (k=97..109). Claims built on "regeneration
  survived 838 erosion rows" are void. `code/out/regeneration_analysis.captured.txt`.
- **Fact (a): block minima grow — `[13,24,96,97,175,2762,5939,31525,31533,
  31534,733574,1094263]`**, smallest 13 (k=3). **Fact (b): regeneration is
  real but NOT monotone** (97→96, 871→872, 21→24 occur).
- **Regeneration mechanism at boundary level (computed, not proved):** all 60
  regenerations fire at (x,y)=(2,4); y∈{6,...,14} never regenerate (0 of 65);
  y drains monotonically by 2 per x==2 step to 4 and sticks; after regen the
  new intruder is 4 in 43/59 cases; 33/60 events adjacent to another regen
  (self-exciting; runs test z=−3.94); 17 maximal y=4-runs (lengths 1..15),
  every run ends in regeneration; regen rate by b-bucket falls 1.00 (b<10) →
  0.20 (b≥10^6); jump sizes median 4.5, 35/60 ≤ 1, 5 ≥ 10^5; big jumps
  correlate with big b (r=0.771), recover ~1.2–2× the block. The 5 structural
  facts a theorem must explain: `research/notes/regeneration_data.md`.
- **Recharge surplus is heavy-tailed (Directive 23).** S_1000 = 1,270,603 vs
  required 998; the tail (9 jumps > 10^4, largest 360,698 at i=146) carries
  the surplus — a mean rate is the wrong summary. **Giants are NOT
  erosion-recovery** (mean gap before big jumps 3.54 vs 2.48 before small;
  arrive 1–13 rows after the previous event); each giant jump ≈ current b
  (total recharge ≈ width of final row); jumps grow sublinearly with b
  (log-log slope 0.388). Rule-90/power-of-2 correlate for these rows refuted
  (B2: 9/13 next-regen at power-of-2-ish offset vs null 0.81). Anchors:
  `code/out/surplus_renewal_structure.md`,
  `code/out/surplus_renewal_table.captured.txt`.

## Recalled

Durable memory holds: the reduction (= `research/notes/reduction.md`), the
oracle generator (`code/lib/gilbreath.py` reproduces the five rows exactly),
the Odlyzko 1993 full text (block lemma, mod-4 linearization, verification
bounds; claim `odlyzko-1993-citation-confirmed`), and — this direction's
originality — **no held source studies the growth rate of b_k, jump
distributions, or a renewal treatment** (claim `block-growth-literature-not-covered`;
never cite literature for a growth-rate claim — prove it yourself). All
recalled claims agree with what this run has independently computed; none with
failing hypotheses is relied on.

## Contradictions

- **Block-protection constant: n/2 vs N — RESOLVED by proof.** /ROOT.md/
  reduction.md say "≈n/2"; the primary sources and this run's re-derivation
  give **1** (n+1 rows). Stale n/2 wording may survive in notes; treat the
  proved n+1 as correct.
- **"General-class" framing vs Eppstein.** ROOT.md commits the run to the
  general class, but Eppstein refutes the broad bounded-gap version of that
  plan; Colonna's g=4 deletion sharpens it further (Ruled out). Unresolved:
  the class must be carved down (non-concentration) or restricted to primes.
- **`research/CLAIMS.md` is a generated ledger** (contradictions section clean,
  one real row: `odlyzko-block-lemma-exact` vs `odlyzko-block-lemma-asserted`);
  `research/notes/library-state.md` is the authoritative hand-maintained ledger.

## Gaps

- **The live question: prove the inter-giant gap is o(b^0.388).** Step law +
  recharge reduce the conjecture to Σ_{i<k}(j_i+1) ≥ k−1−b_1. Under j ~
  C·b^0.388, b_next/b = 1 + C·b^(−0.612) → 1, so the geometic description is
  finite-sample; the conjecture follows if every giant jump exceeds the rows
  consumed since the previous giant (G_k < C·b_k^0.388). Measured G ≤ 26 with
  1.5–3 orders of slack; **a larger width that yields more giants is the only
  thing that separates bounded-gap from growing-gap — this run cannot.**
  Claim `directive25-gap-trend-and-reconciliation` (checked, depth 1000 only).
  The whole growth/renewal direction is original to this run
  (`block-growth-literature-not-covered`); λ̂=0.585 mean-rate and
  "giants keep arriving" framings are superseded by the gap-vs-jump inequality.
- **CHT inverse theorem route needs two analytic steps for the primes:** rule
  out long zero-blocks and long shallow {0,d}-blocks (Cramér-type, unproved).
  A proof bypassing that dichotomy is the alternative.
- **What remains toward a GOAL.md partial result:** block lemma delivered
  (constant 1); Lean 4 formalisation delivered (nine theorems, zero sorry,
  axiom footprint [propext, Classical.choice, Quot.sound], IFF equivalence;
  claim `lean-reduction-machine-checked` — the {0,2} statement is exactly as
  hard as the conjecture, reformulates rather than reduces). Still open: a
  proved invariant forcing A_k(1)∈{0,2}; a general-class theorem (must beat
  Eppstein AND the Colonna g=4 deletion failure); a proved statement on the
  regeneration rate.
- **Library search halted by directive.** FRONTIER.md restored from commits
  twice (Gatti wrapper page, Colonna/DeepMind re-downloads); the documented
  URL filter did not run on those rewrite writes — re-check the candidate
  count after any further write before trusting FRONTIER.md. No downloads
  until a specific gap is stated in research/REQUESTS.md.