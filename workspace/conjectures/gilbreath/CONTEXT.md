# Shared context

What this run knows, in its own words. Carries what an agent would otherwise
rebuild from disk: established results with their basis, dead approaches and
why, computed numbers, durable memory, and disagreements. Not a file catalogue
(`research/INDEX.md` is that) and not a narration of activity.

Budget 10,000 tokens (this file ~8300, so ~1700 under). Length is a bill the
whole run pays on every model call; link the file holding any detail compressed
away.

**Run state (Directive 19): Route A SUPPORTED by conditional-rate experiment. The (2,4) event rate is family-independent post-startup (pooled λ̂ = 0.585, Pearson X² p = 0.68 over 8 families, D=400, W=200000). The answer restores Route A — the mechanism is combinatorial. The gap: λ̂ is measured, not bounded below for all k. Directive 23 sharpens what rate: a mean is the wrong summary for the heavy-tailed jump distribution (the object is the GAP between consecutive large jumps; characterisation DONE — 12/13 giants j>1000 genuine, i=161 the width artifact with true jump ≥ 176,181; claim `bigjump-cap-characterization-1000`). Do not cite the D=40 smoke numbers (predate sign fix, discarded per directive).**

## Established

- **Gatti 2020's claimed class-level/prime proof is invalid — located flaw (full text now in library).** Gatti, *Gilbreath's Sequences and Proof of Conditions for Gilbreath's Conjecture* (Preprints 202003.0145.v1, 2020; the earlier downloadable form of the MDPI-403 "Gilbreath polynomials" paper) proves the valid-extension machinery (Eq. 2: `k = ±s^{n−1}_1 ± … ± s^1_{n−1} + s_n ± 1`, global anti-diagonal criterion; parity alternation Lemmas 1–3 — the general-class half of the run's parity wave) but **Theorem 4's proof of `min K ≤ p_n ≤ max K` for the primes is invalid**: the right-inequality step assumes its own conclusion ("If p_n ≤ max K, then subtracting 2p_{n−1}…") and derives only a trivial `min K ≤ α` via Bertrand. Also his Lemma 4 (valid-extension set = whole parity interval) is **false in general** — Muney 2026's length-5 hole; even `dim K_S = 2^{n−1}` fails on `{2,3,5}`: `|K_S|=5` (solutions `{1,3,5,7,9}`, hand-verified; coder script `code/research_mod_check/verify_gatti_kset.py` queued). So **no published deterministic bounded-gap/prime-class theorem exists** — the REQUESTS row stays open, and Gatti's polynomial inequality (MDPI 2023) remains asserted-by-source only. Claims: `gatti-2020-theorem4-proof-invalid`, `gatti-2020-lemma4-interval-completeness-refuted`, `gatti-2020-valid-extension-global-formula`. Anchor: `research/sources/gatti-2020-preprints-gilbreath-conditions.full.md`.
- **LLM-era claimed "proofs" — all classified not-load-bearing, do not cite.**
  Granville 2026 "Piercing Gilbreath's Conjecture" (arXiv:2607.04166, cs.CR — a
  fintech/data-science author, NOT the number theorist) promises "a path to the
  solution" via sieving/magic-primes and has no checkable statement; Maréchal
  and ZARKOUNA 2026 likewise recorded as unverified claim preprints
  (`research/summaries/granville-2026-piercing-gilbreath-arxiv.md`, claims
  `granville-2026-piercing-gilbreath-not-load-bearing`). No peer review, no
  mechanism this run can test; the conjecture is not proved by any of them.
