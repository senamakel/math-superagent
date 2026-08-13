# Shared context

What this run knows, in its own words. Carries what an agent would otherwise
rebuild from disk: established results with their basis, dead approaches and
why, computed numbers, durable memory, and disagreements. Not a file catalogue
(`research/INDEX.md` is that) and not a narration of activity.

Budget 10,000 tokens (this file ~6000, so ~4000 under). Length is a bill the
whole run pays on every model call; link the file holding any detail compressed
away.

**Run state: erosion settled, step law exact, focus is event-rate lower bound.**
The conjecture reduces to: do (2,4)-events keep arriving fast enough that
`Σ (j_i + 1)` never falls `k−1` behind? A lower bound on the event rate, even
under a stated hypothesis on prime gaps, is a real result. Erosion verification
is no longer useful; the step law is exact and needs no re-derivation.
`research/threads/rule90-regeneration.md` — the absolute-depth and jump-timing
forms are refuted; the relative-depth measure (depth from regime start) gives
21/27 near a power of 2 at tolerance 1; the null is COMPUTED (see the
Rule-90-relative-depth bullet under Established): p = 0.0173 against the exact
binomial Binomial(27, 9/16), but the signal is tolerance-dependent — dead at
tol=0 (p = 0.113) and erased by conditioning on the observed [2,9] range
(p = 0.68). Verdict: a mild concentration, not a structural mechanism. The
Rule 90 interior identification is proved and unaffected.
Anchor: `code/out/rule90_depth_test.captured.txt`, `code/out/rule90_depth_results.json`.
Live thread: `research/threads/regeneration.md` (event-rate bound).

## Established

- **Verification record, CURRENT (sourced this cycle, 4 data points kept distinct):**
  Odlyzko 1993 to 10^13 (G=635); Plouffe 2025 to 10^14 (arXiv:2510.06688); Colonna
  2025–26 to 1.5×10^15 (G(2.8e14)=788, G(6.15e14)=800, G(1.5e15)=800). Run's own: depth
  1000 (1.27M primes), depth 600 (33860 primes). Do not conflate.
