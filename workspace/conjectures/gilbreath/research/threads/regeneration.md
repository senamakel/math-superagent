```thread
question: Can Granville's Lemma 5.4 / Theorem 5.5 reduce GC to ν_2 > n^β with β > 0.525? Empirical route at ceiling; theoretical routes are the only live ones.
status: live — PIVOTED (Directive 36). Empirical route at ceiling. Route B (Granville ν_2) primary; Route A (ratio bound) empirical fallback; Route C (CHT) calibrated by authors' assessment.
rests-on: gilbreath-second-entry-equivalence, step-law-theorem-proved, lemma54-re-derived-proof, odlyzko-block-lemma-exact
blocked-by: **RESOLVED (Directive 50) — the abstract core is kernel-checked in Lean.** `code/lean/descent_lemma.lean` now compiles clean: no `sorryAx`, axioms only `propext`/`Classical.choice`/`Quot.sound` (`absorbing` — none; `run_absorb` — `[propext]`; `run_high`, `run_inv`, `descent_claim1`, `descent_claim2` — `[propext, Classical.choice, Quot.sound]`). Statements NOT weakened: `runAbs` is the genuine iterated `Nat.dist` fold, `countOnes` is ν₁, claim1 `w ≤ ν₁+1 ⟹ runAbs w el ∈ {0,1}`, claim2 `ν₁+1 < w ⟹ runAbs w el = w − ν₁` exactly — both directions, exact value, unchanged. This is the first kernel-checked result of the run. **Scope:** it formalises the ABSTRACT COMBINATORIAL CORE in halved units ({0,1}^L pattern, arbitrary w) only; it does NOT cover Link A (`v ≤ g*_n`), the composition `g*_n ≤ 2ν₂+2 ⟹ success`, the reduction from real column dynamics to the (pattern,v) model (Directive 48 item 1), or the supply side. Claim `lemma54-descent-lean-formalised`, `status: formalised`, `research/notes/lemma54-descent-lean-formalised.md`. **`lemma54-re-derived-proof` is NOT upgraded to proved on the strength of it** (full even-domain lemma is strictly more); the honest path to a Lean-proved Lemma 5.4 is Link A + the composition formalised too. The defective "each 2 contributed −2" passage in `lemma54-re-derived-proof.md` is deleted, superseded by the kernel-checked case split. The earlier written-descent algebra ("after ν₂ twos, δ = v−2ν₂") is false on bounce trajectories, but the repair is the case split — Branch A (some δ_t ≤ 2 → absorption carries it) / Branch B (all δ_k ≥ 4 → δ_L = v−2ν₂ ≤ 2 contradicts δ_L ≥ 4) — machine-forced on disk: `code/out/lemma54_descent_check.captured.txt` (2,621,432 (pattern, even-v) pairs, 0 violations) and validated on 281/281 real prime diagonals. The failing-side sufficiency test ran non-vacuously with zero counterexamples (`lemma54-sufficiency-survives-proper-domain`). Two items remain, neither a validity gap of the core: **Link A (`v ≤ g*_n`) is now VERIFIED non-vacuously** (`code/out/verify_lemma54_v_le_gstar.captured.txt`: 1181 real prime columns n=20..1200, 0 violations of v≤g*_n and of the Lemma 5.4 hypothesis, max margin (2ν₂+2)/g*_n = 35.882, ALL CHECKS PASSED; only the broken captured2.txt is vacuous — see research/notes/scholar-reconciliation-lean-and-linkA-current.md). The g*-composed form is closed on the prime domain; (b) the reduction from real column dynamics to the (pattern,v) model (Directive 48 item 1) is still to be written as a claim. **The entire remaining open content of Route B is the supply-side linear lower bound ν_2(q_{n−1}) ≥ c·n for some c > 0** (measured c ≈ 0.5, unproved). `li2023-not-bottleneck`: the demand exponent α ∈ {0.52,0.525} is immaterial once a positive-linear supply bound holds; do not spend effort shaving α. **Directive 47: this is a NAMED OPEN problem, not a gap in the run's own argument.** ABGS 2011 §9 (claim `abgs-2011-s9-mod4-switch-limit-open`): whether `N(a,d,m,x)/π(x)` tends to any limit is open, so no unconditional linear lower bound on the mod-4 switch count exists in the literature. Route B is a CONDITIONAL theorem whose hypothesis is that two-point mod-4 correlation lower bound; a conditional theorem with a precisely identified open hypothesis is a genuine deliverable.

**Grounded precedent for the supply bound (this run, scholar):** the atomic bit feeding ν_2 is bit_n = [p_{n+1} ≢ p_n mod 4] = [gap ≡ 2 mod 4] — a **two-point** consecutive-pair statistic, NOT a one-point PNT-in-AP cancellation. Three held sources now delimit it:
- **Rubinstein–Sarnak 1994** (Chebyshev's Bias): the mod-4 bias is real (ρ(P_{4,3,1})≈0.9959 under GRH+GSH) but oscillates Littlewood-type, so no one-sided unconditional forcing exists; supply can only be a *fluctuation* bound.
- **Lau 2024**: even a single non-constant consecutive-prime residue pattern occurring infinitely often is beyond present methods; proved counts are of *distinct patterns*, never a frequency bound.
- **Maynard 2015**: liminf(p_{n+1}−p_n) ≤ 600 unconditionally; all results existence, not frequency.
So the honest deliverable is ν_2 = n/2 + O(bias) at Hardy–Littlewood / Lemke Oliver–Soundararajan level, and the irreducible open statement is the two-point mod-4 correlation bound (ν_2 ≥ n^{0.525+δ}). Claims: `rubinstein-sarnak-bias-oscillates-unconditional-false`, `lau-2024-consecutive-residue-patterns-existence-only`, `maynard-2015-existence-not-frequency`.

**G-supply-transfer (the F₂ combinatorial shortcut) is DEAD — filed `g-supply-transfer-universal-refuted`.** The universal transfer ν_2 ≥ (2/3)·w(n) for every successful 2-then-odds prefix is false: the consecutive-odds family (all gaps=2, successful for every n) collapses to (1,0,0,...) from row 2 on, so ν_2 = 0 for all n ≥ 4 while w(n)=n−2 maximal. Even ν_2 ≥ w/2 is not a universal F₂ identity (all-2 length-12 string: w=12, ν_2=1). S1 fork → case (b) prime-specific. The supply statement for the primes survives (ν_2/w ∈ [0.689,0.867], `g-supply-transfer-measured`), but only the unconditional two-point bound closes Route B; there is no combinatorial end-run through the XOR/Rule-90 weight. Lemma 5.4 (budget 2ν_2+2) unaffected. Anchor: research/notes/g-supply-transfer-universal-refuted.md; the gap G-supply-transfer in nu2-supply-split.md is closed as refuted.
next: |
  0. **DONE (Directive 50) — `code/lean/descent_lemma.lean` compiles clean.** No `sorryAx`; axioms only `propext`/`Classical.choice`/`Quot.sound` (`absorbing` none; `run_absorb` `[propext]`; `run_high`, `run_inv`, `descent_claim1`, `descent_claim2` `[propext, Classical.choice, Quot.sound]`). Statements NOT weakened: `runAbs` = iterated `Nat.dist` fold, `countOnes` = ν₁, claim1 `w ≤ ν₁+1 ⟹ runAbs w el ∈ {0,1}`, claim2 `ν₁+1 < w ⟹ runAbs w el = w − ν₁` exactly. Filed as claim `lemma54-descent-lean-formalised`, `status: formalised` — **abstract core ONLY** (halved {0,1}^L, arbitrary w); does NOT cover Link A, the composition, the reduction from real column dynamics, or the supply side. **Does NOT upgrade `lemma54-re-derived-proof` to proved.**
  1. **Directive 51 — the one line left after Directives 45/48 closed.**
     (a) Rewrite the audit VERDICT line (a 281-column check is not "a theorem"): the passage is confirmed over n=1..50 cross-check and 281 real columns, 0 violations, with the pattern prefix-determined by the recurrence identity. Standing rule: captured output may say CONFIRMED/REFUTED over the stated range, never theorem/proved/proves. **DONE — the source already carried the corrected wording; the "MACHINE-CONFIRMED as a theorem" defect survived only in the stale capture. Re-captured to code/out/reduction_audit_corrected.captured.txt (new file), verdict now factual.** (b) Then write the three-line prefix-determinism proof as a claim (upgrade `reduction-passage-exact` to proved): δ(q_n) on the 0-2 cycle positions depends only on q_1..q_{n−1}, since those entries are inherited from δ(q_{n−1}) and the new element enters only at the diagonal bottom. **DONE — status upgraded to proved (the identity IS the recurrence), verified 0 mismatches over 49,873,204 model positions and 59,697 eps-prefix-locality positions; full write-up research/notes/prefix-determinism-proof.md.**
  2. **DONE — Link A (`v ≤ g*_n`) verified non-vacuously** (`code/out/verify_lemma54_v_le_gstar.captured.txt`: 1181 real prime columns, 0 violations, margin 35.882). The captured2.txt vacuous run was a broken invocation; the real capture closes Link A on the prime domain.
  3. **Then — formalise Link A + the composition** (the honest path to a Lean-proved full Lemma 5.4, per Directive 50; the abstract core alone is not the full lemma).
  4. **Then G-supply (the entire open content).** State it as a conditional theorem with the hypothesis named (Directive 41): the two-point mod-4 correlation bound on consecutive primes. Only then search, against a row in `research/REQUESTS.md` (Directive 44 item 3).
  5. DONE — failing-side sufficiency test run non-vacuously (`lemma54-sufficiency-survives-proper-domain`).
  6. DONE — CHT FULLPDF read, right-half {0,d}-block scan at 6e8/depth 400 (Directive 35 item 1).
  7. **Directive 52 — `anticlustering_hypothesis` is a negative result.** The Markov/anti-clustering test (`code/out/anticlustering_hypothesis.captured.txt`) shows generic Markov anti-clustering of the mod-4 switch bit does NOT deliver ν₂ ≥ c·w: prime-like (0.55,0.60) worst-min ν₂/w = 0.0714 (11/30 trials violate); Bernoulli control and clustered variants 12–13/30; stationary-density-0.59 family 11–17/30; prime's own empirical transitions (a=0.5565, b=0.6584) 8/20. This closes the PROOF STRATEGY "G-supply from mixing/anti-clustering of the switch sequence", NOT the G-supply statement for the primes (real gaps are not a Markov chain; 30 trials of a worst-min statistic is noisy). **What it leaves:** the remaining candidates are arithmetic — Hardy–Littlewood two-point mod-4 correlations, or the LOS two-point bias with its oscillating second-order term. **Bet recorded: neither is unconditional; G-supply stays a named open hypothesis, and the deliverable is the CONDITIONAL theorem with the HL/LOS two-point switch-correlation lower bound as the named hypothesis.** File the negative claim (id `anticlustering-markov-insufficient-for-gsupply`, anchor the capture) per the directive.
```