- **Verification record, CURRENT (sourced this cycle, 4 data points kept distinct):**
  Odlyzko 1993 to 10^13 (G=635); Plouffe 2025 to 10^14 (arXiv:2510.06688); Colonna
  2025–26 to 1.5×10^15 (G(2.8e14)=788, G(6.15e14)=800, G(1.5e15)=800). Run's own: depth
  1000 (1.27M primes), depth 600 (33860 primes). Do not conflate.
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
  `second_entry_always_0_or_2=true`, `min_leading_02_block=2`; the
  second-entry sequence also reproduces OEIS A089582's 105 terms exactly
  (`oeis-A089582-second-entry-catalogue`). Pushed to depth
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
  corollary is CLOSED (refuted)** — see Ruled out; do not re-assert it. The
  interior identification is about values inside the block; it says nothing
  about when the boundary regenerates. Anchor:
  `research/notes/block_lemma.md` (apex),
  `research/approaches/rule90-absorbing-boundary.md` (the absorption dead end),
  thread `research/threads/rule90-regeneration.md` (CLOSED).
- **Big-jump characterisation — DONE (Directive 23 item 1): the giants are
  genuine.** Of the 13 (2,4)-events with j > 1000 at depth 1000 (sieve 2e7,
  W=1,270,607), 12 are genuine (landing block ends strictly inside the finite
  row, floors 176,186..1,268,392, no edge clustering) and only **i=161 is the
  width artifact** (b_162 = 1,270,444 = W−162−1; true jump ≥ 176,181 — quote
  it that way, never as an exact jump). Heavy tail (j>10^4) 9 genuine of 10,
  including i=146 (j=360,698) and i=134 (j=217,657); genuine giants carry
  86.1% of S_1000=1,270,603, the 13 giants 99.76%. **The heavy tail is
  genuine prime-renewal structure — the gap-between-large-jumps object is
  real.** This decides Directive 23's fork; rows k ≥ 162 are the
  width-exhaustion artifact. Claim `bigjump-cap-characterization-1000`; anchors
  `code/out/bigjump_characterization.captured.txt`,
  `code/out/bigjump_characterization.notes.md`.
- **Ducci literature (sourced, four primary papers) — cyclic boundary drawn.**
  All classical Ducci theorems are CYCLIC (wraparound |x_n−x_1|): nilpotence-
  iff-power-of-2, cycle structure, Webb's no-uniform-bound do NOT transfer to
  the half-infinite Gilbreath operator; Eppstein's escape is the standing
  witness that the half-infinite object differs. What transfers: the
  mod-2/Pascal law (= this run's proved rule90-interior-xor, now anchored in
  four peer-reviewed sources) and Chamberland's factored-max +
  rigidity-equality-case template — the shape any surviving potential must
  take, since raw run-count/turning-point potentials are dead (Ruled out).
  Gives `ducci-potential-max-decrease` and `p-adic-valuation-carry-dynamics`
  their precedent and their caution. Anchor: `research/notes/library-state.md`
  Ducci section; claims ducci-classical-nilpotence-iff-power-of-2,
  ducci-pascal-mod2-rule90, ducci-max-factoring-potential-template,
  ducci-avart-nilpotent-concatenation.
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
- **Step law + recharge identity — PROVED as general theorems (this run).**
  With the intruder pair `(x,y)=(row[b_k], row[b_k+1])`, exactly:
  `b_{k+1} ≥ b_k ⟺ (x,y)=(2,4)`, and `b_{k+1} = b_k − 1` otherwise (the
  erosion rate is exactly 1 per row, not "≥ b_k−1"). The recharge identity
  `b_k = b_1 + Σ_{events i<k}(j_i+1) − (k−1)` (j_i = jump at event) is exact:
  the `−(k−1)` term *is* the Odlyzko protection constant 1, and the `(2,4)`-
  events are the *only* growth mechanism. **This is the narrowed target**:
  the conjecture holds iff `(2,4)`-events arrive so fast that `Σ(j_i+1)` never
  falls `k−1` behind. **STATUS: these are now PROVED theorems of the
  absolute-difference operator for ANY array (no parity, no primes)** — the
  proof (positions 1..b_k−1 stay in {0,2} by closure; position b_k is
  |x−y| ∈ {0,2} iff (x,y)=(2,4)) is in `research/notes/step_law_proved.md`,
  claim `step-law-theorem-proved`; it upgrades the earlier depth-1000
  observation (`regeneration-lemma-edge-2-intruder-4-established`).
  Corollaries (also proved): drain law `y_{k+1} = y_k − 2·[x_k=2]` on erosion;
  intruder-4 absorbing under erosion (every maximal 4-run ends in
  regeneration). Verified on real primes (depth 1000, 60 events) and 400
  random nonneg arrays (3,521 rows, 610 events, zero failures). Anchor:
  `research/notes/step_law_proved.md`, `code/regeneration/step_law_theorem.py`,
  `code/out/step_law_and_recharge_verified.md` (earlier computed form). Do not re-derive — only the (2,4)-event RATE is open.
