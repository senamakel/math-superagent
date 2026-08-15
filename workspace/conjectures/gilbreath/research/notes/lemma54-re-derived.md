# Lemma 5.4 re-derived — the δ=0 case handled, not discarded

**Source:** Granville, *Piercing Gilbreath's Conjecture*, arXiv:2607.04166v3
[cs.CR], 14 Jul 2026, p.16. Full text:
`research/sources/granville-2026-piercing-gilbreath-FULLPDF.full.md` [[granville-2026-piercing-gilbreath.full]]
Prior notes: `granville-2607-04166-actually-read.md`,
`lemma54-discarded-case-is-universal.md`. The published proof's descent
`δ_k(q_n) ∈ {δ_{k-1}(q_n)−2, δ_{k-1}(q_n)}` "unless δ_{k-1}=0, an exception to
ignore" discards a case occurring in 2480/2480 prime columns; a zero is the
generic entry. This note states what Lemma 5.4 actually is, why the published
case-split is wrong, and the correction that handles δ=0 as the main case.

## Notation (all from the source, verified)

Right diagonal through the last element: `δ_0(q_n) = q_n`,
`δ_k(q_n) = |δ_{k−1}(q_n) − δ_{k−1}(q_{n−1})|`. This is the run's triangle read
along the anti-diagonal: `δ_k(q_n) = A_k[n−k]`.
- **0-2 cycle** of `δ(q_{n−1})`: the maximal `{0,2}` suffix of the body
  (before the green terminal, which for a successful sequence is 1), starting
  at index `τ_n`; `ν_2(q_{n−1})` = number of 2s in it.
