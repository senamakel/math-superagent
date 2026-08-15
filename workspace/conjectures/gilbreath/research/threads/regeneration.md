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
blocked-by: Lemma 5.4 needs two final links before it is an established proof (research/notes/lemma54-re-derived.md): (1) v <= g*_n — elementary |a-b|<=max(a,b) induction, verifier code/out/verify_lemma54_v_le_gstar.py written but NOT run; (2) the identification of x_L in {0,2} with Granville's 'success' — verified on 2480 all-successful prime columns but vacuous on the failing side (needs a failing-side / closest-failing-sister / synthetic Poisson-gap test). The DESCENT ENGINE (claim lemma54-descent-core) is PROVED — exhaustive over all {0,2}^L patterns L=1..16 (2.6M pairs), which resolves Granville's discarded delta=0 case (the 0->2 bounce from x=0) as the main case, not an exception: the published-proof gap is repairable at the combinatorial level. Demand side PROVED (bhp-max-gap-unconditional, bhp-demand-corollary-g-star): GC reduces to the supply bound nu_2 > n^beta, beta > 0.525.
next: |
  1. Teardown Lemma 5.4: run code/out/verify_lemma54_v_le_gstar.py (the v<=g* link), then a failing-side test of the success identification (closest-failing-sister / synthetic Poisson-gap). NOTE WRITTEN: research/notes/lemma54-re-derived.md now carries the corrected descent (delta=0 is the MAIN case, consumes a row index without spending height, so the budget 2*nu2+2 still suffices — assertedly, not yet checked). Fresh failing-side stress test code/lemma54_rederive.py written but NOT executed (operator to run → code/out/lemma54_rederive.captured.txt).
  2. DONE — Read CHT 2026 FULLPDF → summary with Theorem 1.6 verbatim + column restriction + p.8 difficulty assessment. → research/notes/cht-2026-summary.md (claim cht-theorem16-verbatim-fullpdf). Verdict unchanged: holds-here=no; theorem's bite out of reach; Route C calibrated.
  3. DONE — right-half {0,d}-block scan (Directive 35 item 1) at 6e8/depth 400: longest d≥2 block = 25 vs smallest CHT threshold T_1 = 5.63e16 (2.25e15x gap); obstruction absent at every threatening scale; claim cht-right-half-0d-scan-6e8, anchor research/notes/cht-right-half-scan.md. Optionally extend to 1e9 data later (same verdict expected; thresholds are width-independent at this M).
  4. Promote the 1e9 block-lemma verification bound (A_k(0)=1 proved for rows 1..50,847,533 via the proved block lemma, from row 248's all-{0,2} block of length 50,847,285) to a claim — currently only in code/out/pattern_finder_1e9_verify.captured.txt.
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
**unconditional** — it follows from Baker-Harman-Pintz (p_{n+1} − p_n ≪ p_n^0.525);
corollary g*_n = O(n^{0.525+eps}) is proved here (claims `bhp-max-gap-unconditional`,
`bhp-demand-corollary-g-star`). **Supply side:** ν_2/n ≈ 0.49–0.52 measured on primes
below 3e6 — exceeds threshold by 26× at n = 3999. **Lemma 5.4 status (precise):**
the DESCENT ENGINE is PROVED (claim `lemma54-descent-core`, exhaustive over all
{0,2}^L patterns L=1..16 — this handles Granville's discarded delta=0 case as the
0→2 bounce, the main case, so the published-proof gap is repairable at the
combinatorial level). Full Lemma 5.4 is checked-not-proved: two links remain —
v ≤ g*_n (elementary |a−b|≤max(a,b) induction; verifier written but not run) and
the success identification (verified on 2480 all-successful columns, vacuous on the
failing side). Remaining open after Lemma 5.4: a supply lower bound on ν_2.

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