- **Conditional-rate experiment — DONE (TASKS complete, Directive 19).**
  Post-startup (k>10) event rate is family-independent: pooled λ̂ = 0.585
  (1098/1876), Pearson X² p = 0.68 over 8 families, D=400, W=200000,
  seeds 10000..10019. 3 corner-class families (consecutive, f2-rand24,
  rand24) immortal with zero eligible rows — contribute nothing. **λ̂ is
  MEASURED, not bounded below for all k** — the conjecture needs
  Σ(j_i+1) ≥ k−2 for all k, which requires a lower bound holding everywhere,
  not a point estimate at D=400. Do NOT cite D=40 smoke (predates sign fix;
  discarded). Anchors: `code/out/conditional_rate_experiment.captured.txt`,
  `code/out/conditional_rate_records.jsonl`,
  `code/out/conditional_rate_experiment.notes.md`, claim
  `conditional-rate-experiment-family-independent`.
  **Operator grounding (Directive 19):** `code/grounding/check_absdiff_vs_forwarddiff.py`
  verifies the absolute-difference operator is the one the conjecture is about.
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

- **Gatti 2020 "prime-class proof" — REFUTED (invalid Theorem 4; source in library).** Gatti's *Gilbreath's Sequences...* (Preprints 202003.0145.v1, 2020) proves the global valid-extension formula (`k = ±s^{n−1}_1 ± … ± s^1_{n−1} + s_n ± 1`) and parity alternation, but its Theorem 4 (`min K ≤ p_n ≤ max K` for every prime, claimed toward a deterministic class theorem) is invalid: the right-inequality step assumes `p_n ≤ max K` and derives only a trivial `min K ≤ α` via Bertrand. Its Lemma 4 interval-completeness is false in general (Muney's length-5 hole; `dim K_S = 2^{n−1}` fails even at {2,3,5}: |K_S| = 5 — machine-checked this run, two independent programs: direct nested-absolute eval, full-triangle left-edge semantics, and Gatti's Eq.2 formula all give {1,3,5,7,9}). **So no published deterministic bounded-gap or prime-class theorem exists**, consistent with Eppstein: any general-class theorem must add non-concentration or restrict to primes. Do not build on Gatti's implication. Claims `gatti-2020-theorem4-proof-invalid`, `gatti-2020-lemma4-interval-completeness-refuted`, `gatti-2020-valid-extension-global-formula`. Anchor: `research/sources/gatti-2020-preprints-gilbreath-conditions.full.md`, `research/notes/library-state.md`.
- **"Route A refuted by sweep" — WITHDRAWN (Directive 16).** The sweep deaths are g_0 startup (all within k≤10, 90% by k≤3); they do not bear on the asymptotic event rate. rand24 deaths at k=1 (iff g_0=4) vs survivors at trunc_k=2 (iff g_0=2). Route A is live; the conditional-rate experiment tests it.
- **Bounded-support re-scope "gaps ⊆ {2,4,6}, first gap = 2" — REFUTED as vacuous (Directive 13).** The primes violate every finite gap-support condition; a theorem conditional on finite support says nothing about Gilbreath.
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
  class must first state how it beats Eppstein's construction. Sharpener now
  held (asserted-by-source, `colonna-deletion-left-edge-failure`): Colonna's
  record-page footnote deletes 5 (or 7) from the primes, giving a
  2-then-odds sequence with gaps ≤ 4 (≤ 6) whose second entry is 4 — a
  concrete left-edge failure at row 2 within a bounded-gap class. So the
  plain "gaps ≤ g" class is dead for every g ≥ 4, not only by Eppstein's
  asymptotic construction; only g ≤ 3 remains un-refuted.
