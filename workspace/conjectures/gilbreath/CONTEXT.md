# Shared context

What this run knows, in its own words. Carries what an agent would otherwise
rebuild from disk: established results with their basis, dead approaches and
why, computed numbers, durable memory, and disagreements. Not a file catalogue
(`research/INDEX.md` is that) and not a narration of activity.

Budget 10,000 tokens (this file ~2100, so well under). Length is a bill the
whole run pays on every model call; link the file holding any detail compressed
away.

**Run state: library built, oracle built, claim extraction done, one thread
open.** Phase 1's exit test is met (see `research/ROOT.md`: minimal
counterexample structure, verification bounds, ≥3 restricted classes settled).
The current frontier is 2026 work (Chase–Hunter–Tao); the run's own open thread
is `research/threads/regeneration.md`. `research/notes/library-state.md` is the
authoritative claim ledger and is current; `research/CLAIMS.md` lags it (not
yet re-derived from library-state).

## Established

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
- **Mod-4 linearization (invariant candidate).** For k≥1, n≥2 where entries are
  even, `d_{k+1}(n) ≡ d_k(n)+d_k(n+1) (mod 4)` (Odlyzko §2 eq.201). Turns the
  absolute-value problem into linear Pascal-triangle congruences mod 4 — the
  cleanest algebraic handle the run has. CHT Lemma 3.10 generalises:
  `a(i,j) ≡ Σ_k C(i,k) a_{j+k} (mod 2)`.
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

## Numbers

- Block profile (leading {0,2} length) rows k=1..40:
  `2,7,13,13,24,23,22,21,24,58,97,96,97,96,173,175,175,175,175,290,289,288,739,873,872,871,872,871,870,869,868,867,866,865,2179,2178,2177,2176,2770,2769`.
  Grows roughly by doubling bursts around k=15,20,23,35,39.
- Depth 1000 stats: min b=2 (k=1), max b=1,270,444 (k=162); 60 regeneration
  events in 999 transitions; max single jump 360,698 (k=146); longest pure
  single-erosion run 838 rows (b never hits 0); intruder (first value past the
  block): min 4, max 14, 59.6% exactly 4, all ≡0 or 2 mod 4. b never stays at
  2 (jumps 2→7 by k=2).

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

- **Regeneration mechanism uncharacterised** — the whole obstruction. Thread
  `research/threads/regeneration.md` is open: next steps are to characterise
  the intruder, find what makes a block regrow, and stress-case rows where b≤10.
  An explicit mechanism (or an invariant forcing `A_k(1)∈{0,2}` directly) is
  the deliverable.
- **CHT inverse theorem route needs two analytic steps for the primes**: rule
  out long zero-blocks and long shallow `{0,d}`-blocks (Cramér-type hypotheses
  unproved). A proof bypassing that dichotomy is the alternative.
- **What remains toward a GOAL.md partial result:** the block lemma is
  delivered (re-derived, constant explicit). Still open: a proved invariant
  forcing `A_k(1)∈{0,2}`; a theorem for a general class of sequences (must beat
  Eppstein); a proved statement on the regeneration rate; and the Lean 4
  formalisation of the difference operator and induction step (with `#print
  axioms` and every `sorry`). No Lean work is on disk yet.