- **Run-count potential monotonicity — REFUTED by machine, in the actual
  regime.** The candidate Lyapunov function r(T(x)) ≤ r(x) (number of maximal
  constant runs) is false even for the strings the triangle lives in. The
  on-disk verifier `code/out/check_runcount_lemma.py` (written, never run)
  was executed: exhaustively over 6,725,600 strings (len ≤ 8, values
  0..6) the first counterexample is (6,6,6,6,6,6,5,5): r 2 → 3. A second,
  class-restricted exhaustive run (`check_runcount_lemma_class.captured.txt`)
  enumerates the classes the rows actually occupy — all-even {0,2,4,6}
  strings, halved {0,1,2,3} strings, halved {0,1} strings — and the lemma
  fails in each, with the minimal counterexample (0,0,1,1) → (0,1,0) (2 runs
  → 3), the halved form of the {0,2}-block interior string (0,0,2,2). So the
  failure occurs inside the very leading-{0,2} regime the conjecture
  targets. Claim `runcount-lemma-refuted` upgraded from hand-counterexample
  (which used odd-valued (5,5,0,0), technically outside the class) to
  machine-checked, and the approach
  `research/approaches/total-variation-oscillation-potential.md` updated:
  raw r/t potentials are dead; only a corrected weighted/max-factored
  potential (Chamberland's Ducci template) survives, untested. Captures:
  `code/out/check_runcount_lemma.captured.txt` (exit 1),
  `code/out/check_runcount_lemma_class.captured.txt` (exit 0).
- **Parity wave (proved, Ross 2026):** any (2, odd, odd, ...) sequence has every row's
  leading term odd — but odd is NOT 1. Witnesses: 2,3,13 → leading 9; every-sixth-prime
  pyramid leading column 2,15,9,7,5,3,1,1,1,1,1,7,3. The conjecture lives strictly
  between "odd" and "1".
- **{0,d} closure double edge (proved, one line):** {0,d} is closed under absolute
  differencing for every d≥2, so the mechanism pinning 1 at d=2 is also the mechanism
  preserving large disturbances at d≥4 (the CHT obstruction).
- **2-separation is the operative general-class hypothesis** (Ross 2026; consistent with
  CHT condition (ii) and Eppstein): not "gaps slowly growing" but "gaps do not
  concentrate in a 2-separated set" (no two consecutive integers). Odlyzko's
  "sufficiently random" left undefined; Chase 2024 gives the first rigorous form.
- **Generalisation families now sourced:** Li 2026 modulo-k (primes kn+2, leading entry
  stabilises to k; verified odd k<100,000; preprint, asserted-by-source); Croft's
  bounded-gap generalisation FALSE via Eppstein (now triple-sourced: Eppstein, CHT,
  Wikipedia); Chase 2024 random analogue = Math. Ann. 388, arXiv:2005.00530.
- **Continuous-model decay:** CHT Σc_i ≥ log(n+e) (c_i decays no faster than 1/i;
  boundedness open); Ross 2026 exact rational c_4,c_5,c_6, empirical
  c_i ≈ C·λ^{s_2(i)}/i, λ≈1.14–1.20.

- **The whole conjecture = "the second entry of every row lies in {0,2}".**
  `A_1=(1, even, even, ...)` because 2 is the only even prime; the shape
  (odd, even, even, ...) is preserved by the absolute-difference operator; and
  `A_{k+1}(0)=|1-A_k(1)|` is 1 iff `A_k(1)∈{0,2}`. **Proved** (elementary
  parity induction), and numerically checked over full rows to depth 599 + the
  stored slices (`code/out/check_reduction.py`). If ever `A_k(1)=4` (any even
  ≥4) the conjecture dies that row. Anchor: `research/notes/reduction.md`.
- **Oracle exists and is checked.** `witnesses.json` (sieve to 400000, 33860
  primes) reproduces problem.md's rows A_1..A_5 exactly; depth 600,
  `second_entry_always_0_or_2=true`, `min_leading_02_block=2`. Pushed to depth
  1000 (sieve to 2e7, 1.27e6 primes): `first_bad=None`. Anchor:
  `code/out/witnesses.json`, `code/out/blocks_depth1000.json`.
- **Odlyzko's block lemma — RE-DERIVED AND PROVED by this run.** A leading
  `{0,2}` block of length `n` (positions 1..n) forces `A_{k+d}(1)∈{0,2}` for
  `d=0..n−1` and `A_{k+d}(0)=1` for `d=0..n`: **exactly `n+1` rows guaranteed
  to begin with 1; the protection constant is 1 (one row per block entry),
  not the ≈n/2 in problem.md/ROOT.md** (the n/2 claim is refuted — appears in
  no source). Proved by a diagonal-subtriangle argument; verified exhaustively
  over all `2^n` block patterns with adversarial even completions, n=1..11
  (122,820 pairs, zero violations), sharpness for n=1..8; real rows to depth
  600 show zero violations and regenerate far past the guarantee (median 492
  rows margin). Consistent with Odlyzko 1993 §2 and Killgrove–Ralston 1959.
  This is a GOAL.md deliverable ("block lemma re-derived with its constant
  made explicit"). The subtriangle apex is exactly the Sierpinski/XOR-fold of
  the block's bit pattern. Anchor: `research/notes/block_lemma.md`.
  **Regeneration is still the sole obstruction** — row k+n's position 1 needs
  `A_k(n+1)`, outside the block, whose reduction to `{0,2}` the lemma does not
  force.
- **Rule 90 interior dynamics — PROVED.** Within any {0,2} block, halved
  entries evolve under XOR (= Wolfram Rule 90 = Pascal mod 2). For a,b ∈ {0,2},
  |a−b|/2 = (a/2) XOR (b/2). After d descent steps inside a block of length n
  starting at row K, the halved entry is (A_{K+d}(p+1)/2) = XOR_{j=0}^{d}
  [binom(d,j) mod 2] · (A_K(p+1+j)/2). This is the Sierpinski/Pascal-mod-2
  structure of the subtriangle, proved by the block-lemma diagonal argument and
  verified exhaustively over all 2^n patterns for n ≤ 13. Independent
  confirmation from CHT 2026 §1 (Sierpinski note) and Wikipedia (Rule 90;
  same Pascal/mod-2 structure as the run's mod-4 linearization — independent
  confirmation of the microscope).
  **This structure is now split from the refuted absorption wrapper** (which
  claimed a uniform boundary-absorption bound — refuted by CHT Lemma 3.7(iii)
  and Eppstein 2011). The proved Rule 90 core stands alone: at d = 2^j,
  binom(2^j, m) ≡ 1 (mod 2) ∀m, so the halved entry is the XOR of the whole
  width-(2^j+1) window (Sierpinski kernel all-1). **The regeneration-TIMING
  corollary is CLOSED by the null test** (claim `rule90-relative-depth-null`,
  `code/rule90_test/null_rule90_depth.py`, capture
  `code/out/null_rule90_depth.captured.txt`): the absolute-depth and
  jump-timing forms are refuted by the depth-1000 record; the relative-depth
  measure gives 21/27 within tol=1 of a power of 2, which against the exact
  binomial null Binomial(27, 9/16) (uniform over the observed [0,15], with
  the program's depth>0 guard) is p = 0.0173 — significant at 5%, not at
  1% — and the signal lives entirely in the tol=1 tolerance: at tol=0 only
  10/27 hit (p = 0.113), and conditioning on the observed concentrated range
  [2,9] post hoc gives p = 0.68. The permutation null is degenerate (the
  predicate tests depth values, not positions). Net: a mild,
  tolerance-dependent concentration, not a structural regeneration
  mechanism. The interior-XOR identification is about values inside the
  block; it says nothing about when the boundary regenerates.
  Thread: `research/threads/rule90-regeneration.md` (CLOSED).
  Anchor: `research/notes/block_lemma.md` (apex) and
  `research/approaches/rule90-absorbing-boundary.md` (the absorption dead end).
- **Regeneration criterion — ESTABLISHED (depth 1000, exact, oracle-checked).**
  Block occupies 0-based cols `1..b_k`; intruder `c_k = A_k[b_k+1]` (first value
  past block), edge `e_k = A_k[b_k]` (the last `{0,2}` value — index `b_k`, not
  `b_k-1`; the off-by-one that earlier made this look refuted). Then
  `q_k = A_{k+1}[b_k] = |e_k - c_k|` satisfies: `q_k ∈ {0,2} ⟺ (e==2 and c==4)`
  and `b_{k+1} ≥ b_k ⟺ (e==2 and c==4)`, **zero failures over all 998
  transitions, exactly 60 regeneration events** (matches the long-standing
  count). 838 no-intruder rows (block runs to end of row) always have
  `b_{k+1}<b_k` (in fact `b_{k+1}=b_k−1`), so the iff holds across all 998.
  This resolves "intruder==4
  necessary not sufficient": among 96 intruder-4 rows the 60 with edge 2
  regenerate and the 36 with edge 0 erode. So regeneration = the block ends in
  2 with a 4 immediately past it — a single-row local fact, not an artifact,
  but the mod-4/why-it-recurs content is still open (edge 2 + intruder 4 means
  columns b_k,b_k+1 sum to 2 mod 4 giving q=2). **Proved corollary (matches
  durable memory): `c_k ≥ 6` forces `b_{k+1}=b_k−1` exactly** — `|e−c| ∈ {c−2,c}
  ⊄ {0,2}` kills position b_k of the next row, and the erosion bound
  `b_{k+1} ≥ b_k−1` gives the other side. Anchor:
  `code/regeneration/check_regenerate_lemma.py`,
  `code/out/check_regenerate_lemma.captured.txt`, thread
  `research/threads/regeneration.md`.
- **Step law + recharge identity — ESTABLISHED (independent re-derivation).**
  With the intruder pair `(x,y)=(row[b_k], row[b_k+1])`, exactly:
  `b_{k+1} ≥ b_k ⟺ (x,y)=(2,4)`, and `b_{k+1} = b_k − 1` otherwise (the
  erosion rate is exactly 1 per row, not "≥ b_k−1"). The recharge identity
  `b_k = b_1 + Σ_{events i<k}(j_i+1) − (k−1)` (j_i = jump at event) is exact:
  the `−(k−1)` term *is* the Odlyzko protection constant 1, and the `(2,4)`-
  events are the *only* growth mechanism. **This is the narrowed target**:
  the conjecture holds iff `(2,4)`-events arrive so fast that `Σ(j_i+1)` never
  falls `k−1` behind. Verified by a fully independent implementation (own
  sieve/generation/block measure) on primes < 3·10⁶ (216,816 primes) to depth
  800: 0 step-law failures over 799 transitions, 0 recharge failures, 42
  events, min b=2, margin 216,812 vs 798 consumption (≈272× surplus — but
  recharge ≈ row width, so a single event refills nearly the whole block and
  the surplus must not be read as a trend). Also confirmed: the **drain law**
  `y_{k+1} = y_k − 2·[x_k=2]` on erosion steps (101/101) — and the step law
  **holds on random non-prime arrays** (3,521 rows, 610 events, zero failures),
  so these are combinatorial facts about the absolute-difference operator,
  provable outright, with primes entering only through event density. Caveat
  carried by the claim's hypotheses: the law needs an intruder pair to exist
  (`b_k+1 < row width`); when the block runs to the end of a *finite* row
  there is no pair, and that row erodes by 1 — the finite-width artifact
  documented under Numbers. Anchor:
  `code/out/step_law_and_recharge_verified.md` (claim `step-law-and-recharge-identity`). Do not re-derive.
- **Mod-4 linearization (invariant candidate).** For k≥1, n≥2 where entries are
  even, `d_{k+1}(n) ≡ d_k(n)+d_k(n+1) (mod 4)` (Odlyzko §2 eq.201). Turns the
  absolute-value problem into linear Pascal-triangle congruences mod 4 — the
  cleanest algebraic handle the run has. CHT Lemma 3.10 generalises:
  `a(i,j) ≡ Σ_k C(i,k) a_{j+k} (mod 2)`.
- **Gilbreath-polynomial route (alternate handle, UNVERIFIED).** MDPI Mathematics 2023, 11(18), 4006 claims GC follows from `p_n − 2^{n−1} ≤ P_{n−1}(1)`, where `P_{n−1}` is a "Gilbreath polynomial" over weighted factorials built from the first n primes. Sourced-by-search-digest only; the MDPI page returns HTTP 403 to the downloader, no arXiv mirror, author list unconfirmed — treat as asserted-by-source until the text is obtained. Gives a genuinely independent route (a size bound vs p_n) rather than block regeneration, worth the inventor's attention. Do not re-fetch the 403 page blind. Anchor: `research/notes/library-state.md` claim `gilbreath-polynomials-imply-gc`.
- **CHT 2026 inverse theorem (sourced).** (Chase–Hunter–Tao, arXiv:2607.08712,
  submitted 9 Jul 2026) The only ways an array with small non-negative initial
  data can fail to decay to `{0,1}` are **long zero-blocks** or **long shallow
  {0,d}-blocks (d≥2)**. This restates the consumption/regeneration obstruction
  sharply: the run must either rule those two structures out for the primes
  (needs Cramér + analytic hypotheses, both unproved) or find an invariant
  bypassing the dichotomy. Random analogue (Thm 1.3): i.i.d. geometric Cramér
  model satisfies the a.s. `{0,1}` result — strongest known heuristic support,
  not a proof for primes (independence is only conjectural there).
- **Verification bounds, kept distinct.** Run: 33860 primes / depth 600 and
  1.27e6 primes / depth 1000. Literature (sourced, not reproduced here):
  Killgrove–Ralston 1959 to 63,419 primes (<792,722); Odlyzko 1993 to
  `π(10^13) ≈ 3.4×10^11` rows. Do not conflate.
- **Restricted classes proved (this run, from the reduction's mechanism):**
  consecutive odds; any sequence with `A_1=(1,2,2,...,2)`; any triangle
  reaching a row `(1,c,c,c,...)`, c∈{0,2} — leading 1 persists forever from
  there. These are the "regeneration already complete" corner cases; they
  prove the mechanism but not that regeneration is entered infinitely often.
- **`block_profile(k) = A000232(k) − 1`**, checked against the OEIS b-file for
  k=1..16; the shifted sequence itself is **uncatalogued** (OEIS lookup
  returned no match — nobody should re-search). No closed form available from
  the catalogue; the growth must come from the mathematics.

## Ruled out

- **"Regeneration iff lemma" — earlier REFUTED records are WITHDRAWN
  (off-by-one in the edge index); the corrected criterion is ESTABLISHED.**
  Both old "Ruled out" lines treated regeneration as non-local — they were the
  same bug. `check_regenerate_lemma.py` ran two readings over the real rows to
  depth 1000. The literal reading `e=A_k[b_k-1], q=A_{k+1}[b_k-1]` fails
  (141 id-mismatches, 109 iff-failures on 161 intruder rows) — that is the
  "refutation", recorded in `code/out/check_regenerate_lemma.notes.md`. The
  corrected reading `e=A_k[b_k], q=A_{k+1}[b_k]` (correct because
  `A_{k+1}[j]=|A_k[j]-A_k[j+1]|`, so the diff partner of the intruder is
  `A_k[b_k]`) has **zero failures over all 998 transitions**. Regeneration IS
  the single-row local property `(e==2, c==4)` — see Established. Do not let
  the stale notes off-by-one refutation block this or re-derive it.
- **Small gaps alone do NOT suffice (Eppstein 2011 anti-Gilbreath, sourced,
  quoted in CHT).** For any unbounded monotone `f(n)≥2` there is a "2 then
  odds" sequence with gaps ≤ f(n) whose triangle's right edge switches between
  1 and other values infinitely often. **This kills the blanket "general class
  with gaps bounded by g" strategy** that problem.md/GOAL.md hoped could settle
  the prime case as a corollary: the 2-then-odds parity plus a gap bound is
  genuinely insufficient. A general-class theorem needs an extra
  randomness/non-concentration hypothesis (CHT's 2-separated-set condition) or
  must be restricted to the actual primes. Any approach claiming the bounded-gap
  class must first state how it beats Eppstein's construction.
- **Proth's "failed proof" is a retracted myth — there is no proof to locate
  an error in.** GOAL.md's item "locate the error in Proth 1878" rests on a
  claim its originator H.C. Williams retracted (email 2020, quoted in Chase
  2024 §7): Proth's actual paper states the property as a theorem and gives no
  proof; Catalan's appended note calls it a postulate. The corrected result is
  the retraction itself. The GDZ scan is JS-blocked (recorded unobtainable);
  content covered by two independent reader accounts.
- **Randomness is necessary, not optional:** Chase 2024 constructs exotic
  {0,3}-style sequences where the `{0,1}` result fails — evenness/2-then-odds
  alone is not enough.
- **Rule 90 uniform boundary absorption — REFUTED.** The approach in
  `research/approaches/rule90-absorbing-boundary.md` claimed a bounded
  absorption time reducing any intruder v≥4 to {0,2} adjacent to a long
  {0,2} block. Refuted for the 2-then-odds class: CHT Lemma 3.7(iii) shows
  {0,d}-valued blocks persist in all descendants without decrease, and
  Eppstein 2011 constructs small-gap sequences whose right edge escapes
  arbitrarily. The Rule 90 interior identification is proved and survives
  independently (see Established); the absorption mechanism is dead.
  Recorded: `research/approaches/rule90-absorbing-boundary.md`.
- **Mod-4 linearization cannot be lifted — mod 4 is the ceiling.** The lift
  `|a−b| ≡ a+b (mod 2^t)` holds over even entries iff `2·min(a,b) ≡ 0
  (mod 2^t)`, i.e. the smaller entry divisible by `2^{t−1}`. It holds at t=2
  (min of two evens is even) and fails at t=3 (`|2−6|=4 ≢ 0 (mod 8)` vs
  `2+6=8 ≡ 0`). So mod 4 is the ceiling; mod 4 conflates 0↔4 and 2↔6 — exactly
  the failure values the conjecture must exclude — and CHT say the mod-2 parity
  level "will not be used directly" (only parity, never the exact {0,2}).
  Any invariant built on a higher modulus is dead; the mod-4 level itself is
  still the run's best algebraic handle (see Established). Anchor:
  `research/approaches/mod4-pascal-invariant.md`,
  `code/research_mod_check/check_mod_lift.py`.
- **Backward-extension automaton and minimal-counterexample geometry —
  REFUTED (the valid-extension criterion is global, not local).** Alkan et al.
  2023 (factorial-weighted K-criterion) and Muney 2026 (valid-extension set =
  order-sensitive subset-sum analogue with interior holes, smallest at length 5
  for (2,3,5,9,15)) both give criteria that reach back over the whole prefix —
  no bounded window determines whether a row extends into `{0,2}`. The trap
  state hope is Eppstein's class defeat; a bounded SAT/SMT encoding is either
  the global criterion (as hard as the conjecture) or strictly weaker. Muney's
  valid-extension set is the backward analogue of the leading `{0,2}` block and
  re-describes the regeneration obstruction instead of resolving it. Anchors:
  `research/approaches/backward-extension-automaton.md`,
  `research/approaches/minimal-counterexample-geometry.md`.

## Numbers

- Block profile (leading {0,2} length) rows k=1..40:
  `2,7,13,13,24,23,22,21,24,58,97,96,97,96,173,175,175,175,175,290,289,288,739,873,872,871,872,871,870,869,868,867,866,865,2179,2178,2177,2176,2770,2769`.
  Grows roughly by doubling bursts around k=15,20,23,35,39.
- Depth 1000 stats: min b=2 (k=1), max b=1,270,444 (k=162); 60 regeneration
  events in 999 transitions; max single jump 360,698 (k=146); intruder (first
  value past the block): min 4, max 14, 59.6% exactly 4, all ≡0 or 2 mod 4;
  b never stays at 2 (jumps 2→7 by k=2). **All 60 regeneration rows had
  intruder==4, but intruder==4 is NOT sufficient**: 36 non-regen (erosion)
  rows also have intruder==4, so regen ⟹ intruder 4 at depth 1000, converse
  false.
- **CORRECTION: the "/838 rows / 838-row pure-erosion run" is a finite-width
  artifact, not genuine dynamics.** At k=162 the block fills the whole
  remaining finite sieve row (b=1,270,444 = width−1, intruder becomes None);
  the "run" k=162..999 is the block retracting one column per row as the
  finite prime list runs out of width to the right. Genuine live-regime
  longest pure-erosion run is **13** (starting k=97, ending 109). Any claim
  built on "regeneration survived 838 erosion rows" is void; that number is a
  boundary effect. Source: `code/out/regeneration_analysis.captured.txt` (Q3).
- **Fact (a): Block length never approaches 0 — minima grow.** Record of
  minima: `[13,24,96,97,175,2762,5939,31525,31533,31534,733574,1094263]`.
  Smallest after the first few rows is 13 (k=3). Dwell at each minimum is
  1–4 rows. The block length is not merely bounded away from 0, it
  *increases* across the computed range.
- **Fact (b): Regeneration is real but NOT monotone.** 97→96 (k=13), 871→872
  (k=26), 21→24 (k=8) all occur — consumption and regeneration alternate. The
  block can shrink before growing. Source: `code/out/regeneration_analysis.captured.txt`.
- **Regeneration mechanism, characterised at boundary level (computed, not
  proved).** Over the live regime k=1..161 (the only rows where the intruder
  exists), ALL 60 regenerations fire at rows with intruder y=4 and obey
  exactly `(x,y)=(2,4)` for x=last block entry (verified 60/60 by
  erosion_dynamics). Rows with y∈{6,8,10,12,14} NEVER regenerate (0 of 65).
  During erosion, y drains monotonically (drops 2 per x==2 step: 33 drops,
  68 stays; never up), reaching 4 and sticking; regeneration is the event
  (x==2, y==4). After a regeneration the new intruder is 4 in 43/59 visible
  cases (next event regen); when ≥6 it drains to 4 within ≤12 rows and then
  regenerates. Jump-0 stalls (17) are always followed by regeneration;
  33/60 events are adjacent to another regen (self-exciting; runs test
  z=−3.94 over k=1..161, n1=60). 4-runs: 17 maximal runs of consecutive
  y=4 rows, lengths {1,2,3,3,4,4,6,7,11,12,12,15}, every run ends in a
  regeneration (x flips 0↔2 inside a run, explaining the 36 non-regen y=4
  rows; max consecutive non-regen y=4 rows is 6). Regen rate by b-bucket
  decreases with b (1.00 at b<10, 0.58, 0.45, 0.37, 0.31, 0.36, 0.20 at
  b≥10⁶). Jump sizes: median 4.5, 35/60 ≤ 1, 5 jumps ≥10⁵ (max 360,698 at
  k=146); big jumps correlate with big b (r=0.771) and recover ~1.2–2× the
  block. Full table + the 5 structural facts a theorem must explain:
  `research/notes/regeneration_data.md`.

## Recalled

Durable memory now holds: the reduction (= the run's `research/notes/reduction.md`),
the oracle generator (`code/lib/gilbreath.py` reproduces the five rows exactly,
depth 600 / 33860 primes), and the Odlyzko 1993 full text (block lemma, mod-4
linearization, verification bounds). These are recalled, not this run's fresh
findings, but they agree with what this run has independently computed. No
recalled claim is relied on whose hypotheses fail here.

## Contradictions

- **Block-protection constant: n/2 vs N — RESOLVED by proof.** `problem.md`/
  `ROOT.md`/`reduction.md` phrase the lemma as "≈n/2 rows protected"; the
  primary sources (Odlyzko 1993 §2, Killgrove–Ralston 1959) and this run's own
  re-derivation (`research/notes/block_lemma.md`) give constant **1**: a block
  of length n protects n+1 rows. The n/2 claim (claim `odlyzko-block-lemma-asserted`)
  is **refuted** — stale n/2 wording may survive in notes; treat the proved n+1
  as correct.
- **"General-class" framing vs Eppstein.** ROOT.md commits the run to the
  general-class side, but Eppstein's anti-Gilbreath refutes the broad
  bounded-gap version of exactly that plan. The honest position: the class must
  be carved down (add non-concentration/randomness, or restrict to primes), and
  this is unresolved.
- **`research/CLAIMS.md` is a generated ledger with a broken contradictions
  section** (a long claim block gets mis-parsed into spurious "contradicts"
  rows). `research/notes/library-state.md` is the authoritative, hand-maintained
  claim ledger and holds the same content formatted correctly — read
  library-state.md for the current ledger.

## Gaps

- **The live question: bound the (2,4)-event rate from below.** The step law and
  recharge identity (`code/out/step_law_and_recharge_verified.md`) reduce the
  conjecture to: `Σ_{i<k} (j_i + 1) ≥ k − 1 − b_1` for all k. Since `b_1=2`,
  this is a statement about event frequency and jump sizes. A theorem of the
  form "under hypothesis H, events arrive at rate ≥ r, and r suffices" is a
  real partial result. Two routes: combinatorial (bound max erosion between
  events from Rule 90 + drain law) and analytic (bound event density from prime
  gap hypotheses). Measure inter-event gap distribution first.
  **Census (computed, negative): the boundary-data sequences — block profile
  b(k), second entries s(k), regen jumps, regen gaps — show NO low-degree
  polynomial, NO constant-coefficient linear recurrence of order ≤8, and NO
  OEIS match. Do not re-search for recurrence structure.** Event record is
  small: 60 events, live regime k=1..161 (beyond that is the finite-width
  artifact). A wider record (sieve ~1e8, ~5.7M primes, ~1–2 min) is cheap but
  pointless without a specific rate claim to test.
  Threads `research/threads/regeneration.md` and
  `research/threads/rule90-regeneration.md`.
- **CHT inverse theorem route needs two analytic steps for the primes**: rule
  out long zero-blocks and long shallow `{0,d}`-blocks (Cramér-type hypotheses
  unproved). A proof bypassing that dichotomy is the alternative.
- **What remains toward a GOAL.md partial result:** the block lemma is
  delivered (re-derived, constant explicit). Still open: a proved invariant
  forcing `A_k(1)∈{0,2}`; a theorem for a general class of sequences (must beat
  Eppstein); a proved statement on the regeneration rate; and the Lean 4
  formalisation of the difference operator and induction step (with `#print
  axioms` and every `sorry`). No Lean work is on disk yet.
- **Library search halted by directive.** FRONTIER.md is at 309→345 with
  checked at 3. No more downloads until a specific gap is stated that a source
  could close.
- **CHT Theorem 1.6 hypothesis check — DONE, holds-here = no.** Computed on
  sieve 2e7 (1,270,607 primes): max normalized gap a_n = 89 → M = 7, longest
  0-run L = 2, so R_0 = 100·L·8^M = 419,430,400 ≈ 4.2e8 ≫ 1000. The
  no-{0,d}-block hypothesis is not satisfiable at any reachable depth, so the
  CHT inverse theorem does not bite here. `code/out/cht_hyp_check.captured.txt`, claim `cht-inverse-theorem-hyp-check`. Do NOT re-run the check or re-flag the claim unchecked — the determination is final.

