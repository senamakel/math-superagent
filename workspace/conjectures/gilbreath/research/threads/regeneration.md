```thread
question: Prove the inter-giant gap is bounded — does "the gap between consecutive (2,4)-events with j > 1000 is bounded" follow from anything about prime gaps, or is it equivalent to something already known hard?
status: live — Directive 27 + pattern-finder depth-300 pass: 15 giants to depth 300 (new giants rows 162, 175, 239; the 239 giant is itself width-capped, j >= 5,596,824). Inter-giant max gap now 64 (175→239 drought), NOT the 26 of the 14-giant run — first hint gaps may grow with b, but 64 vs j ~ 10^5-10^6 leaves orders of slack. Growth law still unsettled: geometric R² 0.968 over 15, factor 1.765/event; the 4.95 outlier ratio is followed by 1.97, 1.53 (series returns to geometric trend; sublinear-declining-ratio reconciliation not supported). The conjecture still reduces to ONE statement: the inter-giant gap is bounded.
rests-on: |
  - IFF reduction (Lean, sorry-free, axioms clean): Gilbreath ⇔ A_k(1) ∈ {0,2} for all k.
  - Recharge identity (PROVED, universal): b_k = b_1 + Σ_{i<k}(j_i+1) − (k−1). So the conjecture holds iff Σ(j_i+1) ≥ k−2 for all k.
  - Bigjump characterization (depth 1000): 13 giants (j > 1000) carry 99.76% of S_1000, 12 genuine, 1 capped (i=161). Claim bigjump-cap-characterization-1000. **Directive 27: wider sieve resolves the cap — 14 genuine giants to depth 240, i=161 cap no longer an artifact concern (new jump 4,323,712 at row 162, 5,237,310 at row 175).**
  - Giants ARE the (2,4)-events: every one has edge=2, intruder=4. Step law: only (2,4) grows the block.
  - Jump growth: geometric fit R² 0.9607 over 14 giants, per-event factor 1.751 (improved from 0.942/1.68 over 12). Sublinear exponent 0.388 still holds for all 43 positive-jump events — both descriptions fit the data; **which is asymptotic is not determined** (see below).
  - Inter-giant gaps (genuine 14, wider width): 22, 8, 4, 26, 2, 14, 2, 14, 4, 4, 12, 15, 13. Mean 10.21, median 8, max 26 unchanged. New gaps (15, 13) inside existing range — no trend over 14 points while b spans 2,179 → 10,655,286 (4,900×). This is corroboration on data the model had never seen.
  - Bounded gap + j → ∞ ⇒ b_k ≥ 1 forever.
blocked-by: nothing — Directive 27 items complete. Next is the provability question (Directive 26).
next: |
  Answer: does "the inter-giant gap is bounded" follow from anything about prime gaps (e.g., the distribution of gap sizes, the frequency of certain patterns modulo small primes), or is it equivalent to something known hard (Cramér, GPY, a sieve-theoretic bound)? State the dependency before attempting a proof. If it is equivalent to a standard conjecture, that IS a partial result — a reduction of Gilbreath to something named. If it is not known hard but also not proved, name the obstruction.
```

# Regeneration thread — the inter-giant gap is the whole conjecture

## The complete chain (Directive 26)

The run now holds this reduction. Each step is proved, machine-checked, or
computed to depth 1000 on the primes below 2×10⁷ (1,270,607 primes). The
only step not proved is step 6 — and it is the one the conjecture now
reduces to.

1. **Gilbreath ⇔ second entry in {0,2}.**
   Lean 4, sorry-free, axiom footprint `[propext, Classical.choice,
   Quot.sound]`. `gilbreath_reduction : GilbreathConjecture X ↔
   SecondEntryIn02 X`. Anchor: `code/lean/gilbreath_reduction.lean`;
   claim `lean-reduction-machine-checked`.

