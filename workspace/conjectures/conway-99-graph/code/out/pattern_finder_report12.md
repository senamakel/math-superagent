# Pattern-finder report — round 12: tight-coclique family identity d_C = −s (unifies the 99 coclique-design force)

## What changed since round 11

Round 11 catalogued every family count. One 99-specific quantity was on disk
but never restated as a family sequence: the tight-coclique force `d_C=4` at 99
(`code/out/coclique_design.captured.txt`, claim
`coclique-alpha22-forces-22242-design`). This round restates it family-wide and
proves the closed form symbolically.

## Finding — the tight-coclique design identities are a family theorem (PROVEN, not a fit)

For `srg(v,k,1,2)` with `k=u²+u+2`, `v=1+k²/2`, negative eigenvalue `s=−(u+1)`,
Hoffman size `α=(u·k+2)/2` (report 3 closed form): **if a coclique C meets the
Hoffman bound**, equality in the ratio bound forces

```
d_C := α·(k−s)/v  =  u+1  =  −s          (every outside vertex's degree into C)
```

and the outside-restricted neighbourhood blocks form a
`2-(α, u+1, 2)` design with

```
replication r = 2(α−1)/(d_C−1) = k   exactly
block count   b = v−α = (u²+2)(u²+u+2)/2
```

**Symbolic proof** (`pf_tight_coclique_identity_sympy.py`): `d_C−(−s) ≡ 0`,
`r−k ≡ 0`, `b−(u²+2)(u²+u+2)/2 ≡ 0` as polynomial identities in `u` (sympy,
exact); and exact over all five feasible members (`pf_tight_coclique_identity.py`):

| u | k | v | s | α | d_C | −s | r | b |
|---|---|---|---|---|---|---|---|---|
| 1 | 4 | 9 | −2 | 3 | 2 | 2 | 4 | 6 |
| 3 | 14 | 99 | −4 | 22 | 4 | 4 | 14 | 77 |
| 4 | 22 | 243 | −5 | 45 | 5 | 5 | 22 | 198 |
| 10 | 112 | 6273 | −11 | 561 | 11 | 11 | 112 | 5712 |
| 31 | 994 | 494019 | −32 | 15408 | 32 | 32 | 994 | 478611 |

At 99 this is the **2-(22,4,2)** design `b=77, r=14, d_C=4` of claim
`coclique-alpha22-forces-22242-design` — now seen as the `u=3` slice of a
one-line family law rather than ad-hoc arithmetic.

## Sequence-tool results (exact over the terms)

- `d_C` family `[2,4,5,11,32]`: not a low-order recurrence, not low-degree
  poly — it is the linear `u+1` in the `.`-*index* `u∈{1,3,4,10,31}` (sparse
  index set), so it is governed by the `a|63` index arithmetic, not an
  independent law.
- `b` family `[6,77,198,5712,478611]`: no order-≤4 constant-coefficient
  recurrence (checked); quartic-growth closed form `(u²+2)(u²+u+2)/2`.

## Status: a DERIVATION, not a conjecture, and NOT a 99 separator

- The equality-force `d_C = −s` and `r = k` are **symbolically proven** from
  the standard Hoffman/regularity identities — they cannot be falsified by any
  member of the family; there is no first-falsifying term (it inherits from the
  SRG definition). The only hypothesis is *existence of a Hoffman-bound coclique*,
  which is the open question itself.
- It **does not separate 99**: both controls satisfy it (rook `2-(3,2,2)` with
  `d_C=2, r=4`; BvLS `2-(45,5,2)` with `d_C=5, r=22`), as report 11's
  `coclique-design-dead-end` already showed. It is a hard-target/consistency
  identity: any existing or constructed graph must satisfy it, and the 2-(22,4,2)
  design at 99 is arithmetically feasible (symmetric-form BRC inapplicable
  since b≠v; the Gram/det sum-of-squares condition is trivially satisfied).
- Value for the run: it unifies the 99 coclique-design claim into a family
  theorem, confirming the arithmetic obstacle closing that line is structural
  (holds for every member), not a 99-specific accident — consistent with the
  standing conclusion that every parameter-determined family count is
  `a|63`-governed and none separates 99.

## Recommendation

The sequence line remains exhausted (rounds 1–12): every parameter-determined
count is the same `u³/u⁴`-quartic family governed by `a=2u+1|63`, and the only
non-parametric count (n3-seed radius trajectory) is an enumeration with no
algebraic law. The lever the numbers keep pointing at is unchanged: the **22
coclique bound** (report 3) and the **forced n3≥3** (report 6) — both
99-specific values — and the live sub-question is whether any *feasible*
2-(22,4,2) design lifts to a graph (a finite construction/exclusion question,
per `lou-murin-alpha22-block-design-reduction`), which sequence tools cannot
settle. This round adds no new 99-separating ceiling; it hardens the coclique
design force into a family law.

## Files

- `code/out/pf_tight_coclique_identity.py` — 5-member exact check.
- `code/out/pf_tight_coclique_identity_sympy.py` — symbolic proof.
- `code/out/coclique_design.captured.txt` — the 99/control values (source data).
- This report.
