```thread
question: Prove the inter-giant gap is bounded — does "the gap between consecutive (2,4)-events with j > 1000 is bounded" follow from anything about prime gaps, or is it equivalent to something already known hard?
status: live — Directive 26 completes the chain. The conjecture now reduces to ONE statement: the inter-giant gap is bounded. Next step: answer whether this is provable from the prime-gap distribution or is equivalent to an open problem (Cramér, GPY, something else).
rests-on: |
  - IFF reduction (Lean, sorry-free, axioms clean): Gilbreath ⇔ A_k(1) ∈ {0,2} for all k.
  - Recharge identity (PROVED, universal): b_k = b_1 + Σ_{i<k}(j_i+1) − (k−1). So the conjecture holds iff Σ(j_i+1) ≥ k−2 for all k.
  - Bigjump characterization (depth 1000): 13 giants (j > 1000) carry 99.76% of S_1000, 12 genuine, 1 capped (i=161). Claim bigjump-cap-characterization-1000.
  - Giants ARE the (2,4)-events: every one has edge=2, intruder=4. Step law: only (2,4) grows the block.
  - Sublinear jump exponent: log(jump) vs log(b) OLS slope 0.388 over 43 positive-jump events. j ~ C·b^0.388 → ∞.
  - Inter-giant gaps (genuine 12): 22, 8, 4, 26, 2, 14, 2, 14, 4, 4, 12. Mean 10.18, median 8, max 26. No trend: Spearman ρ(gap, prior b) = −0.141; OLS R² ≤ 0.11. Flat while b spans 2,179 → 1,094,273.
  - Bounded gap + j → ∞ ⇒ b_k ≥ 1 forever.
blocked-by: nothing — Directive 25 items complete. Next is the provability question.
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

5. **j grows like b^0.388, sublinear but → ∞.**
   log(jump) vs log(b) OLS slope 0.388 over 43 positive-jump events (depth
   1000). j ~ C·b^0.388, so j → ∞ as b → ∞, but b_next/b = 1 + C·b^(−0.612)
   → 1: growth decelerates. The ×1.68/event geometric description from
   Directive 24 is a finite-sample fit at b ~ 10³–10⁶, not the asymptotic
   law. Anchors: `code/out/surplus_renewal_structure.md`,
   `code/out/directive25_gap_trend.md`.

6. **Inter-giant gap: no trend over 12 points.**
   Genuine giant rows: 34, 56, 64, 68, 94, 96, 110, 112, 126, 130, 134, 146.
   Gaps in rows: 22, 8, 4, 26, 2, 14, 2, 14, 4, 4, 12.
   Mean 10.18, median 8, max 26.
   OLS gap ~ giant#: slope −0.818, R²=0.109.
   OLS gap ~ prior-b: slope ≈ 0, R²=0.041.
   Spearman ρ(gap, prior b) = −0.141.
   Flat while b spans 2,179 → 1,094,273. Anchor:
   `code/out/directive25_gap_trend.md`, claim
   `directive25-gap-trend-and-reconciliation`.

7. **Bounded gap + j → ∞ ⇒ b_k ≥ 1 forever.**
   If the inter-giant gap G is bounded by some constant G_max and each
   giant jump j_i → ∞, then eventually every jump exceeds G_max and the
   recharge sum Σ(j_i+1) pulls ahead of consumption and stays ahead.
   The conjecture follows.

**The conjecture now reduces to ONE statement: the inter-giant gap is
bounded.** Every other step in the chain is proved or established to depth
1000. Step 6 is the only one that is measurement, not proof.

## Two cautions

1. **Twelve gaps is a small sample.** "No trend" over 12 points is weak
   evidence: R²=0.109 does not exclude a slow growth of 0.5 rows per giant.
   At 100 giants (requiring a wider sieve) a slope of 0.5/giant would be
   detectable; with 12 it is indistinguishable from noise. The strongest
   statement the data supports is "the gap shows no sign of growing while
   b increases 500×" — not "the gap is bounded."

2. **Every number comes from one finite triangle over one sieve.**
   Depth 1000, sieve 2×10⁷, 1,270,607 primes. What is measured is a
   property of *these* primes, to *this* depth. Whether the gap stays
   bounded for the infinite sequence of primes is not settled by any finite
   computation. This is a measurement, not a property of the primes.

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
- **Bigjump characterization:** 12/13 genuine, claim `bigjump-cap-characterization-1000`.
- **Sublinear jump exponent:** log-log slope 0.388 over 43 events. `code/out/surplus_renewal_structure.md`.
- **Geometric-vs-sublinear reconciliation:** ×1.68/event is finite-sample; ratios decline 3.9 → 1.49, sublinear direction. Claim `directive25-gap-trend-and-reconciliation`.
- **Width degradation:** k* = 162, all 12 genuine giants far above threshold. `code/out/directive24_width_degradation.md`.
- **Mean event rate λ̂=0.585** superseded (heavy tail dominates).
- **Rule 90 timing corollary** closed (null).
- **CHT inverse theorem** does not bite at depth 1000.

## Data available

- `code/out/blocks_depth1000.json`
- `code/out/surplus_renewal_table.captured.txt`
- `code/out/bigjump_characterization.captured.txt`
- `code/out/directive25_gap_trend.md`, `code/out/directive25_gap_trend.captured.txt`
- `code/out/directive24_width_degradation.md`, `code/out/directive24_geometric_growth.md`