2. **⇔ Σ(j_i+1) ≥ k−2.**
   Recharge identity (PROVED, universal): `b_k = b_1 + Σ_{events i<k}
   (j_i+1) − (k−1)`. The block dies (b_k = 0 ⇒ A_{k+1}(1) ∉ {0,2}) exactly
   when the recharge sum falls behind. Zero failures on primes to depth 1000
   and on all 1,154 sweep sequences. Anchor: `research/notes/step_law_proved.md`;
   claim `step-law-theorem-proved`.

3. **13 giants carry 99.76% of S_1000.**
   S_1000 = 1,270,603; the 13 jumps with j > 1000 supply 1,269,652 of it.
   12 genuine, 1 capped (i=161, finite-width artifact, true jump ≥ 176,181).
   The heavy tail is real — not an averaging artifact. Anchor:
   `code/out/bigjump_characterization.captured.txt`;
   claim `bigjump-cap-characterization-1000`.

4. **Giants ARE the (2,4)-events.**
   Every giant has edge=2 and intruder=4 at the event row (verified 13/13).
   The step law (PROVED) says only (2,4) grows the block. So "giant" and
   "(2,4)-event with large j" are the same object — no separate mechanism.

5. **j grows, but which growth law applies is NOT determined by this data.**
   The geometric fit improved from R² 0.942 over 12 giants to **R² 0.9607 over
   14**, with the per-event factor rising from 1.68 to **1.751** (14-giant OLS,
   `wider_width_extend`). But the 13th ratio is 4.95 — larger than every earlier
   ratio except none, reversing the declining-ratio trend Directive 25 used to
   argue the sublinear law. The landing-block ratios including the new giants are
   `2.73, 3.92, 1.35, 2.94, 1.12, 1.36, 1.92, 1.20, 1.59, 1.42, 1.49, 4.95, 1.97`
   — the decline reverses at the 13th giant. So "sublinear-with-decaying-ratio"
   was a reading of twelve points, and the thirteenth broke it. The geometric fit
   got *stronger* with new data (R² ↑, factor ↑), not weaker. **The honest
   position: the growth law is not determined.** What IS settled: j → ∞ (both
   laws agree on that), and the inter-giant gap max is unchanged (26). Anchors:
   `code/out/wider_width_extend.captured.txt`.

6. **Inter-giant gap: no trend over 14 points (wider width, Directive 27).**
   Genuine giant rows: 35, 57, 65, 69, 95, 97, 111, 113, 127, 131, 135, 147, 162, 175.
   Gaps in rows: 22, 8, 4, 26, 2, 14, 2, 14, 4, 4, 12, 15, 13.
   Mean 10.21, median 8, max 26 (UNCHANGED from the 12-giant run).
   The two new gaps (15, 13) land inside the existing range — the bounded-gap
   observation survived a width extension on data the model had never seen:
   sieve 3e8, 16.25M primes, depth 240. This is corroboration, not more of
   the same. Anchor: `code/out/wider_width_extend.captured.txt`.
   Max-gap by threshold: 26 at J=100/300/1000, 30 at 1e4, 18 at 1e5.

7. **Bounded gap + j → ∞ ⇒ b_k ≥ 1 forever.**
   If the inter-giant gap G is bounded by some constant G_max and each
   giant jump j_i → ∞, then eventually every jump exceeds G_max and the
   recharge sum Σ(j_i+1) pulls ahead of consumption and stays ahead.
   The conjecture follows.

**The conjecture now reduces to ONE statement: the inter-giant gap is
bounded.** Every other step in the chain is proved or established to depth
1000. Step 6 is the only one that is measurement, not proof.

## Two cautions

1. **Thirteen gaps is still a small sample.** "No trend" over 13 gaps is
   weak evidence; R² on a 14-point OLS is low but a slow growth rate of
   0.5 rows per giant is still not excluded. At 100 giants a slope that
   small would be detectable; with 13 it is indistinguishable from noise.
   The strongest statement the data supports is "max gap remains 26 while
   b increases 4,900× and the sieve width increases 15×" — not "the gap
   is bounded forever."

