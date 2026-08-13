# Shared context

What this run knows, in its own words. Carries what an agent would otherwise
rebuild from disk: established results with their basis, dead approaches and
why, computed numbers, durable memory, and disagreements. Not a file catalogue
(`research/INDEX.md` is that) and not a narration of activity.

Budget 10,000 tokens (this file ~8300, so ~1700 under). Length is a bill the
whole run pays on every model call; link the file holding any detail compressed
away.

**Run state: mechanism is combinatorial, event rate is not. Step law + recharge identity hold universally (0 failures across 1,154 random sequences). The event-rate sweep (Directive 12) refutes a purely combinatorial rate bound: 852/1,154 (73.8%) reach b_k=0, wide-support families ({2..20}, {2..100}, Geom(p=.25)) die 100%. Route A re-scoped to require an input hypothesis that the dying families violate. **Directive 13: the bounded-support re-scope (gaps ⊆ {2,4,6}, first gap 2) is VACUOUS for Gilbreath — the primes do NOT satisfy it (gaps 8,10,12,14,34 all below 2000; prime gaps unbounded), so no finite-support hypothesis holds.** The separating property must be a CONCENTRATION condition tolerating rare large gaps — pick one (bounded mean gap per window / frequency of gaps > G / Cramér g_n = O(log² p_n)), state it, check numerically against BOTH primes and {2..20}, then write it in. Target: a theorem "under hypothesis H, the event rate ≥ r, and r suffices" where H separates the primes from the dying sweep families.** Established: regeneration ⟺ `(edge==2, intruder==4)`, zero failures over 998 transitions (the old "refuted iff" record was an off-by-one and is **withdrawn** — `code/out/check_regenerate_lemma.notes.md`; do not keep it). The conjecture is exactly: do (2,4)-events arrive fast enough that `Σ (j_i + 1)` never falls `k−1` behind (recharge identity, Established). Erosion verification is no longer useful — the step law is exact, no re-derivation. Closed by solver (Attempt 1): run-count/total-variation Lyapunov potentials fail even inside the {0,2} regime ((0,0,1,1)→(0,1,0)); Rule 90 relative-depth concentration (z=2.25, p=0.017) is a mild effect, not a mechanism — **do not reopen either**. The concrete candidates are three proposed approaches (all precedent-unchecked in the literature): `renewal-process-edge-flip-hitting-time` — bound the (0,4)-stall hitting time under the Rule 90 edge dynamics, giving inter-event gap ≤ y₀/2 + stall + 1 with y₀ from the gap bound; its conjectural stall bound L ≤ 2·b_k and the constant-zero-block exception are exactly CHT's long-zero-block obstruction — and `block-boundary-causal-separation` — the 2-state (b, y) framing with a Lyapunov function — and `polynomial-evolution-halved-triangle-over-gf2` — lift the Rule 90 operator to Z_2[[X]], prove the carry term (from min(a,b) in |a−b| = a+b−2min) always lies in the ideal (2,X) so it vanishes at position 1; equivalent to the conjecture but gives the carry term an explicit algebraic form to hunt, with BCZ's F_2[[X]] program as the mod-2-level nearest literature. **Each must state how it beats Eppstein 2011**: gap constraints alone fail in the 2-then-odds class, so a purely-gap rate bound must be prime-specific or carry a hypothesis Eppstein's construction violates.

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