- **Proth's "failed proof" is a retracted myth — there is no proof to locate
  an error in.** GOAL.md's item "locate the error in Proth 1878" rests on a
  claim its originator H.C. Williams retracted (email 2020, quoted in Chase
  2024 §7): Proth's actual paper states the property as a theorem and gives no
  proof; Catalan's appended note calls it a postulate. The corrected result is
  the retraction itself. The Google Books capture of NCM vol. 4 is now also
  exhausted — metadata/ToC/word-cloud only, no page text OCR'd
  (`research/summaries/proth-1878-ncm-vol4-googlebooks.md`). GDZ
  (`gdz.sub.uni-goettingen.de/id/PPN598948236_0004`) with a JS-capable browser
  is the only remaining route, and no further offline fetch should be
  attempted.
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
- **Rule 90 depth-prediction timing corollary — CLOSED (null computed).** The
  absolute-depth and jump-timing forms were already refuted; the relative-depth
  form (21/27 within tol=1 of a power of 2) is now null-tested: p = 0.0173
  against the exact binomial Binomial(27, 9/16), but dead at tol=0 (p =
  0.113) and erased by conditioning on the observed [2,9] range (p = 0.68).
  The concentration is real but mild and tolerance-dependent — not a
  structural regeneration mechanism. The proved interior identification
  (rule90-interior-xor) is unaffected; this closes the timing question, not
  the regeneration question.