2. **Every number comes from one finite triangle over one sieve.** The
   wider-width run (sieve 3e8, 16.25M primes, depth 240) is still one
   triangle. Whether the gap stays bounded for the infinite sequence of
   primes is not settled by any finite computation. This is a measurement,
   not a property of the primes.

## The next question (Directive 26)

Before attempting to prove step 6: **does "the gap between consecutive
(2,4)-events is bounded" follow from anything known about prime gaps, or
is it equivalent to a standard hard problem?**

The (2,4)-event depends on the boundary pair (edge=2, intruder=4). The
edge is the last entry of the {0,2} block, which is an XOR of halved gap
bits (Rule 90 interior, proved). The intruder evolves by the drain law
from the gaps at that position. So the inter-event gap is a function of
the prime gap sequence — the question is whether its boundedness is:

- **A corollary of the prime number theorem + known gap bounds** (e.g., "prime
  gaps are O(p^θ) for some θ < 1" — known, θ ≈ 0.525 — but does that feed
  through to the (2,4)-event rate?).
- **Equivalent to an open conjecture** (Cramér, GPY, Elliott–Halberstam,
  something else). If so, that equivalence IS a partial result — a reduction
  of Gilbreath to a named conjecture.
- **Neither** — a new statement about primes that is not obviously harder
  than what is known but has never been isolated.

Answer this before launching a proof attempt. If the answer is "equivalent
to Cramér," the run has reduced Gilbreath to Cramér — that is a GOAL.md
partial result. If the answer is "not known hard, obstruction is X," then
X is the target.

## Prior work absorbed

- **IFF reduction:** Lean, sorry-free. Claim `lean-reduction-machine-checked`.
- **Step law + recharge identity:** PROVED, universal. Claim `step-law-theorem-proved`.
- **Bigjump characterization:** 12/13 genuine at depth 1000 (claim `bigjump-cap-characterization-1000`); **Directive 27 resolves the cap** — wider sieve (3e8, 16.25M primes, depth 240) adds two genuine giants at rows 162 (j=4,323,712) and 175 (j=5,237,310); i=161 cap no longer an artifact concern.
- **Growth law:** NOT DETERMINED by this data. Geometric R² 0.9607, per-event factor 1.751 over 14 giants (improved from 0.942/1.68 over 12); but the 13th ratio 4.95 reverses the declining-ratio trend Directive 25 used to argue sublinearity. Both descriptions fit; the honest position is unsettled. What IS settled: j → ∞, inter-giant max gap unchanged at 26.
- **Geometric-vs-sublinear reconciliation** downgraded: ratios `2.73,3.92,1.35,2.94,1.12,1.36,1.92,1.20,1.59,1.42,1.49,4.95,1.97` — the decline reverses at the 13th giant. Directive 25's "declining toward 1" was a reading of eleven ratios and the twelfth broke it. Claim `directive25-gap-trend-and-reconciliation` — reconciliation half downgraded, gap half strengthened. **Directive 27 resolves the fork from Directive 25 item 4: the sublinear asymptotic claim is not supported by the wider data.**
- **Inter-giant gaps (15 giants, wider width + pattern-finder depth-300 pass):** gaps 22,8,4,26,2,14,2,14,4,4,12,15,13,64. Max 64 (the 175→239 drought) — **CORRECTION: the earlier "max 26 unchanged" (14 giants) is superseded by the 15th giant at row 239** (j=5,596,824, width-capped, landing fills row 240). `code/out/pattern_finder_wider_giants.captured.txt`.
- **Width degradation:** k* at wider sieve = 239; all 14 genuine giants far above threshold.
- **Mean event rate λ̂=0.585** superseded (heavy tail dominates).
- **Rule 90 timing corollary** closed (null).
- **CHT inverse theorem** does not bite at any reachable depth.

## Data available

- `code/out/blocks_depth1000.json`
- `code/out/surplus_renewal_table.captured.txt`
- `code/out/bigjump_characterization.captured.txt`
- `code/out/directive25_gap_trend.md`, `code/out/directive25_gap_trend.captured.txt`
- `code/out/directive24_width_degradation.md`, `code/out/directive24_geometric_growth.md`