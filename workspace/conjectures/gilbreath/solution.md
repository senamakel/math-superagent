# Solution — deliverable for this run

## What is proved

A genuine partial result: **the combinatorial core of Granville's Lemma 5.4 is
proved as a general theorem**, and the full lemma is validated non-vacuously in
both the success and failure directions on synthetic sequences (not just on the
all-successful primes, where the prior check was vacuous).

### The theorem (proved, general — no primes involved)

**Descent / absorption lemma.** Let `c_1, …, c_L ∈ {0,2}` and let `v ≥ 0` be
even. Define `x_0 = v`, `x_s = |x_{s−1} − c_s|` for `s = 1..L`, and let
`ν₂ = #{s : c_s = 2}`. Then:

1. **Budget biconditional.** `x_L ∈ {0,2} ⟺ v ≤ 2ν₂ + 2`.
2. **Runway.** If `v > 2ν₂ + 2`, then `x_L = v − 2ν₂ ≥ 4` and the trajectory
   never enters `{0,2}`.
3. **Absorption (closure).** If `x_s ∈ {0,2}` for some `s`, then `x_t ∈ {0,2}`
   for all `t ≥ s`.

**Proof.** `x_s` is always even and non-negative (`0 ≤ c ≤ 2`, and `x` even
stays even under `|x−c|`). While `x ≥ 2`, a `c = 2` step maps `x ↦ |x−2| = x−2`
(no bounce, since `x ≥ 2`), and a `c = 0` step maps `x ↦ x`. So the value
descends by **exactly 2** per `c=2` step until it reaches `{0,2}`, and is
unchanged by `c=0` steps. To reach `≤ 2` from even `v` requires `⌈(v−2)/2⌉`
descents, i.e. `(v−2)/2` of them since `v` is even. There are exactly `ν₂`
such steps available. Hence enough descents exist (⟺ `ν₂ ≥ (v−2)/2` ⟺
`v ≤ 2ν₂+2`) iff the trajectory reaches `{0,2}`. If `v > 2ν₂+2`, then even
after all `ν₂` descents `v − 2ν₂ ≥ 4`, so the value never falls to `{0,2}` and
the final value is exactly `v − 2ν₂` (monotone non-increasing, all steps
`≥ 4`). For absorption: `|0−c| ∈ {0,2}` and `|2−c| ∈ {0,2}` for `c ∈ {0,2}`. ∎

### Application (Granville's right-diagonal coordinates)

In the iterated-absolute-difference triangle, an extension column `q_1..q_n` is
a one-step diagonal. Let `ε_k ∈ {0,2}` (the `{0,2}` cycle of the previous
diagonal's tail) and `δ_k` the new diagonal; `δ_{k+1} = |δ_k − ε_k|`. The lemma
governs exactly this recursion with `v_n` the entry where the previous
diagonal's maximal `{0,2}` suffix begins. The descent budget `2·ν₂ + 2` is
precisely this run's recharge identity `Σ(j_i+1) ≥ k−2` in right-diagonal
coordinates. **The δ=0 case that Granville's published proof discards as an
"exception" (and which occurs in 100% of real columns) is exactly the
absorption case (3) — and it is now proved, not waved away.**

### Validation (machine, non-vacuous)

- **Exhaustive descent sweep** (`code/lemma54_descent_check.py`): all `{0,2}^L`
  patterns, `L = 1..16`, all even `v` in `[0, 2L+8]` — 131,070 patterns /
  2,621,432 pairs, **0 violations** of (1)(2)(3), sharpness holds.
- **Failing-side validation** (`code/gap_analysis/lemma54_failing_sisters.py`),
  which the prior check could not do (every real prime column succeeds, so the
  biconditional was only confirmed with both sides true). Built 2-then-odd
  synthetic failing sequences (5 gap families including Poisson-gap style),
  cross-checked 8,188,000 triangle cells with **0 mismatches**: among 38,219
  eligible columns (successful prefix `q_1..q_{n-1}` — the lemma's hypothesis),
  30 have genuinely failing extensions; the biconditional
  `v_n ≤ 2ν₂+2 ⟺ success` has **0 violations**; the contrapositive
  (`fails ⟹ g* > budget`) has **0 columns fail under budget**; and
  `A_{n-1}[1] ∈ {0,2} ⟺ A_n[0]=1` (the reduction iff) has 0 disagreements.

**Framing caveat (recorded):** Lemma 5.4 is a *one-step* budget that keeps an
already-Gilbreath sequence Gilbreath; it governs only extensions of successful
prefixes. ~1652 apparent violations in a first test run were columns whose
prefix had *already failed* — outside the lemma's scope, not counterexamples.
Any citation must carry the prefix-successful hypothesis.

## What this reduces the conjecture to

The whole of route B now rests on a single open density statement:

> **G-supply.** There exists `β > 0.525` with `ν₂(q_n) > n^β` for all large `n`,
> where `ν₂(q_n)` = number of 2s in the maximal `{0,2}` suffix of the
> right-diagonal of column `n`.

- The **demand side** `g\*_n < n^{0.525+ε}` is discharged unconditionally by
  Baker–Harman–Pintz (`bhp-max-gap-unconditional`, `bhp-demand-corollary-g-star`).
- The **supply side** is measured at `ν₂/n ∈ [0.420, 0.520]` over
  `n = 50..3999` (26× above the needed `n^0.525`), and reduces cleanly to a
  **prime-gap-mod-4 density statement**: the `{0,2}` tail cells' row-1 ancestor
  union is the fixed interval `[2, n−1]` of `A_1`, halved bits are 1 iff
  `gap ≡ 2 (mod 4)`, with `ν₂ ≥ w/2` holding on every sample — so G-supply is a
  claim about how often `p_{n+1}−p_n ≡ 2 (mod 4)` occurs, not about the
  absolute-difference dynamics. (**Numerical only** at 8 samples; not a proof.)

## Honest status

- **Proved:** the descent/absorption lemma (general theorem, hand proof); the
  reduction `GC ⟺ second entry ∈ {0,2}` (Lean, sorry-free, prior run);
  block lemma constant 1; step law + recharge identity; Rule 90 interior;
  edge-map invertibility.
- **Validated non-vacuously (both directions):** Lemma 5.4's full statement on
  synthetic failing sequences.
- **Open, the entire remaining content:** the ν₂ density lower bound (G-supply),
  equivalently a prime-gap-mod-4 frequency bound. This is exactly the
  regeneration-rate question, reformulated in diagonal coordinates — not a new
  theorem to build but the same open quantity.

## Files

- `code/gap_analysis/lemma54_failing_sisters.py` + `code/out/lemma54_failing_sisters.captured.txt`
- `code/gap_analysis/nu2_vs_gap_parity.py` + `code/out/nu2_vs_gap_parity.captured.txt`
- `code/lemma54_descent_check.py` + `code/out/lemma54_descent_check.captured.txt` (pre-existing, re-verified)
- `research/notes/lemma54-re-derived.md` (scholar analysis), `research/notes/lemma54-discarded-case-is-universal.md`
