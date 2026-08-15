# Suffix-fold Pascal linear operator — the corrected linearization of ν₂

```approach
idea: |
  ν₂(q_n) = wt(Φ_n h) EXACTLY, where Φ_n is the explicit anti-diagonal
  Pascal-mod-2 (Rule-90) matrix folding the halved-gap bit string h over the
  SUFFIX window [n−k, n−1] — NOT the prefix subset-zeta / Möbius transform
  ζ(h)[d] = Σ_{j⊆d} h[j] over the prefix window [0, d]. The two have been
  conflated in this run, and that conflation is what made "fold parity ≠ ν₂"
  look like a fatal flaw. The supply question ν₂ ≥ c·n is the image-weight
  classification of the concrete matrix family {Φ_n} over F₂.
mechanism: |
  (1) [held, proved] rule90-interior-xor: within a {0,2} block the halved
      entries evolve by XOR, and for gap ∈ {2,4} words the whole halved
      triangle is {0,1}-valued (|a−b| of {0,1} values is {0,1}), so XOR is
      EXACT — the halved value of every cell equals its fold bit. No "parity
      vs membership" gap exists for these words.
  (2) [held, machine-verified] The right-diagonal tail cell at depth k is the
      SUFFIX fold Σ_{i⊆k−1} h[n−k+i] (window [n−k, n−1], Pascal-row-(k−1)
      coefficients) — see code/lib/rule90fold.py `fold_cell_bit`. This is the
      concrete matrix Φ_n: rows k=2..n−1, columns j=2..n−1, entry
      C(k−1, j−(n−k)) mod 2. ν₂ = wt(Φ_n h) holds with 0 violations over
      8,001,999 real-prime cells and every sampled/dense n
      (code/out/linearization_verify.captured.txt).
  (3) [NEW, load-bearing] The PREFIX subset-zeta ζ(h)[d] = Σ_{j⊆d} h[j] is a
      DIFFERENT operator (the BCZ left-edge involution, and the object the
      Möbius/Christol literature names). It is NOT the right-diagonal fold.
      The run's Thue–Morse "correction" (thue-morse-sublinear-supply-witness)
      computed the PREFIX fold (7 ones ≤ 100) and compared it to the true
      right-diagonal ν₂ (27 @ n=100) — the mismatch is a WINDOW error, not a
      "parity vs membership" error. In suffix form the identification
      ν₂ = wt(Φ_n h) is exact (proved + verified).
  (4) [held] The collapse theorem (dyadic-collapse-proved) is the nilpotent
      component σ^{2^k}=0 of the suffix fold σ = I+S on cyclic period-2^k
      words. The anti-dyadic converse is refuted (spad-nondegenerate-linear-
      refuted, half-step witness, on the suffix fold). So the classification
      boundary is: 2^k-periodic and Thue–Morse are rigid (wt(Φ_n h) = o(n)),
      odd-factor periodic and the primes are non-rigid (positive density).
status: adopted
side: regeneration (supply side) — general-class / linear-algebra reformulation
named-mathematics: |
  Rule 90 / Pascal mod 2, Lucas' theorem, the F₂ linear operator σ = I+S on
  cyclic groups, anti-diagonal Pascal matrices, code/image weight of an
  explicit F₂ matrix family.
speculative: |
  The open content is unchanged and is NOT closed by this reformulation: a
  positive-density lower bound wt(Φ_n h) ≥ c·n for the PRIME switch bit
  reverts to the named-open two-point mod-4 correlation
  (abgs-2011-s9-mod4-switch-limit-open). What this approach changes is the
  OBJECT: it pins the question to the concrete suffix-fold matrix family {Φ_n}
  and corrects a window error that made the fold look like the wrong object.
falsifier: |
  (a) A gap-{2,4} word h for which the suffix fold weight differs from the
      true right-diagonal ν₂ — would break the exact identification. The
      one-shot check is code/out/resolve_fold_vs_nu2.py.
  (b) An input h with wt(Φ_n h) = Ω(n) whose true ν₂ is o(n) — would break
      the suffix-fold linearization for the supply direction.
first-step: |
  [tool_builder, today] Run code/out/resolve_fold_vs_nu2.py (already written;
  capture to code/out/resolve_fold_vs_nu2.captured.txt) and confirm on one
  code path: suffix fold == halved right diagonal == ν₂ for Thue–Morse and
  P=3, while prefix fold ≠ ν₂ (TM: prefix 7 vs suffix/true 27 @ n=100).
  Then materialise Φ_n explicitly and re-verify ν₂ == wt(Φ_n h) across the
  four families (period 2^k, P=3, Thue–Morse, real prime switch bit).
  This repairs the two contradictory claim rows
  (thue-morse-sublinear-supply-witness uses the prefix fold;
  linearization_verify uses the suffix fold) under one documented convention.
```

## Established vs speculation

- **Established (held claims I read, all machine-anchored):**
  - `rule90-interior-xor` + {0,1} closure ⟹ suffix fold computes the halved
    value exactly for gap-{2,4} words.
  - `linearization_verify.captured.txt`: ν₂ == wt(Φ_n h) with 0 violations on
    8,001,999 real-prime cells, all sparse samples {50..3999} and all dense
    n∈[50,3000].
  - `dyadic-collapse-proved`: period 2^k ⟹ wt(Φ_n h) = O_k(1) (suffix fold).
  - `spad-nondegenerate-linear-refuted`: anti-dyadic does NOT force linear
    supply (half-step witness on the suffix fold, `fold_weight_h`).
  - `thue-morse-sublinear-supply-witness` (read in full): the PREFIX fold
    ζ(h)[d]=Σ_{j⊆d}h[j] gives 7 ones ≤ 100, while measured true ν₂ = 27.
- **Speculation (unchanged open content):** a positive-density lower bound for
  the prime switch bit. This approach does not claim it; it corrects the
  object on which the question is asked.

## Scholze gate (must reproduce a held claim)

The suffix fold reproduces both poles natively:
- `dyadic-collapse-proved`: σ^{2^k}=0 on period-2^k cyclic words ⟹ wt(Φ_n h)
  ≤ 2^k−1 — the nilpotent component of the suffix fold.
- `dyadic-oddfactor-infimum-bounded`: odd-factor periodic words give positive
  density — the non-nilpotent component.

## Window correction (the new content, stated once)

The run holds two contradictory identification claims:
- `linearization_verify` (suffix fold): ν₂ == wt(Φ_n h), 0 violations.
- `thue-morse-sublinear-supply-witness` (prefix fold): fold parity ≠ ν₂,
  TM 7 vs 27.

Both are right about what they computed; the contradiction is a WINDOW error.
The right-diagonal geometry folds over the SUFFIX (rule90fold.py:
`fold_cell_bit` uses `hcol[n−k+i]`; `fold_weight_h` uses `h[m−k+i]`). The
prefix subset-zeta is the BCZ left-edge object, not the right-diagonal supply
object. The Thue–Morse note's "parity vs membership" diagnosis of the mismatch
is wrong for gap-{2,4} words (their halved triangle is exactly {0,1}, so
parity = value); the correct diagnosis is prefix-vs-suffix window. The
qualitative conclusion (Thue–Morse true ν₂ is sublinear, measured 0.27→0.011
density over n=100..4000) survives as measurement, but the "proved O(log n)"
claim is dead — it was proved for the wrong operator.