- **Gatti 2020 "prime-class proof" — REFUTED (invalid Theorem 4; source in library).** Gatti's *Gilbreath's Sequences...* (Preprints 202003.0145.v1, 2020) proves the global valid-extension formula (`k = ±s^{n−1}_1 ± … ± s^1_{n−1} + s_n ± 1`) and parity alternation, but its Theorem 4 (`min K ≤ p_n ≤ max K` for every prime, claimed toward a deterministic class theorem) is invalid: the right-inequality step assumes `p_n ≤ max K` and derives only a trivial `min K ≤ α` via Bertrand. Its Lemma 4 interval-completeness is false in general (Muney's length-5 hole; `dim K_S = 2^{n−1}` fails even at {2,3,5}: |K_S| = 5 — hand-verified, script queued). **So no published deterministic bounded-gap or prime-class theorem exists**, consistent with Eppstein: any general-class theorem must add non-concentration or restrict to primes. Do not build on Gatti's implication. Claims `gatti-2020-theorem4-proof-invalid`, `gatti-2020-lemma4-interval-completeness-refuted`, `gatti-2020-valid-extension-global-formula`. Anchor: `research/sources/gatti-2020-preprints-gilbreath-conditions.full.md`, `research/notes/library-state.md`.
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
  1154 sequences, 26 families × seeds (gaps: {2}; {2,4}; skew{2,4,6,8,10};
  uniform{2..2g}, g=3..50; geometric p=0.5..0.0625; each ± first gap forced to
  2), batches D=600/W=200k ×48, D=1200/W=400k ×10, D=4000/W=2M ×4, 26 workers,
  wall 278 s, exact int64.
  **The step law and the recharge identity (the exact {0,2}-block accounting,
  `b_{k+1} ≥ b_k ⟺ (2,4)`-event else `b_{k+1} = b_k − 1`, and
  `b_k = b_1 + Σ(j_i+1) − (k−1)`) fail 0 times across every one of the 1154
  sequences (46,528 eligible rows, 20,013 events)** — universal in the random
  class, same as the prime rows (0 failures, depth 1000). The step law is a
  theorem for all nonneg sequences, so the check is a sanity pass, now measured
  on random data rather than only on the primes.
  **Regeneration is NOT generic in the random class: 852/1154 (73.8%) reach
  `b_k = 0` — all deaths inside the first 10 rows (89.7% inside the first 3;
  342 at k=1, 346 at k=2); no sequence surviving row 10 ever died (up to
  D=4000).** The class-level failure is the startup transient, never long-run
  erosion. **Forcing the first gap to 2 is decisive where support ⊆ {2,4}:
  consecutive 0/48 and f2-rand24 0/48 sequences die in each batch (incl.
  D=4000), vs 62% deaths at k≤1 for rand24 without it.** Death fraction grows
  monotonically with gap-support width (uniform{2..20}+: 100%); the primes'
  gap profile (2,2,4,2,4,2,4,6,2,…) is the small-support, first-gap-2 skew that
  survives. 240 non-degenerate survivors: `rho_live ≥ 0.318` and `min_b ≥ 1`
  (primes: min b=2). Oracle: 4/4 numpy-vs-pure-Python matches (events, min_b,
  first_b0, densities). Bounded claims in FULL detail + claim blocks:
  `code/out/event_rate_sweep.notes.md`
  (id `event-rate-sweep-step-law-universal`,
  `event-rate-sweep-regeneration-not-generic`,
  `first-gap-2-startup-sufficiency-supported`); raw captures
  `code/out/event_rate_sweep.captured.txt`,
  `code/out/event_rate_sweep_analysis.captured.txt`; stats
  `code/out/event_rate_stats.jsonl`. **Implication for the general-class
  strategy: the naive "2-then-odds, gaps bounded" class FAILS as a whole
  (consistent with Eppstein); a general theorem needs first-gap-2 + a
  small-support skew hypothesis — the primes satisfy both, and the data
  localises the entire class failure to the startup rows. Nothing here
  extends to all k; no regeneration-rate lower bound for the primes follows.**
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
  this is unresolved. Colonna's g=4 deletion example sharpens it further (see
  Ruled out): only gaps ≤ 3 is un-refuted as a plain bounded-gap class.
- **`research/CLAIMS.md` is a generated ledger with a broken contradictions
  section** (a long claim block gets mis-parsed into spurious "contradicts"
  rows). `research/notes/library-state.md` is the authoritative, hand-maintained
  claim ledger and holds the same content formatted correctly — read
  library-state.md for the current ledger.

## Gaps

- **The live question: bound the (2,4)-event rate from below.**
  The step law and recharge identity reduce the conjecture to:
  `Σ_{i<k} (j_i + 1) ≥ k − 1 − b_1` for all k. Since `b_1=2`, this is a
  statement about event frequency and jump sizes.
  **Mechanism vs rate (Directive 12, settled by the 1,154-sequence sweep):**
  the step law, recharge identity, and drain law are combinatorial — they hold
  universally (zero failures on all 1,154 random sequences). But the event
  **rate** is not: 852/1,154 (73.8%) reach `b_k = 0`, all within the first 10
  rows; wide-support families ({2..20}, {2..100}, Geom(p=.25)) die 100% of the
  time with or without first gap forced to 2. The phase boundary is gap support:
  narrow support ({2}, {2,4}, {2,4,6}) + first gap = 2 survives; wide support dies — i.e. survival correlates with gaps CONCENTRATED on small values, not contained in a finite set (Directive 13: the primes themselves are not finite-support, with gaps 8,10,12,14,34 below 2000). Route A (combinatorial bound on max erosion between events) MUST include an input hypothesis that separates the primes from the dying families. **Directive 13: that hypothesis cannot be bounded gap support — the primes violate every finite-support condition, so the {2,4,6} re-scope is vacuous.** It must be a concentration condition tolerating rare large gaps; candidates named in the run-state line; pick one and check it against BOTH primes and {2..20} before writing it in.
- **CHT inverse theorem route needs two analytic steps for the primes**: rule
  out long zero-blocks and long shallow `{0,d}`-blocks (Cramér-type hypotheses
  unproved). A proof bypassing that dichotomy is the alternative.
- **What remains toward a GOAL.md partial result:** the block lemma is
  delivered (re-derived, constant explicit). Still open: a proved invariant
  forcing `A_k(1)∈{0,2}`; a theorem for a general class of sequences (must beat
  Eppstein AND the Colonna g=4 deletion failure — see Established); a proved
  statement on the regeneration rate; and the Lean 4
  formalisation of the difference operator and induction step (with `#print
  axioms` and every `sorry`). **Lean status answered this cycle:** Google
  DeepMind's formal-conjectures repo (commit ed75a6dd) has a statement-only
  `Gilbreath.lean` — `gilbreath_conjecture (k : ℕ+) : d k 0 = 1 := by sorry`,
  no proof formalisation exists publicly; the run's own work (on mathlib4's
  `Nat.dist`) is still to be written. Claim `deepmind-formal-conjectures-gilbreath-lean`.
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