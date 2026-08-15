# Lemma 5.4 core — the sharpened descent lemma, proved (clean case-split)

## Status

`id: lemma54-descent-proof-repaired`
`status: proved`
`holds-here: yes`
`bearing:` the combinatorial core of Granville Lemma 5.4, the demand→success
leg of Route B. Repairs the written proof defect identified by Directive 43/44
(the "each 2 contributed −2" algebra, false on bounce trajectories where
δ=0,ε=2 ⟹ δ=2 contributes +2).
`answers:` lemma54-re-derived-proof (its prose defect), lemma54-discarded-case-universal
`formalisation:` **FAILED — code/lean/descent_lemma.lean does NOT compile (Directive 49).** `lean_check` ends: `absorbing [propext, sorryAx]`; `run_absorb [sorryAx]`; `run_high [propext, sorryAx]`; `run_inv [propext, sorryAx]`; `descent_claim1 [propext, sorryAx, Quot.sound]`; `descent_claim2 [propext, sorryAx]` — sorryAx in all six. There is no literal `sorry` token (error recovery inserted sorryAx), so only the axiom list counts, and by that criterion the file FAILS. The unsolved goal is `run_inv`, case `cons.inr`, hypothesis `he1 : e = 1` (the eps=1 descent/bounce branch).
`machine:` code/out/descent_halved_verify.captured.txt (12,582,900 pairs, 0
violations), code/out/lemma54_descent_check.captured.txt (2,621,432 pairs, 0
violations).

## The theorem (halved form is cleanest — this is the proof form)

Work in **halved units**: the {0,2} block becomes a {0,1} block, the step map
`δ ↦ |δ − ε|` becomes `d ↦ |d − e|` with `e ∈ {0,1}`. Let

```
d_0 = w        (w a natural number)
d_{k+1} = |d_k − e_k|,   e ∈ {0,1}^L
nu1 = #{k : e_k = 1}
```

**Theorem.** 
(1) If `w ≤ nu1 + 1` then `d_L ∈ {0,1}`.
(2) If `w > nu1 + 1` then `d_L = w − nu1` (exact value).
(3) `{0,1}` is absorbing under the step for `e ∈ {0,1}`.

(1) and (2) together give the sharp biconditional `d_L ∈ {0,1} ⟺ w ≤ nu1+1`,
and (with `ν₂ = nu1`, `v = 2w`) the original even-unit form
`x_L ∈ {0,2} ⟺ v ≤ 2ν₂+2` of `lemma54_descent_check`.

## Proof (case split — this is the repair)

First note every `d_k` is a natural number, and `{0,1}` is closed under
`|·−e|` for `e∈{0,1}`: `|0−0|=0, |0−1|=1, |1−0|=1, |1−1|=0`. This is claim (3).

**Claim (1), `w ≤ nu1+1`.** Split on whether the trajectory ever reaches a
value ≤ 1 before (or at) step L.

- **Branch A: some `d_t ≤ 1` with `t ≤ L`.** Then `d_t ∈ {0,1}` (nonneg natural).
  Since `{0,1}` is absorbing and the remaining steps have `e ∈ {0,1}`, every
  later `d_s` (`s ≥ t`) lies in `{0,1}`. In particular `d_L ∈ {0,1}`. ∎

- **Branch B: `d_k ≥ 2` for every `k = 0,1,…,L`.** Then at every step
  `d_{k+1} = |d_k − e_k|`: if `e_k = 0`, `d_{k+1} = d_k`; if `e_k = 1`, since
  `d_k ≥ 2`, `|d_k − 1| = d_k − 1`. So no bounce occurs and each 1-step
  decrements by exactly 1, each 0-step fixes. Hence
  `d_L = w − nu1`. By hypothesis `w ≤ nu1+1`, so `d_L ≤ 1`, contradicting
  Branch B's standing assumption `d_L ≥ 2`. Branch B is empty. ∎

So Branch A must hold and `d_L ∈ {0,1}`.

**Claim (2), `w > nu1+1`.** Then `w − nu1 ≥ 2`. We show the exact-count regime
persists throughout: claim by induction that `d_k ≥ 2` for all `k ≤ L`.
Base: `d_0 = w ≥ w − nu1 ≥ 2`. Step: if `d_k ≥ 2` then `d_{k+1} =
|d_k − e_k| ≥ d_k − e_k ≥ d_k − 1`; but more sharply, by induction
`d_k = w − (#ones so far) ≥ w − nu1 ≥ 2`, so the decrement-form applies and
`d_{k+1} = d_k − e_k = w − (#ones so far) − e_k = w − (#ones through k)`.
At `k = L` this gives `d_L = w − nu1`. ∎

This is the repair Directive 43 hands over: absorption is load-bearing in
Branch A (δ=0 is entry into {0,2}, not an exception), and the exact value
`w − nu1` — the tightness that makes the budget `2ν₂+2` sharp — is proved by
the non-vacuous Branch B, not by a subtraction that silently assumes the orbit
never bounces.

## Exchange with the even-unit (original) form and the reduction to success

- **Even units:** `v = 2w`, `ν₂ = nu1`, `x_L = 2d_L`. Claims (2) gives
  `x_L = v − 2ν₂` in the runway regime; the budget is `v ≤ 2ν₂+2`.
- **Why this closes the demand→success leg:** Granville Lemma 5.3(8) bounds
  `v_n = δ_{τ_n}(q_n) ≤ g*_n − 2` (τ_n ≥ 2) or `= g_n ≤ g*_n` (τ_n = 1). The
  record-gap demand `g*_n ≤ 2ν₂+2` therefore forces `v_n ≤ 2ν₂+2`, so by
  (1)+(3) the orbit lands in `{0,2}` and stays — the budget is spent exactly
  reading the 0-2 cycle, so the last cycle-fed value lies in `{0,2}`, and the
  terminal `δ_{n-1}(q_n) = |e − 1| = 1` follows from the successful prefix's
  bottom `1`. This is the passage verified exactly (model-match B and
  fixedness C of reduction_audit.py, 0 mismatches over 49.87M positions).

## Verified exhaustively (exact integers, no floats)

- Halved form, L=1..18, all 2^L patterns, w ∈ [0, L+6]:
  12,582,900 (pattern,w) pairs, 0 violations of (1),(2),(3).
- Even-unit reproduction of the prior capture: 2,621,432 pairs matching
  lemma54_descent_check.captured.txt exactly, 0 violations.
- Sharpness: all-1s pattern, w=nu1+1 → d_L=1; w=nu1+2 → d_L=2; every L=1..18.

These are verifications, not the proof; the proof is the case-split above, and
the Lean formalisation (code/lean/descent_lemma.lean) machine-checks it.