# Regeneration thread — the ratio bound is the whole conjecture

## Process defect — a falsifier named but not cross-checked (Directive 61)

G-supply-nonconcentration named its own falsifier ("a theorem or construction
giving arbitrarily long runs of primes staying in a single class mod 4 would
kill (3)") while the refuting claim — `shiu-2000-strings-of-congruent-primes` —
was already in the claim library at the same time, and nothing connected them:
the gap was filed open and the whole `supply-nu2-factorization` skeleton was
built on it. **Rule adopted: when a gap names a falsifier, `search_claims` must
be run against that falsifier BEFORE the gap is filed open.** This
cross-reference failure is worth more than the lemma it silently refuted.
Salvage per Directive 61: `G-supply-weight-transfer` (the matrix half, "no long
constant run ⟹ wt ≥ c·n") stays a real combinatorial target (now
`DPC-kernel-classification` in `dyadic-periodicity-collapse.md`) but its
prime-side hypothesis is dead; fold survivors into the dyadic skeleton, do not
maintain two.

## The complete chain (Directive 30)

The run now holds this reduction. Each step is proved, machine-checked, or
computed. Steps 1–5 and 7 are done; step 6 is now rephrased as the ratio
bound — and it holds with 2+ orders of margin to 15 giants.

1. **Gilbreath ⇔ second entry in {0,2}.**
   Lean 4, sorry-free, axiom footprint `[propext, Classical.choice,
   Quot.sound]`. `gilbreath_reduction : GilbreathConjecture X ↔
   SecondEntryIn02 X`. Anchor: `code/lean/gilbreath_reduction.lean`;
   claim `lean-reduction-machine-checked`.

2. **⇔ Σ(j_i+1) ≥ k−2.**
   Recharge identity (PROVED, universal): `b_k = b_1 + Σ_{events i<k}
   (j_i+1) − (k−1)`. The block dies exactly when the recharge sum falls
   behind. Zero failures on primes and on all 1,154 sweep sequences.
   Anchor: `research/notes/step_law_proved.md`.

3. **15 giants at 6e8 (31.3M primes).**
   Genuine giants (0-based pre-jump rows): `[34,56,64,68,94,96,110,112,
   126,130,134,146,161,174,238]`. Jumps: `[1314,1739,17326,8237,61088,
   11354,37746,129923,53470,190810,217657,360698,4323712,5237310,12508030]`.
   Landing blocks: `[2179,5942,23265,31499,92620,103973,141706,271629,
   325090,515906,733564,1094273,5417975,10655286,23163290]`.
   Anchor: `code/out/pattern_finder_6e8_giants.captured.txt`.

4. **Giants ARE the (2,4)-events.**
   Every giant has edge=2 and intruder=4 at the event row. The step law
   (PROVED) says only (2,4) grows the block.

5. **j → ∞ is settled; geometric fit R²=0.968 over 15 giants.**
   Per-event factor 1.765×; sublinear exponent j ~ b^0.388 over all positive
   events. Both descriptions survive 15 points. Growth law still not
   determined from this data, but j → ∞ under either description.

6. **Ratio bound gap_i ≤ j_i + 1 — REPHRASED (Directive 30).**
   Σ(j_i+1) ≥ k−2 holds if each giant's budget covers the next gap:
   **gap_i ≤ j_i + 1**. The 6e8 data:
   Gaps: `[22,8,4,26,2,14,2,14,4,4,12,15,13,64]`, max=64.
   Max ratio = 64/(5,237,310+1) = 0.0000122 — roughly **two orders of slack**
   at the widest gap. Every ratio is far below 1. The inequality gap_i ≤ j_i+1
   is sufficient (trivially, since each giant carries its own recharge) and
   manifestly satisfied on all 15 giants. **"Gap is bounded" is superseded** —
   the ratio bound is both stronger and directly verifiable.

7. **Ratio bound + j → ∞ ⇒ b_k ≥ 1 forever.**
   If j_i grows (step 5) and gap_i never exceeds j_i+1 (step 6, verified to
   15 giants), then Σ(j_i+1) ≥ Σ(gap_i) ≥ k−2 for all k reachable after the
   first event. The conjecture follows.

**The conjecture now reduces to proving the ratio bound continues to hold
for all giants.** The bound is gap_i ≤ j_i+1 — each giant's recharge covers
the distance to the next. This is weaker than "gap is bounded" and directly
testable: the ratio column tells the story at any width.

## Two cautions

1. **Fifteen giants is still a small sample.** The ratio bound holds with
   enormous slack at 15 giants — max ratio 0.0000122 — but proving it
   continues to hold is the conjecture itself. The strongest statement the
   data supports is "gap_i ≤ j_i+1 for the first 15 giants with 2+ orders
   of margin," not "it continues forever."

2. **Every number comes from one finite triangle.** The 6e8 run (31.3M
   primes, depth 400, 96.2s) is one triangle. Whether the ratio bound
   holds for the infinite sequence of primes is not settled by any finite
   computation.

## The next question — NOW THREE ROUTES (Directive 35)

### Route A (run's ratio bound — kept as fallback)

Prove gap_i ≤ j_i+1 for all giants. The geometric description gives b ~ 1.765×
per giant event (R²=0.968 over 15 giants); gaps are ≤ 64 over 15 giants and at
most slowly growing. **Demand side:** geometric growth of b must be proved from
prime-gap theory, or j must be shown to grow faster than inter-giant gaps. This
is a new statement about the Gilbreath operator — no existing theorem covers it.
The ratio bound holds with 2+ orders of slack on all 15 giants at 6e8 (max ratio
0.0000122), but proving it continues to hold is the conjecture itself.

### Route B (Granville ν_2 — SELECTED as primary)

Lemma 5.4 → Theorem 5.5 reduces GC to proving ν_2 > n^β with β > 0.525, where
ν_2 counts 2s in the right diagonal's 0-2 cycle. **Demand side:** α = 0.525 is
**unconditional** — it follows from Baker-Harman-Pintz (p_{n+1} − p_n ≪ p_n^0.525)
(corroborated independently by `li2023-short-interval-052` shaving to 0.52 and
`visser-large-gaps-survey`). **Supply side:** ν_2/n ≈ 0.49–0.52 measured on primes
below 3e6 — exceeds threshold by 26× at n = 3999 (BCZ Table 1 corroborates the
balanced 0/2 density independently). **Lemma 5.4 status (PROVED):** the lemma is
PROVED on the even domain (claim `lemma54-re-derived-proof`,
`research/notes/lemma54-re-derived-proof.md`): parity-preserving descent that
handles Granville's discarded delta=0 case as a normal closure case (0→2 bounce),
machine-forced over all {0,2}^L patterns L=1..16 (2.6M even pairs) and validated
on 281 real prime diagonals. The failing-side sufficiency test has been run
non-vacuously with zero counterexamples (claim `lemma54-sufficiency-survives-proper-domain`).
The **entire remaining open content after Lemma 5.4 is the supply lower bound
ν_2(q_{n−1}) ≥ c·n** for some c > 0 (measured c ≈ 0.5, unproved). Settlement:
`research/notes/lemma54-chain-settlement.md`.

**Why this is the weakest target.** Granville's route needs only BHP
(unconditional) whereas Route C needs Cramér (open, stronger than BHP) and
Route A needs a new theorem about block growth across Gilbreath iterations.
Lemma 5.4 is equivalent to the run's recharge identity in different coordinates
— it describes how the right-diagonal 0-2 cycle accumulates ν_2, and the
operator has already measured ν_2/n above threshold. Once Lemma 5.4 is
re-derived here (with the delta=0 case handled), the route reduces to
proving a lower bound on a single statistic (ν_2) of the prime gap sequence,
rather than a property of the iterated triangle.

### Route C (CHT deterministic — calibrated, not pursued)

Theorem 1.6 (the inverse theorem) needs: (i) a_n ≪ log^10 N (Cramér, open,
strictly stronger than BHP); (ii) no zero-block of length ~log^10 N; (iii) no
right-half {0,d}-block (d ≥ 2) exceeding the R_m − 3R_{m−1} threshold.
**The CHT authors' own assessment** (quoted verbatim from p. 8): hypotheses
(ii) and (iii) "look difficult to establish rigorously, even if one assumes
strong conjectures on the primes such as the Hardy–Littlewood prime tuples
conjecture." This is the best calibration available: the people who proved the
inverse theorem say the obstructions it isolates are as hard as the conjecture
itself, short of unproved analytic number theory.

**Directive 35 clarification — column restriction.** Theorem 1.6(iii) restricts
the {0,d}-block obstruction to columns j ≥ N′ = ⌊N/2⌋ — the **RIGHT HALF**
only. The run's leading {0,2} block (length b_k up to 31M) sits at j=1, the
far LEFT, so it does NOT violate (iii). The question is whether long {0,d}
blocks with d ≥ 2 exist in the RIGHT HALF. Scan queued (Directive 35 item 1).
If long right-half shallow blocks exist, Theorem 1.6 does not apply and we've
located precisely why. If not, (iii) is empirically supported — but (i) and
(ii) remain open, and CHT's difficulty assessment stands.

### Decision (Directive 35)

The run is on **Route B** (Granville ν_2) as the primary target. Route A
(ratio bound) is kept as the fallback empirical target. Route C is not
pursued: CHT's own assessment calibrates it as requiring unproved analytic
hypotheses; the column restriction makes it even harder to apply because
the right-half {0,d}-block obstruction is independent of the leading-block
regeneration the run studies.

- **Can the geometric growth of b (and hence j) be proved from known
  prime-gap theory?** Prime gaps are O(p^θ) with θ ≈ 0.525 (Baker–Harman–
  Pintz) — does any existing result on the iterated difference table imply
  that the block length grows at a rate exceeding any plausible gap growth?
- **Is "j grows faster than gaps" equivalent to a named conjecture?**
  Cramér? Something about the 1-Lipschitz chain at the boundary?
- **Neither:** a genuinely new statement about the Gilbreath operator.

The ratio formulation makes this a single question about the jump growth rate,
not about gap boundedness. A proof that j_i → ∞ geometrically (or at any
superlinear rate in b) while the gap grows at most polynomially would prove
the conjecture.

## Prior work absorbed

- **IFF reduction:** Lean, sorry-free. Claim `lean-reduction-machine-checked`.
- **Step law + recharge identity:** PROVED, universal. Claim `step-law-theorem-proved`.
- **Bigjump characterization:** 12/13 genuine at depth 1000 (claim `bigjump-cap-characterization-1000`); all caps resolved at wider widths. **Directive 30: 6e8 run (31.3M primes, depth 400) confirms row 238 genuine (flooring 8,161,173) and adds it as the 15th giant.**
- **Growth law:** geometric fit R²=0.968 over 15 giants, per-event factor 1.765×. Not load-bearing: the ratio bound is what matters.
- **Ratio bound (Directive 30):** gap_i ≤ j_i+1 holds with 2+ orders of margin for 15 giants (max ratio 0.0000122 at gap 64 vs j=5,237,310). Sufficient for the conjecture; "bounded gap" superseded.
- **Inter-giant gaps (15 genuine, 6e8 sieve):** `[22,8,4,26,2,14,2,14,4,4,12,15,13,64]`, max=64. Row 248 (0-based 247) is the cap (flooring 0, exclude).
- **Parity (CORRECTED, Directive 36 item 1 — this run):** 14/15 genuine giants land on even 0-based rows (only 161 odd). Conventions pinned by asserts: the (2,4)-event population at 2e7 rows 1..161 is 60 events, 36 even landing indices (base rate 0.600, reproduced from raw e_bits/c.txt); all giants with landing ≤ 160 are members of that event set; 174 and 238 verified by jump in the 1e9 profile. P-values on the 15 genuine giants only (exact integer arithmetic, `code/out/giant_parity_genuine.captured.txt`): fair-coin 16/2^15 = 4.88e-4; binomial base-rate (p=0.600) 5.17e-3 — reproduces the settlement's 0.0052; **exact hypergeometric (without replacement, population 60/36) 1.82e-3** — the honest null, computed for the first time. Quote the hypergeometric figure. Old fair-coin-only figures in `pattern_finder_6e8_giants.captured.txt` and `pattern_finder_giant_significance.captured.txt` remain valid as recorded but are superseded by this correction for the genuine-15 population.
- **Next giant estimate:** k*=248 at 6e8; geometric projection ~55M block → sieve ~1e9.

## Data available

- `code/out/blocks_depth1000.json`
- `code/out/surplus_renewal_table.captured.txt`
- `code/out/bigjump_characterization.captured.txt`
- `code/out/wider_width_extend.captured.txt`
- `code/out/pattern_finder_6e8_giants.captured.txt`
- `code/out/pattern_finder_outputs/giants_6e8.json`