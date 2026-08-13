# Shared context

What this run knows, in its own words. Carries what an agent would otherwise
rebuild from disk: established results with their basis, dead approaches and
why, computed numbers, durable memory, and disagreements. Not a file catalogue
(`research/INDEX.md` is that) and not a narration of activity.

Budget 10,000 tokens (this file ~2100, so well under). Length is a bill the
whole run pays on every model call; link the file holding any detail compressed
away.

**Run state: library sufficient, oracle built, search halted per directive.**
`research/threads/rule90-regeneration.md` (test the depth-d=2^j prediction
against `blocks_depth1000.json`). The regeneration thread
(`research/threads/regeneration.md`) holds the **established** criterion: block
regeneration ⟺ `(edge==2, intruder==4)`, zero failures over all 998
transitions. The old "candidate iff lemma refuted" record was an off-by-one and
is **withdrawn** (see `code/out/check_regenerate_lemma.notes.md`) — do not keep
it. Two proposed (unchecked) lines on the inventor's desk, both built on the
established criterion and distinct from the refuted handles:
`research/approaches/block-apex-parity-forcing.md` (constant `{0,0,...}` /
`{2,2,...}` blocks may be unrealisable from the prime gaps — regeneration of the
last-entry parity via the apex formula) and
`research/approaches/prime-gap-mod6-structure.md` (work mod 3 on the halved
triangle, using the ±1 mod 6 prime-residue constraint). The honest open
question remains: is there a k with block length 0?

## Established

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
  and Eppstein 2011). The proved Rule 90 core stands alone. It predicts
  regeneration at depths that are powers of 2: at d = 2^j, binom(2^j, m) ≡ 1
  (mod 2) ∀m, so the halved entry is the XOR of the whole width-(2^j+1) window;
  if that XOR is 1 for a stretch, the original row is all-2 — a clean
  regenerated block. Thread: `research/threads/rule90-regeneration.md`.
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

- **The honest open question, stated sharply:** is there a k with block length
  0? Everything computed says no (minima grow: 13,24,96,97,175,2762,...) and
  nothing proves it. Thread `research/threads/regeneration.md` is open.
- **Regeneration criterion established but the recurrence is open.** The local
  criterion is `(e==2, c==4)` — the block must end in 2 with a 4 immediately
  past it. This holds exactly to depth 1000 (60/60 events, zero failures).
  What is open is **why** the boundary re-enters `(2,4)` before `b` hits 0 —
  i.e. why the block-end flips to 2 and the intruder drains to 4 and sticks
  rather than the block-length decaying to zero. The Rule 90 interior dynamics
  (`research/threads/rule90-regeneration.md`) give one candidate explanation
  (powers-of-2 depths force all-2 stretches via the Sierpinski kernel). The
  mod-4 linearization is the cleanest algebraic handle.
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
- **CHT Theorem 1.6 hypothesis check — DO THIS NOW (directive).** The
  `cht-inverse-theorem` claim has `holds-here: unchecked` in both copies. Take
  the prime-difference data, compute M (from max normalized gap a_n), L
  (longest 0-run), and R_0 = 100L·8^M, and check whether R_0 is at all
  satisfiable at depth ≤ 1000. If R_0 ≫ 1000, the theorem does not bite at
  reachable depths and `holds-here` must be set to `no` with the numbers.
