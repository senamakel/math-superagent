# Eccles, "A stability result for the union-closed size problem" — html copy

**Source URL:** https://arxiv.org/html/1311.2298 (arXiv:1311.2298v1, 10 Nov 2013)
**Full body:** `research/sources/eccles-stability-result-2015-html.full.md` (680 lines)

This is the full-body HTML download. **The canonical digest is
`research/summaries/eccles-stability-result-2015.md`** — read that one; this file
exists only to carry the source pointer so the auto-generated placeholder is not
mistaken for content. It is a duplicate of the ar5iv copy
(`eccles-stability-result-2015-ar5iv.md` / `.full.md`); both hold the same paper.

## What it establishes (verified against this body)

- **Theorem 1.1** (union-closed size problem, settled by Balla–Bollobás–Eccles):
  for `2^{n−1} < m ≤ 2^n`, `f(m) = ‖P(n)‖ − ‖I(m′)‖ − m′` with `m′ = 2^n − m`.
  Extremal complement `P(n)\𝒜 = {B∪{n}: B∈I(m′)}`. In particular if 𝒜 is a
  counterexample with `|𝒜|=m` then `f(m) < nm/2`, i.e. `‖I(m′)‖ + m′ > nm′/2`.
- **Corollary 1.2:** UC holds for `|𝒜| ≥ (2/3)2^n` (from averaging alone; the
  `2/3` barrier — for `m < (2/3)2^n`, `f(m) < nm/2`).
- **Theorem 1.3:** ∃c₁>0: a counterexample 𝒜 with `ℬ=P(n)\𝒜`, `|ℬ|=m` has
  `‖I(m)‖ > m(n/2 − 1 + c₁)`.
- **Corollary 1.4:** UC holds for `|𝒜| ≥ 2^{n(2/3−c₂)}`, with **c₁ ≥ 1/24,
  c₂ ≥ 1/104** (§6 refines both).
- Method: up/down-compressions, simply rooted families (complement of a
  union-closed family is simply rooted, Obs 2.1); Theorem 3.1 is the stability
  result for "‖𝒜‖ near-maximal ⇒ P(n)\𝒜 has an element of high degree".

## Claim

```claim
id: eccles-stability
answers: (corrected) eccles-stability
statement: Stability result for the union-closed size problem: near-extremal
  union-closed families (max total size) cluster around the explicit extremal
  form P(n)\𝒜={B∪{n}: B∈I(m′)} (one complement-universal element), far from any
  UC counterexample. Consequences: (Cor 1.2) UC for |𝒜| ≥ (2/3)2^n;
  (Thm 1.3) a counterexample 𝒜 with ℬ=P(n)\𝒜, |ℬ|=m has ‖I(m)‖>m(n/2−1+c₁);
  (Cor 1.4) UC for |𝒜| ≥ 2^{n(2/3−c₂)}, c₁≥1/24, c₂≥1/104 explicit.
hypotheses: union-closed 𝒜⊆P(n); |𝒜| above the stated thresholds.
holds-here: yes (large-family settled class; Karpas 2^{n−1} is the best
  threshold in this progression).
status: proven-in-source (theorems, proofs §3–6); not re-checked by the run's
  oracle here.
bearing: a counterexample must be FAR from these extremal shapes; feeds the
  minimal-counterexample programme. A counterexample has |F| < 2^{n−1} (Karpas),
  far below the (2/3−1/104)2^n here.
anchor: research/sources/eccles-stability-result-2015-html.full.md
```

## Status
Sourced (§1 statements, §2–6 proofs verified present in body). Wikilink:
[[eccles-stability-result-2015-html.full]]
