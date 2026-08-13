# Gatti 2020 Cor 1 K_S claim — machine-checked on S = {2,3,5}

**Claim being checked.** Gatti 2020, *Gilbreath's Sequences and Proof of
Conditions for Gilbreath's Conjecture* (Preprints 202003.0145.v1), Cor 1 of
Lemma 4 asserts the valid-extension set of a Gilbreath sequence S ∈ G_n has
`dim K_S = 2^{n−1}`, and Lemma 4 asserts K_S fills the whole parity class in
`]min K, max K[` (interval completeness).

**Result.** For S = (2, 3, 5) ∈ G_3:

- `K_S = {1, 3, 5, 7, 9}`, so `|K_S| = 5 ≠ 4 = 2^{3−1}` — the **dimension
  prediction is false** (and with it the counting identity behind Gatti's
  induction).
- Interval completeness happens to hold for this S: K_S is exactly the odd
  interval [1, 9] = ]min K, max K[ ∩ (odd). The interval-completeness failure
  *in general* is Muney 2026's length-5 exhibit (2,3,5,9,15) — a separate,
  sourced exhibit. Keep the two refutation exhibits distinct: dimension fails
  already at length 3; completeness fails at length 5.
- Gatti's Eq. 2 signed-sum formula `k = ±s^{n−1}_1 ± s^{n−2}_2 ± … ± s^1_{n−1}
  + s_n ± 1` is itself confirmed on this example: `±1 ± 2 + 5 ± 1` (8 sign
  combinations × 2 tails) gives exactly {1,3,5,7,9}, agreeing with the
  definition. The formula is the sound part of the paper, independently held
  from Alkan 2023 / Muney 2026 (`gatti-2020-valid-extension-global-formula`).

**Method (three independent routes, all exact integer arithmetic).**

1. `verify_gatti_kset.py` — K_S by the left-edge definition via a
   triangle-descent helper (`row1_of_extended`), and by Eq. 2's signed-sum.
2. `verify_gatti_kset_independent.py` — deliberately different code:
   (a) direct nested-absolute evaluation `abs(1 - abs(2 - abs(5 - k))) == 1`
   over k ∈ [−200, 200]; (b) full-triangle left-edge semantics — (2,3,5,k) is
   Gilbreath iff *every* row of its difference triangle starts with 1;
   (c) Eq. 2 formula built from the anti-diagonal (s²₁ = 1, s¹₂ = 2).
3. Hand check of the five candidates against `|1−|2−|5−k||| = 1` (each
   resolves to `|1−2| = 1` or `|1−0| = 1`).

All three routes agree: K_S = {1,3,5,7,9} in every computation.

**What this settles.** The claim `gatti-2020-lemma4-interval-completeness-refuted`
now carries a machine-checked exhibit (its S={2,3,5} half was previously
hand-verified only, with the coder script marked queued). The consequence for
the run stands: no interval-completeness or `2^{n−1}`-counting property of
valid-extension sets may be assumed anywhere downstream; valid extension is
global and hole-prone (`valid-extension-nonlocal`, Muney 2026).

**Bounds.** |K| computed over k ∈ [−40,40] (route 1) and k ∈ [−200,200]
(routes 2a, 2b); both find exactly the five values 1,3,5,7,9. Since the
nested absolute is piecewise linear with slope ±1 and the two branches
(|5−k| = 4 or 2 at the solutions) cover k near 5, all solutions lie in
[1,9] ⊂ [−200,200]; the range bound is therefore not a truncation artifact.
Complexity O(range × n²), n = 3.

**Anchor outputs.** `code/out/gatti_kset_check.captured.txt`,
`code/out/gatti_kset_independent.captured.txt`; programs
`code/research_mod_check/verify_gatti_kset.py`,
`code/research_mod_check/verify_gatti_kset_independent.py`.