- **Raw run-count potential r(T) ≤ r — MACHINE-REFUTED in the actual
  regime.** The on-disk verifier `code/out/check_runcount_lemma.py` (written,
  never run) was executed: exhaustively over 6,725,600 strings (len ≤ 8,
  values 0..6) the lemma r(T(x)) ≤ r(x) fails (first counterexample
  (6,6,6,6,6,6,5,5), worst at (0,0,1,1,0,0,1,1)). The class-restricted run
  shows failure even in the halved {0,1} interior — minimal counterexample
  (0,0,1,1) → (0,1,0) (2 runs → 3), the halved form of (0,0,2,2) inside the
  leading {0,2} regime. Claim `runcount-lemma-refuted` promoted from hand
  counterexample (odd-valued (5,5,0,0), technically outside the class) to
  machine-checked. The total-variation-oscillation-potential approach's raw
  r/t potentials are dead; only a corrected weighted/max-factored potential
  (Chamberland's Ducci template) survives, untested.
- **Block-apex pattern-class forcing — REFUTED.** The idea that a mixed
  {0,2} block forces intruder reduction (or that constant blocks are the
  pathology) is false as a mechanism: CHT Lemma 3.7(iii) proves a
  {0,d}-valued block persists in ALL descendants regardless of pattern, and
  the depth-1000 record shows regeneration fires on the boundary pair
  (edge, intruder)=(2,4) and nothing else (60/60 regens at y=4, 0/65 at
  y≥6; whole-block pattern class never enters). Do not re-propose. Anchor:
  `research/approaches/block-apex-parity-forcing.md`.
- **Prime-gap mod-6 structure — REFUTED as a constraint machine.** The
  operator has NO reduction mod 3: |a−b| mod 3 is not a function of the
  residues (minimal witness (0,1)/(3,1)), so no F_3 finite-state evolution
  of the halved triangle exists; and "H_k(1) mod 3 ∈ {0,1}" is the
  conjecture restated, not an independent constraint. The real mod-6 gap
  statistics never percolate to the iterated left edge in any source. Do
  not re-propose. Anchor: `research/approaches/prime-gap-mod6-structure.md`.
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

- **Event-rate sweep over the 2-then-odds general class — DONE (TASKS item 1).**
  1154 sequences, 26 families × seeds, batches D=600/W=200k ×48, D=1200/W=400k ×10,
  D=4000/W=2M ×4, 26 workers, wall 278 s, exact int64.
  **The step law and the recharge identity (the exact {0,2}-block accounting)
  fail 0 times across every one of the 1154 sequences (46,528 eligible rows,
  20,013 events)** — universal in the random class, same as the prime rows.
  **852/1154 (73.8%) reach b_k = 0, but ALL within the first 10 rows (764/852 by
  k≤3, 852/852 by k≤10).** Death is g_0 startup: rand24 dies at k=1 iff g_0=4
  (30/48), survives at trunc_k=2 iff g_0=2 (18/18). Wide-support families die
  more because they more often draw g_0≠2. The sweep does NOT measure the
  asymptotic event rate — Route A is untested, not refuted (Directive 16).
  Oracle: 4/4 numpy-vs-pure-Python matches. Full detail:
  `code/out/event_rate_sweep.notes.md`, `code/out/event_rate_sweep_analysis.captured.txt`.
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
- **Recharge surplus is heavy-tailed (Directive 23, depth 1000).** S_1000 =
  1,270,603 vs required 998; most jump sizes are tiny (0,1,2,3,4,9,…) but the
  tail carries the surplus — jumps > 10⁴ at i=64,94,110,112,126,130,134,146,161
  (largest 360,698 at i=146), with the three largest (i=134,146,161) supplying
  the bulk. The mean event rate λ̂ = 0.585 is dominated by this tail, so a
  mean-rate bound is the wrong target. Anchor:
  `code/out/surplus_renewal_table.captured.txt`.
  **The giants are NOT preceded by long erosion — "energy stored during
  erosion" is dead as a recharge mechanism.** Mean gap before the 9 big jumps
  is 3.54 rows vs 2.48 before small jumps; the giants come 1–13 rows after the
  previous event, so they are intrinsic to specific rows, not recovered from a
  long stall. Each giant jump ≈ the current block length (total recharge
  1,270,603 ≈ width of final row); jumps grow sublinearly with b
  (log-log slope 0.388). Fork decided: the giants are genuine (12/13; claim
  `bigjump-cap-characterization-1000`, Established), and the Rule-90/power-of-2
  correlate for these rows is refuted (rule90 form B2: big-jump rows
  34,56,64,68,94,96,110,112,126,130,134,146,161 — 9/13 next-regen at a
  power-of-2-ish offset vs null 0.81, no separation). Anchors:
  `code/out/surplus_renewal_structure.md`,
  `code/out/surplus_renewal_table.captured.txt`.

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
  this is unresolved. Colonna's g=4 deletion example sharpens it further (see
  Ruled out): only gaps ≤ 3 is un-refuted as a plain bounded-gap class.
- **`research/CLAIMS.md` is a generated ledger; the contradictions section is now clean** (one legitimate row: `odlyzko-block-lemma-exact` vs `odlyzko-block-lemma-asserted` — the earlier ~20 spurious "contradicts <word>" rows came from one freetext `contradicts:` value in `research/notes/block_lemma.md` and were fixed by restricting it to the real claim id). `research/notes/library-state.md` is the authoritative, hand-maintained claim ledger; read it for the current ledger in full.

## Gaps

