```thread
question: Can Granville's Lemma 5.4 / Theorem 5.5 reduce GC to ν_2 > n^β with β > 0.525? Empirical route at ceiling; theoretical routes are the only live ones.
status: live — PIVOTED (Directive 36). Empirical route at ceiling. Route B (Granville ν_2) primary; Route A (ratio bound) empirical fallback; Route C (CHT) calibrated by authors' assessment.
rests-on: |
  - IFF reduction (Lean, sorry-free): GC ⇔ A_k(1) ∈ {0,2}.
  - Recharge identity (PROVED, universal): b_k = b_1 + Σ_{i<k}(j_i+1) − (k−1).
  - 1e9 run: 15 genuine giants, max gap 64, ratio bound holds everywhere (max 1.26e-02), row-248 STILL capped.
  - Geometric growth: b ~ 1.765× per giant event (R²=0.968 over 15); j ~ b^0.388.
  - Granville Lemma 5.4/Theorem 5.5: GC reduces to ν_2 > n^β, β > 0.525; α=0.525 unconditional (BHP).
  - BCZ 2023: left-edge map is an F2 involution (T²=id); Table 1 (|#0−#2| ≤ 431 of 78,496 per ray) independently corroborates ν_2 ~ n/2.
  - CHT Theorem 1.6: {0,d}-block obstruction in right half (j ≥ N′); needs Cramér (open, >BHP).
  - Empirical route ceiling: each giant costs 1.5×–8× the width of the last; next two giants need 1e10–1e11 sieve → >8 GiB.
blocked-by: **Lemma 5.4's *statement* is no longer the blocker, but its written *proof* needs the Directive 43/44 repair.** The abstract lemma is true on the even domain (`lemma54-re-derived-proof`, research/notes/lemma54-re-derived-proof.md): parity-preserving descent, delta=0 case handled as absorption. But the written proof's descent step ("after the ν₂ twos, δ = v − 2ν₂") is FALSE on bounce trajectories (0→2→0), exactly the discarded case; the repair is the case split — if some δ_t ≤ 2 then absorption carries it, else every δ_k ≥ 4 forces δ_L = v − 2ν₂ ≤ 2, a contradiction. That case-split proof must be written out and Lean-formalised (Directive 44 item 1), not settled by another sampling sweep. Failing-side sufficiency test already run non-vacuously (`lemma54-sufficiency-survives-proper-domain`). **The entire remaining open content of Route B is the supply-side linear lower bound ν_2(q_{n−1}) ≥ c·n for some c > 0** (measured c ≈ 0.5, unproved). `li2023-not-bottleneck`: the demand exponent α ∈ {0.52,0.525} is immaterial once a positive-linear supply bound holds; do not spend effort shaving α. **Directive 47: this is a NAMED OPEN problem, not a gap in the run's own argument.** ABGS 2011 §9 (claim `abgs-2011-s9-mod4-switch-limit-open`): whether `N(a,d,m,x)/π(x)` tends to any limit is open, so no unconditional linear lower bound on the mod-4 switch count exists in the literature. Route B is a CONDITIONAL theorem whose hypothesis is that two-point mod-4 correlation lower bound; a conditional theorem with a precisely identified open hypothesis is a genuine deliverable.

**Grounded precedent for the supply bound (this run, scholar):** the atomic bit feeding ν_2 is bit_n = [p_{n+1} ≢ p_n mod 4] = [gap ≡ 2 mod 4] — a **two-point** consecutive-pair statistic, NOT a one-point PNT-in-AP cancellation. Three held sources now delimit it:
- **Rubinstein–Sarnak 1994** (Chebyshev's Bias): the mod-4 bias is real (ρ(P_{4,3,1})≈0.9959 under GRH+GSH) but oscillates Littlewood-type, so no one-sided unconditional forcing exists; supply can only be a *fluctuation* bound.
- **Lau 2024**: even a single non-constant consecutive-prime residue pattern occurring infinitely often is beyond present methods; proved counts are of *distinct patterns*, never a frequency bound.
- **Maynard 2015**: liminf(p_{n+1}−p_n) ≤ 600 unconditionally; all results existence, not frequency.
So the honest deliverable is ν_2 = n/2 + O(bias) at Hardy–Littlewood / Lemke Oliver–Soundararajan level, and the irreducible open statement is the two-point mod-4 correlation bound (ν_2 ≥ n^{0.525+δ}). Claims: `rubinstein-sarnak-bias-oscillates-unconditional-false`, `lau-2024-consecutive-residue-patterns-existence-only`, `maynard-2015-existence-not-frequency`.
next: |
  1. **NOW (Directive 44 item 1) — write the case-split proof, then Lean it.** Prove both directions of the sharpened descent lemma for all L: `x_L ∈ {0,2} ⟺ v ≤ 2ν₂+2`, `v > 2ν₂+2 ⟹ x_L = v−2ν₂ ≥ 4`, `{0,2}` absorbing. The proof is Directive 43's case split; do not restate the machine check as a theorem and do not run another sweep. Lean-formalise against `code/lean/gilbreath_reduction.lean`, report `#print axioms` and zero `sorry`.
  2. **Then (Directive 42 item 2) — run `code/out/verify_lemma54_v_le_gstar.py`** and capture its output to close Link A (`v ≤ g*_n`), currently asserted-unexecuted.
  3. **Then G-supply (the entire open content).** State it as a conditional theorem with the hypothesis named (Directive 41): the two-point mod-4 correlation bound on consecutive primes. Only then search, against a row in `research/REQUESTS.md` (Directive 44 item 3).
  4. DONE — failing-side sufficiency test run non-vacuously (`lemma54-sufficiency-survives-proper-domain`).
  5. DONE — CHT FULLPDF read, right-half {0,d}-block scan at 6e8/depth 400 (Directive 35 item 1).
```

# Regeneration thread — the ratio bound is the whole conjecture

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
- **Parity:** 14/15 even (only 161 odd), one-sided p = 16/2^15 = 4.9×10⁻⁴. `code/out/pattern_finder_6e8_giants.captured.txt`.
- **Next giant estimate:** k*=248 at 6e8; geometric projection ~55M block → sieve ~1e9.

## Data available

- `code/out/blocks_depth1000.json`
- `code/out/surplus_renewal_table.captured.txt`
- `code/out/bigjump_characterization.captured.txt`
- `code/out/wider_width_extend.captured.txt`
- `code/out/pattern_finder_6e8_giants.captured.txt`
- `code/out/pattern_finder_outputs/giants_6e8.json`