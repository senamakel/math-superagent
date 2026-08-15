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
stays even under `|x−c|`). Split on whether the trajectory ever reaches `{0,2}`:

- **Branch A (absorption):** if some `x_t ≤ 2` (t ≤ L), then `x_t ∈ {0,2}`
  (even, non-negative), and `{0,2}` is absorbing: `|0−c| ∈ {0,2}` and
  `|2−c| ∈ {0,2}` for `c ∈ {0,2}`. Hence `x_L ∈ {0,2}`. This is the δ=0 case
  Granville's published proof discards as an "exception" — here it is the
  mechanism, not an exception. It supplies the (←) direction and the
  absorption claim (3).
- **Branch B (descent):** otherwise `x_s ≥ 4` for every `s`. Then no bounce
  occurs: `c=2` maps `x ↦ |x−2| = x−2` (since `x ≥ 2`) and `c=0` fixes `x`,
  so `x_L = v − 2ν₂` exactly (monotone). If `v ≤ 2ν₂+2`, then `x_L ≤ 2`,
  contradicting the standing `x_L ≥ 4`; so under the hypothesis the descent
  regime cannot persist, and Branch A must hold — giving the (→) direction.
  If `v > 2ν₂+2`, then `v − 2ν₂ ≥ 4`, so Branch B persists throughout and
  `x_L = v − 2ν₂ ≥ 4` (the runway / tightness direction). This is the repair:
  the old algebra "after the ν₂ twos, δ = v − 2ν₂" is false on bounce
  trajectories (e.g. `v=0, ε=(2,2,2)` gives `0→2→0→2` while `v−2ν₂=−6`); the
  case split never applies the subtraction outside Branch B. ∎

The halved form (cleanest for proof and formalisation): `e ∈ {0,1}^L`, trajectory
`d_0=w`, `d_{k+1}=|d_k−e_k|`, `ν₁=#{1s}`. Claims: `w≤ν₁+1 ⟹ d_L∈{0,1}`,
`w>ν₁+1 ⟹ d_L=w−ν₁` exactly, `{0,1}` absorbing. The proof's engine is the
unconditional invariant: every value is either `w−(#ones so far)` or in
`{0,1}`. **Lean-formalised sorry-free** at `code/lean/descent_lemma.lean`
(compiled=true, verified=true, zero sorryAx; `#print axioms` = only
propext/Classical.choice/Quot.sound). Exhaustively machine-checked in halved
units (12,582,900 `(pattern,w)` pairs, L≤18, 0 violations) and unhalved
(11,534,328 pairs, L≤18, 0 violations); the even-unit reproduction matches the
prior capture pair-for-pair.

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

- **Proved + Lean-formalised (this attempt):** the sharpened descent/absorption
  lemma (general theorem, case-split proof in halved units) — sorry-free in
  `code/lean/descent_lemma.lean`, exhaustively verified (12.58M halved pairs
  + 11.53M unhalved pairs, 0 violations). This repairs the written-proof defect
  of Directive 43/44: the δ=0 case is absorption (Branch A), not an exception,
  and the tight exact value `w−ν₁` is proved (Branch B), not assumed.
- **Proved (prior runs):** the reduction `GC ⟺ second entry ∈ {0,2}` (Lean,
  sorry-free); block lemma constant 1; step law + recharge identity; Rule 90
  interior; edge-map invertibility.
- **Validated non-vacuously (both directions):** Lemma 5.4's full statement on
  synthetic failing sequences (30 genuinely failing columns).
- **The passage from real column dynamics to the (pattern,v) model is EXACT**
  (a theorem): the pattern is read off the prefix-determined previous diagonal,
  independent of the new column's values — reduction_audit Part 1 (45150 cells)
  and model-match (49.87M positions) all 0 violations.
- **Open, the entire remaining content:** the ν₂ density lower bound (G-supply
  `ν₂ > n^β`, β>0.525, equivalently ν₂ ≥ c·n), a prime-gap-mod-4 frequency
  bound that is a NAMED OPEN problem in analytic number theory (no
  unconditional linear lower bound on the mod-4 switch count exists). Route B
  is therefore a conditional theorem with a precisely identified open
  hypothesis — not a proof of Gilbreath.

## Files

- `code/gap_analysis/descent_halved_verify.py` + `code/out/descent_halved_verify.captured.txt` (new, this attempt)
- `code/gap_analysis/descent_absorption_case_split.py` + `code/out/descent_absorption_case_split.captured.txt`
- `code/gap_analysis/reduction_audit_d_investigate.py` + `code/out/reduction_audit_d_investigate.captured.txt` + `code/out/reduction_audit_d_notes.md` (the 1133 diagonal-cycle drops are a transversality artifact, not a counterexample)
- `code/lean/descent_lemma.lean` (Lean 4 formalisation, sorry-free, `#print axioms` reported)
- `research/notes/lemma54-descent-proof-repaired.md` (the case-split proof, this attempt)
- `code/gap_analysis/lemma54_failing_sisters.py` + `code/out/lemma54_failing_sisters.captured.txt`
- `code/gap_analysis/nu2_vs_gap_parity.py` + `code/out/nu2_vs_gap_parity.captured.txt`
- `code/lemma54_descent_check.py` + `code/out/lemma54_descent_check.captured.txt` (pre-existing, re-verified)
- `research/notes/lemma54-re-derived.md` (scholar analysis), `research/notes/lemma54-discarded-case-is-universal.md`