- **The live question: what makes the giant jumps recur?**
  The step law and recharge identity reduce the conjecture to:
  `Σ_{i<k} (j_i + 1) ≥ k − 1 − b_1` for all k. At depth 1000 this holds with
  enormous slack (b_1000 = 1.27M ≫ 1) — the surplus is carried by a handful
  of giant jumps, not by an average rate. The conjecture is tight only if the
  big jumps stop.
  **Directive 23 — characterisation DONE, bound still open.** λ̂ = 0.585 is a
  MEAN, and a mean is the wrong summary for a heavy-tailed jump distribution
  (dominated by the tail). A lower bound on the mean rate controls the wrong
  quantity. The object to bound is the GAP between consecutive large jumps;
  the fork "genuine dynamics vs width artifact" is decided — 12/13 giants
  are genuine, i=161 is capped (j ≥ 176,181), so the gap-between-large-jumps
  object is real (`bigjump-cap-characterization-1000`, Established). The
  giants are not erosion-recovery events (they arrive 1–13 rows after the
  previous event: "energy stored during erosion" is dead) and do not sit on
  Rule-90/power-of-2 structure (rule90 form B2: no separation). What is open:
  a lower bound on the gap between successive large jumps — showing a jump
  exceeding threshold J arrives at least once every T(J) rows — and whether
  the tail persists at larger widths (later giants beyond the i=161 cap).
- **CHT inverse theorem route needs two analytic steps for the primes**: rule
  out long zero-blocks and long shallow `{0,d}`-blocks (Cramér-type hypotheses
  unproved). A proof bypassing that dichotomy is the alternative.
- **What remains toward a GOAL.md partial result:** the block lemma is
  delivered (re-derived, constant explicit). The Lean 4 formalisation is
  delivered (nine theorems, zero sorry, axiom footprint
  `[propext, Classical.choice, Quot.sound]`, IFF equivalence). Still open: a
  proved invariant forcing `A_k(1)∈{0,2}`; a theorem for a general class of
  sequences (must beat Eppstein AND the Colonna g=4 deletion failure — see
  Established); a proved statement on the regeneration rate.
- **Library search halted by directive.** FRONTIER.md restored 2026-08-13 from
  commit db36fc23 (42 rows) after the Gatti-2020 wrapper-page download replaced
  it with 15 social-media share buttons; a second collapse happened this cycle
  (Colonna 2026-08 + DeepMind re-downloads) and was restored from this session's
  read — the documented URL filter did not run on those rewrite writes, so
  re-check the candidate count after any further write before trusting
  FRONTIER.md. No more downloads until a specific gap is stated that a source
  could close.
- **CHT Theorem 1.6 hypothesis check — DONE, holds-here = no.** Computed on
  sieve 2e7 (1,270,607 primes): max normalized gap a_n = 89 → M = 7, longest
  0-run L = 2, so R_0 = 100·L·8^M = 419,430,400 ≈ 4.2e8 ≫ 1000. The
  no-{0,d}-block hypothesis is not satisfiable at any reachable depth, so the
  CHT inverse theorem does not bite here. `code/out/cht_hyp_check.captured.txt`,
  claim `cht-inverse-theorem-hyp-check`. Do NOT re-run the check or re-flag the
  claim unchecked — the determination is final.
- **Lean 4 deliverable — COMPLETE (Directive 17 verified).** Nine theorems
  kernel-checked across three files: `dist_odd_even`, `dist_dist_even`,
  `dist_one_eq_one`, `shape_theorem`, `shape_rows`, `reduction`,
  `reduction_lemma`, `gilbreath_reduction`. Every declaration depends on
  exactly `[propext, Classical.choice, Quot.sound]` (the three standard
  Mathlib axioms), **zero sorry / zero sorryAx**. The central theorem
  `gilbreath_reduction : GilbreathConjecture X ↔ SecondEntryIn02 X` is an
  **IFF** — it proves the {0,2} statement is exactly as hard as the
  conjecture, not a stepping stone to a proof. It reformulates rather than
  reduces. The prime instantiation (row 1 = (1, even, even, ...)) remains
  computation-checked (witnesses.json), not Lean-proved. Regeneration is
  untouched. This is a GOAL.md deliverable. Claim:
  `lean-reduction-machine-checked`. Anchors:
  `code/lean/gilbreath_reduction.lean`, `code/out/lean_gilbreath_reduction.captured.txt`.