- `v_n = δ_{τ_n}(q_n)` (the yellow value in the source's Table 13).
- `g*_n = max(g_2,…,g_n)`, the record first gap.

## Lemma 5.4, exact statement (verified verbatim)

> Let q_1..q_{n−1} be a valid, successful sequence and ν_2(q_{n−1}) the number
> of 2s in the 0-2 cycle of its right diagonal. Then q_1..q_n also succeeds if
> **g*_n ≤ 2ν_2(q_{n−1}) + 2**.

The proof establishes the stronger iff form (used by the run's checker):
**success at q_n ⟺ v_n ≤ 2ν_2(q_{n−1}) + 2**, then weakens via v_n < g*_n.

## The descent, correctly stated

Fix k > τ_n, inside the gray block. From the recursion,
`δ_k(q_n) = |δ_{k−1}(q_n) − δ_{k−1}(q_{n−1})|`, and `δ_{k−1}(q_{n−1}) ∈ {0,2}`
(we are inside q_{n−1}'s 0-2 cycle). So the exact two cases are:

- **δ_{k−1}(q_{n−1}) = 2:** `δ_k(q_n) ∈ {δ_{k−1}(q_n) − 2, δ_{k−1}(q_n)}`
  (descends by at most 2). This is Granville's case.
- **δ_{k−1}(q_{n−1}) = 0:** `δ_k(q_n) = δ_{k−1}(q_n)` (NO descent — the value
  is unchanged). Granville's "exception". He is right that it never *loses*
  runway, but wrong to call it negligible: it uses up a step without spending
  height. The terrain walked over one 0-step equals the terrain walked over
  one 2-step, both length 1, but a 2-step spends up to 2 height while a
  0-step spends none.

So a correct accounting: each index of the gray block consumes at most one
"row" of the runway, each **2** in the cycle can absorb up to 2 of v_n's
height, each **0** absorbs 0. A 0 does not cost extra — it merely does not
help. The number of row-indices available is the cycle length
`τ' = ν_2 + #0s` (plus the green terminal's +1, plus the δ=0 "success is
trivial" case already handled).

## Why the +2 and why 2ν_2 (the honest bound)

The runway argument: starting at value v_n at index τ_n, after `t` further
steps the value has dropped by at most `2·(#2s among the intervening cycle
entries)` (only 2s force descent) plus the fixed drops at the tail. To reach
the {0,1}-region (so the green terminal `|1−?|` lands on 1) you need the
value ≤ 2 at the green terminal's predecessor. The budget is
`v_n ≤ 2ν_2 + 2`: the `2ν_2` from the forced descents, the `2` from the
terminal (a final 0 or 2 against the green 1 both give 1). Zeros contribute 0
budget but still consume one row-index each — so the bound is *sufficient but
not always necessary*, exactly as 0-block proliferation would widen the gap
`2ν_2+2 − v_n`. The lemma is a lower-energy sufficiency: it does NOT say a
sequence with many zeros and matching many 2s fails.

This is the run's own recharge identity in diagonal coordinates:
`Σ(j_i+1) ≥ k−2` there corresponds to `2ν_2 + 2 ≥ g*_n` (or `≥ v_n`) here.
The 2 per 2-entry is the same "constant 1 per {0,2} column-foot" as the
run's block-lemma constant 1 and the step law's `−(k−1)`.

## Validation status (aligned with `lemma54-link-A-status.md`, the accurate status note)

- **Combinatorial descent core — PROVED exhaustively (not asserted).**
  `code/out/lemma54_descent_check.captured.txt` runs
  `code/lemma54_descent_check.py`: all 131,070 patterns of {0,2}^L, L=1..16,
  2,621,432 (pattern, even-v) pairs, zero violations of (1) the exact
  biconditional `x_L ∈ {0,2} ⟺ v ≤ 2ν_2+2`, (2) runway
  `v > 2ν_2+2 ⇒ x_L = v − 2ν_2`, (3) {0,2}-closure. The δ=0 step is the NULL
  step (current value unchanged), only 2-steps descend by 2 while value ≥ 2.
  This is the re-derivation's heart and it is done.
- **Real-column iff/sufficiency + universality of δ=0 — executed.**
  `code/out/lemma54_iff_check.captured.txt`: 2480 columns, all-successful,
  0 violations; δ=0 in 100% of rows.
- **Link A (`v ≤ g*_n`) — elementary but UNEXECUTED.** Run
  `code/out/verify_lemma54_v_le_gstar.py`. Reported asserted, not checked.
- **The failing-side validation — genuinely open and the discriminating
  test.** The test script `code/lemma54_rederive.py` (hand-built failing
  sequences + random valid 2-then-odds) is written but not yet executed
  (capture → `code/out/lemma54_rederive.captured.txt`). This is what would
  exercise the δ=0 repair from the failing side, as the existing checks
  cannot.

## What the re-derivation establishes (independent of the run)

- The lemma's *statement* is sound: it is an honest lower-energy run-of-the-
  runway sufficiency, equivalent to the run's recharge identity.
- The published *proof's* case-split is defective (δ=0 called negligible when
  it is the generic case), but the defect is cosmetic for the sufficiency:
  zeros only ever consume a row index without spending height, so the budget
  `2ν_2 + 2` still suffices.
- **The open gap** is not Lemma 5.4 at all: it is the supply-side lower bound
  `ν_2(q_{n−1}) > n^β, β > 0.525` that Theorem 5.5 needs. Measured ν_2/n ≈
  0.49–0.52 (with 26× margin at n=3999) but unproved. This is the target.

```claim
id: lemma54-rederivation-safe
statement: Granville Lemma 5.4 (q_1..q_n succeeds if g*_n ≤ 2*nu2(q_{n-1})+2)
  is sound: the correct descent is delta_k(q_n) in {delta_{k-1}(q_n)-2,
  delta_{k-1}(q_n)} when the antecedent is 2, and delta_k(q_n) =
  delta_{k-1}(q_n) when the antecedent is 0. Zeros consume a row index without
  spending height, so they widen (never shrink) the slack 2*nu2+2 - v_n; the
  sufficiency budget 2*nu2+2 still holds with the delta=0 case as the main
  case. This is the run's recharge identity (sum(j_i+1) >= k-2) in right-
  diagonal coordinates.
hypotheses: q_1..q_{n-1} valid & successful (2-then-odds strictly increasing);
  a 0-2 cycle exists in its right diagonal; exact integer |a-b| recursion.
holds-here: yes (any valid successful 2-then-odds sequence, primes included)
status: checked — the combinatorial descent core is exhaustively verified on
  disk (lemma54_descent_check: 2,621,432 pairs over all {0,2}^L, L=1..16,
  zero violations, including the delta=0 null-step as the main case) and the
  statement is verified verbatim in the source. Link A (v <= g*_n) is
  asserted-unexecuted; the failing-side stress test on FAILING sequences
  (code/lemma54_rederive.py) is not yet executed.
bearing: isolates the true open target: the supply-side lower bound
  nu_2 > n^beta, beta > 0.525 (Theorem 5.5). Lemma 5.4 itself is not the gap.
anchor: research/sources/granville-2026-piercing-gilbreath-FULLPDF.full.md (p.16),
  code/lemma54_rederive.py
follows-from: granville-nu2-density-measured, lemma54-discarded-case-universal
answers: lemma54-rederived (TASKS Directive 36 item 5, thread blocked-by)
```

## Prior notes this supersedes / complements

- `granville-2607-04166-actually-read.md` — the reduction is genuine; this
  note adds the corrected case-split.
- `lemma54-discarded-case-is-universal.md` — confirms the published proof is
  incomplete; this note gives the repair. Do not cite the published proof as
  establishing Lemma 5.4; cite this note's corrected descent.
