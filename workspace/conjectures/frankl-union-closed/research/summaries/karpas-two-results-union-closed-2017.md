# Eyal Karpas, "Two Results on Union-Closed Families" (arXiv:1708.01434, 2017)

Full text (read): [[karpas-two-results-union-closed-2017.full]] · Source: https://arxiv.org/html/1708.01434v1

## What it establishes (primary source, statements read)

**Theorem 1.2 (large families).** If `ℱ ⊆ 2^[n]` is union-closed and
`|ℱ| ≥ 2^{n−1}`, then some element `i` is abundant: `|ℱ_i| ≥ |ℱ|/2`.

This is the sharpest "large-family" line. The history it records (all
union-closed `ℱ ⊆ 2^[n]`):
- Czédli: `|ℱ| ≥ 2^n − 2^(n/2)` ⇒ UC
- Balla–Bollobás–Eccles: `|ℱ| ≥ (2/3)·2^n` ⇒ UC  (note: in terms of `2^n`, not
  the `2^((3/2)n)` parameterisation that appears in ROOT.md — same family of
  results, different variable)
- Eccles: `|ℱ| ≥ (2/3 − 1/104)·2^n` ⇒ UC
- **Karpas (Theorem 1.2): `|ℱ| ≥ (1/2)·2^n = 2^{n−1}` ⇒ UC** — the best of the
  line. Proof uses Boolean analysis (no prior Boolean-analysis proof of UC).

**Theorem 1.3 (upper shadow).** For any union-closed `ℱ ⊆ 2^[n]`,
`|∂⁺ℱ ∖ ℱ| ≤ 2^{n−1}`, where `∂⁺` is the upper shadow
(`A ∪ {i} : i ∉ A`). Tight via `ℱ = {A ⊆ [n] : 1 ∉ A}`.

**Theorem 1.4.** If `|ℱ| ≥ (1/2 − c)·2^n` for an absolute constant `c > 0`,
then some element is abundant. (Theorems 1.2–1.4; there is also a
"simply-rooted implies rare element" theorem in §3 and an
`I⁺(f) ≤ 1` positive-influence bound for simply-rooted Boolean functions.)

## Why it matters for this run

- Corrects/refines the "large families" row in ROOT.md: the current best is
  Karpas's `|ℱ| ≥ 2^{n−1}`, improving BBE (`(2/3)2^n`) and Eccles
  (`(2/3 − 1/104)2^n`). Any structural argument about a minimal counterexample
  may assume `|ℱ| < 2^{n−1}` (i.e. it is a "small" family).
- The upper-shadow bound `|∂⁺ℱ∖ℱ| ≤ 2^{n−1}` is a clean combinatorial
  constraint a minimal counterexample must satisfy, independent of the entropy
  method.

```claim
id: karpas-large-families
statement: If F subseteq 2^[n] is union-closed with |F| >= 2^(n-1), then some
  element i is abundant (|F_i| >= |F|/2).
hypotheses: F union-closed subseteq 2^[n], |F| >= 2^(n-1)
holds-here: yes
status: proved (Theorem 1.2, Boolean-analysis proof)
bearing: a minimal counterexample must satisfy |F| < 2^(n-1); the sharpest
  large-family threshold
anchor: research/sources/karpas-two-results-union-closed-2017.full.md (Thm 1.2-1.4)
contradicts: none; refines ROOT.md's BBE-only (2/3)2^n row
```

```claim
id: karpas-upper-shadow
statement: For any union-closed F subseteq 2^[n], |upper-shadow(F) \ F| <= 2^(n-1),
  tight via F = {A : 1 notin A}.
hypotheses: F union-closed subseteq 2^[n]
holds-here: yes
status: proved (Theorem 1.3)
bearing: structural constraint on any union-closed family incl. minimal
  counterexample
anchor: research/sources/karpas-two-results-union-closed-2017.full.md (Thm 1.3)
```

## Status
Statements read and confirmed in the full body. Not numerically re-checked here
(the oracle covers n ≤ 4 only, where `2^{n−1} ≤ 8` families are too small to be
informative). Karpas Theorem 1.2 improves BBE/Eccles; the ROOT.md "large
families |F| ≥ 2^((3/2)n)" citation is the BBE parameterisation and should read
as superseded by Karpas's `2^(n−1)`.
